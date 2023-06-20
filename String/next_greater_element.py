def nextgreaterelement(ele):
    n = len(ele)
    for i in range(n-2,-1,-1):   # 132465
        if ele[i] < ele[i+1]:
            break
    for j in range(n-1,i,-1):
        print(ele[j])
        break
    # swaping
    ele[i],ele[j] = ele[j],ele[i]

    #reversed the list
    ele[i+1:] = reversed(ele[i+1:])

    #Converting list into the array
    a = 0
    for k in range(n):
        a = a*10 + ele[k]
    print(a)

ar = "132465"
ar= list(map(int,ar))
nextgreaterelement(ar)
