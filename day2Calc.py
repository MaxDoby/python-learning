x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
operation=input("Choose operation:(+ - / *)")
if operation == "+":
	print(x+y)
elif operation=="-":
	print(x-y)
elif operation=="*":
	print(x*y)
elif operation=="/":
	if y==0:
		print("Error: division by zero")
	else:
		print(x/y)
else:
	print("Uknown operation")