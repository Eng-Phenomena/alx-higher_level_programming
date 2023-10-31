#!/usr/bin/python3
"""protected class"""


class LockedClass:
    """locked class cannot be instantialized dynamically"""

    __slots__ = ["first_name"]
