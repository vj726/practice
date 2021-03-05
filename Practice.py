while True:
    n = (input("Enter a numbers: ")).split(',')
    print(type(n), n)
    n = int(n)
    print(type(n), n)
    if n:
        fact = 1
        for i in range(1, n+1):
            print(i)
            fact *= i

        print(fact,)
    else:
        break
