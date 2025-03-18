m = int(input())
ball = 1  # 처음 공이 들어 있는 컵은 1번

for _ in range(m):
    x, y = map(int, input().split())
    # 공이 들어있는 컵과 바꾸는 컵 중 하나가 같다면 위치 바꾸기
    if ball == x:
        ball = y
    elif ball == y:
        ball = x

print(ball if ball in [1, 2, 3] else -1)