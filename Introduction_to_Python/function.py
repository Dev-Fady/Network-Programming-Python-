def my_message():
    print("Hello, World!")

my_message()

def message():
    print("Enter a value: ")
message = "fady"
print(message)

# ~or
def messagePO():
    print("Enter a value: ")
messagePO = 50
print(messagePO)
# Function with arguments 

def message_with_args(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    print("Hello, "+name+" ! " +" You are"+ age +" years old.")
    print("Hello, ",name," ! " ," You are", age ," years old.")

name =input("Enter a name ")
age=input("Enter a age ")
message_with_args(name,age)
# ~ or 
message_with_args(name=name,age=age)

def happy_new_year(wishes = True): 
    print("Three...") 
    print("Two...") 
    print("One...") 
    if not wishes: 
        return
    print("Happy New Year!")
happy_new_year(wishes=False)
happy_new_year()

def boring_function():
    return 123

x=boring_function()
print("The boring_function has returned its result. It's:",x)

#^ A few words about None: continued
def strange_function(n):
    if(n%2==0):
        return True
print(strange_function(10))
print(strange_function(5))

