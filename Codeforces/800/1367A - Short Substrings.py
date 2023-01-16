def guessString(s):
    for i in range(0, len(s), 2):
        print(s[i], end = "")
    print(s[len(s)-1])

n = int(input())
for i in range(n):
    guessString(input())
