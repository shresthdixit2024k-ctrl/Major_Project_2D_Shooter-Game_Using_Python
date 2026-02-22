#difficulty.py
import pygame

class DifficultyManager:
    def __init__(self):
        self.level = 1
        self.last_level_up = pygame.time.get_ticks()
        self.level_interval = 30000  # 30 seconds
        self.bullet_speed = 8

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_level_up >= self.level_interval:
            self.level += 1
            self.bullet_speed += 1
            self.last_level_up = now
            return True
        return False

    def get_level(self):
        return self.level

    def get_bullet_speed(self):
        return self.bullet_speed
