print("==== Calculator ====")
num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))

print("\nChoose an operation:")
print("  +  Addition")
print("  -  Subtraction")
print("  *  Multiplication")
print("  /  Division")

op = input("\nEnter operator (+, -, *, /): ")

if op == "+":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")

elif op == "-":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")

elif op == "*":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")

elif op == "/":
    if num2 == 0:
        print("\nError: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")

else:

    print("\nInvalid operator. Please use +, -, *, or / only.")
