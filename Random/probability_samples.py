import numpy as np
import scipy as sp
import scipy.stats


# Generate random integers
nums = np.random.randint(1,20,size=(1,15))[0]
print('Generated Data: ', nums)

# Descriptive statistical information:
print('Mean : ', sp.mean(nums))
print('Median : ', sp.median(nums))
print('Standard Deviation : ', sp.std(nums))
print('Variance : ', sp.var(nums))
print('Mode : ', sp.stats.mode(nums))
print('Skew : ', sp.stats.skew(nums))
print('Kurtosis : ', sp.stats.kurtosis(nums))
