
# sentence = input("Enter a sentence: ")
# vowel_o = sentence.lower().count("o")
# vowel_i = sentence.lower().count("i")
# vowel_u = sentence.lower().count("u")
# vowel_e = sentence.lower().count("e")
# vowel_a = sentence.lower().count("a")
# total = vowel_o + vowel_i + vowel_u + vowel_e + vowel_a
# print(total)

# A program to count the number of vowels in a sentence
sentence = input("Enter a sentence: ")

vowel_list = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0

for i in range(len(vowel_list)):
    vowel_count += sentence.lower().count(vowel_list[i])
    print(f"There are {sentence.lower().count(vowel_list[i])} {vowel_list[i]}'s in the sentence {sentence}")
    
    
print(f"There are {vowel_count} vowels in the sentence {sentence}")