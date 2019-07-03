s = 11
   
if s > 1:   
   for i in range(2, s//2):
       if (s % i) == 0: 
           print("no") 
           break
   else: 
       print( "yes") 
