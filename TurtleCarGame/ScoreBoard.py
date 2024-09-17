from turtle import Turtle 
ALIGN = "center"
FONT = ("Arial",24,"normal")
MOVE = False

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230,250)
        self.write(arg=f"Level : {self.level}",move=MOVE,align=ALIGN,font=FONT)

    def increase_level(self) :
        self.clear()
        self.level += 1
        self.write(arg=f"Level : {self.level}",move=MOVE,align=ALIGN,font=FONT)

    def game_over(self) :
        self.goto(0 ,0)
        self.write(arg="GAME OVER",move=MOVE,align=ALIGN,font=FONT)