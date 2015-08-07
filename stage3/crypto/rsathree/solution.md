Because N is huge, but the exponent is small, we can actually check if the encrypted text was just cubed.
Just input the file into python and compute:
```
import binascii

def find_cube_root(n):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo+hi)//2
        if mid**3 < n:
            lo = mid+1
        else:
            hi = mid
    return lo

def is_perfect_cube(n):
    return find_cube_root(n)**3 == n
m = 0
for k in range(100):
    if is_perfect_cube(c + N*k):
        m = find_cube_root(c + N*k)
        break
binascii.unhexlify(hex(m)[2:])
```
