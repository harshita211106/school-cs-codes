##wap to enter three sides and check whether it is a triangle or not 

a=int(input("Enter side 1 : "))
b=int(input("Enter side 2 : "))
c=int(input("Enter side 3 : "))

if a+b>c and b+c>a and c+a>b :
    print("Given sides of ",a," ",b," ",c ,"will form a triangle")
    
else:
    print("Given sides of ",a,b,c,"will not form a triangle")
