import math
def FindingSquareRoots(num):
    return int(math.sqrt(num))

query = int(input())
for i in range(query):
    num = int(input())
    print(FindingSquareRoots(num))
