'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]'''
import numpy as np

nums = np.array([2,7,11,15])
target = 18

'''for i in range(0,nums+1):# nums is a whole array nota  number 
  for j in range(1,nums+1):
    if i+j==target:# you are adding index not values
      print(nums[i],nums[j])'''

#by brute force solution 
print(len(nums))

for i in range(len(nums)):#to use for in array use len
  for j in range(i+1,len(nums)):
    if nums[i]+nums[j]==target:
      print([nums[i],nums[j]])

#by brute force solution 
n=len(nums) 
print(n)

for i in range(0,n-1):#len starst counting fron 1 but index from 0 so last should be n-1
  for j in range(i+1,n):
    if nums[i]+nums[j]==target:
      print([i,j])
      #return [i,j]#return can be used ONLY inside a function


#***********optimal solution***********





        