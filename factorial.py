number = int(input("Enter the number:"))
factorial = 1
temp = number

if number == 0 or number == 1:
	print(factorial)
while number != 0:
	factorial = factorial * number
	number = number - 1

print(f"The factorial of the {temp} is {factorial}.")