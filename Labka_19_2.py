"""
13.	 Дано типізований файл, який містить дійсні числа.
Видалити елементи, які слідують за парними числами.
"""
a = []
m = []
with open("my.txt") as file:
    for line in file:
        num = float(line)
        a.append(num)
    print(a)
    i = 0
    while i < len(a):
        if a[i] % 2 == 0:
            i += 1
            del a[i]
        else:
            i += 1

    print(a)

