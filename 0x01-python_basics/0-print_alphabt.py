#!/usr/bin/python3

start = ord('a')
end = ord('z') + 1
for i in range(start, end):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
