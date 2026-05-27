import pandas as pd
import numpy as np

 #series is a single column of data
numbers=[10,20,30,40,50] #list
print(numbers)
s=pd.Series(numbers)
print("\n list into Series\n",s)

#custom indexing 
print("\n*********custom indexing*********\n ")

labels=["a",'b','c']
num=[1,2,3]

print(pd.Series(num,index=labels))


#coverting array into series
print("\n*****coverting array into series*****\n")
arr=np.array([12,13,14])
print(arr)
a=pd.Series(arr)
# print("\n array into series: \n",pd.Series(arr))
print("\n array into series: \n",a)


#dictionary into series it take  key as index by default
print("\n*****coverting dictionary into series*****\n")


dic={
  1:34,
  2:45,
  3:67
}

print(dic)

print("\n",pd.Series(dic))

#practice

dic1={
  1:"sakshi",
  2:"nisha",
  3:"nitin"
}
print("\n",pd.Series(dic1))



dic2={
  "sakshi":56,
  "nisha":90,
  "nitin":67
}
print("\n",pd.Series(dic2))


dic3={
  "name": "sakshi",
  "age":21,
  "marks":98
 
}
print("\n",pd.Series(dic3))