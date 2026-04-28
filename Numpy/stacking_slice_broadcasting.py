#stacking-lot os array to combine 
# vertically -np.vstack(())
# or 
# horizontally -np.hstack(())    convert 1d into 2d

import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([3,3,3,4,99])
arr3=np.array([4,4,4,4,4])
print(np.hstack((arr1,arr2)))
print("\n",np.vstack((arr1,arr2,arr3)))

print()
#spliting
#dividing arrays into parts
#np.hsplit(array,)  same as np.split()
#np.vsplit()

arr4=np.array([23,34,45,444444444,555555555,666])
print(np.split(arr4,3))
print(np.hsplit(arr4,2))
#print(np.vsplit(arr4,2))#error works on 2d array
arr5=np.array([[23,34,45,99],
               [444444444,555555555,666,00]])
print(np.hsplit(arr5,2))



print()
#broadcasting
#numpy aumotatically makes different sizes  array work together during math operations 
# how it works
# rules 1: match dimensionas
# rule2: expanding shape 
# [1,2,3]+10= [10,20,30]
# rule3: incompatible shapes: Error


price=np.array([100,200,300])
discount=10

final_price=price-(price*discount/100)
print(final_price)


#add
price_incre=price + 20
print(price_incre)

#adding value in 2d  or adding 1d and 2d
arra2d=np.array([[2,3,4],
                [3,4,5]])
arra1d=np.array([4,4,4])
add=arra1d + arra2d
print(add)