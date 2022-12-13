from element import Element

class Sparkler(Element):
	def __init__(self, brightness=100, xposition=0, yposition=0, 
		xvelocity = 0, yvelocity = 0, brightnessWrapper = None):
		self.brightness = brightness
		self.xposition = xposition
		self.yposition = yposition
		self.xvelocity = xvelocity
		self.yvelocity = yvelocity
		if(brightnessWrapper):
			self.brightnessWrapper = brightnessWrapper
		else:
			self.brightnessWrapper = BrightnessWrapper()