 # -- OHNE KLASSE, vereinfacht--

# import pygame

# pygame.init()  #initialisiert pygame, damit wir damit arbeiten können

# window_width = 800
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# clock = pygame.time.Clock()  # fps

# running = True
# while running:
#     delta_time = clock.tick(60) / 1000   # delta_time beschreibt die Zeitdifferenz zwischen dem vorhergehenden Bild und dem aktuell gerenderten Bild
#     for event in pygame.event.get():     # sucht nach events, solange das game läuft, wenn quit (X) gefunden wird, wird das Event bzw Game beendet
#         if event.type == pygame.QUIT:    # X gleich Quit
#             running = False
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:   # Drücke ESC gleich Quit
#             running = False
#
#     window.fill((34, 139, 34))   # Display Farbe in ForestGrün ändern
#     pygame.display.update()
#
# pygame.quit()                    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -- MIT KLASSE (OBJEKTORIENTIERT) --

import pygame
import player
import coin
import random
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 1500
        self.window_height = 1200
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Coin Collector")
        self.clock = pygame.time.Clock()

        self.player = player.Player(self, 32, 32)  # player wird aus der file player importiert
        self.coins = [coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100)),
                      coin.Coin(self, random.randrange(0, 1300), random.randrange(0, 1100))]
        
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

    
            self.delta_time = self.clock.tick(60) / 1000
            self.window.fill((20, 20, 20))
            self.player.update()
        
            for coin in self.coins:
                coin.update()
                if coin.is_destroyed:
                    self.coins.remove(coin)

            pygame.display.update()

    pygame.quit()

game = Game()

# ------------------------------------------------------------------------------------------

#    rect = Rechteck:

#    x = 32
#    y = 32
#    width = 100
#    height = 200
#    pygame.draw.rect(window, "darkgrey", (x, y, width, height))

# --------------------------------------------------------------------------------------------

#   line = Linien

#   pygame.draw.line(window, "yellow", (0, 0), (window_width, window_height), 10)


