# menu.py
import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsans", 50)
        self.small_font = pygame.font.SysFont("comicsans", 30)

    def draw_button(self, text, x, y, w, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.screen, (0, 128, 255), button_rect)

        if button_rect.collidepoint(mouse):
            pygame.draw.rect(self.screen, (0, 200, 255), button_rect)
            if click[0] == 1:
                return True

        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x + (w - text_surface.get_width()) // 2, y + (h - text_surface.get_height()) // 2))
        return False

    def main_menu(self):
        while True:
            self.screen.fill((0, 0, 0))
            title = self.font.render("SHOOTER GAME", True, (255, 255, 255))
            self.screen.blit(title, (400 - title.get_width() // 2, 100))

            if self.draw_button("Start", 300, 200, 200, 60):
                return "start"
            if self.draw_button("Instructions", 300, 280, 200, 60):
                return "instructions"
            if self.draw_button("Exit", 300, 360, 200, 60):
                return "exit"

            pygame.display.update()

    def instructions_screen(self):
        back_btn = pygame.Rect(20, 20, 100, 40)
        while True:
            self.screen.fill((50, 50, 50))
            text = self.small_font.render("Use Arrow Keys or W/S to Move. Space to Shoot.", True, (255, 255, 255))
            self.screen.blit(text, (100, 200))
            pygame.draw.rect(self.screen, (0, 128, 255), back_btn)
            back_text = self.small_font.render("Back", True, (255, 255, 255))
            self.screen.blit(back_text, (30, 25))
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if back_btn.collidepoint(mouse) and click[0]:
                return

            pygame.display.update()

