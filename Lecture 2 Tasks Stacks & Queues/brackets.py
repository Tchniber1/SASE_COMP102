def is_valid_brackets(s):
    stack = []
    bracket = {")":"(","}":"{","]":"["}
    opening = "{[("
    closing = "}])"
    for character in s:
        if character in opening: 
            stack.append(character)
        elif character in closing:
            if len(stack) == 0:
                return False
            if stack[-1] == bracket[character]:
                stack.pop()
            else:
                return False
    return len(stack) == 0