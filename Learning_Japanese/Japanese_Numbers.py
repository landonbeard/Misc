# Creates a dictionary mapping Japanese romanji to English numbers
number_dict = {
  "ichi": "one",
  "ni": "two",
  "san": "three",
  "shi": "four",
  "go": "five",
  "roku": "six",
  "shichi": "seven",
  "hachi": "eight",
  "kyuu": "nine",
  "juu": "ten"
}

# Prints a list of Japanese romanji
print("Japanese romanji:")
for word in number_dict.keys():
  print(word)

# Prompts the user to enter a Japanese romanji
japanese_romanji = input("Enter a Japanese romanji: ")

# Look up the corresponding English number
english_number = number_dict.get(japanese_romanji, "")

# Prints the English number
print(f"English: {english_number}")

