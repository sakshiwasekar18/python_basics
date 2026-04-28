import numpy as np
ny_array= np.array([1,2.3,4.5,8,9])
print(ny_array)

print()
#2d array is also called multidimensional array
d2_array=np.array([[2,3,4],[3,5,6],[4,5.6,9]])
print(d2_array)

print()
#creating an empty array 
empty= np.zeros(9)
print(empty)

print()
#adding 1 to the array in starting(row,column)
one_in= np.ones((2,3))
print(one_in)

print()
#full function : giving default value to array 
#full((shape),value)
ful_function=np.full((2,3),2)
print(ful_function)

print()
#creating sequence of a number in array 
#relate to for in range 
# arange(start,stop,step)
range1=np.arange(1,20,2)
print(range1)

print()
#creating identity matrix
#eye
identity_max =np.eye(4)
print(identity_max)

print()
#************* 1D operations ************************
arr=np.array([1,2,3,4,5])
print(arr[1])
#append meaning add at the last 



arry=np.append(arr,10)
array=np.append(arr,[6,7,8,9])
print(array)
print(arry)

#inset a value in array 
arr1=np.insert(arry,4,299)
print(arr1)
arr1=np.insert(arr1,2,[0,3,5,6,7,8,9,0,0,0,])
print(arr1)