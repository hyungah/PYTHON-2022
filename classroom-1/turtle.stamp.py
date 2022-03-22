import turtle as t
import random
#왼쪽 마우스를 클릭해서 도장 찍음
def screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()

    tSize = random.randrange(1, 6)
    tAngle = random.randrange(0, 361)

    t.shapesize(tSize)
    t.color(r, g, b)
    t.right(tAngle)
    t.stamp()
# 거북이 이동 함수
def screenRightClick(x, y):
    t.penup()
    t.goto(x, y)

r, g, b = 0.0, 0.0, 0.0

t.shape("turtle")

t.onscreenclick(screenLeftClick, 1)
t.onscreenclick(screenRightClick, 3)

t.done()