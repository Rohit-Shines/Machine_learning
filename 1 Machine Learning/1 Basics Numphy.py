import numpy

SpeedsOfCar = [30,23,45,63,78,95,88,88,34]
# Mean = Average speed
print(numpy.mean(SpeedsOfCar)) # 60.44
# Median = Midpoint
print(numpy.median(SpeedsOfCar)) # 63.0

from scipy import stats

# mode = most repeated value
print(stats.mode(SpeedsOfCar)) # ModeResult(mode=array([88]), count=array([2]))





