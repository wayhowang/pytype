"""Tests for imports_map_loader.py."""

import textwrap

from pytype import file_utils
from pytype import imports_map_loader
from pytype.tools import tempfile as compatible_tempfile

import unittest


class ImportMapLoaderTest(unittest.TestCase):
  """Tests for imports_map_loader.py."""

  def test_read_imports_info(self):
    """Test reading an imports_info file into ImportsInfo."""
    with compatible_tempfile.NamedTemporaryFile() as fi:
      fi.write(textwrap.dedent(file_utils.replace_seperator("""
        a/b/__init__.py prefix/1/a/b/__init__.py~
        a/b/b.py prefix/1/a/b/b.py~suffix
        a/b/c.pyi prefix/1/a/b/c.pyi~
        a/b/d.py prefix/1/a/b/d.py~
        a/b/e.py 2/a/b/e1.py~
        a/b/e 2/a/b/e2.py~
        a/b/e 2/a/b/foo/#2.py~
      """)).encode("utf-8"))
      fi.seek(0)  # ready for reading
      self.assertCountEqual(
          imports_map_loader._read_imports_map(fi.name, open).items(),
          [
              (file_utils.replace_seperator("a/b/__init__"), [file_utils.replace_seperator("prefix/1/a/b/__init__.py~")]),
              (file_utils.replace_seperator("a/b/b"), [file_utils.replace_seperator("prefix/1/a/b/b.py~suffix")]),
              (file_utils.replace_seperator("a/b/c"), [file_utils.replace_seperator("prefix/1/a/b/c.pyi~")]),
              (file_utils.replace_seperator("a/b/d"), [file_utils.replace_seperator("prefix/1/a/b/d.py~")]),
              (file_utils.replace_seperator("a/b/e"), [file_utils.replace_seperator("2/a/b/foo/#2.py~"), file_utils.replace_seperator("2/a/b/e1.py~"), file_utils.replace_seperator("2/a/b/e2.py~")]),
          ])

  def test_do_not_filter(self):
    with file_utils.Tempdir() as d:
      d.create_file(file_utils.replace_seperator("a/b/c.pyi"))
      imports_info = f"{file_utils.replace_seperator('a/b/c.pyi')} {d[file_utils.replace_seperator('a/b/c.pyi')]}\n"
      d.create_file("imports_info", imports_info)
      imports_map = imports_map_loader.build_imports_map(d["imports_info"])
      self.assertEqual(imports_map[file_utils.replace_seperator("a/b/c")], d[file_utils.replace_seperator("a/b/c.pyi")])

  def test_invalid_map_entry(self):
    with file_utils.Tempdir() as d:
      imports_info = f"{file_utils.replace_seperator('a/b/c.pyi')} {d[file_utils.replace_seperator('a/b/c.pyi')]}\n"
      d.create_file("imports_info", imports_info)
      with self.assertRaises(ValueError):
        imports_map_loader.build_imports_map(d["imports_info"])


if __name__ == "__main__":
  unittest.main()
