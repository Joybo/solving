# 118A - String Task
# http://codeforces.com/problemset/problem/118/A
# AC
s = raw_input().lower()
def remove_vowel(ch):
  return ch not in ['a', 'o', 'y', 'e', 'u', 'i']

print('.{0}'.format('.'.join(filter(remove_vowel, s))))

