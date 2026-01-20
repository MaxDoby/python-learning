
while True:
	try:
		x=int(input("Enter a number from 1 to 10"))
		if x<0 or x>10:
			print("Wrong Number")
			continue
		for y in range(1, 11):
			print(f"{x} x {y} = {x * y}")
		break
	except ValueError:
		print("Please introduce a number")


def is_even(num):
    return num % 2 == 0

try:
    num = int(input("Give me an integer number to check: "))
    if is_even(num):
        print("The number is even")
    else:
        print("The number is odd")
except ValueError:
    print("Please introduce an integer number")






def cube(x):
	return x * x * x
try:
	num=float(input("Give me a number: "))
	print(f"The result is: {cube(num)}")
except ValueError:
	print("Please introduce a number: ")






def is_even(num):
	return num % 2 == 0
try:
	num=int(input("Give me a number to check: "))
	print(f"The result is {is_even(num)}")
except ValueError:
	print("Please introduce a number")



def is_prime(num):
	if num<=1:
		return False
	for x in range(2, num):
		if num % x == 0:
			return False
	return True
try:
	num=int(input("Give me a number to check:"))
	print(f"The result is {is_prime(num)}")
except ValueError:
	print("Please introduce an integer number")
