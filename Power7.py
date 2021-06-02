#python 3.8.8
#contract: zigm1315@gmail.com
import time
while True:
    def power7v1(n):
        total = 7**n
        return str(total)[-1]

    def power7v2(n):
        a = "1793"
        return a[n%4]

    n = int(input())

    start = time.time()
    print("answer:", power7v1(n))
    print("time:", (time.time()-start)*1000)

    start = time.time()
    print("answer 1:", power7v2(n))
    print("time 1:", (time.time()-start)*1000)