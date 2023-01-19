# 140 ms, 5000 KB
def add(x):
    return sum([int(i) for i in str(x)])

def codeforces(n):
    if (add(n//1000) == add(n%1000)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        codeforces(int(input()))

