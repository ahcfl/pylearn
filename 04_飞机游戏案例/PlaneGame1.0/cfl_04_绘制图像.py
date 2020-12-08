import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
# 1> 加载图像数据
screen.blit(bg, (0, 0))
# 2> blit 绘制图像
pygame.display.update()
# 3> update 更新屏幕显示

while True:

    pass

pygame.quit()


