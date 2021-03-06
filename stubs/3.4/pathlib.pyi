# Stubs for pathlib (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from collections import Sequence

class _Flavour:
    join = ... # type: Any
    def __init__(self): ...
    def parse_parts(self, parts): ...
    def join_parsed_parts(self, drv, root, parts, drv2, root2, parts2): ...

class _WindowsFlavour(_Flavour):
    sep = ... # type: Any
    altsep = ... # type: Any
    has_drv = ... # type: Any
    pathmod = ... # type: Any
    is_supported = ... # type: Any
    drive_letters = ... # type: Any
    ext_namespace_prefix = ... # type: Any
    reserved_names = ... # type: Any
    def splitroot(self, part, sep=...): ...
    def casefold(self, s): ...
    def casefold_parts(self, parts): ...
    def resolve(self, path): ...
    def is_reserved(self, parts): ...
    def make_uri(self, path): ...

class _PosixFlavour(_Flavour):
    sep = ... # type: Any
    altsep = ... # type: Any
    has_drv = ... # type: Any
    pathmod = ... # type: Any
    is_supported = ... # type: Any
    def splitroot(self, part, sep=...): ...
    def casefold(self, s): ...
    def casefold_parts(self, parts): ...
    def resolve(self, path): ...
    def is_reserved(self, parts): ...
    def make_uri(self, path): ...

class _Accessor: ...

class _NormalAccessor(_Accessor):
    stat = ... # type: Any
    lstat = ... # type: Any
    open = ... # type: Any
    listdir = ... # type: Any
    chmod = ... # type: Any
    lchmod = ... # type: Any
    mkdir = ... # type: Any
    unlink = ... # type: Any
    rmdir = ... # type: Any
    rename = ... # type: Any
    replace = ... # type: Any
    def symlink(a, b, target_is_directory): ...
    utime = ... # type: Any
    def readlink(self, path): ...

class _Selector:
    child_parts = ... # type: Any
    successor = ... # type: Any
    def __init__(self, child_parts): ...
    def select_from(self, parent_path): ...

class _TerminatingSelector: ...

class _PreciseSelector(_Selector):
    name = ... # type: Any
    def __init__(self, name, child_parts): ...

class _WildcardSelector(_Selector):
    pat = ... # type: Any
    def __init__(self, pat, child_parts): ...

class _RecursiveWildcardSelector(_Selector):
    def __init__(self, pat, child_parts): ...

class _PathParents(Sequence):
    def __init__(self, path): ...
    def __len__(self): ...
    def __getitem__(self, idx): ...

class PurePath:
    def __init__(self, *args): ...
    def __reduce__(self): ...
    def as_posix(self): ...
    def __bytes__(self): ...
    def as_uri(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    drive = ... # type: Any
    root = ... # type: Any
    @property
    def anchor(self): ...
    @property
    def name(self): ...
    @property
    def suffix(self): ...
    @property
    def suffixes(self): ...
    @property
    def stem(self): ...
    def with_name(self, name): ...
    def with_suffix(self, suffix): ...
    def relative_to(self, *other): ...
    @property
    def parts(self): ...
    def joinpath(self, *args): ...
    def __truediv__(self, key): ...
    def __rtruediv__(self, key): ...
    @property
    def parent(self): ...
    @property
    def parents(self): ...
    def is_absolute(self): ...
    def is_reserved(self): ...
    def match(self, path_pattern): ...

class PurePosixPath(PurePath): ...
class PureWindowsPath(PurePath): ...

class Path(PurePath):
    def __init__(self, *args, **kwargs): ...
    def __enter__(self): ...
    def __exit__(self, t, v, tb): ...
    @classmethod
    def cwd(cls): ...
    def iterdir(self): ...
    def glob(self, pattern): ...
    def rglob(self, pattern): ...
    def absolute(self): ...
    def resolve(self): ...
    def stat(self): ...
    def owner(self): ...
    def group(self): ...
    def open(self, mode='', buffering=-1, encoding=None, errors=None, newline=None): ...
    def touch(self, mode=438, exist_ok=True): ...
    def mkdir(self, mode=511, parents=False): ...
    def chmod(self, mode): ...
    def lchmod(self, mode): ...
    def unlink(self): ...
    def rmdir(self): ...
    def lstat(self): ...
    def rename(self, target): ...
    def replace(self, target): ...
    def symlink_to(self, target, target_is_directory=False): ...
    def exists(self): ...
    def is_dir(self): ...
    def is_file(self): ...
    def is_symlink(self): ...
    def is_block_device(self): ...
    def is_char_device(self): ...
    def is_fifo(self): ...
    def is_socket(self): ...

class PosixPath(Path, PurePosixPath): ...
class WindowsPath(Path, PureWindowsPath): ...
