# Here we gonna converting the given string into the camel case
# Camel case - Capitalize the first letter of each word except the first one.

def camelcase(string):
    s = string.lower()
    words = s.split(" ")

    for i in range(1,len(words)):
        words[i] = words[i].capitalize()
    camel_case = " ".join(words)
    return camel_case

string = "hello HARSHAL HOW are you"
print(camelcase(string))