#!/usr/bin/python3
""" 100-write.py - print text to stderr using sys.write()
"""

import sys


txt = "and that piece of art is useful - Dora Korpar, 2015-10-19"
sys.stderr.write(txt+"\n")
sys.exit(1)
