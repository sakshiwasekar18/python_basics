# np.insert(array,index,value,asix=0 or 1)
#used in 2d axis =0, add in row axis =1 ,add data in column

import numpy as np

print("\n****** reshape ****************")
#reshape 
# changes 1d to 2d  or from 2d to 2d
#.reshape(rows,column) only if dimension match
print("from 1d to 2d")
arr6=np.array([2,3,4,5,6,7,8,9])
print("original array",arr6)

reshape_arr=arr6.reshape(4,2)
print("\n reshape array",reshape_arr)

print("\n without making a variable: ",arr6.reshape(4,2))   #write in one line , without making a variable


print("\n from 2d to 2d ")# we change only shape 
print("\n",reshape_arr.reshape(2,4))

print("\n **insert in 1d array using axis ***********")
arr=np.array([2,2,3,4,5,6,7,8])
print(arr.size)
print(arr)
new_arr=np.insert(arr,2,100,axis=0) 
print(new_arr.size)
print(new_arr)


#insert in  2d array

print("\n ***insert in  2d array using axis **********")
arr2=arr.reshape(2,4)
print(arr2)

#add a column
#new2=np.insert(arr2,1,[8,8,8,8],axis=1)#error
# Column needs 2 values (one for each row)
new2=np.insert(arr2,1,[100,200],axis=1)

#add a row
new2=np.insert(new2,1,[8,8,8,8,8],axis=0)
print("\n",new2)

print("\n**** concatenate:**** ")
#concatenate Used to join multiple arrays
#np.concatenate((array1,aaray2,aaray3))
arrr1=np.array([1,2,3])
arrr2=np.array([11,22,33])
arrr3=np.array([0,88,44])
arrr4=np.array([1,2,3])
new_ar=np.concatenate((arrr1,arrr2,arrr3))
print(new_ar)

#append
new=np.append(arrr1,arrr2)
print("\n append:",new)
# new=np.append((arrr1,arrr2,arrr3))#Mainly for adding one array to another not many  , this will give error 
new1=np.append(arrr1,[arrr2,arrr3])#not recomended for joining many arrays
print("\n append:",new1)

print("\n",np.append(new,444)) #use for adding a value at last
#if you want to add using index use insert

print("\n ***delete*****")
#delete
#np.delete(array,index)
print(new_ar)
new_ar1=np.delete(new_ar,4)
print("after deleting:",new_ar1)

print("**** shape and size and dimension ******")
print(" *** 1d array")
arr00=np.array([2,4,5,6,7,8,88,99])
print("\n shape for 1d array",arr00.shape)
print("\n size for 1d array ",arr00.size)
print("\n dimension  for 1d array ",arr00.ndim)

print("\n**** for 2d array")
ar11=np.array([[2,4]
                ,[5,6]
                ,[7,8]])
print("\n shape for 2d array",ar11.shape)
print("\n size for 2d array ",ar11.size)
print("\n dimension  for 2d array ",ar11.ndim)