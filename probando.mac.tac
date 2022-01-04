@staticv A0 5
@string S0 "0000\n"
@string S1 "0000Caracteres: %c %c%cNumeros: %i %i%c%cTextos %s %s%c"
@string S2 "0000Hello"
@string S3 "0000 world!"
@string S4 "0000Final"
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
add T18 T18 4
print T18
add T12 T12 4
goto L1
@label L1_end
assignw T15 BASE[20]
add T15 T15 4
print T15
return 0
@endfunction 24
assignw S1[0] 51
assignb T20 65
assignb T21 9
assignb T22 110
assignb T23 10
assignb T24 10
assignb T25 10
assignw T26 6
assignw T28 T26
assignw T29 1
mult T29 T29 T28
add T29 T29 4
malloc T27 T29
assignw T27[0] T28
assignb T27[9] T25
assignb T27[8] T24
assignb T27[7] T23
assignb T27[6] T22
assignb T27[5] T21
assignb T27[4] T20
assignw T30 42
assignw T31 69
minus T32 T31
assignw T33 2
assignw T35 T33
assignw T36 4
mult T36 T36 T35
add T36 T36 4
malloc T34 T36
assignw T34[0] T35
assignw T34[8] T32
assignw T34[4] T30
assignw S2[0] 5
assignw S3[0] 7
assignw T39 2
assignw T41 T39
assignw T42 4
mult T42 T42 T41
add T42 T42 4
malloc T40 T42
assignw T40[0] T41
@label L7
sub T42 T42 4
lt test T42 0
goif L7_end test
goto L7
@label L7_end
assignw T40[8] S3
assignw T40[4] S2
assignw S4[0] 5
param T44 0
assignw T44[0] S1
assignw T46 T27[0]
assignw T47 1
mult T47 T47 T46
add T47 T47 4
malloc T45 T47
memcpy T45 T27 T47
param T48 4
assignw T48[0] T45
assignb A0[0] 1
assignw T50 T34[0]
assignw T51 4
mult T51 T51 T50
add T51 T51 4
malloc T49 T51
memcpy T49 T34 T51
param T52 8
assignw T52[0] T49
assignb A0[1] 1
assignb A0[2] 0
assignw T54 T40[0]
assignw T55 4
mult T55 T55 T54
add T55 T55 4
malloc T53 T55
assignw T56 T55
@label L8
sub T56 T56 4
lt test T56 0
goif L8_end test
assignw T57 T40[T56]
assignw T58 T53[T56]
assignw T59 T57[0]
assignw T60 1
mult T60 T60 T59
add T60 T60 4
malloc T58 T60
assignw T58[0] T58
memcpy T58 T57 T60
goto L8
@label L8_end
param T61 16
assignw T61[0] T53
assignb A0[3] 1
param T62 20
assignw T62[0] S4
assignb A0[4] 1
call T63 PRINT 6
