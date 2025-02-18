number1 =int(input("enter the number one "))
number2 = int(input("enter the number two "))
if number1>number2:
    larger_number = number1
else:
    larger_number = number2
print(larger_number)

x = 10
if x > 5:
    if x==6:
        print("x is 6")
    else:
        print("nested: else")
else:
    print("outer: else")

#* elif statement

x=int(input("enter the number"))
if(x==10):
    print("x is 10")
if(x>15):
    print("x is greater than 15")
elif(x>10):
    print("x is greater than 10")
elif(x>5):
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")