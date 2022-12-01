#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    sum = 0
    for i in av[1:]:
        sum += int(i)
    print(sum)
