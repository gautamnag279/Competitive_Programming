query = int(input())
arr = []
for i in range(query):
    arr.append(int(input()))
ans = sorted(arr)
for i in ans:
    print(i)
