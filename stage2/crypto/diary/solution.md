Just notice that the key is at most 255, and just use xortool.

`xortool -l 1 -o encrypted && grep -r "flag" xortool_out`