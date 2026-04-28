print("welcome to login page")
password="123wer"
count=3
while True:
  pass1 = input("enter your password:")
  if(password==pass1):
    print("login successful")
    break
  else:
    print(f"you have {count} chance remaining")
    count-=1
    if(count==0):
      print("your login fail , try  again after 1 hr ")
    break
  
