import sys
import functools
import os
import os.path
import glob as glob_module


def _replace_return_path_seperator(func):
  if sys.platform == "win32" and False:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
      return func(*args, **kwargs).replace(os.path.sep, '/')
    return wrapped
  else:
    return func


if sys.platform == 'win32' and False:
  def splitext(path):
    filename, ext = os.path.splitext(path)
    return filename.replace(os.path.sep, '/'), ext

  def glob(*args, **kwargs):
    path_list = glob_module.glob(*args, **kwargs)
    return list(map(lambda x: x.replace(os.path.sep, '/'), path_list))
else:
  splitext = os.path.splitext
  glob = glob_module.glob


# return path.replace(os.path.sep, '/') in win32.
abspath = _replace_return_path_seperator(os.path.abspath)
relpath = _replace_return_path_seperator(os.path.relpath)
dirname = _replace_return_path_seperator(os.path.dirname)
expanduser = _replace_return_path_seperator(os.path.expanduser)
normpath = _replace_return_path_seperator(os.path.normpath)
realpath = _replace_return_path_seperator(os.path.realpath)
join = _replace_return_path_seperator(os.path.join)
getcwd = _replace_return_path_seperator(os.getcwd)

exists = os.path.exists
isdir = os.path.isdir
isabs = os.path.isabs
basename = os.path.basename
split = os.path.split
isfile = os.path.isfile

sep = os.path.sep # '/'
