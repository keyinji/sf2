file_name = 'book.txt'
try: 
    input_file = open(file_name, "r")
except FileNotFoundError: 
    print("ok")
    output_file = open(file_name, 'w')
else:
    for line in input_file:
        print(line.rstrip())

input_file = open("The_Ugly_Duckling.txt", 'r', encoding="UTF8")

ugly_duckling_txt = input_file.readlines()
output_file.writelines(ugly_duckling_txt)
input_file.close()
output_file.close()