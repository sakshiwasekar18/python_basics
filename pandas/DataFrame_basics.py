#DataFrame is a function in pandas
#  DataFrame = a table-like data structure in pandas used to store and manipulate data, 
# DataFrame is a 2D table (like Excel sheet) in pandas 

import pandas as pd
data={
  "Name":["sakshi","nesha","isha","amit","tisha","priyanka","satish"],
  "age":[21,20,45,23,21,20,19]
}

df=pd.DataFrame(data)
print("\n",df)

#gives the size of the table row, column
print("\n shape:",df.shape)

#head prints top 5 rows of the data
print("\n print top 5 rows: \n", df.head())


#tail prints last 5 rows
print("\n print last 5 rows: \n",df.tail())


#columns gives column names basically header
print("\n print header of the data: \n",df.columns)


#print a specific row  using loc and iloc
print("\n*********print a specific row  using loc and iloc****************\n")

info = pd.DataFrame({
  "name":["savita","kavita","sunita"],
  "age":[21,43,45]

},index=[10,20,30])

print(info)

print("\n loc acsses by index(lable):", info.loc[10])

print("\n iloc acsses by position : ",info.iloc[1])


#adding a column
print("\n*****adding a column******\n")
print("\n",df)

df["marks"]=[78,87,89,90,87,97,90]
print("\n after adding column marks:\n ",df)

#updating the data
print("\n *********updating the data**********\n ")
print("\n",df)

df.loc[0,"marks"]=100

print("\n result after upadting \n",df)

#filtering data
print("\n**************filtering data*************\n")

print(df[df["marks"]>90])




print("\n**************sorting data*************\n")

print("sorting in the column marks in ascending \n")
print(df.sort_values("marks"))  #for ascending

print("sorting in the column marks in descending\n ")
print(df.sort_values("marks",ascending=False)) #for descending values
#note : when u sort the whole table is sorted

#sorting from a-z

print("\nsorting from a-z in name \n")
print(df.sort_values('Name'))

print("\nsorting from z-a in name\n")
print("\n",df.sort_values("Name",ascending=False)) #for z to a




print("\n***************sorting using lamba**********\n")

#lets aply normal non case sensitive sort and see
name=pd.DataFrame({
  "Name":["nita","Ankita","Om","boby","kartik","aisha","Zyan"]
  })

print(name.sort_values("Name")) #see it prints all capital 1st then sort and print the lower case

print("\n convert → lowercase → sort ascending\n")
print(name.sort_values('Name',key=lambda x:x.str.lower()))  #key = your custom logic before sorting , lambda is the lambda = a short, one-line function (no name)



print("\n  convert → lowercase → sort descending\n")
print(name.sort_values("Name", key=lambda x: x.str.lower(), ascending=False))






print("\n***************lets find mean of marks **********\n")

print(df["marks"].mean())

# print(f"{df["marks"].mean():.2f}") will not work
print(f"{df['marks'].mean():.2f}")

print("\n***************lets find min of marks **********\n")
print(df["marks"].min())

print("\n***************lets find max of marks **********\n")
print(df["marks"].max())