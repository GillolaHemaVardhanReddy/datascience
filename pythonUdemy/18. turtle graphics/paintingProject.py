import colorgram as cg
from turtle import Turtle,Screen
import turtle as t
import random as rd
from challenges import moveToStart


# colorgram.extract(image, number_of_colors)
def collectColors():
    rgbColor = []
    x = cg.extract("hirst.jpg", 30)
    for color in x:
        rgbColor.append((color.rgb.r,color.rgb.g,color.rgb.b))
    return rgbColor
# print(collectColors())
collected_colors = [(199, 162, 114), (54, 92, 138), (143, 164, 187), (147, 76, 55), (222, 207, 114), (186, 183, 20), (138, 67, 86), (193, 152, 168), (126, 190, 158), (209, 87, 67), (52, 23, 36), (173, 14, 7), (149, 22, 37), (41, 43, 64), (196, 83, 93), (30, 25, 12), 
(47, 56, 99), (33, 125, 92), (227, 175, 165), (26, 171, 147), (220, 172, 193), (150, 214, 185), (15, 102, 58), (62, 78, 28), (113, 113, 162), (36, 56, 36)] 

# painting rules
# 10 rows and 10 columns of dots
# each dot must be of around 20 in size and spaced apart 50 in size

pencil = Turtle()

t.colormode(255)

pencil.penup()
pencil.setheading(225)
pencil.forward(250)
pencil.setheading(0)
pencil.speed(0)

# pencil.dot(size,color)
for i in range(10):
    for j in range(10):
        pencil.dot(20,rd.choice(collected_colors))
        pencil.forward(50)
    moveToStart(pencil) if i<9 else None


screen = Screen()
screen.exitonclick()