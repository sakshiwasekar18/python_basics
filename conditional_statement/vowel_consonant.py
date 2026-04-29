a=input("enter a character: ")
if a in 'a,e,i,o,u,A,E,I,O,U':
  print("character is a vowel")
else:
  print("character is a consonant")
  #another way 

a=input("\n enter a character: ")
if a in 'AEIOUaeiou':
  print("character is a vowel")
else:
  print("character is a consonant")

  #using list

a=input("\n enter a character: ")
lst=["a","e","i","o","u","A","E","I","O","U"]
if a in lst:
  print("character is a vowel")
else:
  print("character is a consonant")

