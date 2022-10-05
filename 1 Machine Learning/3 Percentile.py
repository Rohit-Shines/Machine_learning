import numpy

# It will help you to tell the percentile of the given data with specific number
# example it will tell you the % of people whoes age is less than specific number 

age = [1,1,2]
print(numpy.percentile(age, 75)) # 75% of the ages are younger than 1.5
print(numpy.percentile(age, 50))  # 50% of the ages are younger than 1
print(numpy.percentile(age, 25))  # 25% of the ages are younger than 1

speed = [1,2,3,4,5,6,7,8,9,10]
print(numpy.percentile(speed, 70)) # 70% of the speed  are less  than 7.3
print(numpy.percentile(speed, 50))  # 50% of the speed  are less  than 5.5
print(numpy.percentile(speed, 20))  # 20% of the speed  are less  than 2.8