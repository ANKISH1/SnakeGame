from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)


    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)


    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading()!= LEFT:
            self.segments[0].setheading(RIGHT)