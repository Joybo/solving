# 71A - Way Too Long Words
# http://codeforces.com/problemset/problem/71/A
# AC
n = input()
s = ''
def get_abbr():
  s_len = len(s)
  if s_len <= 10: return s
  return '{0}{1}{2}'.format(s[0], s_len - 2, s[-1])

for _ in xrange(n):
  s = raw_input()
  print(get_abbr())

