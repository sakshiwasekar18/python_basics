import numpy as np
data = np.genfromtxt(
  r"C:\Users\91862\Desktop\SAKSHI_PYTHON\projects\student_marks.csv",
  delimiter=",",
  skip_header=1
)


print("\n original data", data)

#getting boolean mask for column 1
print(np.isnan(data[:,1]))

#count total missing values in column 1
print(np.isnan(data[:,1]).sum())

#print students with missing marks
marks=data[:,1]
print(marks)
data1=data[np.isnan(marks)]
print("\n",data1)

#get students with marks
data2=data[~np.isnan(marks)]
print("\n",data2)

#calculate average marks
avg=np.nanmean(marks)# it ignores nan
print(avg)

#replace missing marks with zero
# data(np.isnan(marks),1)=0#error
'''data[np.isnan(marks),1]=0
print(data)'''

#replace with 1
'''data[np.isnan(data[:,1]),1]=1
print("\n",data)'''

#replace with avg 
data[np.isnan(marks),1]=avg
print(data)

#find student above 80
print("\n",data[data[:,1]>80])
#or
print("\n",data[marks>80])