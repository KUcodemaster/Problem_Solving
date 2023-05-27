n = int(input())

total = 1
cnt = 1

i = 1
j = 1

while j != n:
  if total > n:
    total -= i
    i += 1
  elif total < n:
    j += 1
    total += j
  else:
    j += 1
    total += j
    cnt += 1
    
print(cnt)