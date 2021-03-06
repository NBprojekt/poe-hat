import logging
import sys
import time
import math
import smbus
import RPi.GPIO as GPIO

import os
import socket
import fcntl
import struct

from PIL import Image, ImageDraw, ImageFont
from waveshare import SSD1306

screen = SSD1306.SSD1306()
screen.Init();


class PoeHat:
    def __init__(self, font = './Courier_New.ttf', address = 0x20, maxTemp = 36):
        self.i2c = smbus.SMBus(1)
        self.font = font
        self.address = address
        self.maxTemp = maxTemp
        screen.ClearBlack()

    def fanOn(self):
        self.i2c.write_byte(self.address, 0xFE & self.i2c.read_byte(self.address))

    def fanOff(self):
        self.i2c.write_byte(self.address, 0x01 | self.i2c.read_byte(self.address))

    def getIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def getTemp(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
            temp = (int)(f.read() ) / 1000.0
        return ((int)(temp*10))/10.0

    def updateDisplay(self):
        image = Image.new('1', (screen.width, screen.height), 'WHITE')
        draw = ImageDraw.Draw(image)
        ip = self.getIp()
        temp = self.getTemp()

        draw.text((0,1), 'IP:' + str(ip), font = self.font, fill = 0)
        draw.text((0,15), 'Temp:' + str(temp), font = self.font, fill = 0)

        if(temp >= self.maxTemp):
            draw.text((77,16), 'FAN:ON', font = self.font, fill = 0)
            self.fanOn()
        else:
            draw.text((77,16), 'FAN:OFF', font = self.font, fill = 0)
            self.fanOff()

        screen.ShowImage(screen.getbuffer(image))
