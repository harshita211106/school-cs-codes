import math
print("For quadratuc equation, ax**2+bx+c=0, enter coefficients below")

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

if a==0:
    print("Value of", a," should not be zero")
    print("/nAborting!!")
else:
    delta=b*b-4*a*c
    if delta>0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("Roots are REAL and UNEQUAL")
        print("Root1=",root1)
        print("Root2=",root2)
    elif delta==0:
        
        root1=-b/(2*a);
        print("Roots are REAL and EQUAL")
        print("Root1=",root1,"Root2=",root2)
    else :
        print("Roots are COMPLEX and IMAGINARY")
        
