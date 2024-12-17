# in this file I want to do the turtle graphics challenges

# import turtle

# # 60
# for i in range(4):
#     turtle.forward(84)
#     turtle.right(90)
# turtle.exitonclick()

# # 61
# for i in range(3):
#     turtle.forward(84)
#     turtle.left(120)
# turtle.exitonclick()

# # 62
# for i in range(360 * 2):
#     turtle.forward(1 / 2)
#     turtle.left(1 / 2)
# turtle.exitonclick()

# # 63
# for color in ['red', 'blue', 'purple']:
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.color('black', color)
#     for i in range(3):
#         turtle.forward(84)
#         turtle.left(120)
#     turtle.end_fill()
#     turtle.penup()
#     turtle.forward(84 + 48)
# turtle.exitonclick()

# # 64
# for i in range(5):
#     turtle.forward(84)
#     turtle.right(144)
# turtle.exitonclick()

# # 65
# turtle.pendown()
# turtle.left(90)
# turtle.forward(48)
# turtle.penup()
# turtle.right(90)
# turtle.forward(48)
# turtle.right(90)
# turtle.forward(48)
# turtle.left(90)
# turtle.forward(48)
# turtle.pendown()
# turtle.left(180)
# turtle.forward(48)
# turtle.right(90)
# turtle.forward(24)
# turtle.right(90)
# turtle.forward(48)
# turtle.left(90)
# turtle.forward(24)
# turtle.left(90)
# turtle.forward(48)
# turtle.penup()
# turtle.right(180)
# turtle.forward(96)
# turtle.right(90)
# turtle.forward(48)
# turtle.pendown()
# turtle.left(90)
# turtle.forward(48)
# turtle.left(90)
# turtle.forward(24)
# turtle.left(90)
# turtle.forward(40)
# turtle.penup()
# turtle.right(180)
# turtle.forward(40)
# turtle.pendown()
# turtle.left(90)
# turtle.forward(24)
# turtle.left(90)
# turtle.forward(48)
# turtle.exitonclick()

# # 66
# import random
# for i in range(8):
#     color= random.choice(['red', 'blue', 'purple', 'black', 'orange', 'green'])
#     turtle.color(color)
#     turtle.forward(48)
#     turtle.left(45)
# turtle.exitonclick()

# # 67
# for i in range(10):
#     for j in range(8):
#         turtle.forward(48)
#         turtle.left(45)
#     turtle.right(36)
# turtle.exitonclick()

# # 68
# import random
# lines= random.randint(1, 48)
# for i in range(lines):
#     length= random.randint(1, 48)
#     angle= random.randint(1, 360)
#     turtle.forward(length)
#     turtle.right(angle)
# turtle.exitonclick()