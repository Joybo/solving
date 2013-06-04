# http://projecteuler.net/problem=2
# Answer: 4613732

a = 0
b = 1
c = 0
ans = 0
while True:
  c = a + b
  if c > 4000000: break

  a = b
  b = c
  if b % 2 == 0:
    ans += b
  
print(ans)
