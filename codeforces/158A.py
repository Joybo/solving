# 158A - Next Round
# http://codeforces.com/problemset/problem/158/A
# AC
n, k = map(int, raw_input().split())
ar = map(int, raw_input().split())

def get_ans():
  if ar[0] == 0: return 0

  count = 1

  for i in xrange(1, n):
    if ar[i] == 0: return count
    if ar[i] == ar[i-1]:
      count += 1
      continue
    if count >= k: break
    count += 1
  # End of for i in xrange(1, n):

  return count

print(get_ans())
