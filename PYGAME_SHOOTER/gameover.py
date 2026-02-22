# gameover.py
import pygame

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsans", 60)

    def show(self, final_score):
        while True:
            self.screen.fill((0, 0, 0))
            title = self.font.render("GAME OVER", True, (255, 0, 0))
            score_text = self.font.render(f"Score: {final_score}", True, (255, 255, 255))
            restart_text = self.font.render("Restart", True, (0, 255, 0))
            quit_text = self.font.render("Quit", True, (255, 0, 0))

            self.screen.blit(title, (400 - title.get_width() // 2, 100))
            self.screen.blit(score_text, (400 - score_text.get_width() // 2, 180))

            restart_rect = pygame.Rect(300, 280, 200, 60)
            quit_rect = pygame.Rect(300, 360, 200, 60)

            pygame.draw.rect(self.screen, (0, 255, 0), restart_rect)
            pygame.draw.rect(self.screen, (255, 0, 0), quit_rect)

            self.screen.blit(restart_text, (restart_rect.x + 40, restart_rect.y + 10))
            self.screen.blit(quit_text, (quit_rect.x + 60, quit_rect.y + 10))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if restart_rect.collidepoint(mouse) and click[0]:
                return "restart"
            if quit_rect.collidepoint(mouse) and click[0]:
                return "quit"

            pygame.display.update()
