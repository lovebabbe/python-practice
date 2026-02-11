# Safe division program
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter numbers only.")


# Handle file error
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")



# Use finally block
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("Error occurred")
finally:
    print("Program finished")
