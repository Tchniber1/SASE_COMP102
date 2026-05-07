def generate_sub(s): #recursive function to generate all subsets of a string
    if len(s) == 0: 
        return [""]
    res = generate_sub(s[1:])
    ans = []
    for sub in res:
        ans.append(sub)
        ans.append(s[0] + sub)
    return ans

def generate_sub_2(s):
    def helper(index, current_sub):
        if index == len(s):
            return [current_sub]
        
        exclude_char = helper(index + 1, current_sub)
        
        include_char = helper(index + 1, current_sub + s[index])
        
        return exclude_char + include_char

    return helper(0, "")
