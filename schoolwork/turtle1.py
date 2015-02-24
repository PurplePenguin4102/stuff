import turtle

def demo():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.exitonclick()

#1

def forwardleft(int1):
    """makes turtle go forward then left"""

    turtle.forward(int1)
    turtle.left(90)

def rectangle(int1,int2):
    """makes rectange dimensions int1xint2"""

    i = 1
    while i <= 2:
        forwardleft(int1)
        forwardleft(int2)
        i += 1

    turtle.exitonclick()

#2

def rotated_rectangle(int1,int2,rot):
    """does the same as rectangle but with a rotation rot"""

    turtle.left(rot)
    rectangle(int1,int2)
    turtle.exitonclick()

#3

def polygon(size,n):
    """makes a polygon with n sides and side length size*sin(pi/n)"""

    import math
    i = 0
    side = size*math.sin(math.pi/n)
    rot = 360.0/n
    while i < n:
        turtle.forward(side)
        turtle.left(rot)
        i += 1
    turtle.exitonclick()

#4

def turn(a,b):
    """need this for good interact so that I can turn easily, takea a direction
        and a new direction and turns the turtle"""

    key = "{0} {1}".format(a,b)

    t_dict = {"e n": 90,
              "e e": 0,
              "e w": 180,
              "e s": -90,
              "n n": 0,
              "n e": -90,
              "n w": 90,
              "n s": 180,
              "w n": -90,
              "w e": 180,
              "w w": 0,
              "w s": 90,
              "s n": 180,
              "s e": 90,
              "s w": -90,
              "s s": 0}

    return turtle.left(t_dict[key])

    
def interact():
    """Same as interact but hopefully written a little better"""
    
    direc = "e"
    step = int(raw_input("distance: "))
    i = True

    while i:

        newd = raw_input("direction: ")

        if newd == "q":
            break
        
        turn(direc,newd)
        turtle.forward(step)

        direc = newd

    turtle.exitonclick()

#challenge

def spiral(n):
    """creates a spiral with n lengths"""

    step = 20
    direc = "e"
    newddict = {"e": "n",
                "n": "w",
                "w": "s",
                "s": "e"}
    dummy = 1
    
    while n > 0:

        turtle.forward(step)
        turn(direc,newddict[direc])
        
        if dummy % 2 == 0:
            step += 20

        direc = newddict[direc]
        n += -1
        dummy += 1

    turtle.exitonclick()
