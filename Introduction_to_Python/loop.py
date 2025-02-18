myNumbers=[1,2,3,4,50,45,90]
for number in myNumbers:
    if number%2==0:
        print("even ",number)
    else:
        print("odd ",number)
    print(number*15)

myname="fady emil"

for char in myname:
    print(char)

# Store the current largest number here. 
largest_number = -999999999 
number = int(input("Enter a number or type -1 to stop: ")) 
while number != -1: 
    if number > largest_number: 
        largest_number = number 
    number = int(input("Enter a number or type -1 to stop: ")) 
print("The largest number is:", largest_number)

for i in range(10):
    print("the value of i is currently",i)
for i in range(10,15):
    print("the value of i is currently",i)

for i in range(2, 8, 3):
    print("The value of i is currently", i)

#~ start is 2
#~ end is 8
#~ increment is 3