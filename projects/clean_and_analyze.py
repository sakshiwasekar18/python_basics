import numpy as np
# data=np.genfromtxt(
#   "employee_big_data.csv",
#   delimiter=",",
#   skip_header=1
# )
# r means raw string It tells Python:“Treat everything as normal text, don’t process special characters”
data = np.genfromtxt(
    r"C:\Users\91862\Desktop\SAKSHI_PYTHON\projects\employee_big_data.csv",
    delimiter=",",
    skip_header=1
)

print(data)

#replace salary by avg salary
avg_salary=np.nanmean(data[:,2])
print("\n********avg_salary: ",avg_salary)

data[np.isnan(data[:,2]),2]=avg_salary
# print("\n***",data)

#missing experiance with avg_exp
avg_exp=np.nanmean(data[:,3])
print("\n*** avg_exp: ",avg_exp)
data[np.isnan(data[:,3]),3]=avg_exp
# print("\n****",data)

#replace missing bonus
avg_bonus=np.nanmean(data[:,4])
print("\n***** avg_bonus",avg_bonus)
data[np.isnan(data[:,4]),4]=avg_bonus
# print("/n****",data)

#replace missing rating
avg_rating=np.nanmean(data[:,5])
print("\n*** avg_rating",avg_rating)
data[np.isnan(data[:,5]),5]=avg_rating
# print("/n****",data)

print("\n clean data",data)

print("\n *********analysis*********")

print("\n average Salary:",np.mean(data[:,2]))
print("\n heights Salary:",np.max(data[:,2]))
print("\n lowest Salary:",np.min(data[:,2]))

print("\n average Age :",np.mean(data[:,1]))
print("\n average Experience, :",np.mean(data[:,3]))
print("\n average Bonus:",np.mean(data[:,4]))
print("\n average rating:",np.mean(data[:,5]))

#highest salary employee
index=np.argmax(data[:,2])
 #argmax :return the index (position), not the value
print(index)
print("\n employee id with hightest salary :")
print(int(data[index,0]))#[index,0]=0th column of the index

#save file
np.savetxt(
  r"C:\Users\91862\Desktop\SAKSHI_PYTHON\projects\clean_and_analyze_data.csv",
  data,delimiter=",",header="EmpID,Age,Salary,Experience,Bonus,Rating",fmt="%2f"
)

print("\n clean file saved")
