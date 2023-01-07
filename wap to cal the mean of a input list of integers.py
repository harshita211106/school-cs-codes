##wap to cal the mean of a input list of integers

## first type of way to solve this :

def oneway () :

    lst=eval(input("Enter list elements : "))
    length=len(lst)
    print("Number of list elements : ",length)

    summ=sum(lst)
    print("Sum of the input list : ",summ)

    mean=summ/length
    print("Mean of the input list : ",mean)

oneway()


def secondway ():
    lst=eval(input("\nEnter list elements : "))
    length=len(lst)

    for i in range(0,length):
        summ+=lst[i]
        mean=summ/length
    

    print("Mean of input list : ",mean)    

secondway ()
