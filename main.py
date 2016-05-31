import GameEngine
from GameEngine import Display
from pygame import *
import pygame
import random, math
from Vector2f import *
from Renderer import *
from ParticleSystem import *
from Particle import *

display = Display()
winw = 800
winh = 600
delta = 0

display.setDimensions(winw, winh)
system = ParticleSystem(winw, winh)

for i in range(10):
    system.addParticle()

while True:
    display.refresh()
    delta = display.getDelta()

    system.update(delta)
    renderParticleSystem(display, system)

    display.show()
