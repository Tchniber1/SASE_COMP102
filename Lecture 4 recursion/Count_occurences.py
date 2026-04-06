def count_occurences(a, x):
    if len(a) == 0:
        return 0
    right_part = count_occurences(a[1:], x)
    if a[0] == x:
        return 1 + right_part  
    return right_part
   
a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x = 3
print(count_occurences(a, x))
