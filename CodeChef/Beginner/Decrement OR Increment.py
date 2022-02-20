def CodeChef(num):
    if num%4 ==0:
        return num+1
    else:
        return num-1
    
num = int(input())
print(CodeChef(num))
