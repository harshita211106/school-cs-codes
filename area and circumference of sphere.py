#wap to enter radius of sphere and cal its area and circumference

def area():

    radius=float(input("enter radius"))
    height=radius
    area=4/3*3.14*radius**2*height
    print("area of sphere =",area)

area()



def circumference():
    
    radius=float(input("enter radius"))
    circumference=2*3.14*radius
    print("circumference of sphere =",circumference)

circumference()    
