# practice of pandas  operation in csv file
# NaN = float So if a column has even one missing value whole column becomes float


import pandas as pd
df= pd.read_csv(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\pandas\student.csv")
print(df)

print("\n printing head\n",df.head())

print("\n printing tail\n",df.tail())
print("\n printing size\n",df.shape)

print("\n printing header\n ",df.columns)



print("\nstructure of data\n")
df.info()   # no print needed # it gives the structure of data of every column in the data
# df.info(marks)  # gives error


print("\n statistical summary of your numeric columns\n",df.describe())  # statistical summary of your numeric columns 



print("\n",df["name"])   #note no header is printed
print("\n",df[["name","total_marks"]]) 
print("\n",df[["name","total_marks","city"]]) #note no header is printed if more than 1 column datat u need get it by two [[]]

print("\n",df.loc[0]) #this print value by index (any custom index)
print("\n",df.iloc[1]) #this print values /row by position 


#filtering data

print("\n",df[df["marks"]>90])

print("\n",df[df[["marks","total_marks"]]>89])



#sorting values in asecending and desending

print("\n",df.sort_values("marks"))
print("\n",df.sort_values("marks",ascending=False))

#*****************************adding a column***************************

# df["marks"]=[78,87,89,90,87,97,90]  # nornmal adding of a column but u need to give all the data as per the index here if 49 rows it should have 49 values 

#add a column "grade" using a if else  

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

df["grade"] = df["marks"].apply(get_grade)
print(df)


# *******what u should practice ************
df["grade"] = df["marks"].apply(lambda x:
    "A" if x >= 90 else
    "B" if x >= 75 else
    "C" if x >= 60 else
    "D" if x >= 40 else
    "F"
)

print("\n",df)


#acessing a row by index 

print("\n acessing column using loc ",df.loc[2])

# replacing values using index
df.loc[2,"marks"]=100 #
print("\n replace value at 2 index: \n",df)

#replace more than one values at once
df.loc[[4,15,10],"marks"]=99.9
print("\n replace more than 1 value: \n",df)

#sorting 
print("\n sorting \n",df.sort_values("marks",ascending=False))


#***************deleting************
# axis = 0
# delete Row

# axis = 1
# delete col
# inplace = True to see the changes of deletion

#deleting column
df.drop("city",axis=1,inplace=True)
print("\n deleting column city by drop \n",df)

df.drop(1,axis=0,inplace=True)
print("\n deleting 1 th index row \n",df)

#mathematical calculations for a column
print("\n max of total :",df["total_marks"].max())
print("\n  min of total :",df["total_marks"].min())
print("\n  mean of total :",df["total_marks"].mean())


#saving data into csv
df.to_csv(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\pandas\new_student.csv",index=False)

print("file saved successfully !")


