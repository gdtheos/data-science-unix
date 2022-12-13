from charBrightness import BrightnessWrapper
from element import Element
from pixelupdate import PixelUpdate

class Particle(Element):
	def __init__(self, brightness=100, xposition=0, yposition=0, xvelocity = 0, yvelocity = 0, brightnessWrapper = None):
		self.brightness = brightness
		self.xposition = xposition
		self.yposition = yposition
		self.xvelocity = xvelocity
		self.yvelocity = yvelocity
		if(brightnessWrapper):
			self.brightnessWrapper = brightnessWrapper
		else:
			self.brightnessWrapper = BrightnessWrapper()

	def getPixelUpdates(self):
		return [PixelUpdate(x = int(self.xposition),
			y = int(self.yposition),
			brightness = self.brightness,
			char = self.brightnessWrapper.closestBrightness(self.brightness))]

	def nextFrame(self):
		self.xposition = self.xposition + self.xvelocity
		self.yposition = self.yposition + self.yvelocity
		self.xvelocity *= 0.9
		self.yvelocity += 0.1
		self.brightness *= 0.97
		self.brightness -= 2