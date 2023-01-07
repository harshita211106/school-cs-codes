##wap to count the frequency of a given element in a list

def count_element():
    lst=eval(input("Enter list elements : "))
    length=len(lst)
    element=int(input("Enter element : "))
    count=0
    
    
    for i in range(length):
        if element==lst[i]:
            count+=1
            

    if count==0:
        print(element,"not found in entered list")

    else:
        print(element,"found in entered list with frequency",count)

count_element()
