This is an awesome problem. It doesn't use 3 as an exponent, where this attack is best known, but instead 17. However, the rsa key is huge, so this attack is still possible.

Consider a message `m`. RSA encrypts it as `c = m^17 (mod N)`. Suppose we get consecutive messages `c1, c2, ..., c17`, and keys `n1, n2, ..., n17`. Then we can use the chinese remainder theorem to compute `m^17 (mod n1*n2*n3*...*n17)`. As this modulus is HUGE, probably greater than `m^17`, we can then just take the 17th root of `m` to get the result.



Implementation:

```
#!/usr/bin/env python

import socket
import gmpy
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

host = 'vuln2015.icec.tf'
port = 31896
size = 1024
n = []
c = []
e = 17
for i in range(500):
    print(i)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    f = s.makefile()
    data = ""
    msg = f.readline()
    s.send(str(i) + "\n")
    msg = f.readline()
    pkey = f.readline().strip()
    crypted = f.readline().strip()
    n.append(int(pkey, 16))
    c.append(int(crypted, 16))
    s.close()


a = chinese_remainder(n,c)
m0 = gmpy.mpz(a)
x,_ = m0.root(17)
print(hex(x).strip("0x").strip("L").decode("hex"))


```