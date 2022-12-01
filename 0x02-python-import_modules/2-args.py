#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    av = sys.argv

    if argc < 2:
        print('0 arguments.')
    elif argc == 2:
        print('1 argument:')
        print('1: {:s}'.format(av[1]))
    else:
        i = 1
        print('{:d} arguments:'.format(argc - 1))
        for arg in av[1:]:
            print('{:d}: {:s}'.format(i, arg))
            i += 1;
