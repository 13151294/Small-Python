#python 3.8.8
#contract: zigm1315@gmail.com
lists = []
while True:
    n = int(input())
    if n != 0:
        lists.append(n)
        print(lists)
    else:
        lists.sort()
        if input() == "Min":
            print(lists)
        else:
            lists.sort(reverse=True)
            print(lists)