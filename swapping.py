# Python program to swap two numbers

print("program to swap two numbers using a temporary variable")

# Taking input from the user
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

# Display original values
print("Before Swapping")
print("First Number :", num1)
print("Second Number:", num2)

# Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Display swapped values
print("\nAfter Swapping")
print("First Number :", num1)
print("Second Number:", num2)

print("\nSwapping completed successfully!")
