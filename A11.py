N,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N//2+1):
    if A[i]==X:
        print(i+1)
        break
    elif A[N-1-i]==X:
        print(N-i)
        break