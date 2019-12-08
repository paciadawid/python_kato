def fibonacci1(n):
    a1 = 0
    a2 = 1
    n_seq = [a1, a2]

    if type(n) != int:
        return False

    if n <= 0 or n > 10000:
        return False

    if n == 1:
        return a1
    elif n == 2:
        return a2
    else:
        for i in range(2, n):
            n_seq.append(n_seq[-1] + n_seq[-2])
            #print(n_seq)
        return n_seq[-1]

def fibonacci2(n):
    a1 = 0
    a2 = 1
    if n == 0:
        return a1
    elif n == 1:
        return a2
    else:
        for i in range(2, n):
            a1, a2 = a2, a1 + a2

print(fibonacci1(10))
