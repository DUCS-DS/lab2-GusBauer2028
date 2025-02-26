def AA_(n,m):
    for _ in range(n):  
        print("a" * m)  # 50 characters wide

AA_(8,50)

def AAA_():
    n = 8
    m = 7
    d = 0
    z = 0
    for _ in range(n):
        if m > 0:  
            print(" " * d + "a" * m)
            z += m
            m -= 1
            d += 1

    print("The triangle prints out", z, "A's")

AAA_()
def ABCs():
    string = "ABCDEFGHIJ"
    for i, char1 in enumerate(string): 
        for d, char2 in enumerate(string[:i+1]):  # Limit columns to i+1
            print(abs(ord(char2) - ord(char1)), end=" ")
        print()  

ABCs()

