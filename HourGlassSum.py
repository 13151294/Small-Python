Grid = []
for i in range(6):
    row = list(map(int, input().split()))
    Grid.append(row)
HourGlassSum = []
for i in range(4):
    for j in range(4):
        FirstRowSum = sum(Grid[i][j:j+3])
        SecondRowSum = Grid[i+1][j+1]
        LastRowSum = sum(Grid[i+2][j:j+3])
        HGSum = FirstRowSum+SecondRowSum+LastRowSum
        HourGlassSum.append(HGSum)
print(max(HourGlassSum))