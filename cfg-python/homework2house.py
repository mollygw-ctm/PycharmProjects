import turtle

def roof():
    side_length = 200
    angle = 120
    turtle.color('red')
    turtle.begin_fill()
    for side in range(3):
        turtle.forward(side_length)
        turtle.left(angle)
    turtle.end_fill()
roof()

def building():
    side_length = 200
    angle = 90
    turtle.color('yellow')
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.end_fill()

building()

def doortravel():
    turtle.color('yellow')
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(75)
doortravel()

def door():
    angle = 90
    turtle.color("brown")
    turtle.begin_fill()

    turtle.left(angle)
    turtle.forward(90)
    turtle.right(angle)
    turtle.forward(50)
    turtle.right(angle)
    turtle.forward(90)
    turtle.end_fill()
door()

# travel to bottom right window
def window4travel():
    turtle.color('yellow')
    turtle.right(180)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(10)
window4travel()

def window():
    side_length = 50
    angle = 90
    turtle.color("dark blue")
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.forward(25)
    turtle.right(angle)
    turtle.forward(side_length)
    turtle.right(angle)
    turtle.forward(25)
    turtle.right(angle)
    turtle.forward(25)
    turtle.right(angle)
    turtle.forward(side_length)
window()

#travel to top right window
def window3travel():
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.color("yellow")
    turtle.forward(30)
window3travel()

window()

# travel to top left window
def window2travel():
    turtle.left(90)
    turtle.forward(25)
    turtle.color("yellow")
    turtle.forward(70)
    turtle.left(90)
window2travel()
window()

# travel to bottom left window
def window1travel():
    turtle.left(90)
    turtle.forward(25)
    turtle.color("yellow")
    turtle.right(90)
    turtle.forward(25)
window1travel()
window()

# travel to garden
def gardentravel():
    turtle.color("yellow")
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.color("green")
    turtle.forward(200)

gardentravel()

def grass():
    turtle.color("green")
    turtle.begin_fill()
    side_length = 50
    angle = 120
    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.end_fill()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180)
grass()
grass()
grass()
grass()
grass()

