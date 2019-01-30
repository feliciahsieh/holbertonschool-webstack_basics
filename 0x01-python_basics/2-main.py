#!/usr/bin/env python3
islower = __import__('2-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

print("blank is {}".format("blank" if islower("") else "upper"))
print("None is {}".format("None" if islower(None) else "upper"))
print("float is {}".format("float" if islower(3.25) else "upper"))
