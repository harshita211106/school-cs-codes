##wapp to input 2 lists and create a new list that contains all the elements of the  first list and the second list respectively

l1=eval(input("Enter list 1 elements : "))
print(list(l1))

l2=eval(input("\nEnter list 2 elements : "))
print(list(l2))

l3=list(l1+l2)
print("\nList 3 containing elements of both the lists together : ",list(l3))
