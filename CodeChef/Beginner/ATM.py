def ATM(withdrawl, balance):
    if withdrawl%5 == 0 and withdrawl+0.50 <= balance:
        return (balance-withdrawl-0.50)
    else:
        return balance

withdrawl, balance = list(map(float, input().split()))
ans = "{:.2f}".format(ATM(withdrawl, balance))
print(ans)
