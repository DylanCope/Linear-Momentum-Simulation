import GameEngine
from GameEngine import Display
from pygame import *
import pygame
import pygame.gfxdraw
import Particle

def renderParticle(display, pos, r, colour):
    pygame.gfxdraw.filled_circle(display.screen, pos[0], pos[1], r, colour)
    pygame.gfxdraw.aacircle(display.screen, pos[0], pos[1], r, colour)

def renderParticleSystem(display, system):
    for p in system.particles:
        pos = [int(p.s.x), int(p.s.y)]
        colour = (255, 0, 0, 255)
        renderParticle(display, pos, p.r, colour)
        l = len(p.trail)
        for i in range(0, l):
            t = p.trail[i]
            pos = [int(t.x), int(t.y)]
            colour = (255, 0, 0, int(30 * i / l) if i < l-1 else 255)
            renderParticle(display, pos, p.r, colour)
