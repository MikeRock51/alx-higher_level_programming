#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for a in my_list:
        if y < x:
            try:
                print(a, end="")
                y += 1
            except Exception:
                break
    print()
    return (y)
