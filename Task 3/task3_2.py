# 6
given_sring = "python is a good programming language"
print("python" in given_sring)

# 7
word = reversed("Hello World")
rev_word = "".join(word)
print(rev_word)

# 8
text = " Hello World "
print(text.strip())

# 9
sentence = input("Enter a sentence: ")
vowel_o = sentence.lower().count("o")
vowel_i = sentence.lower().count("i")
vowel_u = sentence.lower().count("u")
vowel_e = sentence.lower().count("e")
vowel_a = sentence.lower().count("a")
total = vowel_o + vowel_i + vowel_u + vowel_e + vowel_a
print(total)

# 10
string_text = '1234'
string_to_int = int(string_text)
print(string_to_int * 2)