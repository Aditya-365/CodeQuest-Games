from turtle import Turtle
STARTING_DISTANCE = (0,-280)
MOVE_DISTANCE = 10
FINISHING_LINE = (0,280)

class Player(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.car_speed = STARTING_DISTANCE
        self.goto(self.car_speed)

    def is_at_finish_line(self) :
        if self.ycor() > 280 :
            return True
        else :
            return False
        


    
