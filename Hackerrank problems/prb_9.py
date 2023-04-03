def gen(n):
    seq = "1"
    for i in range(n-1):
        seq += str(i%2)
        print(seq)
gen(5)