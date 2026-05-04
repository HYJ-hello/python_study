num = 0
print("num的初始值是",num)
flag = int(input("请输入一个整数："))
for i in range(flag):
    print(flag)
    flag-=1


import turtle
p = turtle.Pen()
p.speed(0)
p.pensize(10)
p.color("red")
p.forward(100)
p.circle(80)
r = int(input("请输入圆的半径："))

def draw_circle(r):
    p.circle(r)
draw_circle(r)
turtle.done()