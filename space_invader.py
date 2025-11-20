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

    def shoot(self, all_sprites_group, bullets_group):
        """ 發射子彈 """
        new_bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites_group.add(new_bullet) # 動態添加子彈到 Sprite Group
        bullets_group.add(new_bullet) # 動態添加子彈到 Bullet Group


# --- 新增 Bullet 類別 ---
class Bullet(pygame.sprite.Sprite):
    """ 代表玩家發射的子彈 """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15)) # 5x15 的方塊
        self.image.fill(WHITE) # 白色
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        """ 移動子彈 """
        self.rect.y += self.speed_y
        # 飛出畫面頂端就刪除
        if self.rect.bottom < 0:
            self.kill()


# --- 新增 Enemy 類別 ---
class Enemy(pygame.sprite.Sprite):
    """ 代表敵人的太空船 """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30)) # 30x30 的方塊
        self.image.fill(RED) # 紅色
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 2 # 敵人會左右移動

    def update(self):
        """ 左右移動 """
        self.rect.x += self.speed_x
        # 簡易的邊界反彈
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x *= -1
            self.rect.y += 10 # 碰壁時下降一點


# --- 遊戲主程式 ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("宇宙巡航機")
clock = pygame.time.Clock()

# --- 建立 Sprite Groups ---
all_sprites = pygame.sprite.Group()

bullets = pygame.sprite.Group() # 存放所有子彈
enemies = pygame.sprite.Group() # 存放所有敵人

player = Player()
all_sprites.add(player)

# --- 產生敵人 ---
for row in range(3): # 3 排
    for col in range(8): # 8 欄
        enemy = Enemy(col * 60 + 50, row * 40 + 50)
        all_sprites.add(enemy) # 動態添加敵人到 Sprite Group
        enemies.add(enemy) # 動態添加敵人到 Enemy Group

running = True
while running:
    clock.tick(60)

    # --- 處理事件 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 按下空格鍵
                player.shoot(all_sprites, bullets)

    # --- 遊戲邏輯更新 ---
    all_sprites.update()

    # --- 碰撞偵測 ---
    # 檢查子彈是否打中敵人
    # groupcollide 會回傳一個字典，告訴我們哪些敵人被擊中
    # 兩個 True 表示子彈和敵人在碰撞後都「消失」 (kill)
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    print(f">>> hits: {hits}") # 觀察一下會打印什麼

    # --- 繪圖 ---
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
