def AddTwoNumbers(n1, n2):
    return n1+n2

query = int(input())
for i in range(query):
    n1 , n2 = list(map(int, input().split()))
    print(AddTwoNumbers(n1, n2))
