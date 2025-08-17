# task 1
bio_data = {}

bio_data['name'] = input("Enter your full name: ")
bio_data['age'] = int(input("Enter your age: "))
bio_data['gender'] = input("Enter your gender: ")
bio_data['course'] = input("Enter your courses: ")

print(bio_data)

# task 2
items = ['Bread', 'Sardine', 'Coke', 'Pepsi']

items_dict = {}

for item in items:
    user_input = input(f"Enter the price of {item}: ")
    items_dict[item] = user_input

print(items_dict)

item_to_update = input("Enter an item you want to update: ")

items_dict[item_to_update] = input("Enter the updated amount: ")

print(items_dict)

# 3
