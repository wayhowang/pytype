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

if sys.platform == 'win32':
    def splitext(path):
        filename, ext = os.path.splitext(path)
        return filename.replace(os.path.sep, '/'), ext
else:
    splitext = os.path.splitext


# return path.replace(os.path.sep, '/') in win32.
abspath = _replace_return_path_seperator(os.path.abspath)
relpath = _replace_return_path_seperator(os.path.relpath)
dirname = _replace_return_path_seperator(os.path.dirname)
expanduser = _replace_return_path_seperator(os.path.expanduser)
normpath = _replace_return_path_seperator(os.path.normpath)
realpath = _replace_return_path_seperator(os.path.realpath)
join = _replace_return_path_seperator(os.path.join)


exists = os.path.exists
isdir = os.path.isdir
isabs = os.path.isabs
basename = os.path.basename
split = os.path.split
isfile = os.path.isfile

sep = '/'
