def sub(a,b):
    if b == 0:
        # raise ZeroDivisionError
        raise Exception('B can not be 0')
    return a/b

def main():
    a = 10
    b = 0
    print(a, '/', b , '=', str(sub(a,b)))

    print('End Program!!')

main()