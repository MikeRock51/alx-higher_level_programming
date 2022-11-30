#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            j = ord(i) - 32
            k = chr(j)
            upper += k
        else:
            upper += i
    print(upper)

# uppercase("best FRIENd")
