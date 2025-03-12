#하나의 콘센트, 몇개의 멀티탭, 여러 대의 컴퓨터
#첫째 줄에 멀티탭의 개수 N이 주어짐.
#둘째 줄부터 N개의 줄에 걸쳐 각 멀티탭이 몇 개의 플러그를 꽂을 수 있도록 되어 있는지를 나타내는 자연수가 주어짐.
#출력: 첫째 줄에 최대로 전원에 연결될 수 있는 컴퓨터의 수
import sys
n = int(sys.stdin.readline()) #int(input()) 시간초과
sum=0
for _ in range(n):
    sum+=int(sys.stdin.readline()) #int(input()) 시간초과
print(sum-(n-1))