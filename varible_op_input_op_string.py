var = 1 
print(var)
var = 2
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance , client_name,var)
print(var)
print("tell me anythings")
anything =input()

print("Hmm...", anything, "... Really?")

# !  error
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)


anything = int( input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#  ~ or
anything = float( input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

fnam = input("May I have your first name, please? ") 
lnam = input("May I have your last name, please? ") 
print("Thank you.\n") 
print("Your name is "+fnam+" "+lnam+".")

print("+" + 10 * "-" + "+")
print( ("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))