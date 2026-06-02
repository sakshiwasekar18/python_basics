#tables has int then why float?

# NaN = float ,
# So if a column has even one missing value whole column becomes float


import pandas as pd
df=pd.read_csv(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\pandas\employee.csv")
print(df)

# checking null values
print("\n",df.isnull()) #retuens a boolean of the entire table

#checking null values in a column
print("\n check null values in name\n",df["name"].isnull())
print("\ncheck null values in city\n",df["city"].isnull())

#count null in each column in whole file 
print(df.isnull().sum())
#count  total null value in a column
print("\n null values of column marks:\n",df["marks"].isnull().sum())

#get rows with null values 
print(df[df["marks"].isnull()]) #we printed row where only marks is null

print("/n row where only city is null\n",df[df["city"].isnull()])
'''in data df print all rows where column city has null'''

#********************fill null values*******************
# .copy() creats a copy of a original life
# Use .copy() when:testing fillna(),using dropna(),experimenting

df_copy=df.copy()
print("\n\ncreated a copy of df :\n",df_copy)

#fill all null witha value
df_copy.fillna(1,inplace=True)
print("\n fill all nulls with 1\n ",df_copy)

#fill a specific column
# print(df_copy["city"].fillna(00,inplace=True)) will not work 

''' now we need null values so we will create copy of df again and again and understand the concept'''

#fill nan with text
df_copy1=df.copy()
df_copy1["city"].fillna("no_city",inplace=True)
print("\n filling  null with 'no_city' in city column\n",df_copy1)


#fill nan with numbers
df_copy1=df.copy()
df_copy1["marks"].fillna(0000,inplace=True)
print("\n filling nan in marks by 0000\n",df_copy1) #but as its a float it prints 0.0 

#best practice is to fill with the mean 
df_copy2=df.copy()
df_copy2["marks"].fillna(df["marks"].mean(), inplace=True)
print("\n filling na in marks with mean \n",df_copy2)

print("\n mean of marks column : \n ",df_copy2["marks"].mean()) #mean of marks 

# df_copy2["age"].fillna(df_copy2["age"].mean(),inplace=True)
# print(df_copy2)

print("************************************drop***************************")

#drop rows with any null
df_drop=df.copy()
print("\n",df_drop)

df_drop.dropna(inplace=True)

print("\n drop all rows with any null\n",df_drop)

#drop rows where a column value is null , we use subset
df_drop2=df.copy()
print("\n",df_drop2)

df_drop2.dropna(subset=["marks"],inplace=True)

print("\ndrop rows where marks is null\n",df_drop2)


#drop columns how has nan values 
df_drop3=df.copy()
print("\n",df_drop3)

df_drop3.dropna(axis=1,inplace=True)
print("\ndrop all column with naa \n",df_drop3)

#**************threshold***********
#have atleast thresh amount (2)of data then only keep the row or drop it 

df_condition=df.copy()
print("\n", df_condition)

df_condition.dropna(thresh=2,inplace=True) # only those rows who has at least 2 values 
print("\n",df_condition)

#*****************FORWARD FILL / BACKWARD FILL*******************
# FORWARD FILL :Fills missing value using the value ABOVE it/ starts filling from above 
# BACKWARD FILL:Fills missing value using the value BELOW it/ starts filling fron below 


df_ffill = df.copy()
print("\n",df_ffill)

df_ffill.fillna(method="ffill", inplace=True)
print("\nForward fill:\n", df_ffill)


df_bfill = df.copy()
print("\n",df_bfill)

df_bfill.fillna(method="bfill", inplace=True)
print("\nBackward fill:\n", df_bfill)

# *****************notnull*******************

print("\nnotnull value in whole dataset\n",df.notnull())



no_null_df=df[df.notnull().all(axis=1)]
print("\nRows where NO null  values exists\n",no_null_df) #Rows where NO null  values exists

any_value=df[df.notnull().any(axis=1)] # rows where any value is present 
print("\n rows where any value is present \n",any_value)

no_null_marks=df[df["marks"].notnull()] #rows with no null valuesin a specifice column
print("\nRows where there r no null values in marks\n",no_null_marks)


