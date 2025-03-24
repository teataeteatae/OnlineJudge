# 좌표 3개를 입력받음
points = [tuple(map(int, input().split())) for _ in range(3)]

# x와 y 좌표를 각각 리스트로 분리
x_vals = [x for x, y in points]
y_vals = [y for x, y in points]

# 한 번만 등장한 x, y를 찾음
for x in x_vals:
    if x_vals.count(x) == 1:
        x_result = x
        break

for y in y_vals:
    if y_vals.count(y) == 1:
        y_result = y
        break

# 결과 출력
print(x_result, y_result)
