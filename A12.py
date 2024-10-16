def can_print_in_time(T, A, K):
    total_prints = sum(T // a for a in A)
    return total_prints >= K

def find_min_time(N, K, A):
    low, high = 1, max(A) * K

    while low < high:
        mid = (low + high) // 2
        if can_print_in_time(mid, A, K):
            high = mid
        else:
            low = mid + 1

    return low

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(find_min_time(N, K, A))
