from __future__ import print_function
import string
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

class BrightnessWrapper:

    def __init__(self):
        self.scaledMap = self.constructScaledMap()


    def charToPixels(self, text, path='/System/Library/Fonts/Supplemental/Andale Mono.ttf', fontsize=12):
            """
            Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
            """
            font = ImageFont.truetype(path, fontsize) 
            w, h = font.getsize(text)  
            h *= 2
            image = Image.new('L', (w, h), 1)
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), text, font=font) 
            arr = np.asarray(image)
            arr = np.where(arr, 0, 1)
            arr = arr[(arr != 0).any(axis=1)]
            return arr

    def calculateIntensity(self, pixels):
        spaces = 0
        filled = 0
        if(len(pixels) < 10):
            spaces += (10 - len(pixels)) * 7
        for row in pixels:
            for pixel in row:
                if(pixel == 1):
                    filled += 1
                spaces += 1

        return filled/spaces


    def constructMap(self):
        brightnessMap = {}
        for char in (string.ascii_letters + string.digits + string.punctuation + " "):
            brightnessMap[char] = self.calculateIntensity(self.charToPixels(char))
        return brightnessMap

    def constructScaledMap(self):
        brightnessMap = self.constructMap()
        maxBrightness = max(brightnessMap.values())
        minBrightness = min(brightnessMap.values())
        range = 100
        slope = range / (maxBrightness - minBrightness)
        n = -minBrightness * slope
        for char in list(brightnessMap.keys()):
            brightnessMap[char] = slope * brightnessMap[char] + n
        del brightnessMap["i"]
        #sort the thing before we hand it out
        return dict(sorted(brightnessMap.items(), key=lambda item: item[1]))

    def closestBrightness(self, x):
        lastChar = list(self.scaledMap.keys())[0]
        for char in list(self.scaledMap.keys()):
            if(x < self.scaledMap[char]):
                break
            else:
                lastChar = char
        return lastChar

    def brightnessFromChar(self, char):
        return self.scaledMap[char]