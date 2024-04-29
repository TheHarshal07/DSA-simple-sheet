# Here we have to find the vowels, consonant and special charcter in the string

def CountAll(Str):
    vowels = 'aeiou'
    count_vowel = 0
    count_conso = 0
    count_num = 0
    count_special = 0

    for i in range(0, len(Str)):

        ch = Str[i]

        if ((ch >= 'a' and ch <= 'z') or (ch >="A" and ch <= "Z")):

            ch = ch.lower()
            if ch in vowels:
                count_vowel += 1
            else:
                count_conso += 1

        elif (ch >= '0' and ch <= '9'):
            count_num += 1
        else:
            count_special += 1
    
    return [count_vowel, count_conso,count_num,count_special]


Str = "geeks for geeks121"
print(CountAll(Str))




    