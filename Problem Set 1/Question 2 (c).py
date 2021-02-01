# Get the 50 random variables generated in part (b)
a = 4781
c = 8521
m = 16384
Z0 = 1136
n = 50
j = 3 # The lag
Z = Z0
RVar = [ ]
for i in range(n):
    Z = (a*Z + c) % m
    RVar.append(Z/m)

# Calculate the autocorrelation test statistic
h = int((n - 1)/j) - 1
rho_j = (12/(h + 1))*sum([RVar[i*j]*RVar[(i + 1)*j] for i in range(h + 1)]) - 3
A_j = (h + 1)*rho_j/pow(13*h + 7, 0.5)
print(A_j)

# Calculate the p-value of this test
import scipy.stats as st
# The p-value
print(2*(1 - st.norm.cdf(abs(A_j), 0, 1)))
