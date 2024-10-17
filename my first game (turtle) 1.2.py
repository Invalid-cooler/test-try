# game "Hit the target"
from turtle import *
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
level = int(input("enter the level (1-4): "))
if level == 1:
    TARGET_LLEFT_X = 100
    TARGET_LLEFT_Y = -175
elif level == 2:
    TARGET_LLEFT_X = 100
    TARGET_LLEFT_Y = 250
elif level == 3:
    TARGET_LLEFT_Y = 100
    TARGET_LLEFT_X = 250
elif level == 4:
    TARGET_LLEFT_Y = -250
    TARGET_LLEFT_X = 200
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# adjust the screen.
setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# draw the turger.
hideturtle()
speed(0)
penup()
goto(280, 0)
write("0")
goto(-290, 0)
write("180")
goto(0, 280)
write("90")
goto(0, -290)
write("270")
goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
pendown()
fillcolor("red")
begin_fill()
setheading(EAST)
forward(TARGET_WIDTH)
setheading(NORTH)
forward(TARGET_WIDTH)
setheading(WEST)
forward(TARGET_WIDTH)
setheading(SOUTH)
forward(TARGET_WIDTH)
end_fill()
penup()

# center the turtle.
goto(0, 0)
pensize(+1)
dot(10)
pencolor("orange")
setheading(EAST)
showturtle()
speed(PROJECTILE_SPEED)

# get the shooting angle and power.
angle = float(input("enter a shooting engle: "))
force = float(input("enter a starting force (1-10): "))

# calculate distance
distance = force * FORCE_FACTOR

# set direction
setheading(angle)

# launch a projectile
pendown()
forward(distance)

# did the projectile hit the target?
if (xcor() >= TARGET_LLEFT_X and
    xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    ycor() >= TARGET_LLEFT_Y and
    ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("YOU WIN")
else:
    print("YOU LOOSE")
print(TARGET_WIDTH, TARGET_LLEFT_X)
done()
