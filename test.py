from screen import Screen
from particle import Particle
from trailedParticle import TrailedParticle
from firework import Firework
from charBrightness import BrightnessWrapper
from termcolor import colored
import random
import time
import cProfile

def main():
	brightnessWrapper = BrightnessWrapper()
	testScreen = Screen(width = 100, height = 50, brightnessWrapper = brightnessWrapper)
	fireworkTest = Firework(brightness=100, xposition=25, yposition=25, 
		xvelocity = 3, yvelocity = -1, particleCount = 25,
		brightnessWrapper = None)
	testScreen.addElement(fireworkTest)
	while(testScreen.elements):
		time.sleep(0.05)
		testScreen.advanceScreen()
		'''for element in testScreen.elements:
			print((element.xposition, element.yposition))'''

main()
#cProfile.run("main()")
#print(colored('hello', 'red'), colored('world', 'green'))