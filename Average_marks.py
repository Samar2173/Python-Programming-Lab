
x=int(input("Enter English  MArks for A")) 
y=int(input("Enter MAthemAtics MArks for A")) 
z=int(input("Enter Science MArks for A"))


k=int(input("Enter English  MArks for B"))
l=int(input("Enter MAthemAtics MArks for B"))
m=int(input("Enter Science MArks for B"))
p=(x+y+z)/3
n=(k+l+m)/3
if p>n:
 print("A hAs scored highest Avg MArks")
else:
 print("B hAs highest Avg MArks")
