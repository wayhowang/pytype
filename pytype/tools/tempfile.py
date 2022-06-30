import tempfile
import sys
import os


# Windows Cannot open a temp file twice without delete=False"""
if sys.platform == 'win32':
  class NamedTemporaryFile:
    # pylint: disable=W0622
    def __init__(self, mode='w+b', buffering=-1, encoding=None,
            newline=None, suffix=None, prefix=None,
            dir=None, delete=True, *, errors=None):
      # pylint: disable=R1732
      self._tempfile = tempfile.NamedTemporaryFile(
        mode=mode, buffering=buffering, encoding=encoding,
        newline=newline, suffix=suffix, prefix=prefix, dir=dir,
        delete=False, errors=errors)
      self._delete = delete

    def __enter__(self):
      return self._tempfile.__enter__()

    def __exit__(self, *args, **kwargs):
      self._tempfile.__exit__(*args, **kwargs)
      if self._delete:
        os.remove(self._tempfile.name)
else:
  NamedTemporaryFile = tempfile.NamedTemporaryFile
