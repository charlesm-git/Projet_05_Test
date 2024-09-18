words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

word_list = []
for word in words:
    vowels = 0
    for char in word:
        if char in ['a', 'e', 'i', 'o', 'u', 'y']:
            vowels += 1
    vowel_counting = (word, vowels)
    word_list.append(vowel_counting)
print(word_list)
