import statistics

a = [1,2,3,4,5,6,7,8,9,10]
num = statistics.mean(a)
print(num)

num = statistics.harmonic_mean(a)
print(num)

a = [1,2,3,4]
num = statistics.median(a)
print(num)

a = [1,2,3,4,5]
num = statistics.median(a)
print(num)


a = [1,2,3,4]
num = statistics.median_low(a)
print(num)

a = [1,2,3,4,5]
num = statistics.median_high(a)
print(num)

a = [1,2,3,4]
num = statistics.median_grouped(a)
print(num)

a = [1,2,3,4,5,4]
num = statistics.mode(a)
print(num)

a = [1,2,3,4,5,1]
num = statistics.mode(a)
print(num)

a = [1,2,3,4]
num = statistics.stdev(a)
print(num)

a = [1,2,3,4]
num = statistics.pvariance(a)
print(num)

a = [1,2,3,4]
num = statistics.pstdev(a)
print(num)







