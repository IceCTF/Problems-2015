Two things should be noted here. If 2 repeating xor ciphers are used, then the length of the repeating key is just the product of their lengths.

They said the length was short, so we'll assume under 10.
This still leaves about 100 keys, but we can optimize the search to only look at numbers which could be products of 2 numbers less than 10.

```
set([a*b for a in range(10) for b in range(10)])
```

Anyway, given this, we just run xortool to analyze the encrypted text, pick whichever item exists in both lists, and we're done.