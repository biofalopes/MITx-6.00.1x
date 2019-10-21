s = 'abcdefghijklmnopqrstuvwxyz'


def is_sorted(lst, key=lambda x: x):
    for x, el in enumerate(lst[1:]):
        if key(el) < key(lst[x]):
            return False
    return True


biggest = s[0]

for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        if is_sorted(s[i:j]):
            if len(biggest) < len(sorted(s[i:j])):
                biggest = s[i:j]
        else:
            break

print("Longest substring in alphabetical order is: " + biggest)
