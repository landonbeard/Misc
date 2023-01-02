# Creates a dictionary mapping English words to Katakana characters
katakana_dict = {
  "a": "ア",
  "i": "イ",
  "u": "ウ",
  "e": "エ",
  "o": "オ",
  "ka": "カ",
  "ki": "キ",
  "ku": "ク",
  "ke": "ケ",
  "ko": "コ",
  "sa": "サ",
  "shi": "シ",
  "su": "ス",
  "se": "セ",
  "so": "ソ",
  "ta": "タ",
  "chi": "チ",
  "tsu": "ツ",
  "te": "テ",
  "to": "ト",
  "na": "ナ",
  "ni": "ニ",
  "nu": "ヌ",
  "ne": "ネ",
  "no": "ノ",
  "ha": "ハ",
  "hi": "ヒ",
  "fu": "フ",
  "he": "ヘ",
  "ho": "ホ",
  "ma": "マ",
  "mi": "ミ",
  "mu": "ム",
  "me": "メ",
  "mo": "モ",
  "ya": "ヤ",
  "yu": "ユ",
  "yo": "ヨ",
  "ra": "ラ",
  "ri": "リ",
  "ru": "ル",
  "re": "レ",
  "ro": "ロ",
  "wa": "ワ",
  "wo": "ヲ",
  "n": "ン",
}

# Print a list of English words
print("English:")
for word in katakana_dict.keys():
  print(word)

# Prompt the user to enter an English word
english_word = input("Enter an English word: ")

# Look up the corresponding Katakana character
katakana_char = katakana_dict.get(english_word, "")

# Print the Katakana character
print(f"Katakana: {katakana_char}")

