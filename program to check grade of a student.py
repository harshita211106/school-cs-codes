##wap to check the grade of a student

grade=""
name=input("Enter Student name ")
percent=float(input("Enter Percentage"))
if (percent>90):
    grade=" A++"
   
elif(percent>80):
    grade=" A"
    print ("Your grade= ",grade)

elif (percent>65):
    grade=" B"
    print ("Your grade =",grade)

elif(percent>45):
    grade=" C"
    print ("Your grade =",grade)
   
else:
    print("\n")
    print(name,"You are failed")
    print(name,"Your grade = F")
