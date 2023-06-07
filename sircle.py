import turtle
w = turtle.Screen()
w.bgcolor('black')
color = ['white','gray','gray1','gray2','gray3','gray4']
color2 = ['red','red4']
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1.5)
for i in range(50):
    t.pencolor(color[i%2])
    t.circle(90)
    t.right(i)
    t.fd(i)
turtle.mainloop()