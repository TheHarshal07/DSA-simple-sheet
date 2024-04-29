''' 
Here we have to change the case of the letter
i.e if the input is in "HELLO" change it to --> "hello"  ( Upper to lower or vice vers )

'''
def Change_case(letter):
    if letter.islower():
        return letter.upper()
    elif letter.isupper():
        return letter.lower()
    
    else:
        return "invalid input"

word = input("HARSHAL")
print(Change_case(word))  # Output  --> harshal