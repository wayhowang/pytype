import sys
import functools
import os
import os.path
import glob as glob_module

def _replace_driver_code(path: str):
  drive, other = os.path.splitdrive(path)
  drive = drive.capitalize()
  return os.path.join(drive, other)

def _capitalize_return_drive_code(func):
  if sys.platform == "win32":
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
      return _replace_driver_code(func(*args, **kwargs))
    return wrapped
  else:
    return func

splitext = os.path.splitext
glob = glob_module.glob

abspath = _capitalize_return_drive_code(os.path.abspath)
relpath = _capitalize_return_drive_code(os.path.relpath)
dirname = _capitalize_return_drive_code(os.path.dirname)
expanduser = _capitalize_return_drive_code(os.path.expanduser)
normpath = _capitalize_return_drive_code(os.path.normpath)
realpath = _capitalize_return_drive_code(os.path.realpath)
join = _capitalize_return_drive_code(os.path.join)
getcwd = _capitalize_return_drive_code(os.getcwd)

exists = os.path.exists
isdir = os.path.isdir
isabs = os.path.isabs
basename = os.path.basename
split = os.path.split
isfile = os.path.isfile

sep = os.path.sep
