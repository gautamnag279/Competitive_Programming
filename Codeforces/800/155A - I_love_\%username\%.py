n = int(input())
points = [int(i) for i in input().split(" ")]

maxPoints = points[0]
minPoints = points[0]
count = 0

for i in points:
    if(i < minPoints):
        minPoints = i
        count += 1
    if(i > maxPoints):
        maxPoints = i
        count += 1
print(count)
