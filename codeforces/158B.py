# 158B - Taxi
# http://codeforces.com/problemset/problem/158/B
# AC
ar = [0] * 5
def statistic(val):
  ar[int(val)] += 1

def num_cars():
  a, b, c, d = ar[1:5]

  ans = d + c + b/2
  b %= 2
  ans += (max(0, a-c)+3 + b*2) / 4

  return ans

n = input()
map(statistic, raw_input().split())
print num_cars()
