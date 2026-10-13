import time 
#Calculator
print("Welcome to the calculator!")
time.sleep(1)



num1 = 23
num2 = 89

print(f"The result of {num1} + {num2} is {num1 + num2}")

print(f"The result of {num1} - {num2} is {num1 - num2}")

print(f"The result of {num1} * {num2} is {num1 * num2}")

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result of {num1} / {num2} is {num1 / num2}")

print("Invalid operation. Please try again.")



