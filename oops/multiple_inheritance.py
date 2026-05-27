

class Father:
  def father(self):
    print("father earns")

class Mother:
  def mother(self):
    print("mother cares")

class Kid(Father,Mother):
  def kid_1(self):
    print("kids are parents joy")

c1=Kid()
c1.father()
c1.mother()
c1.kid_1()

#*****multiple inheritance example sentence***
print("\n *****multiple inheritance example sentence***")


class sentence1:
  def sen1(Self):
    print("day is good")

class sentence2:
  def sen2(self):
    print("its a sunny day")

class join(sentence1,sentence2):
  def sen3(self):
    print(" wind blowing from east to west")

c2=join()
c2.sen1()
c2.sen2()
c2.sen3()
# print(c2.sen1()+" "+c2.sen2()+" "+ c2.sen3()) not possible it will give error 



 

  
