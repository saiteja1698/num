l = 100
u = 2000
for n in range(l, u + 1):
   order = len(str(n))
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if n == sum:
       print(n,end =" ")
