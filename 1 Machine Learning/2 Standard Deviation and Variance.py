# Standard Deviation is often represented by the symbol Sigma: σ
# Variance is often represented by the symbol Sigma Square: σ2


import numpy
import math

########### Standard Deviation ########## more the stnadard deviation  the value is deviated from average value ##
# As you can see, a higher standard deviation indicates that the values are spread out over a wider range.
a=[2,2,5 ]; print(numpy.std(a)) # -1.4  Average is 3 other values are less or more than 3 so 1.4 deviation
b=[2,2,2 ]; print(numpy.std(b)) # --0 Average is 2 other values are also 2 so "0 deviation
c=[3,2,1 ]; print(numpy.std(c)) # - 0.8


# Variance = Std * Std / We will prove below
# Variance
a=[2,2,5 ]
print(numpy.var(a)) # 2
# STD *STD σ
print(numpy.std(a)*numpy.std(a)) # 2
# sqrt of VARIANCE
print(math.sqrt(numpy.var(a)))




# Std = Square rood of (Variance)


