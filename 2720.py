def get_coins(cents):
    coins = [25, 10, 5, 1]  # 쿼터, 다임, 니켈, 페니 순서
    result = []
    for coin in coins:
        result.append(cents // coin)
        cents %= coin
    return result

# 입력 받기
n = int(input())  # 테스트 케이스 개수
cases = [int(input()) for _ in range(n)]

# 출력
for case in cases:
    print(*get_coins(case))
