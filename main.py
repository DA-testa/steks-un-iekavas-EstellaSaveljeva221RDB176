# python3
#Estella Saveljeva 221RDB176
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            if not are_matching (opening_brackets_stack.pop().char, next):
                return i+1
            pass

def main():
    print("Use an input to choose files or input - F or I (Capital i) ")
    text = input("F or I?")
    if text =="F":
        fname = input("Input file name ")
        with open(fname,"r") as mfile:
            text = mfile.read()
            mismatch = find_mismatch(text)
            if mismatch == None:
                print("Success")
            else:
                print(mismatch)
    elif text == "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == None:
                print("Success")
        else:
                print(mismatch)
    else:
         print("wrong input")

if __name__ == "__main__":
    main()
