x = int(input("Select a number to be x :"))

y = int(input("Select a number to be y :"))

ans = 0

if y < 0:
  count = -y
else:
  count = y

while count > 0:
  if x == 0:
    count = 0
  ans += x
  count -= 1

print (x,"+",x,"+",x,"=", ans)
