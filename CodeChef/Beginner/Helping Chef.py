def HelpingChef(n):
    if n < 10:
        return "Thanks for helping Chef!"
    else:
        return -1

query = int(input())
for i in range(query):
    n = int(input())
    print(HelpingChef(n))
