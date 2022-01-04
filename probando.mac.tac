@staticv A0 5
@string S0 "0000\n"
@string S1 "0000Hello %c%cworld!"
assignw NULL 0
assignw lastbase 0
assignw T0 1
@function READ 4
assignw T1 BASE[0]
read T1
return 0
@endfunction 4
@function READC 0
readc T2
return T2
@endfunction 0
@function READI 0
readi T3
return T3
@endfunction 0
@function READF 0
readf f0
return f0
@endfunction 0
@function CTOI 1
assignw T4 BASE[0]
return T4
@endfunction 1
@function ITOC 4
assignb T5 BASE[0]
return T5
@endfunction 4
@function FTOI 4
assignw f1 BASE[0]
ftoi T6 f1
return T6
@endfunction 4
@function ITOF 4
assignw T7 BASE[0]
itof f2 T7
return f2
@endfunction 4
@function PRINT 24
assignb test A0[4]
goif L0 test
assignw BASE[20] S0
@label L0
assignw T8 4
assignw T9 4
assignw T10 4
assignw T11 4
assignw T12 4
assignw T13 BASE[0]
@label L1
assignb T14 T13[T8]
add T8 T8 1
eq test T14 0
goif L1_end test
eq test T14 37
goif L2 test
printc T14
goto L1
@label L2
assignb T14 T13[T8]
add T8 T8 1
eq test T14 99
goif L3 test
eq test T14 105
goif L4 test
eq test T14 102
goif L5 test
eq test T14 115
goif L6 test
goto L1
@label L3
assignw T15 BASE[4]
assignb T16 T15[T9]
printc T16
add T9 T9 1
goto L1
@label L4
assignw T15 BASE[8]
assignw T17 T15[T10]
printi T17
add T10 T10 4
goto L1
@label L5
assignw T15 BASE[12]
assignw f3 T15[T11]
printf f3
add T11 T11 4
goto L1
@label L6
assignw T15 BASE[16]
assignw T18 T15[T12]
print T18
add T12 T12 4
goto L1
@label L1_end
assignw T15 BASE[20]
add T15 T15 4
print T15
return 0
@endfunction 24
assignw S1[0] 16
assignb T20 10
assignb T21 10
assignw T22 2
assignw T24 T22
assignw T25 1
mult T25 T25 T24
add T25 T25 4
malloc T23 T25
assignw T23[0] T24
assignb T23[5] T21
assignb T23[4] T20
param T26 0
assignw T26[0] S1
assignw T28 T23[0]
assignw T29 1
mult T29 T29 T28
add T29 T29 4
malloc T27 T29
memcpy T27 T23 T29
param T30 4
assignw T30[0] T27
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T31 PRINT 6
