from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        self.wait(1)  # wait for 1 second


class CreateSquare(Scene):
    def construct(self):
        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        self.play(Create(square))  # show the square on screen
        self.wait(1)  # wait for 1 second
