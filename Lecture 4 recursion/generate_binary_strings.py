def generate_binary_strings(n, base):
    if n <= 0:
        return [""]
    res = generate_binary_strings(n - 1 , base)
    ans = []
    for i in range(base):
         for s in res:
            ans.append(s + str(i))
    return ans
def count_bit_strings(n):
    MOD = 10**9 + 7
    result = generate_binary_strings(n, 2)
    return len(result) % MOD
n = int(input())
print(count_bit_strings(n))
