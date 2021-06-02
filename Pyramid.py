n = int(input())
symbol = input()
for i  in range(n):
    print(str(symbol*(1+i*2)).center(1+(n-1)*2))