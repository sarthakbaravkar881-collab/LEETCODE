class Solution(object):
    def myAtoi(self, s):
        i, n = 0, len(s)

        # 1. skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. read optional sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. read digits until the first non-digit
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # 4. apply sign and clamp to 32-bit range
        num *= sign
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num