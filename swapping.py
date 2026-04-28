a=int(input("enter a number :"))
b=int(input("enter a number :"))
print(f" \n value before swapping :a={a},b={b}")
c=0
c=b+c
b=a
a=c
print(f" \n ...value after swapping  :a={a},b={b}")

# best way 
print(f" \n value before swapping  :a={a},b={b}")
c=a
a=b
b=c
print(f"\n========best way logic  result==== :a={a},b={b}")

# most used logic 
a=10 
b=5
print(f" \n value before  swapping  :a={a},b={b}")

a,b=b,a      # python creates a tuple then “First collect values (right), then assign (left)”
print(f" \n **** most used logic *****a={a} ,b={b}")


x = 10, 20
print(type(x))


#using arethematic
print()
print("swapping without creating a 3rd variable")
c=int(input("enter a number :"))
d=int(input("enter a number :"))
print(f"value befor swapping c={c},d={d}")
c=c+d
d=c-d
c=c-d
print(f"value after swapping c={c},d={d}")


# swapping using 3 values
print("swapping using 3 values")
a=1
b=2
c=3
print(f"value befor swapping a={a}, b={b} ,c={c}")

a,b,c=c,a,b

print(f"value after swapping a={a}, b={b} ,c={c}")


#swapping  3 values using aretehmatics operators 

print("\n swapping  3 values using aretehmatics operators ")
a=1
b=2
c=3
print(f"values before swapping: a={a},b={b}, c={c}")
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)

print(f"values after  swapping: a={a},b={b}, c={c}")