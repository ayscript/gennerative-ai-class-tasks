# 1. Create and display
print("Enter 3 nigerian dishes")
dish1 = input("Enter the first dish: ")
dish2 = input("Enter the second dish: ")
dish3 = input("Enter the third dish: ")

dishes = (dish1, dish2, dish3)
print(dishes)
print(f"{dishes[0]}\n, {dishes[1]}\n, {dishes[2]}\n")

# 2. tuple and input
friends = input("Enter five friends name: ")
friends = friends.split()
friends_tuple = tuple(friends)
print(friends_tuple)

# 3 Tuple operations
print("Enter 5 Nigerian State: ")
first_state = input("Enter first state: ")
second_state = input("Enter second state: ")
third_state = input("Enter third state: ")
fourth_state = input("Enter fourth state: ")
fifth_state = input("Enter fifth state: ")

nigerian_state = (first_state, second_state, third_state, fourth_state, fifth_state)
# print the First state
print(nigerian_state[0])
# Check if Lagos is in the taple
lagosInTuple = "Lagos" in nigerian_state

if lagosInTuple:
    print("Yes, Lagos is there")
else:
    print("No, Lagos is not there")
print(f"Number of state is {len(nigerian_state)}")

# 4 Tuple Unpacking

user_info = (input("Enter your first name: "),
input("Enter your age: "),
input("Enter your favourite colour: "),
input("Enter your home town: ")
    
)

userName, age, favorite_color, home_town = user_info
print(f"User Name: {userName}\nAge: {age}\nFavorite Color: {favorite_color}\nHome Town: {home_town}")

# 5 Modify Tuple Indirectly
shopping_list = (input("Enter your first shopping item"), input("Enter your second shopping item: "), input("Enter your third shopping item: "))
shopping_list = list(shopping_list)
one_more = input("Enter one  more item: ")
shopping_list.append(one_more)
another_one = input("Enter another one: ")
shopping_list.append(another_one)

print("|".join((tuple(shopping_list))))

# Task 6 - Attendance tracker
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
month_of_the_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

user_info = (input("Enter student's name: "), input("Enter Gender: "), input("Enter Course track: "), int(input("Enter current month (1 - 12): ")), int(input("Enter current day (1-7): ")))
