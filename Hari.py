import turtle

#Creating turtle screen
screen = turtle.Screen()

#Defining title of program
turtle.title("Peacock Tail")

#keeping the background color dark blue
turtle.bgcolor('#ffc233')

t = turtle.Turtle()
t.pensize(5)
t.speed(4)
t.right(20)
sw1 = 0                             #switch: sw1 = 0 for main "feather", sw1 = 1 for secondary ones 
sw2 = 0                             #secondswitch: sw2 = 0 for secondary "feather" A, = 1 for B 
for i in range(23):
    t.penup()
    t.goto(0, -120)
    t.forward(50)
    t.pendown()
    t.forward(290)
    if sw1 == 0:                    #conditional for main "feather", which has circles at tip of rib
        t.right(90)
        t.fillcolor("#006A50")
        for j in [20, 10]:
            t.begin_fill()
            t.circle(j)
            t.end_fill()
            t.fillcolor("blue")
        t.left(100)
        sw1 = 1                     #sw1 switches to 1 from 0 to avoid successive main "feathers"
    else:
        if sw2 == 0:                #conditional for secondary "feather" A, which has circles at mid rib 
            t.backward(100)
            t.right(90)
            t.fillcolor("#006A50")
            for j in [20, 10]:
                t.begin_fill()
                t.circle(j)
                t.end_fill()
                t.fillcolor("blue")
            t.left(100)
            sw1 = 0                 #sw1 switches back to 0 after a secondary "feather" is drawn 
            sw2 = 1                 #sw2 switches to 1 from 0 to avoid successive secondary "feathers" A
        else:                       #conditional for secondary "feather" B, which has circles at low rib
            t.backward(200)
            t.right(90)
            t.fillcolor("#006A50")
            for j in [20, 10]:
                t.begin_fill()
                t.circle(j)
                t.end_fill()
                t.fillcolor("blue")
            t.left(100)
            sw1 = 0                 #sw1 switches back to 0 after a secondary "feather" is drawn
            sw2 = 0                 #sw2 switches back to 0 to avoid successive secondary "feathers" B
 
 #writing a message
t.color("#00a606")
t.write("\tHappy Janmashtami!....", align ="left",font=("Script",40, "bold"))
t.hideturtle()
screen.exitonclick()
