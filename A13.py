N, K = map(int, input().split())
A = list(map(int, input().split()))
count = int(0)
j = 0

for i in range(N):
    while j < N and A[j] - A[i] <= K:
        j += 1
    count += j - i - 1
print(count)