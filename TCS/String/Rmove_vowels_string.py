
# Here we have to remove the vowels fromt the string


def Remove_vowle(String):
    vowel = "aeiou"
    new_string = ""

    for char in String:
        if char not in vowel:
            new_string += char

    return new_string

string = "GeeksforGeeks - A Computer Science Portal for Geeks"
print(Remove_vowle(string))