#!/usr/bin/env python

def greetings():
    """Salut RESIF"""
    print("Hello RESIF people")
    print("On est vendredi, ca avance")

def repeat(x, callback):
    """Call x time"""
    for _ in range(x):
        callback()

if __name__ == "__main__":
    repeat(3, greetings)
