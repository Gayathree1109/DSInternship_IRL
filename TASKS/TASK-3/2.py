# Enter your code here. Read input from STDIN. Print output to 

import math

AB=int(input())
BC=int(input())
h=math.hypot(AB,BC)                     
r=round(math.degrees(math.acos(BC/h)))  
deg=chr(176)                                
print(r,deg, sep='')