"""
13.	Дано текстовий файл, який містить кількість цілих чисел кратну 3.
 Визначити суму елементів з номерами, які кратні 3.
"""
with open("my.txt") as s:
    r = s.readlines()
    print(r)
    r_three = r[2::3]
    print(r_three)
    s = int(r_three[0])+int(r_three[1])+int(r_three[2])
    print(s)

