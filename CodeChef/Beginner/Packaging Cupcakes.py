def CodeChef(order):
    if order%2 == 0:
        print((order//2)+1)
    else:
        print((order+1)//2)

query = int(input())
for i in range(query):
    order = int(input())
    CodeChef(order)
