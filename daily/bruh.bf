+++++>++>>>><<<<<
?
A B 0 0 0 0
>[->>>+<<<]<
[->+>>+>-[<-]<[<<[->>>+<<<]>>>>+<<-<]<<]
>>>>[-]>[-<<<<<+>>>>>]<<<<<
Q R 0 0 0 0
?

A R 0 E B 0 Q
[                    while dividend is not null
  -                  decrease dividend
  >+                 increase remainder
  >>+                set else flag
  >-                 decrease divisor
  [<-]               if divisor is not null reset else flag
  <[                 and if divisor is null
    <<[->>>+<<<]     rebuild divisor
    >>>>+            increase quotient
  <<-<]              move between remainder and else flag (reset it btw)
<<]                  loop

HOLY WORK OF ART DAMNNN