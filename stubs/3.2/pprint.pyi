# Stubs for pprint

# Based on http://docs.python.org/3.2/library/pprint.html

from typing import Any, Dict, Tuple, TextIO

def pformat(o: object, indent: int = 1, width: int = 80,
            depth: int = None) -> str: ...
def pprint(o: object, stream: TextIO = None, indent: int = 1, width: int = 80,
           depth: int = None) -> None: ...
def isreadable(o: object) -> bool: ...
def isrecursive(o: object) -> bool: ...
def saferepr(o: object) -> str: ...

class PrettyPrinter:
    def __init__(self, indent: int = 1, width: int = 80, depth: int = None,
                 stream: TextIO = None) -> None: ...
    def pformat(self, o: object) -> str: ...
    def pprint(self, o: object) -> None: ...
    def isreadable(self, o: object) -> bool: ...
    def isrecursive(self, o: object) -> bool: ...
    def format(self, o: object, context: Dict[int, Any], maxlevels: int,
               level: int) -> Tuple[str, bool, bool]: ...
