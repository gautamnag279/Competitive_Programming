def FirstandLastDigit(num):
    return int(num[0]) + int(num[-1])
    
query = int(input())
for i in range(query):
    num = input()
    print(FirstandLastDigit(num))
