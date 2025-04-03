print("Enter 2 numbers, which i wil divide")
print('Enter  \'q\' to quit: ')

while True:
    first_number = int(input())
    if first_number == "q":
        break
    firs_number = int(input())
    if firs_number == "q":
        break
    try:
        print(first_number/firs_number)
    except ZeroDivisionError:
        print("CANT")
    else: #execute if try block succeed
        pass