#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = [*set(my_list)]
return (uniq)

plist = [1, 2, 3, 4, 2, 1, 5, 3]
print(uniq_add(plist))
