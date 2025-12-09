import pygame
import random
import os

# --- Setup pygame audio ---
pygame.mixer.init()

# Path to your folder of mp3s
SOUND_DIR = "keyboard_sounds"

# Load all sound files from 1.mp3 to 10.mp3
sounds = []
for i in range(1, 11):
    filepath = os.path.join(SOUND_DIR, f"{i}.mp3")
    sounds.append(pygame.mixer.Sound(filepath))

# --- Setup pygame window for key events ---
pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Press any key to play a sound")

running = True
while running:
    for event in pygame.event.get():
        # Quit on window close
        if event.type == pygame.QUIT:
            running = False

        # Play a random sound on keypress
        if event.type == pygame.KEYDOWN:
            random.choice(sounds).play()

pygame.quit()
