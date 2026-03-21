#Mateusz Drozdz, made on Phyton Online IDE.

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b 
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
    if b == 0:
        return("Error: You cannot divide by zero!")
        
#1 Ask for numbers

n1 = int(input("Enter the 1st nb:  "))
n2 = int(input("Enter the 2nd nb:  "))

# Ask what they want to do with it

print("\nChoose an operation")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1/2/3/4): ")

# Logistics

if choice == '1':
    print(f"Result: {n1} + {n2} = {add(n1, n2)}")
elif choice == '2':
    print(f"Result: {n1} - {n2} = {subtract(n1, n2)}")
elif choice == '3':
    print(f"Result: {n1} * {n2} = {multiply(n1, n2)}")
elif choice == '4':
    print(f"Result: {n1} * {n2} = {divide(n1, n2)}")

