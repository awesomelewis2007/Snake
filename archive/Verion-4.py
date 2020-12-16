
# Simple Snake Game in Python 3 for Beginners

import turtle
import time
import random

delay = 0.1


# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#border A

border_a = turtle.Turtle()
border_a.speed(0)
border_a.shape("square")
border_a.color("red")
border_a.shapesize(stretch_wid=30, stretch_len=1)
border_a.penup()
border_a.goto(-299, 0)


#border B

border_b = turtle.Turtle()
border_b.speed(0)
border_b.shape("square")
border_b.color("red")
border_b.shapesize(stretch_wid=30, stretch_len=1)
border_b.penup()
border_b.goto(290, 0)


#border C

border_c = turtle.Turtle()
border_c.speed(0)
border_c.shape("square")
border_c.color("red")
border_c.shapesize(stretch_wid=30, stretch_len=1)
border_c.penup()
border_c.left(90)
border_c.goto(0, -299)


#border D

border_d = turtle.Turtle()
border_d.speed(0)
border_d.shape("square")
border_d.color("red")
border_d.shapesize(stretch_wid=30, stretch_len=1)
border_d.penup()
border_d.left(90)
border_d.goto(0, 299)
segments = []

#uix adons
uiadd = turtle.Turtle()
uiadd.color("white")
uiadd.hideturtle()
uiadd.penup()
uiadd.goto(350,200)
uiadd.write("SNAKE",font=(r'consolas', 30))
uiadd.goto(350,190)
uiadd.write("awesomelewis2007",font=(r'consolas', 10))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        shapexy = random.randint(1,3)
        if shapexy == 1:
            food.shape("square")
        if shapexy == 2:
            food.shape("triangle")
        if shapexy == 3:
            food.shape("circle")
        colours = ["red","green","blue","gold"]
        coloursxx = random.choice(colours)
        food.color(coloursxx)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("skyblue1")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()


    time.sleep(delay)

wn.mainloop()