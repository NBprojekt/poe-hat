import time
import sys
import os
import logging


libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from nbprojekt.poe_hat import PoeHat


dir_path = os.path.dirname(os.path.abspath(__file__))
font = ImageFont.truetype(dir_path + '/fonts/Courier_New.ttf', 13)

logging.basicConfig(level = logging.INFO)
poeHat = PoeHat.PoeHat(font = font)

try:
    while(1):
        poeHat.updateDisplay()
        time.sleep(1)

except KeyboardInterrupt:
    print("ctrl + c:")
    poeHat.fanOff()
