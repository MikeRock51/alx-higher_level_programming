#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_result = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
            continue
        except IndexError:
            print("out of range")
            div_result = 0
            continue
        finally:
            div_list.append(div_result)

    return (div_list)
