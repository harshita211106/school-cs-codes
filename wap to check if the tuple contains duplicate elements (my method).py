##wap to check if the tuple contains duplicate elements or not 
## for a limited and known amount of tuple elements

tp=(12,51,51,41)
dupl=0
length=len(tp)
for i in range (length):
    if tp[0]==tp[i]:
        dupl="true"
    elif tp[1]==tp[i]:
        dupl="true"
    elif tp[2]==tp[i]:
        dupl="true"
    elif tp[3]==tp[i]:
        dupl="true"
    elif tp[4]==tp[i]:
        dupl="true"

    else:
        dupl="false"

if dupl=='true':
    print("tuple cointains duplicate elements")

else:
    print("tuple doesnot cointain duplicate elements")
