N = int(input())  
A = list(map(int, input().split()))  
D = int(input())  

left_max = [0] * N
left_max[0] = A[0]
for i in range(1, N):
    left_max[i] = max(left_max[i - 1], A[i])

right_max = [0] * N
right_max[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], A[i])

for _ in range(D):
    L, R = map(int, input().split())
    L -= 1  
    R -= 1  

    left_part_max = left_max[L - 1] if L > 0 else -float('inf')
    right_part_max = right_max[R + 1] if R < N - 1 else -float('inf')

    print(max(left_part_max, right_part_max))
