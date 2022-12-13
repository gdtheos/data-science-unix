from charBrightness import BrightnessWrapper
from element import Element
from trailedParticle import TrailedParticle
from charBrightness import BrightnessWrapper
from pixelupdate import PixelUpdate
import random

class Firework(Element):
	def __init__(self, 
		brightness=100, xposition=0, yposition=0, 
		xvelocity = 0, yvelocity = 0, particleCount = 0,
		brightnessWrapper = None):
		self.brightness = brightness
		self.xposition = xposition
		self.yposition = yposition
		self.xvelocity = xvelocity
		self.yvelocity = yvelocity
		self.particleCount = particleCount
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
		if(self.yvelocity > 0):
			return self.burst()

		self.xposition = self.xposition + self.xvelocity
		self.yposition = self.yposition + self.yvelocity
		self.xvelocity *= 0.9
		self.yvelocity += 0.1

	def burst(self):
		burstParticles = []
		for i in range(self.particleCount):
			burstParticles.append(TrailedParticle(
				brightness= random.randrange(70, self.brightness), 
				xposition = self.xposition,
				yposition = self.yposition,
				xvelocity = random.randrange(-4, 4),
				yvelocity = random.randrange(-2, 2),
				brightnessWrapper = self.brightnessWrapper
			))
		#elements can't directly delete themselves
		#so this is what we have to do for now
		self.xposition = -1
		self.yposition = -1
		self.xvelocity = 0
		self.yvelocity = 0
		return burstParticles
		
		
