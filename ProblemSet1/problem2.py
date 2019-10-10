s = 'azcbobobegghakl'

count = 0
bob_count = 0
while count+2 < len(s):
    s_slice = s[count:count+3:1]
    count += 1
    if 'bob' in s_slice:
        bob_count += 1
print(str(bob_count))
