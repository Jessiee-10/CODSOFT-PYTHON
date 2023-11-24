def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (1/2/3/4): ")
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operation in ['1', '2', '3', '4']:
        if operation == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    calculator()
