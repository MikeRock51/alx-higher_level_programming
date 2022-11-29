#!/usr/bin/python3
i = 0
while i < 9:
    j = i + 1
    while j < 10:
        print('{:d}{:d}'.format(i, j), end='')
        if (i != 8 or j != 9):
            print(', ', end='')
        j += 1
    i += 1
print()
