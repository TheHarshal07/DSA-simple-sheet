def encode(word):
    encoded_word = []
    for letter in word:
        letter_code = ord(letter)
        letter_code += 2  # shift by 2 places
        if letter_code > ord('Z'):
            letter_code -= 26
        encoded_letter = chr(letter_code)
        encoded_word.append(encoded_letter)
    return ''.join(encoded_word)

# print(encode(['I', 'N', 'F', 'O', 'R', 'M']))
# Output: IPFQRO



# This is for Odd number of letter in words
def transform_word(word):
    transformed_word = ''
    for i, letter in enumerate(word):
        if i % 2 == 1:  # Check if the position is even
            if letter.isalpha():
                transformed_letter = chr(ord(letter) + 2)
                if transformed_letter > 'Z':
                    transformed_letter = 'A'  # Wrap around to 'A'
            else:
                transformed_letter = letter
        else:
            transformed_letter = letter
        transformed_word += transformed_letter
    return transformed_word

word = "INFORM"
print(transform_word(word))

# This is for even number of letter in words

def pattern(w):
    T = ''
    for i, letter in enumerate(w):
        if i % 2 == 0:
            if letter.isalpha():
                text = chr(ord(letter)+2)
                if text > 'Z':
                    text = 'A'
            else:
                text = letter
        else:
            text = letter

        T += text
    return T

w = "INFORM"
print(pattern(w))


# THis is also for even letter in words

def patternEven(w):
    tt = ''
    for i, letter in enumerate(w):
        if i % 2 == 0:
            if letter.isalpha():
                textTrans = chr(ord(letter)-2)
                if textTrans < 'A':
                    textTrans = 'Z'
            else:
                textTrans = letter
        else:
            textTrans = letter

        tt += textTrans
    return tt

ww = "INFORM"
print(patternEven(ww))


print("-----------Pattern-----------------")

def check_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        #start
        for k in range(2*i+1):
            print("*",end="")
        #space
        for l in range(n-i-1):
            print(" ",end="")
        print("\r")

def ReverseCheck(n):
    for i in range(1,n+1):
        for j in range(i):
            print(" ", end="")
        #stars
        for k in range(2*n-(2*i+1)):
            print("*",end="")
        #space
        for l in range(i):
            print(" ",end="")
        print("\r")


n = 5
check_pattern(n)
ReverseCheck(n)


print("-----------------Number Pattern-------------------------")

def NumberPattern(n):
    for i in range(n):
        for j in range(i+1,0,-1):
            print(j,end=" ")
        print("\r")

n = 5
NumberPattern(n)
print("")
print("----------------- Pythgoral tiplet ---------------")

def Pythagoral(a):
    if a % 2 == 0:
        n = 1
        m = a//2
    else:
        m = a//2 + 1
        n = m-1
        return [m**2-n**2, 2*m*n, m**2+n**2]
    
n = 5
print(Pythagoral(n))
print("")
print("------------ Triplet till limits -------------------")
# /If I want to find out the Pythogoral triplet for limit

def triplet(limit):
    c,m =0,2

    while c < limit:
        for n in range(1,m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > limit:
                break

            print(a,b,c)
        
        m = m + 1


limit = 20
triplet(limit)


print("")
print("----------------Move all # in front------------")

def Movehash(strr):
    # Find out no. of hash in string
    num_hash = strr.count("#")

    # replace the # with empty space
    strr = strr.replace('#', '')

    return "#" * num_hash + strr


input_string = "move#hash#to#front"
print(Movehash(input_string))

print("")
print("--------------- another methode to move the hash ---------------")

# let's point one pointer at the start and one at the end

def Move(strr):
    result = ""

    for s in strr:
        if s == "#":
            result = s + result
        else:
            result += s
    
    return result

input_string = "move#hash#to#front"
print(Move(input_string))

print("")
print("----------- sort the array -----------------")

def sort(arr):
    result = []
    for i in range(len(arr)-1 ,-1,-1):
        result.append(arr[i])

    return result

arr = [ 4,3,2,1]
print(sort(arr))


print("")
print("------ Bubble sort --------------")

def bubbleSort(arr):
    s = 0
    h = len(arr)-1

    while(s<=h):
        arr[s],arr[h] = arr[h],arr[s]
        s += 1
        h -= 1

    return arr

arr = [8,7,6,5]
print(bubbleSort(arr))


print("")
print("-------------- Factorial realted ----------")

def fact(n):
    fact = [0]*(n+1)
    fact[0] = 1
    for i in range(1,n+1):
        fact[i] = fact[i-1]*i
    return fact[n-1]*2

n = 4
print(fact(n))


print("")
print("------------------- Birthday Candles problems ---------------------")
print(" There are candles on cake, you need to identify the tallest candle and find out the occurance of the tallest candle")

import sys
def BirthCandle(arr):
    n = len(arr)
    maxi = -sys.maxsize-1
    for i in range(n):
        if arr[i] >= maxi:
            maxi = arr[i]
    count = 0
    for i in range(n):
        if arr[i] == maxi:
            count += 1
    return count

arr = [4,4,1,2,3]
print(BirthCandle(arr))

print("------------Pattern numbers ------------ ")


def pattern(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end="")
        for k in range(i,n+1):
            print(k,end="")
        print()

def ReversePattern(n):
    for i in range(n-1,0,-1):
        for k in range(i-1):
            print(" ",end="")

        for j in range(i,n+1):
            print(j,end="")
        print("\r")
n = 5
pattern(n)
ReversePattern(n)

print()
print("------ pattern -------------")


def pattern(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end="")
        for k in range(i,n+1):
            print(k,end="")

        for l in range(i):
            print(" ",end="")
        print()

def ReversePattern(n):
    for i in range(n-1,0,-1):
        for k in range(i-1):
            print(" ",end="")

        for j in range(i,n+1):
            print(j,end="")
        print("\r")
n = 5
pattern(n)
ReversePattern(n)

def pattern1(n):
    for i in range(n):
        print(" " * i, end="")
        for j in range(i + 1):
            print(j if j <= i // 2 else i - j, end=" ")
        print()

# Test the function
n = 5
pattern1(n)
