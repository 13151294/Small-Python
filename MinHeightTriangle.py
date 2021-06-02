import math

for i in range(int(input())):
    base, area = map(int, input().split())
    print(math.ceil(2*area/base))