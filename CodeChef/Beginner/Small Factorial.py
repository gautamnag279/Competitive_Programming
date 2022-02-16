def SmallFactorials(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

query = int(input())
for i in range(query):
    num = int(input())
    print(SmallFactorials(num))
