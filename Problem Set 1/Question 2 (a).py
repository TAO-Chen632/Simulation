# Generate the random variables using the LCG
a = 4781
c = 8521
m = 16384
Z0 = 1136
n = 30
Z = Z0
RV = [ ]
for i in range(n):
    Z = (a*Z + c) % m
    RV.append(Z/m)
print(RV)

# Calculate the KS test statistic
RV_sort = sorted(RV)
S1 = [((i + 1)/n - RV_sort[i]) for i in range(n)]
S2 = [(RV_sort[i] - i/n) for i in range(n)]
D_plus = max(S1)
D_minus = max(S2)
D = max(D_plus, D_minus)
KS = (pow(n, 0.5) + 0.12 + 0.11/pow(n, 0.5))*D
print(KS)
