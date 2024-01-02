import turtle

t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'white', 'violet', 'indigo']

for i in range(160):
    t.color(colors[i % 8])
    t.circle(100)
    t.right(200)

t.hideturtle()
turtle.exitonclick()
