#Here we have to remove the all the character other than alphabets from string

def remove_charcter(String):
    n = len(String)
    new_string = ""
    for char in String:

        if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
            new_string += char

    return new_string


String =  "$Gee*k;s..fo, r’Ge^eks?"
print(remove_charcter(String))