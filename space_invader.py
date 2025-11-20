import pygame
import sys
import random

# --- 常數 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



# --- 遊戲主程式 ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("宇宙巡航機")
clock = pygame.time.Clock()

# --- 建立 Sprite Groups ---
all_sprites = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)

running = True
while running:
    clock.tick(60)

    # --- 處理事件 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # player.shoot()
                pass

    # --- 遊戲邏輯更新 ---
    all_sprites.update()

    # --- 繪圖 ---
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
