num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")

# The output above compares num1 with num2 using the equality sign to see if both values are equal
# 3 use case:
# 1. user identification
# 2. Password confirmation
# 3. CAPTCHA verification

# Password Confirmation
password = input("Create a new password: ")
confirm_password = input("Confirm your password: ")

print(f"Password matched?: {password == confirm_password}")

print(f"{num1} != {num2} : {num1 != num2}")

# The output above checks if a num1 is not equal to num2
# 3 use cases:
# 1. Username creation (to check if a username has already existed)
# 2. checking if a seat number has been booked or not
# 3. checking if a file name is already existing

# Username creation
user_name = 'ayscript'
create_user_name = input("Enter a new user name: ")
print(f"User name existing?: {user_name == create_user_name}")


print(f"{num1} > {num2} : {num1 > num2}")

# The above output check if num1 is greater than num2
# Use cases:
# 1. Age categorizing
# 2. Password length restriction
# 3. Age restrictions

# Age categorizing
user_age = int(input("Enter your age: "))
print(f"User is an adult?: {user_age > 18}")


print(f"{num1} < {num2} : {num1 < num2}")

# The above output check if num1 is less than num2
# Use cases:
# 1. Password length restriction
# 2. Age restriction
# 3. Power saving mode for phone batteries

# Power saving mode for phone batteries
battery_limit = 20
my_battery_limit = int(input("Enter your battery level: "))
print(f"Activate power saving mode?: {my_battery_limit < battery_limit}")