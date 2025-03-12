#조건
#첫째 줄 : 현재 시각, 시와 분을 정수로 빈칸을 사이에 두고 순서대로 주어짐
#두번째 줄 : 요리하는데 필요한 시간이 분단위로 주어짐
#출력 : 첫째줄에 종료되는 시와 분을 공백을 사이에두고 출력
A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B + C

A = (total_minutes // 60) % 24  
B = total_minutes % 60

print(A, B)
