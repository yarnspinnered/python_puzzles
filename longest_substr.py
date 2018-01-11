
def lengthOfLongestSubstring(s):

    current = ""
    longest = ""

    for c in s:
        if c in current:
            if len(current) > len(longest):
                longest = current
            while c in current:
                current = current[1:]
            current = current + c
        else:
            current += c

    if len(current) > len(longest):
        longest = current

    return len(longest)

print(lengthOfLongestSubstring("pwwkew"))