import time
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging

from . import PoeHatDisplay

 
logging.basicConfig(level = logging.INFO)

display = PoeHatDisplay.PoeHatDisplay()
        
try:  
    while(1):
        display.update()
        time.sleep(1)
        
except KeyboardInterrupt:    
    print("ctrl + c:")
    POE.FAN_OFF()
