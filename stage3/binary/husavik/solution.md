You decompile the apk with a tool like jadx and then you can see in the b class (or one of the classes) there's a message being sent through a socket
if you look at the message it seems to be a base64 string and if decode that you get the flag
flag: `flag_wait_wasnt_it_dalvik`
