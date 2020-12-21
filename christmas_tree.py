s = "Khanh Pham"

def canh_cay(n):
    for i in range(n):
        for j in range(n-i):
            print('.', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        for l in range(n-i):
            print('.', end=' ')
        print()

def than_cay(n):
    m = len(s)
    for i in range(m+2):
        for j in range(n-1):
            print('.', end=' ')
        print('*', end=' ')
        if i==0 or i==m+1 or s[i-1]==' ':
            print('*', end=' ')
        else:
            print(s[i-1].upper(), end=' ')
        print('*', end=' ')
        for k in range(n-1):
            print('.', end=' ')
        print()


def ve_cay(n):
    canh_cay(n)
    canh_cay(n)
    than_cay(n)

ve_cay(7)


