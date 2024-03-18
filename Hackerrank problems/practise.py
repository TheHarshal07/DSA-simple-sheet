# Pythagoral triplet

def triplet(limit):
    c,m = 0,2
    while c < limit:
        for n in range(1,m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n*n

            if c > limit:
                break
            print(a,b,c)

        m = m+1

limit = 20
triplet(limit)


print()
print("------------------- Move the Hashes --------------")

def MoveHash(string):
    result = ""
    for letter in string:
        if letter == "#":
            result = letter + result
        else:
            result += letter
    return result

string = "###MoveHashtoFront" 
print(MoveHash(string))

print()
print("-------------- another methode -----------")

def hash(strint):
    #count the number of Hashes
    num_hashe = string.count("#")

    #replce the hash with space
    strr = string.replace("#","")

    return "#"*num_hashe + strr

string = "###MoveHashtoFront" 
print(hash(string))

print()
print("--------------------- conference probmles ----------")

def conferance(n):

    fact = [0]*(n+1)
    fact[0] = 1

    for i in range(1,n+1):
        fact[i] = fact[i-1]*i
    return fact[n-1]*2

print(conferance(4))

print()
print("------- Start Pattern ------------")


def star(n):
    for i in range(n):
        #space
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        #space
        for l in range(n-i-1):
            print(" ",end="")
        print("\r")

def ReverseStar(n):
    for i in range(1,n+1):
        #space
        for j in range(i):
            print(" ",end="")
        #star
        for k in range(2*n-(2*i+1)):
            print("*",end="")
        for l in range(i):
            print(" ",end ="")
        print("\r")


star(5)
ReverseStar(5)

print()
print("-------- number pattern ----------")

def NumberPattern(n):
    for i in range(n):
        for j in range(i+1,0,-1):
            print(j,end=" ")
        print("\r")

NumberPattern(4)


print()
print("------------ number pattern ---------- ")

def num(n):
    for i in range(1,n+1):
        for j in range(i):
            if j % 2 == 0:
                print("1",end="")
            else:
                print("0",end="")
        print("\r")

num(5)


print()
print("---------- start pattern----------")

def ss(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print("\r")
    
def Rs(n):
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end="")
        print("\r")
ss(4)
Rs(4)


def hidden(string):
    text  = ""
    for i,letter in enumerate(string):
        if i % 2 == 1:
            if letter.isalpha():
                textTransForm = chr(ord(letter)+2)
                if textTransForm > "Z":
                    textTransForm = "A"
            else:
                textTransForm = letter
        else:
            textTransForm = letter
        text += textTransForm
    return text

string = "LEARN"
print(hidden(string))


print()
print("---------------- pattern try  ------------------")
def patt(n):
    for i in range(n-1,0,-1):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(1,i+1):
            print(k,end="")
        for l in range(n-i-1):
            print(" ",end="")
        
        print("\r")
patt(5)



print()
print("------------- Odd hddern pattern ---------------")


def OddPattern(string):
    Text = ""
    for i,letter in enumerate(string):
        if i % 2 == 0:
            if letter.isalpha():
                textTransform = chr(ord(letter)-2)
                if textTransform < 'A':
                    textTransform = 'Z'
            else:
                textTransform = letter
        else:
            textTransform = letter
        Text += textTransform
    return Text


string = "TALENT"
print(OddPattern(string))



