def generate_binary_strings(n, base):
    if n <= 0:
        return [""]
    res = generate_binary_strings(n - 1 , base)
    ans = []
    for i in range(base):
         for s in res:
            ans.append(s + str(i))
    return ans
n = 3
base = 2
print(generate_binary_strings(n, base)) # Output: ['000', '001', '010', '011', '100', '101', '110', '111']