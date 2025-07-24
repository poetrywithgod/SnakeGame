import random
import turtle
import time

# Initial delay
delay = 0.1

# Score
score = 0
high_score = 0

# Theme customization using text input
bg_color = turtle.textinput("Theme Setup", "Enter background color (e.g. blue, black, white):") or "blue"
snake_color = turtle.textinput("Theme Setup", "Enter snake color (e.g. black, green, red):") or "black"
food_color = turtle.textinput("Theme Setup", "Enter food color (e.g. pink, yellow, orange):") or "pink"

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Victor Agi")
wn.bgcolor(bg_color)
wn.setup(width=700, height=700)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(snake_color)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(food_color)
food.penup()
food.goto(0, 100)

# Snake segments
segments = []

# Pen for displaying score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: 0 High Score: 0", align="center", font=("courier", 24, "normal"))

# Direction functions
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

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Main game loop
while True:
    wn.update()

    # Check border collision
    if head.xcor() > 330 or head.xcor() < -330 or head.ycor() > 330 or head.ycor() < -330:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset
        score = 0
        delay = 0.1
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("courier", 24, "normal"))

    # Check food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(snake_color)
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("courier", 24, "normal"))

    # Move segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check body collision
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            delay = 0.1
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score),
                      align="center", font=("courier", 24, "normal"))
            break

    time.sleep(delay)

wn.mainloop()
