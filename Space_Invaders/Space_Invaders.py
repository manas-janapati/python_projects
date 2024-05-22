import pygame
import sys
import random

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 5
INITIAL_ENEMY_SPEED = 1
ENEMY_SPEED_INCREMENT = 0.1  # Amount by which enemy speed increases per second
WIN_CONDITION = 50  # Adjust as desired

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
player_img = pygame.image.load('player.png')
player_rect = player_img.get_rect()
player_rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
enemy_img = pygame.image.load('enemy.png')
bullet_img = pygame.image.load('bullet.png')

# Load sounds
shoot_sound = pygame.mixer.Sound('shoot.wav')
enemy_hit_sound = pygame.mixer.Sound('enemy_hit.wav')
player_hit_sound = pygame.mixer.Sound('player_hit.wav')

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = player_rect
        self.score = 0
        self.shoot_delay = 250  # Bullet firing rate in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

        # Auto-fire bullets
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = INITIAL_ENEMY_SPEED

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Main loop
running = True
clock = pygame.time.Clock()
wins = 0
start_time = pygame.time.get_ticks()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds

    # Increase enemy speed gradually
    if elapsed_time > 0:
        for enemy in enemies:
            enemy.speedy = INITIAL_ENEMY_SPEED + elapsed_time * ENEMY_SPEED_INCREMENT

    # Spawn new enemy
    if len(enemies) < 5:  # Adjust the number of enemies on the screen
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Check bullet-enemy collisions
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        enemy_hit_sound.play()
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        player.score += 1

    # Check if the player has won
    if player.score >= WIN_CONDITION:
        wins += 1
        player.score = 0
        pygame.mixer.music.stop()
        font = pygame.font.Font(None, 36)
        win_text = font.render("You won!", True, WHITE)
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(win_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before closing
        running = False

    # Check if any enemy reached the bottom end of the screen
    for enemy in enemies:
        if enemy.rect.top > SCREEN_HEIGHT:
            pygame.mixer.music.stop()
            font = pygame.font.Font(None, 36)
            lose_text = font.render("You lose!", True, WHITE)
            text_rect = lose_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(lose_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds before closing
            running = False
            break  # Stop checking further enemies

    # Check player-enemy collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        player_hit_sound.play()
        player.score -= 1

    # Show score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {player.score}', True, WHITE)
    wins_text = font.render(f'Wins: {wins}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(wins_text, (10, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()
