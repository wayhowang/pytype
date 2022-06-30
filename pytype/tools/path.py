from genericpath import exists
from posixpath import expanduser
import sys
import functools
import os.path

def _replace_return_path_seperator(func):
    if sys.platform == "win32":
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs).replace(os.path.sep, '/')
        return wrapped
    else:
        return wrapped


# return path.replace(os.path.sep, '/') in win32.
abspath = _replace_return_path_seperator(os.path.abspath)
relpath = _replace_return_path_seperator(os.path.relpath)
dirname = _replace_return_path_seperator(os.path.dirname)
expanduser = _replace_return_path_seperator(os.path.expanduser)
normpath = _replace_return_path_seperator(os.path.normpath)


join = _replace_return_path_seperator(os.path.join)


exists = os.path.exists
sep = '/'
