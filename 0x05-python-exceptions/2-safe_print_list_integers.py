#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    while (True):
        try:
            for i in range(index, x):
                print("{:d}".format(my_list[i]), end="")
                count += 1
                index += 1
            print("")
            return count
        except (TypeError, ValueError):
            index += 1
            continue
        except IndexError:
            print("")
            return count
