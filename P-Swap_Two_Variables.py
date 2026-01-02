# Swap Two Variables in Python

x = 13 
y = 12

temp = x 

print("the value of temp variables is : ", temp)

x = y
print("the value of x is : ", x)


y = temp
print("the value of y is : ", y)


print("Second method Swap Two Variables in Python ")

x = 13
y = 12

x,y = y,x

print("the value of x : ", x)
print("the value of y : ", y)