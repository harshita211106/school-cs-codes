##wap to input a integer list to be appended to an existing list.
##whether the user enters a single number of list,the program should append the list accordingly


elist=[1,2,4,52,41,6]                        ##existing list variable
print("Existing list elements are : ",elist)

ilist=eval(input("Enter list elements to be appendend to the existing list : "))

if type(ilist)==type([]):                   ##if a list is input
    elist.extend(ilist)

elif type(ilist)==type(1):                  ##if an integer is input
   elist.append(ilist)

else:
     print("Please enter either an integer or a list ")

print("Appended list is :  ",elist)
