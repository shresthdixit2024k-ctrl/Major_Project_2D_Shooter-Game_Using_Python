#ai_player.py
import pygame
import random

class AIPlayer:
    def __init__(self, shooter_rect, bullet_list, target_rect):
        self.shooter = shooter_rect
        self.bullets = bullet_list
        self.target = target_rect
        self.fire_delay = 1000  # milliseconds
        self.last_fire_time = pygame.time.get_ticks()

    def move(self):
        if self.target.centery < self.shooter.centery and self.shooter.top > 0:
            self.shooter.y -= 3
        elif self.target.centery > self.shooter.centery and self.shooter.bottom < 600:
            self.shooter.y += 3


    def fire(self):
        now = pygame.time.get_ticks()
        if now - self.last_fire_time > self.fire_delay:
            bullet = pygame.Rect(
                self.shooter.x, self.shooter.y + self.shooter.height // 2 - 2, 10, 5
            )
            self.bullets.append(bullet)
            self.last_fire_time = now
