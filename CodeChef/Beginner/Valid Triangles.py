def ValidTriangles(a, b, c):
    if a+b+c == 180:
        return "YES"
    else:
        return "NO"
    
query = int(input())
for i in range(query):
    a, b, c = list(map(int, input().split()))
    print(ValidTriangles(a, b, c))
