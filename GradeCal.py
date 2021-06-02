#python 3.8.8
#contract: zigm1315@gmail.com
score = int(input())
gradeLable = "FFFFFDCBAAAA"
print((score < 0 or score > 100) and "error" or gradeLable[score//10])