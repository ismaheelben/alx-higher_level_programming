#!/usr/bin/python3
"""1-my_list module
"""


class MyList(list):
    """_A class that inherits from list
    """
    def print_sorted(self):
        """Prints the sorted list
        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
