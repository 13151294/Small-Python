import re
def LongestWord(k):
    Sentence = list(k.split())
    word = []
    for each in Sentence:
        res = "".join(re.findall("[a-zA-Z]+", each))
        word.append(res)
    LenWord = []
    for each in word:
        LenWord.append(len(each))
    return word[LenWord.index(max(LenWord))]
print(LongestWord(input()))