def ChefAndOperators(n1, n2):
    if n1>n2:
        return ">"
    elif n1<n2:
        return "<"
    else:
        return "=" 

query = int(input())
for i in range(query):
    n1, n2 = list(map(int, input().split()))
    print(ChefAndOperators(n1, n2))
