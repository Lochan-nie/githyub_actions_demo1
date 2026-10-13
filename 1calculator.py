import time 
#Calculator
print("Welcome to the calculator!")
time.sleep(1)
while True:
    print("What operation would you like to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    op = int(input("Enter the number of the operation you want to perform: "))
    if op == 5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if op == 1:
            print(f"The result of {num1} + {num2} is {num1 + num2}")
        elif op == 2:
            print(f"The result of {num1} - {num2} is {num1 - num2}")
        elif op == 3:
            print(f"The result of {num1} * {num2} is {num1 * num2}")
        elif op == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"The result of {num1} / {num2} is {num1 / num2}")
        else:
            print("Invalid operation. Please try again.")
    


