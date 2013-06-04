# http://projecteuler.net/problem=1
# Answer: 233168

n = 1000
print(
  sum(
    [
      i for i in xrange(2, n) 
      if (i % 3 == 0) or (i % 5 == 0)
    ]
  )
)
