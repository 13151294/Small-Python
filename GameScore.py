Games = int(input())
ScoreList = list(map(int, input().split()))
MaxBreak = 0
MinBreak = 0
MaxScore = ScoreList[0]
MinScore = ScoreList[0]
for game in ScoreList:
    if MaxScore < game:
        MaxScore = game
        MaxBreak += 1
    if MinScore > game:
        MinScore = game
        MinBreak += 1
print("{} {}".format(MaxBreak, MinBreak))