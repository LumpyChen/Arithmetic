def judge(n, c, x, d):
    m = 1
    k = 0
    for i in range(1, n):
        if x[i] - x[k] >= d:
            m = m + 1
            k = i
        if m >= c: break
    return m >= c

def binarySearch(n, c, x):
    l = 0
    r = x[n-1] - x[0]
    while l < r:
        mid = (l + r) >> 1
        mid = mid + 1
        ok = judge(n, c, x, mid)
        if ok: l = mid
        else: r = mid - 1
    return l

def main():
    ncase = input()
    for case in range(ncase):
        a = map(int, raw_input().split())
        n = a[0]
        c = a[1]
        x = [0] * n
        for i in range(n):
            x[i] = input()
        x.sort()
        ans = binarySearch(n, c, x)
        print ans

main()