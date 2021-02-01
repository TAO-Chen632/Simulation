# Generate 50 random variables
a = 4781
c = 8521
m = 16384
Z0 = 1136
n = 50
d = 2
k = 3
Z = Z0
RVar = [ ]
for i in range(n):
    Z = (a*Z + c) % m
    RVar.append(Z/m)

# Perform the serial test
import numpy as np
# Form n d-dimensional vectors by using sequential points
RVec = np.array(RVar).reshape(n//d, d)
# Find out which bin the observation belongs to
count = np.zeros((k, k))
for i in range(n//d):
    if RVec[i, 0] < 1/k:
        posi_x = 0
    elif RVec[i, 0] < 2/k:
        posi_x = 1
    else:
        posi_x = 2
    if RVec[i, 1] < 1/k:
        posi_y = 0
    elif RVec[i, 1] < 2/k:
        posi_y = 1
    else:
        posi_y = 2
    count[posi_x, posi_y] += 1
# Find the value of the chi-square test statistic for the serial test
chi_sq = sum(sum(((count - (n//d)/pow(k, d))**2)/((n//d)/pow(k, d))))
print(chi_sq)
# Calculate the p-value of the test
import scipy.stats as st
# The p-value
print((1 - st.chi2.cdf(chi_sq, df = k**d - 1)))
