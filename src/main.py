import time
import sys
import os
import logging


libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from nbprojekt import PoeHat

logging.basicConfig(level = logging.INFO)
poeHat = PoeHat.PoeHat()

try:
    while(1):
        poeHat.updateDisplay()
        time.sleep(1)

except KeyboardInterrupt:
    print("ctrl + c:")
    poeHat.fanOff()
