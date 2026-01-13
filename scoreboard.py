from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode = 'r+') as data:
            self.high_score = int(data.read())
        self.color("#1A1A1A")
        self.hideturtle()
        self.penup()
        self.goto(x =0, y = 270 )
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score:,}. High Score: {self.high_score:,}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score()
    def reset_score(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as data:
                self.high_score = self.score
                data.write(f"{self.high_score}")

        self.score = 0


    def game_over(self):
        self.goto(0,0)
        self.color('DarkSlateBlue')
        self.write("Game Over", align=ALIGNMENT, font=FONT)