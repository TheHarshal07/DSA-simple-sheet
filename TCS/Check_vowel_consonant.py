'''
Here we have to check wether the alphabet is vowel and consonent

for example:
alphabet -> "a" is a vowel
alphabet -> "h" is consonent

'''
def Check_alphabet(alpha):
    vowel = "aeiou"

    for letter in alpha:
        if letter.lower() in vowel:
            print("vowel")
        else:
            print("consonent")

word = input("Enter the alphabet")
Check_alphabet(word)
        