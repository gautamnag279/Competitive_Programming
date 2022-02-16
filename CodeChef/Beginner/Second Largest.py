def SecondLargest(lst):
    l = sorted(lst)
    return l[-2]

query = int(input())
for i in range(query):
    lst = list(map(int, input().split()))
    print(SecondLargest(lst))
