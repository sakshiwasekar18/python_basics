import numpy as np
# shape of an array 
arr1=np.array([
  [1,2,3],
  [4,5,6],
  [6,7,8]
])
print(arr1.shape)

# size of data
print(f"the size of array is : {arr1.size}")

print()
#to know the dimensions of an array 
#ndim

arr1=np.array([1,2,3,4])
arr2=np.array([
  [1,2],
  [3,4]
  ])
arr3=np.array([[
   [1,2,3,4],
   [4,5,6,7],
   [9,9,9,9]
   ]])
arr4=np.array([[[
  [1,2,3,4],
  [8,8,8,9],
  [7,8,8,9],
  [3,4,5,6]

  ]]])
print("printing the dimensions")
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

print()
#to check the type of data in array 
#.dtype
# u32 : u means text/string, and 32 means it keeps space for a letter upto 32 characters

arr6=np.array([3,4,5,6,7.8,])
arr5=np.array([3,4,5,6,7.8,8.8,9.0,5.5,"hello","you"])
print(arr5.dtype)
print(arr6.dtype)

print()
#to cahnge the dtattype of a array
#.astype
arr7=np.array([9.0,7.9,7.0,7.0])
arry8=arr7.astype(int)
print(arry8)

print()
#to conver from string to int 
arry8=np.array(["3","6","7"])
arry9=arry8.astype(int)
print(arry9)

print()
#conver fron str tio int
arry11=np.array(["2","4","5","6"])
arry12=arry11.astype(int)
print(arry12)

