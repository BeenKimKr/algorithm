import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    x, y = map(int, input().split())
    print('Case #', i, ':', x, '+', y, '=', x+y)
