# powerups.py

import pygame
import random

class PowerUpManager:
    def __init__(self):
        self.powerups = []
        self.spawn_timer = pygame.time.get_ticks()

    def spawn_powerup(self, player_rect, mode="2P"):
        now = pygame.time.get_ticks()
        if now - self.spawn_timer >= 20000:  # 20 seconds
            type = random.choice(["health", "speed"])
            if mode == "AI":
                x = random.randint(50, 200)  # Left side
            else:
                x = random.randint(400, 750)  # Right side
            y = random.randint(50, 550)
            rect = pygame.Rect(x, y, 20, 20)
            self.powerups.append((rect, type))
            self.spawn_timer = now

    def draw(self, screen):
        for rect, type in self.powerups:
            color = (0, 255, 0) if type == "health" else (0, 0, 255)
            pygame.draw.rect(screen, color, rect)

    def check_collision(self, player_rect, player_stats):
        for powerup in self.powerups[:]:
            rect, type = powerup
            if player_rect.colliderect(rect):
                if type == "health":
                    player_stats["health"] += 1
                elif type == "speed":
                    player_stats["speed"] += 2
                self.powerups.remove(powerup)
