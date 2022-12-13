from os import system
from charBrightness import BrightnessWrapper

class Screen:
	def __init__(self, width = 20, height = 20, brightnessWrapper = None):
		self.width = width
		self.height = height
		self.elements = []
		if (brightnessWrapper):
			self.brightnessWrapper = brightnessWrapper
		else:
			self.brightnessWrapper = BrightnessWrapper()


	def addElement(self, element):
		self.elements.append(element)

	def refresh(self):
		pixelUpdates = []
		self.pixels = [[" " for j in range(self.width)] for i in range(self.height)]
		for element in self.elements:
			pixelUpdates += element.getPixelUpdates()

		for pixelUpdate in pixelUpdates:
			if (pixelUpdate.x < self.width - 1 and pixelUpdate.x >= 0 
				and pixelUpdate.y < self.height - 1 and pixelUpdate.y >= 0):
				if (self.brightnessWrapper.brightnessFromChar(self.pixels[pixelUpdate.y][pixelUpdate.x]) < 
					self.brightnessWrapper.brightnessFromChar(pixelUpdate.char)):
					self.pixels[pixelUpdate.y][pixelUpdate.x] = pixelUpdate.char

		system('clear')
		screenString = ""
		for row in self.pixels:
			for char in row:
				screenString += char
			screenString += "\n"

		print(screenString)
	
	def advanceScreen(self):
		self.elements = [element for element in self.elements if element.brightness > 0]
		for element in self.elements:
			newElements = element.nextFrame()
			if(newElements):
				self.elements += newElements
		self.refresh()
		self.cleanup()

	def cleanup(self):
		self.elements = [element for element in self.elements if not 
			(element.xposition > self.width or element.xposition < 0 or 
			element.yposition > self.height or element.yposition < 0)]



















