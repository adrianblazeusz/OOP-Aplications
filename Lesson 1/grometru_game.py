from geometry import Point, Rectangle
from random import randint

rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

print("Rectangle Coordinates: X1:",
      rectangle.lowleft.x, ", Y1:",
      rectangle.lowleft.y, "and X2:",
      rectangle.upright.x, ", Y2:",
      rectangle.upright.y)

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))