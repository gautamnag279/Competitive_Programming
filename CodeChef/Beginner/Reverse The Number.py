def ReverseTheNumber(string):
    return int(string[::-1])

query = int(input())
for i in range(query):
    string = input()
    print(ReverseTheNumber(string))
