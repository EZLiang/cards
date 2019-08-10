# cards

[Go to wiki](https://github.com/EZLiang/cards/wiki)<br />
[See directory](docs/dir.md)

To use:
 * Download and unzip.
 * Create and open cardsim.py where you want to use cards.
 * Write <br />
 ```py
 import sys
 if "[download location]" not in sys.path:
     sys.path.append("[download location]/lib")
 import deck
 import hand
 ```
 * Now if you want to use, just type
 ```py
 from cardsim import deck, hand
 rest of code here
 ```
