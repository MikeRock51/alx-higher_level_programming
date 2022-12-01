#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    av = sys.argv
    ac = len(av)
    
    print(av[2])

    a = int(av[1])
    b = int(av[3])
    
    if ac != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    if av[2] != '+' and av[2] != '-' and av[2] != '*' and av[2] != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit

    if av[2] == '+':
        print('{:} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif av[2] == '-':
        print('{:} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif av[2] == "*":
        print('{:} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif av[2] == '/':
        print('{:} / {:d} = {:d}'.format(a, b, div(a, b)))
