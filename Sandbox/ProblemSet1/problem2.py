s = 'bobbfhbobbzbobbobbobboobbobboboboejobob'
count = 0

for i in range(0, len(s)):
    if s[i:i+3] == 'bob' and i+3 <= len(s):
        count += 1

print("Number of times bob occurs is: " + str(count))
