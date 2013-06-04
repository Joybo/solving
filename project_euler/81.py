# http://projecteuler.net/problem=81
# Answer: 427337
# Time: 0.00676798820496
# Solution: DP (Dynamic Programming)

from common import cal_time, read_file

@cal_time
def get_ans():
  width = 80

  m = []
  for line in read_file('81_matrix.txt').splitlines():
    m += [map(int, line.split(','))]

  dp = []
  for i in xrange(width):
    dp += [[0] * width]

  dp[0][0] = m[0][0]
  for i in xrange(1, width):
    dp[0][i] = dp[0][i-1] + m[0][i]
    dp[i][0] = dp[i-1][0] + m[i][0]

  for i in xrange(1, width):
    for j in xrange(1, width):
      dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]

  return dp[width - 1][width - 1]

get_ans()

