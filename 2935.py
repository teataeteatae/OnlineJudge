a = input().strip()  # 첫 번째 숫자
num = input().strip()  # 연산자
b = input().strip()  # 두 번째 숫자

if num == '+':
    print(int(a) + int(b))  # 문자열을 정수로 변환 후 덧셈
elif num == '*':
    print(int(a) * int(b))  # 문자열을 정수로 변환 후 곱셈