r = int(input("enter the number :"))
# Time complexity is O(n^2)
# for i in range(r):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print("\r")


#Time complexity is O(n)
hashmap=[]
for i in range(1,r+1):
    hashmap.append("* "*i)
print("\n".join(hashmap))