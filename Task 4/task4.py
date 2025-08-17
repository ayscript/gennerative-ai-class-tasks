# Task 1: Favorite life quote
lifeQuote = input("Enter your favorite life quote: ")
lifeQuote = lifeQuote.title()
print(f"\"{lifeQuote}\"")

# Task 2: Shopping list manager
shoppingList = []
userInput = input("Enter the first item: ")
shoppingList.append(userInput)
userInput = input("Enter the second item: ")
shoppingList.append(userInput)
userInput = input("Enter the third item: ")
shoppingList.append(userInput)
print(shoppingList)

# Task 3: Word counter
word = input("Enter a sentence: ")
print(len(word.split()))

# Task 4: Name Organozer
userInput = input("Enter 5 names separated by spaces: ")
userInput = userInput.lower().split()
userInput.sort()
print(userInput)

# Task 5: Student score tracker