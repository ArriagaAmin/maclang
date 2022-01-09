@staticv A0 5
@string S0 "0000\n"
@string S1 "0000fact(%i)"
@string S2 "0000Resultado: %i"
@string S3 "0000Input: "
@string S4 "0000Hasta luego!"
@string S5 "0000Calculando factorial de %i"
@string S6 "0000Resultado calculado: %i"
@string S7 "0000Caracteres: %c %c %c%cNumeros: %i %i%cTextos: %s %s%c"
@string S8 "0000Hello"
@string S9 "0000 world!"
@string S10 "0000Final"
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
@function Function0 16
assignw S1[0] 8
assignw T20 1
assignw T21 T20
assignw T22 4
mult T22 T22 T21
add T22 T22 4
malloc T23 T22
assignw T23[0] T21
assignw BASE[4] T23
assignw T24 BASE[4]
assignw T25 BASE[0]
assignw T24[4] T25
param T26 0
assignw T26[0] S1
assignb A0[0] 0
assignw T28 BASE[4]
assignw T29 T28[0]
assignw T30 4
mult T30 T30 T29
add T30 T30 4
malloc T31 T30
assignw T27 T31
memcpy T27 T28 T30
param T32 8
assignw T32[0] T27
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T33 PRINT 
@label L7
assignw T34 0
assignw T35 BASE[0]
eq test T35 T34
goif B138 test
goto B142
@label B138
assignw T36 1
assignw lastbase BASE
return T36
goto Function0_end
@label B142
assignw T37 1
assignw T39 BASE[0]
sub T38 T39 T37
param T40 0
assignw T40[0] T38
call T41 Function0 
assignw BASE[8] T41
assignw S2[0] 13
assignw T43 1
assignw T44 T43
assignw T45 4
mult T45 T45 T44
add T45 T45 4
malloc T46 T45
assignw T46[0] T44
assignw BASE[12] T46
assignw T47 BASE[12]
assignw T48 BASE[8]
assignw T47[4] T48
param T49 0
assignw T49[0] S2
assignb A0[0] 0
assignw T51 BASE[12]
assignw T52 T51[0]
assignw T53 4
mult T53 T53 T52
add T53 T53 4
malloc T54 T53
assignw T50 T54
memcpy T50 T51 T53
param T55 8
assignw T55[0] T50
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T56 PRINT 
assignw T58 BASE[0]
assignw T59 BASE[8]
mult T57 T58 T59
assignw lastbase BASE
return T57
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 16
assignw S3[0] 7
param T62 0
assignw T62[0] S3
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T63 PRINT 
call T64 READI 
assignw T60 T64
assignw T65 0
lt test T60 T65
goif B203 test
goto B215
@label B203
assignw S4[0] 12
param T67 0
assignw T67[0] S4
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T68 PRINT 
assignw T69 0
exit T69
goto B215
@label B215
assignw S5[0] 26
assignw T71 1
assignw T73 T71
assignw T74 4
mult T74 T74 T73
add T74 T74 4
malloc T75 T74
assignw T75[0] T73
assignw T72 T75
assignw T72[4] T60
param T76 0
assignw T76[0] S5
assignb A0[0] 0
assignw T78 T72[0]
assignw T79 4
mult T79 T79 T78
add T79 T79 4
malloc T80 T79
assignw T77 T80
memcpy T77 T72 T79
param T81 8
assignw T81[0] T77
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T82 PRINT 
assignw S6[0] 23
param T84 0
assignw T84[0] T60
call T85 Function0 
assignw T86 1
assignw T88 T86
assignw T89 4
mult T89 T89 T88
add T89 T89 4
malloc T90 T89
assignw T90[0] T88
assignw T87 T90
assignw T87[4] T85
param T91 0
assignw T91[0] S6
assignb A0[0] 0
assignw T93 T87[0]
assignw T94 4
mult T94 T94 T93
add T94 T94 4
malloc T95 T94
assignw T92 T95
memcpy T92 T87 T94
param T96 8
assignw T96[0] T92
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T97 PRINT 
assignw S7[0] 53
assignb T99 65
assignb T100 9
assignb T101 70
assignb T102 10
assignb T103 10
assignb T104 10
assignw T105 6
assignw T107 T105
assignw T108 1
mult T108 T108 T107
add T108 T108 4
malloc T109 T108
assignw T109[0] T107
assignw T106 T109
assignb T106[9] T104
assignb T106[8] T103
assignb T106[7] T102
assignb T106[6] T101
assignb T106[5] T100
assignb T106[4] T99
assignw T110 42
assignw T111 69
minus T112 T111
assignw T113 2
assignw T115 T113
assignw T116 4
mult T116 T116 T115
add T116 T116 4
malloc T117 T116
assignw T117[0] T115
assignw T114 T117
assignw T114[8] T112
assignw T114[4] T110
assignw S8[0] 5
assignw S9[0] 7
assignw T120 2
assignw T122 T120
assignw T123 4
mult T123 T123 T122
add T123 T123 4
malloc T124 T123
assignw T124[0] T122
assignw T121 T124
@label L8
sub T123 T123 4
lt test T123 4
goif L8_end test
goto L8
@label L8_end
assignw T121[8] S9
assignw T121[4] S8
assignw S10[0] 5
param T126 0
assignw T126[0] S7
assignw T128 T106[0]
assignw T129 1
mult T129 T129 T128
add T129 T129 4
malloc T130 T129
assignw T127 T130
memcpy T127 T106 T129
param T131 4
assignw T131[0] T127
assignb A0[0] 1
assignw T133 T114[0]
assignw T134 4
mult T134 T134 T133
add T134 T134 4
malloc T135 T134
assignw T132 T135
memcpy T132 T114 T134
param T136 8
assignw T136[0] T132
assignb A0[1] 1
assignb A0[2] 0
assignw T138 T121[0]
assignw T139 4
mult T139 T139 T138
add T139 T139 4
malloc T140 T139
assignw T137 T140
assignw T141 T139
@label L9
sub T141 T141 4
lt test T141 4
goif L9_end test
assignw T142 T121[T141]
assignw T143 T142[0]
assignw T144 1
mult T144 T144 T143
add T144 T144 4
malloc T145 T144
assignw T137[T141] T145
assignw T146 T137[T141]
memcpy T146 T142 T144
goto L9
@label L9_end
param T147 16
assignw T147[0] T137
assignb A0[3] 1
param T148 20
assignw T148[0] S10
assignb A0[4] 1
call T149 PRINT 
