import random
import turtle
#turtle is a builtin module of python which is used to draw on canvas

import time
#these are the necessary libraries for this game

delay = 0.1
score, high_score = 0, 0

# we have initialized above variables to 0
# turtle.screen() is method which enables us to configure the screen properties

sd = turtle.Screen()
sd.title("Snake Game by Adarsh")
sd.bgcolor("blue")
sd.setup(width=600, height=600)

#after configuring the screen lets configure the head of snake

sd.tracer(0)
head = turtle.Turtle()
head.speed(0)
#initializing speed to 0 initially
head.shape("square")
#here I have made the shape of head as square but I can also make other shapes as circle
head.color("black")
#making the color of head as black
head.penup()
#penup method is used to pick up the total without leaving tracks when the error exception handling occurs

#now let's configure the food which the snake is going to eat

head.goto(0,0)
#placing at origin
head.direction = "stop"

item = turtle.Turtle()
item.speed(0)
#as item should be constant at a place
item.shape("circle")
#giving shape to the food of snake
item.color("red")
item.penup()
item.goto(0,100)

#here penup method tells to leave the  ink on the screen
#it'll go upto the range of 100
#pen is the method containing dictionary with some keys and it is assigning to turtle.Turtle()
#when snake catches or eats it's food it'll add a square to it
#color of that square is white and penup is used to add other items

new_layer = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()

pen.hideturtle()
#it will hide the turtle and it describes the size, alignment and fontsize of score and highscore

pen.goto(0,260)
pen.write("SCORE: 0, HIGH SCORE: 0", align = "center", font = ("Courier", 24 , "normal"))

#method to go up but it should only work when head is not down as it is not possible to go up when head is down
def go_up():
    if head.direction != "down":
        head.direction = "up"

#same like other methods these are other methods to go in other directions
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

    # if head is moving up then get the y coordinate of y and increment in necessary direction by some value say 20
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    #similarily do for the other directions
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


#taking the input from the keyboard and calling required funtion based on it
sd.listen()
sd.onkeypress(go_up,"w")
sd.onkeypress(go_down,"s")
sd.onkeypress(go_left,"a")
sd.onkeypress(go_right,"d")

#main game starts here , when true the game proceeds
while True:
    sd.update()
    #update method is used to update the levels of the game

    #checking for collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #if collided go sleep for one second , go to center and stop

        #hiding the layers
        for i in new_layer:
            i.goto(1000,1000)

        #it will clear the screen and let's score to 0 and delay to 0.1
        new_layer.clear()

        score = 0
        delay = 0.1

        pen.clear()
        #it will clear the turtles from the screen
        pen.write("SCORE: {} HIGH SCORE: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        #it will write the score

        #if distance is less than 20 then move the item to random spot on scree
    if head.distance(item) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        item.goto(x,y)

        #now we need to add layer with the shape square and grey color and it will append the new layer
        layer_1 = turtle.Turtle()
        layer_1.speed(0)
        layer_1.shape("square")
        layer_1.color("grey")
        layer_1.penup()
        new_layer.append(layer_1)

        #shorten the delay
        delay -= 0.001

        #every time snake catches item score is increased by 10 points and if it higher than highscore
        #then high score is updated then will delete the screen and return and display the score and
        #high score

        score += 10
        if (score > high_score):
            high_score = score

        pen.clear()
        pen.write("SCORE: {} HIGH SCORE: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    #below for loop is used to move the end layers first in the reverse order
    #it will move layer 0 at the head when length of the layer is greater than zero

    for i in range(len(new_layer)-1, 0, -1):
        x = new_layer[i-1].xcor()
        y = new_layer[i-1].ycor()
        new_layer[i].goto(x,y)

    if len(new_layer) > 0:
        x = head.xcor()
        y = head.ycor()
        new_layer[0].goto(x,y)

    move()
    #move method is used to move from one location to another and return the destination

        #below code checks for the head collsion with body layers if the distance is less than 20 and collided
        #after that it will stop
    for i in new_layer:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #below for loop hides the layer and resets score and delay

            for i in new_layer:
                i.goto(10000,10000)

            new_layer.clear()
            score = 0
            delay = 0.1

            #clear the screen and display the new score
            pen.clear()
            pen.write("SCORE: {} HIGH SCORE: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    time.sleep(delay)

sd.mainloop()
