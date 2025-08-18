store = {
    "Book": 10,
    "Pen": 20,
    "Bag": 5
}


item_to_buy = input("Enter the item you want to buy (We have Book, Pen and Bag): ")
quantity = int(input(f"Enter the quantity of {item_to_buy}s you want to buy: "))

print(f"Before purchase: {store}")

store[item_to_buy.title()] -= quantity

print(f"After purchase: {store}")