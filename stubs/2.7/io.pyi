# Stubs for io

# Based on https://docs.python.org/2/library/io.html

# Only a subset of functionality is included.

DEFAULT_BUFFER_SIZE = 0

from typing import List, BinaryIO, TextIO, IO, overload, Iterator, Iterable, Any, Union

def open(file: Union[str, unicode, int],
         mode: unicode = 'r', buffering: int = -1, encoding: unicode = None,
         errors: unicode = None, newline: unicode = None,
         closefd: bool = True) -> IO[Any]: ...

class IOBase:
    # TODO
    ...

class BytesIO(BinaryIO):
    def __init__(self, initial_bytes: str = b'') -> None: ...
    # TODO getbuffer
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = -1) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = -1) -> str: ...
    def readlines(self, hint: int = -1) -> List[str]: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = None) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: str) -> None: ...
    def writelines(self, lines: Iterable[str]) -> None: ...
    def getvalue(self) -> str: ...
    def read1(self) -> str: ...

    def __iter__(self) -> Iterator[str]: ...
    def __enter__(self) -> 'BytesIO': ...
    def __exit__(self, type, value, traceback) -> bool: ...

class StringIO(TextIO):
    def __init__(self, initial_value: unicode = '',
                 newline: unicode = None) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = -1) -> unicode: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = -1) -> unicode: ...
    def readlines(self, hint: int = -1) -> List[unicode]: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = None) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: unicode) -> None: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...
    def getvalue(self) -> unicode: ...

    def __iter__(self) -> Iterator[unicode]: ...
    def __enter__(self) -> 'StringIO': ...
    def __exit__(self, type, value, traceback) -> bool: ...

class TextIOWrapper(TextIO):
    # write_through is undocumented but used by subprocess
    def __init__(self, buffer: IO[str], encoding: unicode = None,
                 errors: unicode = None, newline: unicode = None,
                 line_buffering: bool = False,
                 write_through: bool = True) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = -1) -> unicode: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = -1) -> unicode: ...
    def readlines(self, hint: int = -1) -> List[unicode]: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = None) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: unicode) -> None: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...

    def __iter__(self) -> Iterator[unicode]: ...
    def __enter__(self) -> StringIO: ...
    def __exit__(self, type, value, traceback) -> bool: ...

class BufferedIOBase(IOBase): ...
