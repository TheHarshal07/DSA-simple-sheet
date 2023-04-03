def encode(word):
    encoded_word = []
    for letter in word:
        letter_code = ord(letter)
        letter_code += 2  # shift by 2 places
        if letter_code > ord('Z'):
            letter_code -= 26
        encoded_letter = chr(letter_code)
        encoded_word.append(encoded_letter)
    return ''.join(encoded_word)

print(encode(['I', 'N', 'F', 'O', 'R', 'M']))
# Output: IPFQRO