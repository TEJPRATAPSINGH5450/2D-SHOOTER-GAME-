import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 2
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter Game")

# Load images
player_image = pygame.Surface((50, 50))
player_image.fill(GREEN)
bullet_image = pygame.Surface((5, 10))
bullet_image.fill(WHITE)
enemy_image = pygame.Surface((50, 50))
enemy_image.fill(RED)

# Player class
class Player:
    def __init__(self):
        self.rect = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def move(self, dx, dy):
        self.rect.x += dx * PLAYER_SPEED
        self.rect.y += dy * PLAYER_SPEED
        # Keep player on screen
        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y))

    def draw(self):
        screen.blit(player_image, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = bullet_image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        screen.blit(bullet_image, self.rect)

# Enemy class
class Enemy:
    def __init__(self):
        self.rect = enemy_image.get_rect(center=(random.randint(0, SCREEN_WIDTH), 0))

    def update(self):
        self.rect.y += ENEMY_SPEED

    def draw(self):
        screen.blit(enemy_image, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    bullets = []
    enemies = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        player.move(dx, dy)

        # Shooting bullets
        if keys[pygame.K_SPACE]:
            if len(bullets) < 10:  # Limit the number of bullets
                bullets.append(Bullet(player.rect.centerx, player.rect.top))

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Spawn enemies
        if random.randint(1, 30) == 1:  # Adjust spawn rate
            enemies.append(Enemy())

        # Update enemies
        for enemy in enemies[:]:
            enemy.update()
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies.remove(enemy)

        # Draw everything
        screen.fill(BLACK)
        player.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()