#Create 3 doors with 2 hidden goats and 1 cars behind them

from manim import *

class CreateDoors(Scene):
    def construct(self):
        door1 = Rectangle(height=2, width=1, color=BLUE)
        door2 = Rectangle(height=2, width=1, color=BLUE)
        door3 = Rectangle(height=2, width=1, color=BLUE)

        door1.shift(LEFT*2)
        door2.shift(RIGHT*2)
        door3.shift(LEFT*2)

        doors = VGroup(door1, door2, door3)
        doors.arrange(RIGHT, buff=2)

        self.play(Create(doors))
        self.wait(2)

        #make door 1 bigger, turn red
        runtime = 0.4
        self.play(Transform(door1, door1.copy().set_color(RED).scale(1.20), run_time=runtime))
        self.play(Transform(door1, door1.copy().set_color(BLUE).scale(100/120), run_time=runtime))

        self.play(Transform(door2, door2.copy().set_color(RED).scale(1.20), run_time=runtime))
        self.play(Transform(door2, door2.copy().set_color(BLUE).scale(100/120), run_time=runtime))

        self.play(Transform(door3, door3.copy().set_color(RED).scale(1.20), run_time=runtime))
        self.play(Transform(door3, door3.copy().set_color(BLUE).scale(100/120), run_time=runtime))

        #Fade in goats above doors 1 and 3, car above door 2
        goat1 = ImageMobject("goat.PNG").scale(0.25)
        goat2 = ImageMobject("goat.PNG").scale(0.25)
        car = ImageMobject("car.png").scale(0.25)
        goat1.next_to(door1, UP*0.5)
        goat2.next_to(door3, UP*0.5)
        car.next_to(door2, UP*0.5)

        self.play(doors.animate.shift(DOWN*0.5),
                  FadeIn(goat1),
                  FadeIn(goat2),
                  FadeIn(car))
        self.wait(1)



                            

        
        


