#Here we have to find the number of words and vowels in String

def count_words(sentence):
    sent = sentence.split()
    return len(sent)

string = "My name is Harry"
print(count_words(string))
