def Sorting(lst):
    lst.sort(key=len)
    return lst
lists = []
for i in range(int(input())):
    lists.append(input())
for each in Sorting(lists):
    print(each)