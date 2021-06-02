#python 3.8.8
#contract: zigm1315@gmail.com
#test list [1,2,3,4,5,6,7,8,9] [1,2,3,4]
raw = input()
slice_ = slice(1,-1)
inputList = [int(j) for j in raw[slice_].split(',')]
target = int(input())
differenceList = {}
for i in range(len(inputList)):
    index1 = inputList.index(inputList[i])
    difference = target - inputList[i]
    backup = inputList.pop(i)
    if (difference in inputList):
        inputList.insert(i,backup)
        index2 = inputList.index(difference)
        print(f"[{index1},{index2}]")
        break
    inputList.insert(i,backup)