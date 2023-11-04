#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        if 'c' in my_string:
            index = my_string.find("c")
            new_string = my_string[:index] + my_string[index + 1:]
            if 'C' in new_string:
                index = new_string.find("C")
                new_string = new_string[:index] + new_string[index + 1:]
                return (new_string)
            else:
                return (new_string)
        elif 'C' in my_string:
            index = my_string.find("C")
            new_string = my_string[:index] + my_string[index + 1:]
            return (new_string)
        else:
            return (my_string)
