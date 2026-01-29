import turtle as t

def setup():
    t.speed(0)
    t.bgcolor("white")
    t.color("grey")
    t.hideturtle()

def jump(x, y):
    """Helper to move turtle without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_hanger_around_text():
    t.pensize(5) 
    start_x = 0
    start_y = 200 
    
    jump(start_x, start_y)
    t.setheading(90)   
    t.forward(50)      
    t.circle(45, 230)  
    

    t.pensize(5)      
    
    jump(start_x, start_y)
    t.setheading(205) 
    t.forward(320)     
    
    t.setheading(0)   
    t.forward(60)     
    
    jump(start_x, start_y)
    t.setheading(335) 
    t.forward(320)     
    t.setheading(180)  
    t.forward(60)      

if __name__ == "__main__":
    setup()
    draw_hanger_around_text()
    t.done()