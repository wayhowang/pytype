"""Utilities for xref."""

from pytype.tools import path as path_tools
import os

from pytype import module_utils


def get_module_filepath(module_filename):
  """Recover the path to the py file from a module pyi path."""

  def _clean(path):
    """Change extension to .py."""
    prefix, fname = path_tools.split(path)
    fname, _ = path_tools.splitext(fname)
    path = path_tools.join(prefix, fname + ".py")
    return path

  return _clean(module_filename)


def process_imports_map(imports_map):
  """Generate a map of {module name: canonical relative path}."""
  if not imports_map:
    return {}

  # Store maps of the full path and canonical relative path.
  mod_to_fp = {}
  fp_to_cp = {}

  for path, v in imports_map.items():
    mod = module_utils.path_to_module_name(path)
    mod_to_fp[mod] = v
    if v not in fp_to_cp or len(path) > len(fp_to_cp[v]):
      fp_to_cp[v] = path

  return {mod: fp_to_cp[fp] for mod, fp in mod_to_fp.items()}
