f = int(input(""))
sum = 0
temp = f
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if f == sum:
   print("yes")
else:
   print("no")
