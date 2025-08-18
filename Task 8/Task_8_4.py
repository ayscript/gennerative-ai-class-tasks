student = {}

user_name = input("Enter your name: ")
age = int(input("Enter your age: "))

student["name"] = user_name
student["age"] = age

student["scores"] = [70, 85, 90]

student["passed"] = (sum(student["scores"]) / len(student["scores"])) >= 50

student["Teenager"] = student["age"] >= 13 and student["age"] <= 19

print(f"Student Record:\nName: {student["name"]}\nAge: {student["age"]}\nScores: {student["scores"]}\nPassed: {student["passed"]}\nTeenager: {student["Teenager"]}")

