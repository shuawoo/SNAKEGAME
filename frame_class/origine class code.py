# 初始框架
import random
from pygame import *

# 基础窗口数值（许多类中用的到，所以设成全局变量）
W = 800
H = 600
ROW = 30
COL = 40


# 基础方格类，用于生成方格
class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)


# 蛇头类
class SnakeHead:
    row = int(ROW / 2)
    col = int(COL / 2)
    head = Point(row=row, col=col)
    direct = 'left'

    def __init__(self, window):
        self.window = window
        pass

    def head_move(self):
        if self.direct == 'left':
            self.head.col -= 1
        elif self.direct == 'right':
            self.head.col += 1
        elif self.direct == 'up':
            self.head.row -= 1
        elif self.direct == 'down':
            self.head.row += 1
        pass


# 蛇身类
class SnakeBody:
    headBFollow = SnakeHead
    body = [
        Point(row=headBFollow.head.row, col=headBFollow.head.col + 1),
        Point(row=headBFollow.head.row, col=headBFollow.head.col + 2),
        Point(row=headBFollow.head.row, col=headBFollow.head.col + 3)
    ]

    def __init__(self, window):
        self.window = window

    def body_move_i(self):
        self.body.insert(0, self.headBFollow.head.copy())

    def body_move_o(self):
        self.body.pop()

    def normal_move(self):
        self.body_move_i()
        self.body_move_o()

    def body_add(self):
        self.body_move_i()
        # 优化蛇头吃到食物后蛇头消失一下的情况（实际上只是加快了一下，并没有解决）
        if self.headBFollow.direct == 'left':
            self.headBFollow.head.col -= 1
        elif self.headBFollow.direct == 'right':
            self.headBFollow.head.col += 1
        elif self.headBFollow.direct == 'up':
            self.headBFollow.head.row -= 1
        elif self.headBFollow.direct == 'down':
            self.headBFollow.head.row += 1


# 食物类
class Food:
    row = random.randint(1, ROW - 1)
    col = random.randint(1, COL - 1)
    pos = Point(row=row, col=col)
    snakes = SnakeBody

    def __init__(self, window):
        self.window = window

    def creat(self):
        self.pos = Point(row=random.randint(1, ROW - 1), col=random.randint(1, COL - 1))
        for i in self.snakes.body:
            if i.row == self.pos.row and i.col == self.pos.col:
                self.creat()
                pass
            pass


# 画出方格
def rect(self, color, window):
    # 行宽和列宽
    cell_width = W / COL
    cell_height = H / ROW
    # 左边宽度是列数*行宽，上面宽度是行数*列宽
    left = self.col * cell_width
    top = self.row * cell_height
    # 画出方格
    draw.rect(
        window, color,
        [left, top, cell_width, cell_height]
    )
    pass


# 键盘控制监听
def key_control(snake_obj):
    for i in event.get():
        if i.type == QUIT:
            exit()
            pass
        elif i.type == KEYDOWN:
            if i.key == K_w or i.key == K_UP:
                if snake_obj.direct == 'left' or snake_obj.direct == 'right':
                    snake_obj.direct = 'up'
            elif i.key == K_s or i.key == K_DOWN:
                if snake_obj.direct == 'left' or snake_obj.direct == 'right':
                    snake_obj.direct = 'down'
            elif i.key == K_a or i.key == K_LEFT:
                if snake_obj.direct == 'up' or snake_obj.direct == 'down':
                    snake_obj.direct = 'left'
            elif i.key == K_d or i.key == K_RIGHT:
                if snake_obj.direct == 'up' or snake_obj.direct == 'down':
                    snake_obj.direct = 'right'
        pass


# 失败检测
def failure_check(snake_h, snake_b):
    failed = False
    # 1.撞墙
    if snake_h.head.col < 0 or snake_h.head.row < 0 or snake_h.head.col >= COL or snake_h.head.row >= ROW:
        failed = True
        pass

    # 2.撞自己
    for i in snake_b.body:
        if snake_h.head.col == i.col and snake_h.head.row == i.row:
            failed = True
            break
        pass
    return failed


# 主函数
def main():
    # 初始化
    init()
    # 设置窗口大小
    size = (W, H)
    window = display.set_mode(size)
    # 设置标题
    display.set_caption('贪吃蛇')
    # 设置颜色
    bg_color = (255, 255, 255)
    head_color = (0, 128, 128)
    snake_color = (200, 200, 200)
    food_color = (255, 255, 0)

    # 创建各类对象
    snake_head = SnakeHead(window)

    snake_body = SnakeBody(window)
    snake_body.headBFollow = snake_head

    food_obj = Food(window)
    food_obj.snakes = snake_body

    clock = time.Clock()

    # 游戏循环
    while True:
        # 检测蛇头移动
        key_control(snake_head)

        # 检测蛇头是否与食物坐标一致
        if snake_head.head.row == food_obj.pos.row and snake_head.head.col == food_obj.pos.col:
            # 若一致则重新生成食物，并增长蛇身
            food_obj.creat()
            snake_body.body_add()
            pass
        snake_body.normal_move()
        snake_head.head_move()

        if failure_check(snake_head, snake_body):
            exit()
            pass

        # 渲染——画出来
        # 背景,rect用来画窗口
        draw.rect(window, bg_color, (0, 0, W, H))

        # 蛇头
        rect(snake_head.head, head_color, window)
        # 蛇身
        for i in snake_body.body:
            rect(i, snake_color, window)
            pass
        # 食物
        rect(food_obj.pos, food_color, window)

        # 交还控制权给系统，让系统完成渲染
        display.update()

        # 设置帧频（锁帧），等于1000ms/帧数
        clock.tick(10)
        pass
    pass


if __name__ == '__main__':  # 固定搭配
    main()