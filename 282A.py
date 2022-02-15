# ++, --연산 문제

# 풀이
# 0에서 시작해 연산에 따라 작업 진행

x = 0
T = int(input())
for _ in range(T):
    s = input()
    if s[0] == '+' or s[-1] == '+':
        x += 1
    else:
        x -= 1
print(x)