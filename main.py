from nrzi import NRZI
from hdb3 import HDB3
from manchester import Manchester
#from multilevel import Multilevel

bits = NRZI("1011001110")
print("Bits:", bits.get_bits())
print("Code:", bits.get_code())

bits.plot()