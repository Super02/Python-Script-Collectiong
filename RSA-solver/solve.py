from Crypto.Util.number import inverse

# Just insert the values below to decode it.

n = 1
c = 1
e = 1

# p and q can be calculated by factor.db
p = 1
q = 1

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

m = pow(c, d, n)
print(bytes.fromhex(hex(m)[2:]).decode())
