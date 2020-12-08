import random
import pygame

# 设定屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机刷新事件的定时器常量, USEREVENT是pygame提供的 用户事件常量(整数)
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 这里的self-> 精灵对象
# 创建 精灵类 调用pygame提供的精灵父类的Sprite方法
class GameSprite(pygame.sprite.Sprite):
    """飞机大战的游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 主动调用父类的初始化方法,继承父类的方法
        super().__init__()

        # 定义对象属性
        # 加载精灵图片
        self.image = pygame.image.load(image_name)
        # 自动获取精灵位置
        self.rect = self.image.get_rect()
        # 设定精灵速度
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


# 父类提供的方法不能满足子类的需求, 从父类派生出一个子类,在子类中重写父类的方法,
# 根据子类的需求,对父类的方法进行扩展 -> 继承
class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1. 调用父类方法实现精灵创建(image/rect/speed)属性
        # super()特殊对象 主动调用 父类初始化方法 并且指定背景精灵需要显示的图像
        super().__init__("./images/background.png")

        # 2.(扩展方法) 判断是否是交替图像, 如果True,则需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1. 调用父类的方法实现 -> 让bg在屏幕的垂直方向上移动
        super().update()

        # 2. (扩展方法) 判断是否移除屏幕,if移出屏幕,将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """游戏敌机精灵"""

    def __init__(self):

        # 1. 调用父类方法,创建敌机精灵,同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2.(扩展初始方法speed属性) 指定敌机的初始随机速度
        # -> 使用random模块调用randit方法:产生均匀分布的随机整数矩阵1~3
        self.speed = random.randint(1, 3)

        # 3. (扩展初始方法rect属性)指定敌机的初始随机位置
        # y = bottom - height / x = 屏幕宽度 - 敌机宽度
        self.rect.bottom = 0

        # 定义一个 -> 最大x值的全局变量: max_x , x最小为0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1. 调用父类方法, 保持垂直方法飞行
        super().update()

        # 2.(扩展update方法) 判断是否飞出屏幕,如果True->从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("enemy飞出屏幕,需要从精灵组删除...")

            # pygame提供的精灵类中,封装了kill方法
            # 让某一个敌机精灵自动调用kill方法,
            # 就可以把这个精灵从所有的精灵组中一次性删除,同时也从内存中销毁
            self.kill()

    # 在程序结束后自动运行
    def __del__(self):
        # print("敌机销毁了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """游戏英雄精灵"""

    def __init__(self):

        # 1. 调用父类方法,设置image&speed,hero初始不移动->speed=0
        super().__init__("./images/me1.png", 0)

        # 2. 设置英雄的初始位置 使用pygame.Rect提供的centerx属性
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3. 创建子弹的精灵组(为hero的属性)-> 为了self.fire()
        self.bullets = pygame.sprite.Group()

    def update(self):

        # pygame提供的key模块下的方法
        # -> 使用键盘提供的方法获取键盘按键-(定义按键元组接收获取值(0,1))
        keys_pressed = pygame.key.get_pressed()

        # 英雄在水平方向移动
        if keys_pressed[pygame.K_RIGHT] == 1 \
                or keys_pressed[pygame.K_LEFT] == 1:

            self.rect.x += self.speed
            if self.rect.x < 0:
                self.rect.x = 0
            # elif self.rect.x > 480 - 102:
            #     self.rect.x = 378
            # right是pygame.Rect类中的属性
            elif self.rect.right > SCREEN_RECT.right:
                self.rect.right = SCREEN_RECT.right

        elif keys_pressed[pygame.K_UP] == 1 \
                or keys_pressed[pygame.K_DOWN] == 1:

            super().update()
            if self.rect.y < 0:
                self.rect.y = 0
            # elif self.rect.y > 700 - 126:
            #     self.rect.y = 574
            # bottom同上
            elif self.rect.bottom > SCREEN_RECT.bottom:
                self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print("发射子弹...")
        for i in (0, 1,):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵位置 这里的self是英雄 y初始在top
            bullet.rect.bottom = self.rect.y - i * 20
            # 水平中心点保存一致->子弹在hero的正上方
            bullet.rect.centerx = self.rect.centerx
            # 3. 将精灵添加到精灵组
            # 在fire() 方法 里 定义的 英雄实例属性
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        # 调用父类方法,设置子弹图片(image),设置初始速度(speed)
        super().__init__("./images/bullet1.png", -2)

    def update(self):

        # 调用父类方法,让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):

        print("子弹销毁...")