## write a code to find consonent and vowel for a letter

def vowel():
     
     Al=input("Enter Alphabet\n") 
     if (Al=="a"or Al=="A"):
         print("Alphabet is vowel")
     elif (Al=='e' or Al=='E'):
          print("Alphabet is vowel")
     elif (Al=='i' or Al=='I'):
          print ("Alphabet is vowel")
     elif (Al=='o' or Al=='O'):
          print("Alphabet is vowel")
     elif (Al=='u' or Al=='U'):
          print("Alphbet is vowel")
     else:
         print("Alphabet is consonent\n")


vowel()


## write a code to check if given values are alphabetic numeric or symbol

def alpha ():

     val=input("\nEnter Alphabet\n")
     if (val>='a' and val<='z'):
          print("It's a small case character")
     if (val>='A' and val<='Z'):
          print("It's upper case character")
     if (val>'o' and val<'9'):
          print("It's numeric")
     else:
          print("It's symbol")
                
vowel()
