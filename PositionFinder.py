#python 3.8.8
#contract: zigm1315@gmail.com
amount = int(input())
code = str(input())
allcode = []
for i in range(amount):
    goods = str(input())
    allcode.append(goods)
if code in allcode:
    codepos = [i for i,x in enumerate(allcode) if x==code]
    print("Position:", ','.join(map(str, codepos)))

else:
    print("Not Found")