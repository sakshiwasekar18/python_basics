import numpy as np

print("***Boolean masking using np.isnan()**")
#np.isnan - used to check is if a value is nan 
# np.isnan(value)
# if true - value is missing
# false- valus is there

arr=np.array([2,3,4,np.nan,6,np.nan,np.nan])

print("\n",np.isnan(arr))

print("\n ****count the total missing values*****")
#count the total missing values
print(np.isnan(arr).sum())

#store in a variable and print
arr1= np.array([5, np.nan, 8, np.nan, 2])
count = np.isnan(arr1).sum()
print(count)

#replace nan with zero
print("\n ****replace nan with zero*****")
print("orignal: ",arr)
#print(arr[np.isnan(arr)]=100)#cannot assign = in print ,You cannot assign inside print()
arr[np.isnan(arr)]=100
print("replace by 100 : ",arr)

print("\n ****replace nan with average***")
arr4=np.array([2,3,np.nan,4,np.nan,56,78,np.nan,9])
print(arr4)

avg=np.nanmean(arr4)

print(avg)
arr4[np.isnan(arr4)]=avg
print("\n",arr4)

#****************Check 2d array************
data=np.array([[1,6],
               [7,8],
               [5,np.nan],
               [3,np.nan]])
print(np.isnan(data))

#find nan only in second column

data=np.array([
  [2,3,np.nan],
  [6,8,np.nan],
  [6,np.nan,9],
  [4,np.nan,90]
])

print(data[:,1])
print(np.isnan(data[:,1]))

#******replace nan in column*****
data[np.isnan(data)]=1000 # this replaces all values with the given values
print(data)

data1=np.array([
  [2,3,np.nan],
  [6,8,np.nan],
  [6,np.nan,9],
  [4,np.nan,90]
])

Env=data1[np.isnan(data1[:,1])]#print rows at which 1st column values are nan
print("\n",Env)

data1[np.isnan(data1[:,1]),2]=900#explained below

print("\n",data1)

#explaination
print("Original:\n", data1)
print("\n",data1[:,1])
print("\n",np.isnan(data1[:,1]))
data1[np.isnan(data1[:,1]),2]=900#It replaced values in the 3rd column (index 2)
                                 # ❗ ONLY for rows where the 2nd column (index 1) has NaN
# *************************************************


# ================================
# BOOLEAN MASKING WITH NUMPY
# ================================

import numpy as np


# --------------------------------
# 1. CHECK NaN VALUES
# --------------------------------
# np.isnan() returns True where value is NaN

arr = np.array([2, 3, 4, np.nan, 6, np.nan, np.nan])

print("Original array:", arr)

# Boolean mask (True = NaN, False = normal value)
print("\nNaN check:", np.isnan(arr))


# --------------------------------
# 2. COUNT NaN VALUES
# --------------------------------
# True = 1, False = 0 → so sum() counts NaN

print("\nTotal missing values:", np.isnan(arr).sum())


# --------------------------------
# 3. REPLACE NaN WITH A FIXED VALUE
# --------------------------------
# Replace all NaN with 100

arr[np.isnan(arr)] = 100

print("\nAfter replacing NaN with 100:", arr)


# --------------------------------
# 4. REPLACE NaN WITH AVERAGE
# --------------------------------
# np.nanmean() ignores NaN while calculating mean

arr4 = np.array([2, 3, np.nan, 4, np.nan, 56, 78, np.nan, 9])

print("\nOriginal arr4:", arr4)

avg = np.nanmean(arr4)   # mean without NaN
print("Average (ignoring NaN):", avg)

# Replace NaN with average
arr4[np.isnan(arr4)] = avg

print("After replacing NaN with avg:", arr4)


# --------------------------------
# 5. 2D ARRAY NaN CHECK
# --------------------------------

data = np.array([
    [1, 6],
    [7, 8],
    [5, np.nan],
    [3, np.nan]
])

# Check NaN in 2D (True where NaN)
print("\n2D NaN check:\n", np.isnan(data))


# --------------------------------
# 6. CHECK NaN IN A SPECIFIC COLUMN
# --------------------------------

data = np.array([
    [2, 3, np.nan],
    [6, 8, np.nan],
    [6, np.nan, 9],
    [4, np.nan, 90]
])

# Select column index 1 (2nd column)
col = data[:, 1]
print("\nColumn 2 values:", col)

# Check where NaN in that column
mask = np.isnan(col)
print("NaN mask for column 2:", mask)


# --------------------------------
# 7. REPLACE ALL NaN IN WHOLE ARRAY
# --------------------------------

data[np.isnan(data)] = 1000

print("\nAfter replacing all NaN with 1000:\n", data)


# --------------------------------
# 8. SELECT ROWS WHERE A COLUMN HAS NaN
# --------------------------------

data1 = np.array([
    [2, 3, np.nan],
    [6, 8, np.nan],
    [6, np.nan, 9],
    [4, np.nan, 90]
])

# Select rows where column 2 has NaN
rows_with_nan = data1[np.isnan(data1[:, 1])]

print("\nRows where column 2 has NaN:\n", rows_with_nan)


# --------------------------------
# 9. MODIFY ANOTHER COLUMN BASED ON CONDITION
# --------------------------------

# CONDITION:
# Find rows where column 2 has NaN

# ACTION:
# In those rows → change column 3 (index 2) to 900

data1[np.isnan(data1[:, 1]), 2] = 900

print("\nFinal array after modification:\n", data1)


# --------------------------------
# FINAL UNDERSTANDING
# --------------------------------
# 1. Use np.isnan() → to find missing values
# 2. It creates a Boolean mask (True/False)
# 3. Use that mask to:
#    - count values
#    - replace values
#    - filter rows
#    - modify other columns
#
# IMPORTANT:
# 👉 Condition can be on one column
# 👉 But modification can be done on another column