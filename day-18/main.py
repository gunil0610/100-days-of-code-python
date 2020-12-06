# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst-spot-painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import random


color_list = [(226, 234, 243), (131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211)]

painter = turtle.Turtle()
painter.speed(0)
turtle.colormode(255)
painter.penup()
y_pos = -250


def draw_line():
    for _ in range(10):
        painter.dot(20, random.choice(color_list))
        painter.fd(50)


for _ in range(10):
    painter.setposition(-300, y_pos)
    draw_line()
    y_pos += 50

painter.hideturtle()

screen = turtle.Screen()
screen.exitonclick()

