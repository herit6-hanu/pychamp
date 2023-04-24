def romanToInt(s):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            res += roman_to_int[s[i+1]] - roman_to_int[s[i]]
            i += 2
        else:
            res += roman_to_int[s[i]]
            i += 1
    return res


print(romanToInt('MCMXCIV'))