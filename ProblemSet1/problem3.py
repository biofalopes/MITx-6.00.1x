s = 'abcbcd'

i = 0
longest = ''

while i < len(s):
    j = i + 1
    while j <= len(s):
        s_sorted = sorted(s[i:j])
        s_sorted = ''.join(s_sorted)
        if s[i:j] == s_sorted:
            if len(s_sorted) > len(longest):
                longest = s_sorted
        j += 1
    i += 1

print('Longest substring in alphabetical order is: ' + longest)
