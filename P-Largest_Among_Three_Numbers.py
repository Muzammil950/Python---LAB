# Find the Largest Among Three Numbers

num1 = float(input("Enter the 1st Number : "))
num2 = float(input("Enter the 2nd Number : "))
num3 = float(input("Enter the 3rd Number : "))


if num1 > num2 and num1 > num3 :
    print("the num1 is the greatest")

elif num2 > num1 and num2 > num3 :
    print("the greatest is the num2")

else:
    print("the greatest is the num3")