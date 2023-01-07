##wap to input a list and search that element

lst=eval(input("Enter list elements : "))
print(lst)
length=len[lst]
sch=int(input("Enter searching element : "))
for i in range (0,length) :
    if (lst[i]==sch):
        print("Value found at index : ",i)
    else:
        print("Value not found")
