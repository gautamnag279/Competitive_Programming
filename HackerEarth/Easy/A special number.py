query = int(input())
while query:
    query -= 1
    num = int(input())
    while sum([int(i) for i in str(num)]) % 4:
        num += 1
    print(num)
