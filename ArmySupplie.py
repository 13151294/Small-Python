b,h = map(int,input().split())
package = 0
package += (b//2)*(h//2)
package += ((b * h) - ((b//2)*(h//2)*4))//2
if (b * h % 2 != 0):
    package += 1
print(package)
