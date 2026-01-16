passw = input("Enter your password:")
if passw == ("Python123"):
	print("Access granted")
else:
	print("Access denied")
x=7
number=int(input("Guess the number:"))
if x<7:
	print("Too low")
elif x>7:
	print("Too high")
else:
	print("Correct!")