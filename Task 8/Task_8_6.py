utme_score = int(input("Enter you utme score: "))
score_above_200 = utme_score >= 200

olevel_credits = int(input("how many credit do you have in your o level in relevant subject including English and maths? "))
number_of_sittings = int(input("How many sitting do you have in o level? "))
olevel_qualification = olevel_credits >= 5 and number_of_sittings == 1

student_age = int(input("How old are you? "))
student_age_qualification = student_age >= 16

print(f"Student is qualified for admission? {score_above_200 and olevel_qualification and student_age_qualification}")

print(f"Because:\nScored at least 200: {score_above_200},\nHad at least 5 credit in wassce including maths and english: {olevel_qualification} and\nStudent's age is at least 16: {student_age_qualification}")