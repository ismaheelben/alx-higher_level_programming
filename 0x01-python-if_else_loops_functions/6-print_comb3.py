#!/usr/bin/python3
for num in range(0, 10):
    for y in range(num + 1, 10):
        if num == 8 and y == 9:
            print(89)
        else:
            print('{}{}, '.format(num, y), end='')
