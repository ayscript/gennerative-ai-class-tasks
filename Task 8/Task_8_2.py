# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

"""
The code accepts the user's name, age and score, it then checs the eligibility of the user by comparing the age with 18 and the score with 70, if user is below 18 and score above 70, the user is eligible
"""


# Federal govt. scholarship eligibility requirements
name = input("Enter your name: ")
citizenship = bool(input("You are from which country? (Enter any key if you are from Nigeria, leave blank if otherwise): "))

university_requirement = bool(input("Enter any key if you are enrolled in a recognized university, leave blank if otherwise: "))

existing_scholarship = bool(input("Enter any key if you are currently under a scholarship, leave blank if otherwise: "))

academic_qualification = bool(input("Enter any key if you have five distinctions in your WASSCE exams, leave blank if otherwise: "))

print(f"{name} is qualified?: {citizenship and university_requirement and existing_scholarship and academic_qualification}")