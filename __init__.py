import sys

if "C://lib" not in sys.path:
    sys.path.append("C://lib")

if "C://script" not in sys.path:
    sys.path.append("C://script")

from imp import Deck, Hand

__all__ = ["Deck", "Hand"]
__doc__ = "cards for Python"
