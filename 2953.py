totals = []

# 참가자 5명의 점수를 입력받고 총합 계산
for _ in range(5):
    scores = list(map(int, input().split()))
    totals.append(sum(scores))

# 최고 점수와 참가자 번호 찾기
max_score = max(totals)
winner = totals.index(max_score) + 1  # 참가자는 1번부터 시작하므로 +1

print(winner, max_score)
