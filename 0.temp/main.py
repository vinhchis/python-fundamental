def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    a = 10
    b = 20
    
    print(f"{a} + {b} = ", add(a,b))
    print(f"{a} - {b} = ", sub(a,b))


if __name__ == '__main__':
    main()