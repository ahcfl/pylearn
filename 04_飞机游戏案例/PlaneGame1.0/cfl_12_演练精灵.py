import pygame
from plane_sprites import *

# 游戏的初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")
# 2> 绘制在屏幕
screen.blit(bg, (0, 0))

# 绘制英雄图像
# 1> 加载图像
hero = pygame.image.load("./images/me1.png")
# 2> 绘制在屏幕
screen.blit(hero, (150, 300))

# 3> 更新显示 - update 方法会把之前所有绘制的结果，一次性更新到屏幕窗口上
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机精灵 speed 默认是1
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环 -> 意味着游戏的正式开始
while True:

    # 可以指定循环体内部代码执行的频率
    # 1/60s切换一帧图像
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型 是否是退出事件
        if event.type == pygame.QUIT:
            print("退出游戏...")

            # quit 卸载所以模块
            pygame.quit()

            # 退出系统
            exit()
    # 2. 修改飞机的位置 大概1s移动一个坐标距离
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3. 调用blit绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update
    enemy_group.update()
    # draw
    enemy_group.draw(screen)

    # 4. 调用update方法更新显示
    pygame.display.update()

    pass

pygame.quit()







