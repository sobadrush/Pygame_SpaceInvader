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

class Player(pygame.sprite.Sprite):
    """ 代表玩家的太空船 """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 25)) # 50x25 的方塊
        self.image.fill(GREEN) # 綠色
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        """ 處理玩家移動 """
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -7
        if keys[pygame.K_RIGHT]:
            self.speed_x = 7
        
        self.rect.x += self.speed_x
        
        # 防止移出視窗
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # 我們等一下再來實作
        print("SHOOT!")

# --- 遊戲主程式 ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("宇宙巡航機")
clock = pygame.time.Clock()

# --- 建立 Sprite Groups ---
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(60)

    # --- 處理事件 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 按下空格鍵
                player.shoot()

    # --- 遊戲邏輯更新 ---
    all_sprites.update()

    # --- 繪圖 ---
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
