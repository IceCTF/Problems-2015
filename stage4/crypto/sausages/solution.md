First, you gotta find the key! Anyway, to some people, its known that github has a public key api, so the public key is just here: [https://github.com/icectf-steve.keys](https://github.com/icectf-steve.keys)

Now that we have the key, we have to crack it to get the private key. This is actually kindof difficult. 

First, look at the key with `ssh-keygen -f key.pub -e -m PKCS8 | openssl rsa -pubin -text`.

Note that the exponent is huge. This doesn't open up many doors, a small exponent would allow for a couple of the previous attacks. However, there is one.

The problem name references the name of the attack that should be used. Wiener's attack. Without going into details, it can be used when d < N^(1/4), which we can kind of infer from the size of e.

Anyway, we can then just use the implementation at `git@github.com:pablocelayes/rsa-wiener-attack.git`, and add some code to recover p and q, and convert it to PEM format, and voilá.

```
from RSAwienerHacker import hack_RSA
import sys
from Crypto.PublicKey import RSA
import gmpy

sys.setrecursionlimit(100000)

import fractions #for gcd function (or easily implementable to avoid import)
import random #for random elements drawing in RecoverPrimeFactors

def outputPrimes(a, n):
    p = fractions.gcd(a, n)
    q = int(n / p)
    if p > q:
        p, q = q, p
    print("Found factors p and q")
    print("p = {0}".format(str(p)))
    print("q = {0}".format(str(q)))
    return p,q


def RecoverPrimeFactors(n, e, d):
    """The following algorithm recovers the prime factor
        s of a modulus, given the public and private
        exponents.
        Function call: RecoverPrimeFactors(n, e, d)
        Input:  n: modulus
                e: public exponent
                d: private exponent
        Output: (p, q): prime factors of modulus"""

    k = d * e - 1
    if k % 2 == 1:
        return 0, 0
    else:
        t = 0
        r = k
        while(r % 2 == 0):
            r = int(r // 2)
            t += 1
        for i in range(1, 101):
            g = random.randint(0, n) # random g in [0, n-1]
            y = pow(g, r, n)
            if y == 1 or y == n - 1:
                continue
            else:
                for j in range(1, t): # j \in [1, t-1]
                    x = pow(y, 2, n)
                    if x == 1:
                        p, q = outputPrimes(y - 1, n)
                        return p, q
                    elif x == n - 1:
                        continue
                    y = x
                    x = pow(y, 2, n)
                    if  x == 1:
                        p, q = outputPrimes(y - 1, n)
                        return p, q

pubkey = """
0f:69:0c:8c:39:01:68:c0:9f:f0:aa:95:a6:92:a8:
    99:b5:f5:96:23:74:d9:34:85:c9:cb:a2:c1:f5:33:
    e7:04:97:cd:8b:4a:65:30:03:f8:a8:49:70:07:8a:
    49:54:f1:65:c9:5a:25:e4:27:9f:3e:f7:11:43:be:
    2d:ca:de:47:42:32:a2:4e:65:bf:a1:14:26:12:6b:
    ec:13:17:89:a1:48:40:10:44:3b:ae:ab:ab:65:56:
    d4:b3:1b:31:94:fe:4d:86:e2:03:27:d0:a3:b7:69:
    1f:f9:13:80:2a:0f:40:9e:bb:32:a2:68:01:6e:58:
    53:d6:00:6e:4e:a6:1d:13:66:5b:30:c5:2e:a8:fa:
    c5:45:f9:e7:92:b6:29:ef:f1:28:1a:54:a0:40:c2:
    de:bd:6f:5f:07:5a:d1:f8:52:90:4a:58:5f:07:c4:
    40:6c:28:03:0d:87:41:54:68:0d:fb:82:f5:92:8d:
    79:8d:71:94:08:88:6c:33:c7:f0:27:7c:3c:7f:5d:
    ac:8b:2b:7e:a2:86:91:4d:c1:c4:60:3d:3e:a2:87:
    23:53:6e:ec:67:76:50:7b:4a:30:4a:8d:e1:bc:d1:
    b9:84:d9:79:b1:c2:8f:4f:7b:f5:7a:77:b1:ba:8c:
    d1:54:51:f9:5a:28:24:b0:7e:26:bf:3c:7a:93:81:
    8f
""".replace(" ", "").replace(":","").replace("\n","")
exp = """
    01:74:e6:0c:c9:68:9b:fa:56:ed:e6:ac:8f:f9:aa:
    d7:34:4d:3a:b9:bd:6e:89:95:e9:c1:a2:8d:71:5e:
    30:e3:a6:db:23:78:6e:39:78:f0:e4:a9:14:60:90:
    af:8f:a3:30:7b:ef:bc:af:d7:ce:2f:3f:17:ec:08:
    6a:96:4c:21:fe:5b:55:a3:af:12:ee:91:8a:7e:23:
    0d:8b:62:5d:8b:50:23:b6:89:c9:c1:b1:61:98:16:
    f0:3c:67:94:54:3a:bb:91:10:83:6c:45:bc:7f:53:
    6c:92:a3:f9:b5:d6:d0:df:98:62:43:4c:c3:ec:92:
    56:0b:6d:bb:40:d4:49:49:01:db:6b:a5:cf:da:4f:
    6e:12:01:b1:a6:01:1e:8f:51:9b:e9:46:8d:2d:a3:
    93:22:63:21:22:08:af:71:0c:3c:60:d1:03:26:81:
    f5:86:db:ea:94:29:37:fe:0a:11:04:39:ab:59:20:
    89:38:bc:79:e7:4e:36:19:07:49:6f:d0:94:b0:44:
    ff:23:1c:29:82:fb:20:2f:59:c1:39:00:17:95:70:
    fe:f4:ec:b6:c1:94:51:cf:f5:3f:3f:e6:65:9a:d8:
    af:97:9e:48:e2:15:0c:bd:48:ee:73:4e:d9:fb:07:
    06:02:73:55:4b:9c:ef:1b:89:68:87:68:be:d6:b7:
    ef
""".replace(" ", "").replace(":","").replace("\n","")
N = int(pubkey,16)
e = int(exp,16)
d = hack_RSA(e, N)
p, q = RecoverPrimeFactors(N,e,d)
key = RSA.construct((N, e, d, p, q))
priv_key = key.exportKey()
with open("test.rsa", "wb") as f:
    f.write(priv_key)
print(priv_key)

```

Then just run `ssh -i test.rsa -p 2222 ctf@vuln2015.icec.tf`.

