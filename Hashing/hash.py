# '''
# What is hashing ?
# it is nothing but the pre storing and fetching the element in the array

# '''



# def hashiing(arr, n):
    
#     max_element = max(arr)
#     hash = [0] * (max_element + 1)

#     # pre-compute
#     for i in range(n):
#         hash[arr[i]] += 1

#     for i in range(max_element + 1):
#         # if hash is not 0 
#         # i.e element has occured at leas for one time
#         if hash[i] != 0:
#             print(i, "-->", hash[i])

# n = 5
# arr = [ 5,1,2,5,2,3,1,4]
# print(hashiing(arr,n))


# def precompute_occurrences(s):
#     hash_count = [0] * 26
#     for char in s:
#         hash_count[ord(char) - ord('a')] += 1
#     return hash_count

# if __name__ == "__main__":
#     # Step 1: Static input for the string
#     input_string = "abracadabra"

#     # Precompute occurrences
#     occurrences = precompute_occurrences(input_string)

#     # Print the occurrences of characters in the input string
#     for char in input_string:
#         print(f"{char}: {occurrences[ord(char) - ord('a')]} times")


def hashmap(edges,n):
    dump = {}

    for i in range(n):
        dump[i+1] = 0
    for j in range(n):
        if edges[j] in dump:
            dump[edges[j]] += 1
    return dump.values()

arr = [11, 14, 8, 3, 12, 14, 1, 7, 4, 3 ]
n = 10
print(hashmap(arr,n))



d = {1:0, 2:1,3:2}

for key in d.keys():
    print(key)