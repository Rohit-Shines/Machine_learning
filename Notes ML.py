import numpy

SpeedsOfCar = [30,23,45,63,78,95,88,88,34]
# Mean = Average speed
print(numpy.mean(SpeedsOfCar)) # 60.44
# Median = Midpoint
print(numpy.median(SpeedsOfCar)) # 63.0

from scipy import stats

# mode = most repeated value
print(stats.mode(SpeedsOfCar)) # ModeResult(mode=array([88]), count=array([2]))



########### Standard Deviation ########## who much the value is deviated from average value ##
# As you can see, a higher standard deviation indicates that the values are spread out over a wider range.
a=[2,2,5 ]; print(numpy.std(a)) # -1.4  Average is 3 other values are less or more than 3 so 1.4 deviation
b=[2,2,2 ]; print(numpy.std(b)) # --0 Average is 2 other values are also 2 so "0 deviation
c=[3,2,1 ]; print(numpy.std(c)) # - 0.8

