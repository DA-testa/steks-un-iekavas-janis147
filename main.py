# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
opening_brackets_stack = []

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            if len(opening_brackets_stack) > 0:
                status = True

                if (are_matching(opening_brackets_stack[len(opening_brackets_stack)-1],next) != True):
                    status = False
                else:
                    status = True
                    opening_brackets_stack.pop(len(opening_brackets_stack)-1)

                if status != True:
                    return i+1
            else:
                return i+1
    
    if len(opening_brackets_stack) > 0:
        return len(opening_brackets_stack)

def main():
    while True:
        check_type = input("F or I:> ")
        if check_type == "F" or check_type == "I":
            if check_type == "F":
                test_file = input("Test File Name:> ")
                f = open(f"./test/{test_file}","r")
                content = f.read()
                mismatch = find_mismatch(content)
                f.close()
                break
            else:
                text = input("Input Symbols:> ")
                mismatch = find_mismatch(text)
                break
        else:
            continue
    
    if mismatch != None:
        print(mismatch)
    else:
        print("Success")

if __name__ == "__main__":
    main()
