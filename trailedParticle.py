from charBrightness import BrightnessWrapper
from element import Element
from particle import Particle
from pixelupdate import PixelUpdate

class TrailedParticle(Particle):
	def __init__(self, brightness=100, xposition=0, yposition=0, xvelocity = 0, yvelocity = 0, brightnessWrapper = None):
		self.brightness = brightness
		self.xposition = xposition
		self.yposition = yposition
		self.lastxposition = 0
		self.lastyposition = 0
		self.xvelocity = xvelocity
		self.yvelocity = yvelocity
		self.trail = []
		if(brightnessWrapper):
			self.brightnessWrapper = brightnessWrapper
		else:
			self.brightnessWrapper = BrightnessWrapper()

	def getPixelUpdates(self):
		return [PixelUpdate(x = int(self.xposition), 
			y = int(self.yposition), 
			brightness = self.brightness, 
			char = self.brightnessWrapper.closestBrightness(self.brightness))]

	'''def pixelAt(self, x, y):
		if ((x == int(self.xposition)) and (y == int(self.yposition))):
			return self.brightnessWrapper.closestBrightness(self.brightness)
		for trailer in self.trail:
			if ((x == int(trailer.xposition)) and (y == int(trailer.yposition))):
				return trailer.brightnessWrapper.closestBrightness(trailer.brightness)
		return None'''

	def nextFrame(self):
		self.lastxposition = self.xposition
		self.lastyposition = self.yposition
		self.xposition = self.xposition + self.xvelocity
		self.yposition = self.yposition + self.yvelocity
		self.xvelocity *= 0.9
		self.yvelocity += 0.15
		self.brightness *= 0.92
		self.brightness -= 1

		if ((self.lastyposition != self.yposition or self.lastxposition != self.xposition) 
			and (self.lastxposition != 0 and self.lastyposition != 0)):
			return [Particle(brightness = self.brightness * 0.85, 
				xposition = self.lastxposition,
				yposition = self.lastyposition,
				xvelocity = 0,
				yvelocity = 0,
				brightnessWrapper = self.brightnessWrapper)]

