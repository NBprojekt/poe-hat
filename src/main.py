import time
import sys
import os
import logging

from ./peo-hat import PoeHat

logging.basicConfig(level = logging.INFO)
poeHat = PoeHat()
        
try:  
    while(1):
        poeHat.updateDisplay()
        time.sleep(1)
        
except KeyboardInterrupt:    
    print("ctrl + c:")
    poeHat.fanOff()
