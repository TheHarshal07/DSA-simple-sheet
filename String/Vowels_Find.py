#Here we need to find the vowels and consonents from the given list

def unique_letters(word):
    return list(set(word))

def vowel_consonent(letters):
    vowel = 'aeiou'
    vowel_list = []
    consonent_list = []

    for letter in letters:
        if letter.lower() in vowel:
            vowel_list.append(letter.lower())
        else:
            consonent_list.append(letter)
    
    return vowel_list, consonent_list

words = ['Ankur', 'Tejas', 'Yash']
vow = []
conso = []
for name in words:
    unique_letter = unique_letters(name)
    vowels, cons = vowel_consonent(unique_letter)
    vow.append(vowels)
    conso.append(cons)

print("Vowels ", vow)
print("Consonent ", conso)
