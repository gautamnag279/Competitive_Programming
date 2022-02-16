query, factor = list(map(int, input().split()))
count = 0
for i in range(query):
    num = int(input())
    if num%factor == 0:
        count += 1
print(count)
