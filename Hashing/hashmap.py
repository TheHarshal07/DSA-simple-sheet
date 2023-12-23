'''
hashing methode:

In this we will first pre-compute the each element in the frequency array
and then we will fetch form that array

'''

def hash_count(arr):
    hashmap = {}
    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1 # pre-computing is done over here
    
    for values, key in hashmap.items():
        print(f"{values} --> {key} times")

arr = [1,2,4,1,2,5,6,3,2]
print(hash_count(arr))



'''
But what I want to find out the occurenc of particular string,
Then I can go with ASCII values.

'''

def hash_char(s):
    hash_str = {}

    for char in s:
        if char in hash_str:
            hash_str[char] += 1
        else:
            hash_str[char] = 1  # pre-computing is done over here
    
    for char, count in hash_str.items():
        print(f"{char} --> {count} times")

string = "abcrdhbcacbdrf"
print(hash_char(string))