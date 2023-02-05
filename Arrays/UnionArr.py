a = [1,2,4,6,8]
b = [1,2,3,4,7,8,9]





hashmap = {}

for i in range(len(a)):
    hashmap[a[i]] = i
    # print(hashmap[a[i]])

for i in range(len(b)):
    hashmap[b[i]] = i
    print(hashmap[b[i]])

print("Union of the two arrays is :")
print(hashmap)
for key in hashmap.keys():
    print(key,end="")
print("\n")
hs =set()


#Here we gonna used set to store multiple items in variable

for i in range(len(a)):
    hs.add(a[i])
print("Intersection is :")
for i in range(len(b)):
    if b[i] in hs:
        print(b[i],end="")