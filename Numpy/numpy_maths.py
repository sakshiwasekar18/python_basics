import numpy as np
# arethematic operations on array directly 
print("arethematic operations on array directly ")
arr1=np.array([2,3,4,5,6,7])
print(arr1 +2)
print(arr1 *2)
print(arr1 /2)
print(arr1 //2)
print(arr1 %2)
print(arr1 **2)
print(arr1 -2)

print(" \n aggregation function **")
#aggregation function
arr2=np.array([1,2,3,4,5,6,9])
print(np.max(arr2))
print(np.min(arr2))
print(np.std(arr2))
print(np.var(arr2))
print(np.mean(arr2))
print(np.sum(arr2))

print(" \n ************replacing a value in array ********* ")
#replacing a value in 1d array 
print("\n replacing a value in  1d array ")
arr2[0]=300
print(arr2)

print("\n  replacing a value in 2d array ")
#replace in 2d array
arr20=np.array([[2,3,4],
                [7,77,88]])
print("original 2d :",arr20)

arr20[1][0]=8888888
print("\n",arr20)


print(" \n indexing for 1d array")
#indexing
print(arr2[0])# same syntax to acess index value in list 
print(arr2[1])
print(arr2[-1])

print(arr2[-3])#starts from the last value


print("\n indexing for 2d array ")
#indexing for 2d array 
arr3=np.array([
  [2,3],
  [4,5],
  [6,7]
  ])
print(arr3)
print(arr3[0,0])
print(arr3[1,0])
print(arr3[1,1])

print("\n ******slicing ****************")
#************************************************************important*************************************************
#slicing - getting a slice or a peice fron an array
#array[start,stop,step]
#array[start,n] stop: goes to n-1
# negative step -1 reverse

arr4=np.array([2,2,3,4,5,6,00])
print("\n slicing by positive indexing ")
#slicing by positive indexing starts from 0
print(arr4[1:5])
print(arr4[1:5:2])
print(arr4[::2])

print("\n slicing by negative indexing")
#slicing by negative indexing starts from -1
print(arr4[::-1])#it print reverse
print(arr4[-5:-2]) # note the value at -2 index  is not printing 
print(arr4[-7:-1:2])#step cannot be negetive and negative index never print value at stop index -1


print("\n fancy indexing")
#fancy indexing: acess value of more than one index at once- it selects  from the copy not the original data
arr5=np.array([2,3,4,5,0])
print(arr5[0])
print(arr5[[0,2,4]])


print("\n***************booleam masking ***********")
#boolean masking you use True/False (boolean values) to filter data from an array.
# used mostly in ml
arr=np.array([2,3,4,5,6,66,77])
mask = arr > 5
print(mask)

print("\n ",arr5[arr5>2])

print("\n ******multidimensional to 1d array*********")
#multidimensional to 1d array
#.ravel()-> return view , makes changes in the original data
#.flatten()-> makes a copy of data and them makes changes

arr7=np.array([
              [2,3,4]
              ,[5,6,7],
              [8,99,99]
              ,[99,99,99]
              ])
print("shape : ",arr7.shape)


r=arr7.ravel()
print(r)
f= arr7.flatten()
print(f)

print()
#lets try making a change then print it useing this two
print("+ original array :",arr7)
arr7 [0][2]=44444

print("\n ravel:",r)
print(" \n flatten :",f)#no change in flatten

#lets change in flatten
'''f[0][1]=9999
print(f)'''#NO CHANGE BECAUSE FLATTEN AND RAVEL ARE 1D ARRAY

f[1]=898897887
print(" \n after change in f :",f)






