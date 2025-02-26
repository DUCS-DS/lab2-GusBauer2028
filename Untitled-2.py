def AA_():
    n = 8
    m = 50
    for _ in range(n):  
        print("a" * m)  # 50 characters wide

AA_()

def AAA_():
    n = 8
    m = 7
    d = 0
    z = 0
    for _ in range(n):
        if m > 0:  # Avoid printing an empty line
            print(" " * d + "a" * m)
            z += m
            m -= 1
            d += 1

    print("The triangle prints out", z, "A's")

AAA_()
