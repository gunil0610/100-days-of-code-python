from turtle import Turtle


class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.x_increment = 10
    self.y_increment = 10
    self.move_speed = 0.1

  def move(self):
    new_x = self.xcor() + self.x_increment
    new_y = self.ycor() + self.y_increment
    self.goto(new_x, new_y)

  def wall_collision(self):
    self.y_increment *= -1

  def paddle_collision(self):
    self.x_increment *= -1
    self.move_speed *= 0.9

  def reset_position(self):
    self.goto(0, 0)
    self.x_increment *= -1
    self.move_speed = 0.1