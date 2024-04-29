'''
Here we have to find the most frequent alphabet in string
for example:

string = Happy
so here "p" is the most frequent alphabet
'''

def most_frequent(string):
    hashmap = {}
    for char in string:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    
    max_freq = 0
    max_char_freq = None
    for key,value in hashmap.items():
        if value > max_freq:
            max_freq = value
            max_char_freq = key

    return max_char_freq

word = "Happy"
print(most_frequent(word)) # output --> p