import matplotlib.pyplot  as plt
'''x=[1,2,3,4,5,6,7,8,9,10]
y=[10,20,30,40,50,60,70,80,90,100]

plt.plot(x,y)
plt.show()

plt.title("sales report")
plt.xlabel("months")
plt.ylabel("sales")
plt.show()

plt.plot(x,y, color="red")
plt.show()

plt.plot(x,y, linestyle="-.", color="blue")
plt.show()


#markers on the line to plot values 
#  "o" circle
# "s" square
# "*"  star
#"^" triangle
# "x" gives arc , cross
plt.plot(x,y, marker="x")
plt.show()

 
#  customize everything
plt.plot(x,y , color="green", linestyle=":",marker= "^")
plt.show()


x=[1,2,3,4,5]
y1=[10,20,30,40,50]

y2=[15,20,25,40,55]

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()

#adding a legend ,shows information about colours on the graph 

x=[1,2,3,4,5]
y1=[10,20,30,40,50]

y2=[15,20,25,40,55]

plt.plot(x,y1 , label="product 1")
plt.plot(x,y2, label="product 2")
plt.legend()
plt.show()
'''


#grid 

x=[10,20,30,40,50]

y=[15,20,25,40,55]

# plt.plot(x,y)
plt.plot(x,y , color="green", linestyle=":",marker= "^")
plt.grid(True)
plt.show()
