from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Helvetica", 60, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.score_user = 0
        self.score_comp = 0
        self.update_score(self.score_user,self.score_comp)


    def update_score(self,score_user, score_comp):
        self.clear()
        self.goto(x=-60, y=210)
        self.write(f"{score_user}", True, align=ALIGNMENT, font=FONT)
        self.goto(x=60, y=210)
        self.write(f"{score_user}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)



