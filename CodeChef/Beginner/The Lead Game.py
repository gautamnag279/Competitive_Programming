from itertools import accumulate
def TheLeadGame (query, player1, player2):
    p1 = list(accumulate(list(map(int, player1))))
    p2 = list(accumulate(list(map(int, player2))))

    diff = []

    for j in range(query):
        diff.append(p1[j] - p2[j])
    
    if max(diff) > abs(min(diff)):
        print(1, max(diff))
    else:
        print(2, abs(min((diff))))


query = int(input())
player1 = []
player2 =[]
for i in range(query):
    players = input().split()
    player1.append(players[0])
    player2.append(players[1])
TheLeadGame(query, player1, player2)
