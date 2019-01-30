#!/usr/bin/python3


def islower(c):
    try:
        if len(c) == 1:
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                return True
        return False
    except Exception as e:
        print("type error: " + str(e))
        return False
