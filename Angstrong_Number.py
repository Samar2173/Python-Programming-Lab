#Angstrong
#Defining Func
def AngN(x):
#Assining sum as 0 for calc
 sum=0
#To use t for performing on number
 t=x
#Giving Condition
 while(t>0):
#perfoming on the unit place digit 
  d=t%10 
#sum=sum+d**3
  sum+=d**3 
#considering digits other then unit
  t=t//10 
#condition
 if sum==x:
  print('Angstrong Number')
#condition
 else:
  print('Not Angstrong Number')

