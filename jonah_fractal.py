from turtle import *
import random

def main():

    dots = int(input("How many dots? "))

    setup(500, 500)
    bgcolor("black")
    hideturtle()
    tracer(False)

    draw_dots(dots)
    
    tracer(True)
    exitonclick()

# define function to take in integer of how many points
def draw_dots(n):
    colours = ["red", "orange", "yellow", "green", "blue", "purple"]
    

    for i in range(n):
        penup()
       
        # something to go to half of a corner...
        goto(new_coord())

        new_colour = random.choice(colours)

        pencolor(new_colour)

        dot(size=1)

def new_coord():
    corners = {
        "a": [-250, -250],
        "b": [0, 250],
        "c": [250, -250]
    }

    corner = random.choice(list(corners.values()))

    x1, y1 = position()

    # x&y coordinates to subtract the position from
    x2 = corner[0]
    y2 = corner[1]
    
    x = (x1 - x2) / 2
    y = (y1 - y2) / 2

    new = (x, y)

    return new



                

if __name__ == "__main__":
    main()