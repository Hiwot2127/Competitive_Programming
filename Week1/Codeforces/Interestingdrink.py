from bisect import bisect_right

t = int(input())
shops = list(map(int,input().split()))
n = int(input())
days = [int(input()) for _ in range(n)]
shops.sort()

for i in range(n):
    print(bisect_right(shops,days[i]))