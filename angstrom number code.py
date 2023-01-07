num=int(input("Enter number : "))

sum=0
rem=0
temp=num
while(num>0) :
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10



if (temp==sum):
    print("Its angstrom number")
else:
    print("It is not angstrom number")
