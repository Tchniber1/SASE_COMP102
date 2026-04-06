def remove_char(s,c):
    if len(s) == 0:
        return s
    right_part = remove_char(s[1:],c)
    if s[0] == c:
        return right_part
    else:
        return s[0] + right_part
print(remove_char("hello world", "o"))
print(remove_char("mississippi", "s"))
print(remove_char("banana", "a"))