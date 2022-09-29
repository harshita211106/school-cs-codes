#wite a program to enter name ,marks of 5 subjects and calculate total and percentage of student

name=(input ("Enter Student Name\n"))


english=float(input("Enter English Marks\n"))
maths=float(input("Enter Math Marks\n"))
science=float(input("Enter Scinece Marks\n"))
hindi=float(input("Enter Hindi Marks\n"))
computer=float(input("Enter Computer Marks\n"))

if english>80:
    print("incorrect marks")
    
if maths>80:
    print("incorrect marks")

if science>80:
    print("incorrect marks")
    
if hindi>80:
    print("incorrect marks")
    
if computer>80:
    print("incorrect marks")
    

overallmarks=english+maths+science+hindi+computer
print ("Total Marks = ",overallmarks)

overallpercentage=overallmarks/400*100
print("Total Percentage = ",overallpercentage)
