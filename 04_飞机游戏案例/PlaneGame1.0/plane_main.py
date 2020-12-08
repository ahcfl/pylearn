import pygame
from plane_sprites import *

# 这里的self->game对象


# 主程序飞机游戏类
class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 初始化-> 设置属性

        # 1. 创建游戏的窗口-> 使用pygame提供的display模块,调用set_mode类,进行创建
        #    size()函数主要是用来统计矩阵元素个数,或矩阵某一维上的元素个数的函数.
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2 .创建游戏的时钟-> 使用pygame提供的time模块,调用Clock类,进行创建
        self.clock = pygame.time.Clock()

        # 3. 调用私有方法-> 使用PlaneGame自定义的私有方法,完成精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件-> 创建 敌机1s 出现一次 ->调用pygame的time类set_timer方法
        #               -> 创建 子弹0.5s 发射一次
        # (eventid, milliseconds)
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)



    # 创建精灵的私有方法
    def __create_sprites(self):

        # 创建背景精灵(对象)
        # 把对象的职责封装到类的code内部, 简化外界的程序调用
        bg1 = Background()
        bg2 = Background(True)
        # 背景精灵组(对象)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组 (对象)
        # 后续要针对英雄做 碰撞检测&发射子弹-> 所以英雄需要单独定义成属性
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 启动游戏
    def start_game(self):
        print("游戏开始...")

        while True:

            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞测试
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    # 定义start_game的四个个私有方法
    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏 ->事件类型是否是pygame定义的退出事件
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 定时器判断事件 敌机到1s就刷新出来
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵(对象)因为敌机的图像已经封装在Enemy类中的初始化方法中
                # 所以创建敌机是不需要指定任何参数
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组 -> 参数是刚刚创建的敌机精灵
                self.enemy_group.add(enemy)
                # 监测 到 0.5s 自动刷新
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...") 这种方法一直按下不作用

        # 使用键盘提供的方法获取键盘按键-(定义按键元组接收获取值) -> pygame提供的key模块下的方法
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中,对应按键索引值是否为1(按下为1) ->元组对应的索引,用中括号
        if keys_pressed[pygame.K_RIGHT]:
            # 赋值(game带有的英雄属性对象)的speed属性
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed = 2
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1. 子弹摧毁敌机 ->谁是True,谁碰撞后就被销毁
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2. 敌机撞毁英雄:sprite模块的精灵碰撞方法 返回一个列表值
        enemyies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表是否有内容-> len 看出列表的长度
        if len(enemyies) > 0:

            # 让英雄牺牲
            self.hero.kill()
            # 游戏结束
            # self.__game_over()
            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新&绘制精灵组"""

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        # 参数->敌机的精灵组需要知道把每一个精灵绘制到哪一个屏幕上 / 调用draw方法,屏幕的对象->敌机精灵组
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod   # 不需要参数, 故定义__game_over为进静态method.
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


# 当一个模块被直接执行时，其__name__必然等于__main__;
# 当一个模块被引用时，其__name__必然等于文件名（不含.py）
# 如果模块是被直接运行的, 则代码块被运行，如果模块被import，则代码块不被运行.
if __name__ == '__main__':

    # 创建一个游戏对象
    game = PlaneGame()

    # 调用启动游戏方法
    game.start_game()


