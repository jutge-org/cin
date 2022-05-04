"""
cin package
https://github.com/jutge-org/cin
"""

import sys
from typing import Optional, TypeVar, Type, Iterator


version = '1.0'
"""package version"""


sys.setrecursionlimit(1000000)  # hack to get more stack size


T = TypeVar('T', int, float, str)


def read(t: Type[T]) -> T:
    """
    Returns the next word of the input interpreted as having type t.

    Raises EOFError if trying to read past the end of the input.
    Raises ValueError if the read word does not match the type t.
    Raises TypeError if t is not int, float or str.
    """

    _check(t)
    word = _get()
    if word is None:
        raise EOFError
    else:
        return t(word)  # might rise ValueError


def scan(t: Type[T]) -> Optional[T]:
    """
    Returns the next word of the input interpreted as having type t.
    Returns None when trying to read past the end of the input
    or if the read word does not match the type t.

    Raises TypeError if t is not int, float or str.
    """

    _check(t)
    word = _get()
    if word is None:
        return None
    else:
        try:
            return t(word)
        except ValueError:
            return None


def _check(t: Type[T]) -> Optional[str]:
    """Check that the type t is valid."""
    if t not in [int, float, str]:
        raise TypeError


def _get() -> Optional[str]:
    """Returns the next word in the input or None if eof."""

    try:
        word = next(_generator)
    except StopIteration:
        return None
    return word


def _word_generator() -> Iterator[str]:
    """Generates the words in all the lines of input."""
    for line in sys.stdin:
        for word in iter(line.split()):
            yield word


_generator = _word_generator()
"""Generator instance."""
