def shift_letters(s):
    result = [' '] * (len(s) + 25)
    
    for i in range(len(s)):
        shift = ord(s[i]) - ord('A')
        result[i + shift] = s[i]

    return "".join(result).rstrip()