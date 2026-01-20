def is_even(num):
    return num % 2 == 0

def is_prime(num):
	if num<=1:
		return False
	for x in range(2, num):
		if num % x == 0:
			return False
	return True

def square(num):
    return num * num

while True:
	print("\nMenu:")
	print("1 - Check even/odd")
	print("2 - Check prime")
	print("3 - Square a number")
	print("4 - Exit")

	choice=input("Choose an option (1-4): ")
	if choice=="4":
		print("Goodbye!")
		break
	elif choice not in ("1", "2", "3", "4"):
		print("Wrong number")
		continue

	try:
		num=int(input("Enter a number:"))
	except ValueError:
		print("Please introduce an integer number")
		continue
	if choice=="1":
		print("Even" if is_even(num) else "Odd")
	elif choice=="2":
		print("Prime" if is_prime(num) else "Not prime")
	elif choice=="3":
		print(f"Square: {square(num)}")
	else:
		print("Uknown operation")