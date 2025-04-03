flag = True
while flag:
    try:
        n1 = int(input())
        n2 = int(input())

        result = n1/n2
    except ZeroDivisionError:
        print("NO")
    except ValueError:
        print("NO")
    print(f'{result:.2f}')