s=int(input(""))
fact = 1
if s < 0:
   print("")
elif s == 0:
   print("1")
else:
   for i in range(1,s + 1):
       fact = fact*i
   print(fact)
