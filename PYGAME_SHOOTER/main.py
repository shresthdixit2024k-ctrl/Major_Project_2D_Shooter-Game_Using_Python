#main.py
import pygame 
import os 
from ai_player import AIPlayer
from difficulty import DifficultyManager  # 🔴 Added for level system

pygame.font.init()
pygame.mixer.init()
Bullet_Hit = pygame.mixer.Sound("Play.mp3")
Bullet_Fire = pygame.mixer.Sound("Sound.mp3")
FPS = 60
WIDTH = 1200
HEIGHT = 600
Shooter_Width = 95
Shooter_Height = 95
Vel = 5

# 🔴 Removed static Bullet_Vel. Will use dynamic speed from DifficultyManager

Max_Bullets = 5
HEALTH_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)
MENU_FONT = pygame.font.SysFont("comicsans", 60)

S1_HIT = pygame.USEREVENT + 1
S2_HIT =pygame.USEREVENT + 2

BLACK = (0,0,0)
WHITE = (255,255,255)
Border = pygame.Rect((WIDTH/2)-5,0 ,10 ,HEIGHT)
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shooter By ShresthDixit")
SPACE_IMG = pygame.transform.scale(pygame.image.load("Brown2.jpg"),(WIDTH,HEIGHT))
Shooter_Image = pygame.image.load("Shooter.png")
Shooter_1 = pygame.transform.scale(Shooter_Image,(Shooter_Width,Shooter_Height))
Shooter_2 = pygame.transform.flip(pygame.transform.scale(Shooter_Image,(Shooter_Width,Shooter_Height)),True,False)

def draw_start_menu():
    win.fill(BLACK)
    title_text = MENU_FONT.render("SHOOTER GAME", True, WHITE)
    start_text = HEALTH_FONT.render("Press 1 for 2 Player", True, WHITE)
    ai_text = HEALTH_FONT.render("Press 2 for AI Mode", True, WHITE)

    win.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 150))
    win.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 300))
    win.blit(ai_text, (WIDTH//2 - ai_text.get_width()//2, 360))
    pygame.display.update()

    waiting = True
    mode = None
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "2P"
                    waiting = False
                elif event.key == pygame.K_2:
                    mode = "AI"
                    waiting = False
    return mode

def drawWindows(S1,S2,S1_BULLET,S2_BULLET,S1_HEALTH,S2_HEALTH):
    win.blit(SPACE_IMG,(0,0))
    win.blit(Shooter_1,(S1.x,S1.y))
    win.blit(Shooter_2,(S2.x,S2.y))
    pygame.draw.rect(win,BLACK,Border)

    S1_healthtext = HEALTH_FONT.render("Health: " + str(S2_HEALTH),1,BLACK)
    S2_healthtext = HEALTH_FONT.render("Health: " + str(S1_HEALTH),1,BLACK)
    win.blit(S1_healthtext,(WIDTH - S1_healthtext.get_width()-10,10))
    win.blit(S2_healthtext,(10,10))

    for bullet in S1_BULLET:
        pygame.draw.rect(win,BLACK,bullet)
    for bullet in S2_BULLET:
        pygame.draw.rect(win,BLACK,bullet)

    pygame.display.update()

def S1_movement(S1,keys_pressed):
    if keys_pressed[pygame.K_w] and S1.y -Vel >0:
        S1.y -= Vel
    if keys_pressed[pygame.K_s] and S1.y + Vel <510:
        S1.y += Vel
    if keys_pressed[pygame.K_d] and S1.x + Vel < 530:
        S1.x += Vel
    if keys_pressed[pygame.K_a] and S1.x - Vel >0:
        S1.x -= Vel

def S2_movement(S2,keys_pressed):
    if keys_pressed[pygame.K_UP] and S2.y - Vel >0:
        S2.y -= Vel
    if keys_pressed[pygame.K_DOWN] and S2.y + Vel <510:
        S2.y += Vel
    if keys_pressed[pygame.K_RIGHT] and S2.x + Vel <1120:
        S2.x += Vel
    if keys_pressed[pygame.K_LEFT] and S2.x - Vel > 590:
        S2.x -= Vel

# 🔴 Updated: handlebullets to take dynamic Bullet_Vel
def handlebullets(S1_BULLET,S2_BULLET,S1,S2,Bullet_Vel):
    for bullet in S1_BULLET:
        bullet.x += Bullet_Vel
        if S2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(S2_HIT))
            Bullet_Hit.play()
            S1_BULLET.remove(bullet)
        elif bullet.x > WIDTH:
            S1_BULLET.remove(bullet) 
    for bullet in S2_BULLET:
        bullet.x -= Bullet_Vel
        if S1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(S1_HIT))
            Bullet_Hit.play()
            S2_BULLET.remove(bullet)
        elif bullet.x<0:
            S2_BULLET.remove(bullet)

# ... [Your Existing Imports and Variables Above Stay Same]

def winner(text):  # 🔴 This can stay for 5 sec display if needed
    draw_text = WINNER_FONT.render(text,1,BLACK)
    win.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# 🔴 Added: Game Over screen with Restart and Quit options
def draw_game_over_screen(winner_text):
    win.fill(BLACK)
    winner_message = WINNER_FONT.render(winner_text, True, WHITE)
    restart_text = HEALTH_FONT.render("Press R to Restart", True, WHITE)
    exit_text = HEALTH_FONT.render("Press Q to Quit", True, WHITE)

    win.blit(winner_message, (WIDTH//2 - winner_message.get_width()//2, HEIGHT//2 - 100))
    win.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2))
    win.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//2 + 50))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # 🔴 Restart Game
                    waiting = False
                    run()
                elif event.key == pygame.K_q:  # 🔴 Quit Game
                    pygame.quit()
                    exit()

def run():
    mode = draw_start_menu()

    pygame.init()
    S1 = pygame.Rect(100,300,Shooter_Width,Shooter_Height)
    S2 = pygame.Rect(1100,300,Shooter_Width,Shooter_Height)

    S1_BULLET = []
    S2_BULLET = []
    S1_HEALTH = 10
    S2_HEALTH = 10

    ai = None
    if mode == "AI":
        ai = AIPlayer(S2, S2_BULLET, S1)

    difficulty = DifficultyManager()

    clock = pygame.time.Clock()
    Flag = True

    while Flag:
        clock.tick(FPS)

        level_up = difficulty.update()
        Bullet_Vel = difficulty.get_bullet_speed()

        if level_up:
            level_text = WINNER_FONT.render(f"LEVEL {difficulty.get_level()}", True, BLACK)
            win.blit(level_text, (WIDTH//2 - level_text.get_width()//2, HEIGHT//2 - 100))
            pygame.display.update()
            pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Flag = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(S2_BULLET)<Max_Bullets:
                    bullet = pygame.Rect(S2.x,S2.y+S2.height//2 -2, 10,5)
                    Bullet_Fire.play()
                    S2_BULLET.append(bullet)

                if event.key == pygame.K_LCTRL and len(S1_BULLET)<Max_Bullets:
                    bullet = pygame.Rect(S1.x+30,S1.y+S1.height//2 -2, 10,5)
                    Bullet_Fire.play()
                    S1_BULLET.append(bullet) 

            if event.type == S1_HIT:
                S1_HEALTH -= 1
            if event.type == S2_HIT:
                S2_HEALTH -= 1 

        winner_text = ""
        if S1_HEALTH <= 0:
            winner_text = "Player 2 Wins !"
        if S2_HEALTH <= 0:
            winner_text = "Player 1 Wins !"

        if winner_text != "":
            # winner(winner_text)  # 🔴 Old 5 sec screen (optional)
            draw_game_over_screen(winner_text)  # 🔴 New Restart/Quit Screen
            break

        keys_pressed = pygame.key.get_pressed()
        drawWindows(S1,S2,S1_BULLET,S2_BULLET,S1_HEALTH,S2_HEALTH)
        S1_movement(S1,keys_pressed)
        if mode == "2P":
            S2_movement(S2,keys_pressed)
        elif ai:
            ai.move()
            ai.fire()
        
        handlebullets(S1_BULLET,S2_BULLET,S1,S2,Bullet_Vel)

if __name__ == "__main__":
    run()
