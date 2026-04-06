def generate_sub(s): #recursive function to generate all subsets of a string
    if len(s) == 0: 
        return [""]
    res = generate_sub(s[1:])
    ans = []
    for sub in res:
        ans.append(sub)
        ans.append(s[0] + sub)
    return ans
