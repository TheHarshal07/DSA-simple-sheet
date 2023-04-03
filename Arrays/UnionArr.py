a = [1,2,4,6,8,9]
b = [2,4,8,7]

hashmap = {}

for i in range(len(a)):
    hashmap[a[i]] = i
    # print(hashmap)

for i in range(len(b)):
    hashmap[b[i]] = i
    print(hashmap)

print("Union of the two arrays is :")
# print(len(hashmap))
for key in hashmap.keys():
    print(key,end="")
print("\n")
hs =set()   #Used to store multiple items in single variable


#Here we gonna used set to store multiple items in variable

for i in range(len(a)):
    hs.add(a[i])
print("Intersection is :")
for i in range(len(b)):
    if b[i] in hs:
        print(b[i],end="")