# Task 1
favorite_fruits = (input('Enter your first favorite fruit: '), input('Enter your second favorite fruit: '), input('Enter your third favorite fruit: '), input('Enter your fourth favorite fruit: '), input('Enter your fifth favorite fruit: '))
print(favorite_fruits)


# Task 2
#unique names collector 
#collect the names one by one
print("Enter your full name: ")
i= tuple(range(1,5))
attendance = set()
for x in i:
    user_input = input(f"Enter your full name: ").lower()
    if user_input in attendance:
        print("input is existing")
    attendance.add(user_input)
    print(sorted(attendance))


# Task 3
seat_numbers = set(range(1,51))

booking_number = int(input("Pick a seat number between 1 to 50: "))

seat_numbers.remove(booking_number)

print(seat_numbers)

# Task 4
voter_names = set()

for i in range(1,5):
    user_input = input("Enter your name: ")
    if user_input in voter_names:
        print('You have already voted!')
    else:
        voter_names.add(user_input)

print(voter_names)