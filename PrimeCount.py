import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
t = 0
for i in range(2, n):
    if all(i%j for j in range(2,int(i**0.5)+1)):
        t += 1
print(t)