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
            pass

        if next in ")]}":
            status = True
            print(*opening_brackets_stack)

            if (are_matching(opening_brackets_stack[len(opening_brackets_stack)],next) != True):
                status = False
            else:
                status = True
                opening_brackets_stack[len(opening_brackets_stack)] = ""

            if status != True:
                print(i+1)
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)

if __name__ == "__main__":
    main()
