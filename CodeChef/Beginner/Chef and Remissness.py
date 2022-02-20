def CodeChef(less, high):
    print(max(less,high), less+high)
    
query = int(input())
for i in range(query):
    less, high = list(map(int, input().split()))
    CodeChef(less, high)
