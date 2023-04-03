# Here we can find the repeated element in the array

a = [1,2,3,2,5,6,7,1,2]
hashmap = {}
rep = set()
if not rep:
    print("Hello0")
for i in a:
   if i in hashmap:
    hashmap[i] += 1
    rep.add(i)
   else:
    hashmap[i] = 1
    print(hashmap)
print(rep)