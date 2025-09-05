import math
result=math.sqrt(9)
print(result)

from math import sqrt,pi    #from keyword
result=sqrt(9) * pi
print(result)

from math import pi,sqrt as s   #from math as m           #as keyword
result=s(9) * pi                #result=m.sqrt(9) *m.pi
print(result)                 

import math                  #dir function
print(dir(math))
print(math.nan, type(math.nan))

