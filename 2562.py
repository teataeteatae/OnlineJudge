import sys
num = []
for _ in range(9): #첫째줄부터 9번째줄까지 하나의 자연수가 주어짐)
    num.append(int(sys.stdin.readline()))
num1 = max(num)
print(num1)
print(num.index(num1)+1)