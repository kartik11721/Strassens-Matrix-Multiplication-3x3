#Strassens Matrix Multiplication
def strassens():
    a = firstMatrix()
    print("\n")
    b = secondMatrix()
    c = multiplication(a,b)
    print(f'AxB :\n|{c[0]} {c[1]}|\n|{c[2]} {c[3]}|')
    return c

def firstMatrix():
    a = []
    for i in range(3):
        x = []
        for j in range(3):
            x.append(int(input(f"Enter Value in A[{i}][{j}] : ")))
        a.append(x)
    return a

def secondMatrix():
    b = []
    for i in range(3):
        y = []
        for j in range(3):
            y.append(int(input(f"Enter Value in B[{i}][{j}] : ")))
        b.append(y)
    return(b)

def multiplication(a,b):
    m1 = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
    m2 = (a[1][0] + a[1][1]) * b[0][0]
    m3 = a[0][0] * (b[0][1] - b[1][1])
    m4 = a[1][1] * (b[1][0] - b[0][0])
    m5 = (a[0][0] + a[0][1]) * b[1][1]
    m6 = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
    m7 = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1])
    c =[[m1 + m4 - m5 + m7],[m3 + m5],[m2 + m4],[m1 - m2 + m3 + m6]]
    return c

if __name__ == "__main__":
    strassens()
