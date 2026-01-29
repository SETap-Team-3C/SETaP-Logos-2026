import turtle

def draw_t(turtle_obj, start_x, start_y):
    turtle_obj.penup()
    turtle_obj.goto(start_x, start_y)
    turtle_obj.pendown()
    turtle_obj.fillcolor("lightblue")
    turtle_obj.begin_fill()
    turtle_obj.goto(start_x + 100, start_y)      
    turtle_obj.goto(start_x + 100, start_y - 15)      
    turtle_obj.goto(start_x + 60, start_y - 15)      
    turtle_obj.goto(start_x + 60, start_y - 100)     
    turtle_obj.goto(start_x + 40, start_y - 100)    
    turtle_obj.goto(start_x + 40, start_y - 15)     
    turtle_obj.goto(start_x, start_y - 15)  
    turtle_obj.goto(start_x, start_y)
    turtle_obj.end_fill()

t = turtle.Turtle()
t.pensize(5)
draw_t(t, -280, 50)
turtle.done()