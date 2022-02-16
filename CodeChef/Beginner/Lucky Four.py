def LuckyFour(num):
    return num.count('4')

query = int(input())
for i in range(query):
    num = input()
    print(LuckyFour(num))
