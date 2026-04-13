from exercise1 import Stack;

def check_balance(text):
    # Your code here
    stack = Stack()
    pairs = dict([(')', '('), ('}', '{'), (']', '[')])
    i = 0
    for pos, c in enumerate(text):
        if (c == "(" or c == "{" or c == "["):
            stack.push((c, pos))
        elif (c == ")" or c == "}" or c == "]"):
            if len(stack) == 0:
                return f"Match error at position {pos}"
            char, position = stack.pop()
            if (char != pairs[c]):
                return f"Match error at position {pos}"
            else:
                i += 1
    if len(stack) != 0:
        char, position = stack.pop()
        return f"Match error at position {position}"
    return f"Ok - {i}"