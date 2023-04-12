# Program which emulates the snake game

# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
my_window = turtle.Screen()
my_window.title("Python Game")
my_window.bgcolor("grey")
# the width and height can be put as user's choice
my_window.setup(width=600, height=600)
my_window.tracer(0)

# prey in the game
prey = turtle.Turtle()
colors = random.choice(['white'])
shapes = random.choice(['circle'])
prey.speed(0)
prey.shape(shapes)
prey.color(colors)
prey.penup()
prey.goto(0, 100)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Current Score : 0  Best Score : 0", align="center",
          font=("sans", 24, "bold"))


# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def left():
    if head.direction != "right":
        head.direction = "left"


def right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y_coord = head.ycor()
        head.sety(y_coord + 20)
    if head.direction == "down":
        y_coord = head.ycor()
        head.sety(y_coord - 20)
    if head.direction == "left":
        x_coord = head.xcor()
        head.setx(x_coord - 20)
    if head.direction == "right":
        x_coord = head.xcor()
        head.setx(x_coord + 20)


my_window.listen()
my_window.onkeypress(group, "w")
my_window.onkeypress(down, "s")
my_window.onkeypress(left, "a")
my_window.onkeypress(right, "d")
segments = []

# Main Gameplay
while True:
    my_window.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Current Score : {}  Best Score : {} ".format(
            score, high_score), align="center", font=("sans", 24, "bold"))
    if head.distance(prey) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        prey.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Current Score : {}  Best Score : {} ".format(
            score, high_score), align="center", font=("sans", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Current Score : {}  Best Score : {} ".format(
                score, high_score), align="center", font=("sans", 24, "bold"))
    time.sleep(delay)

my_window.mainloop()
