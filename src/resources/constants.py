import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font('src/resources/fonts/minecraft_font.ttf', 16)
G = 100
SCALE = 1.0
PARTICLES = []
ADDED_RADIUS = 20
ADDED_MASS = 20
ADDED_VELOCITY = pygame.Vector2(0, 0)
NUM_PARTICLES = 30
ADDED_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()