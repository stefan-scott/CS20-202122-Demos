import turtle

wind = turtle.Screen()
t = turtle.Turtle()


def cross(side_length):
    #create the plus sign primitive
    for i in range(4):
        t.fd(side_length)
        t.left(90)
        t.fd(side_length)
        t.right(90)
        t.fd(side_length)
        t.left(90)


def cross_complex():
    for i in range(4):
        cross(10)
        t.right(90)
  
# cross_complex()