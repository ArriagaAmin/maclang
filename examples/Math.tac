@staticv A0 5
@staticv A4 1
@string S0 "0000\n"
@string S1 "0000No esta definido el factorial para numeros negativos."
@string S2 "0000No esta definido el factorial para numeros negativos."
@string S3 "0000No se puede calcular el minimo de un arreglo vacio."
@string S4 "0000No se puede calcular el maximo de un arreglo vacio."
assignw NULL 0
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
assignw T8 4
assignw T9 4
assignw T10 4
assignw T11 4
assignw T12 4
assignw T13 BASE[0]
@label L0
assignb T14 T13[T8]
eq test T14 0
goif L0_end test
eq test T14 37
goif L1 test
printc T14
add T8 T8 1
goto L0
@label L1
assignb T14 T13[T8]
add T8 T8 1
eq test T14 99
goif L2 test
eq test T14 105
goif L3 test
eq test T14 102
goif L4 test
eq test T14 115
goif L5 test
goto L0
@label L2
assignw T15 BASE[4]
assignb T16 T15[T9]
printc T16
add T9 T9 1
goto L0
@label L3
assignw T15 BASE[8]
assignw T17 T15[T10]
printi T17
add T10 T10 4
goto L0
@label L4
assignw T15 BASE[12]
assignw f3 T15[T11]
printf f3
add T11 T11 4
goto L0
@label L5
assignw T15 BASE[16]
assignw T18 T15[T12]
print T18
add T12 T12 4
goto L0
@label L0_end
assignw T15 BASE[20]
print T15
return 0
@endfunction 24
@function Function0 4
assignw T19 0
assignw T20 BASE[0]
lt test T20 T19
goif B100 test
goto B112
@label B100
assignw S1[0] 53
param T22 0
assignw T22[0] S1
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T23 PRINT 6
assignw T24 1
exit T24
goto Function0_end
@label B112
@label L6
assignw T25 0
assignw T26 BASE[0]
eq test T26 T25
goif B118 test
goto B122
@label B118
assignw T27 1
assignw lastbase BASE
return T27
goto Function0_end
@label B122
assignw T28 1
assignw T30 BASE[0]
sub T29 T30 T28
param T31 0
assignw T31[0] T29
call T32 Function0 1
assignw T34 BASE[0]
mult T33 T34 T32
assignw lastbase BASE
return T33
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function1 8
assignw T35 0
assignw T36 BASE[0]
lt test T36 T35
goif B142 test
goto B154
@label B142
assignw S2[0] 53
param T38 0
assignw T38[0] S2
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T39 PRINT 6
assignw T40 1
exit T40
goto B154
@label B154
assignw T41 1
assignw BASE[4] T41
@label L7
assignw T42 0
assignw T43 BASE[0]
gt test T43 T42
goif B162 test
goto B171
@label B162
assignw T45 BASE[4]
assignw T46 BASE[0]
mult T44 T45 T46
assignw BASE[4] T44
assignw T47 1
assignw T49 BASE[0]
sub T48 T49 T47
assignw BASE[0] T48
goto L7
@label B171
assignw T50 BASE[4]
assignw lastbase BASE
return T50
@label Function1_end
assignw lastbase BASE
return 0
@endfunction 8
@function Function2 4
assignw T51 0
assignw f4 BASE[0]
lt test f4 T51
goif B184 test
goto B189
@label B184
assignw f6 BASE[0]
minus f5 f6
assignw lastbase BASE
return f5
goto Function2_end
@label B189
assignw f7 BASE[0]
assignw lastbase BASE
return f7
@label Function2_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function3 20
assignb T52 A4[0]
goif L8 T52
assignw f8 0.000001
assignw BASE[4] f8
@label L8
assignw f9 1.000000
assignw f10 BASE[0]
assignw BASE[8] f10
assignw BASE[12] f9
@label L9
assignw f11 BASE[12]
assignw f12 BASE[4]
gt test f11 f12
goif B212 test
goto B230
@label B212
assignw f13 BASE[8]
assignw BASE[16] f13
assignw f15 BASE[0]
assignw f16 BASE[8]
div f14 f15 f16
assignw f18 BASE[8]
add f17 f18 f14
assignw T53 2
div f19 f17 T53
assignw BASE[8] f19
assignw f21 BASE[8]
assignw f22 BASE[16]
sub f20 f21 f22
param T54 0
assignw T54[0] f20
call f23 Function2 1
assignw BASE[12] f23
goto L9
@label B230
assignw f24 BASE[8]
assignw lastbase BASE
return f24
@label Function3_end
assignw lastbase BASE
return 0
@endfunction 20
@function Function4 16
assignw f25 0.000000
assignw BASE[8] f25
assignw T56 0
assignw BASE[12] T56
@label L10
assignw T57 BASE[12]
assignw T58 BASE[4]
lt test T57 T58
goif B248 test
goto B257
@label B248
assignw T59 BASE[0]
assignw T60 BASE[12]
mult T61 4 T60
add T61 T61 4
assignw f27 BASE[8]
assignw f28 T59[T61]
add f26 f27 f28
assignw BASE[8] f26
goto L10
@label B257
assignw f30 BASE[8]
assignw T62 BASE[4]
div f29 f30 T62
assignw lastbase BASE
return f29
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function5 16
assignw T64 1
assignw T65 BASE[4]
lt test T65 T64
goif B272 test
goto B284
@label B272
assignw S3[0] 51
param T67 0
assignw T67[0] S3
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T68 PRINT 6
assignw T69 1
exit T69
goto B284
@label B284
assignw T70 0
assignw T71 BASE[0]
mult T72 4 T70
add T72 T72 4
assignw f31 T71[T72]
assignw BASE[8] f31
assignw T73 1
assignw BASE[12] T73
@label L11
assignw T74 BASE[12]
assignw T75 BASE[4]
lt test T74 T75
goif B298 test
goto B315
@label B298
assignw T76 BASE[0]
assignw T77 BASE[12]
mult T78 4 T77
add T78 T78 4
assignw f32 T76[T78]
assignw f33 BASE[8]
lt test f32 f33
goif B307 test
goto L11
@label B307
assignw T79 BASE[0]
assignw T80 BASE[12]
mult T81 4 T80
add T81 T81 4
assignw f34 T79[T81]
assignw BASE[8] f34
goto L11
goto L11
@label B315
assignw f35 BASE[8]
assignw lastbase BASE
return f35
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function6 16
assignw T83 1
assignw T84 BASE[4]
lt test T84 T83
goif B328 test
goto B340
@label B328
assignw S4[0] 51
param T86 0
assignw T86[0] S4
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T87 PRINT 6
assignw T88 1
exit T88
goto B340
@label B340
assignw T89 0
assignw T90 BASE[0]
mult T91 4 T89
add T91 T91 4
assignw f36 T90[T91]
assignw BASE[8] f36
assignw T92 1
assignw BASE[12] T92
@label L12
assignw T93 BASE[12]
assignw T94 BASE[4]
lt test T93 T94
goif B354 test
goto B371
@label B354
assignw T95 BASE[0]
assignw T96 BASE[12]
mult T97 4 T96
add T97 T97 4
assignw f37 T95[T97]
assignw f38 BASE[8]
gt test f37 f38
goif B363 test
goto L12
@label B363
assignw T98 BASE[0]
assignw T99 BASE[12]
mult T100 4 T99
add T100 T100 4
assignw f39 T98[T100]
assignw BASE[8] f39
goto L12
goto L12
@label B371
assignw f40 BASE[8]
assignw lastbase BASE
return f40
@label Function6_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function7 20
@label L13
assignw T102 0
assignw T103 BASE[4]
eq test T103 T102
goif B385 test
goto B389
@label B385
assignw f41 0.000000
assignw lastbase BASE
return f41
goto B389
@label B389
assignw T105 BASE[0]
assignw T106 T105[0]
assignw T107 4
mult T107 T107 T106
add T107 T107 4
malloc T104 T107
memcpy T104 T105 T107
param T108 0
assignw T108[0] T104
assignw T109 BASE[4]
param T110 4
assignw T110[0] T109
call f42 Function4 2
assignw f43 0.000000
assignw BASE[8] f42
assignw BASE[12] f43
assignw T111 0
assignw BASE[16] T111
@label L14
assignw T112 BASE[16]
assignw T113 BASE[4]
lt test T112 T113
goif B413 test
goto B432
@label B413
assignw T114 BASE[0]
assignw T115 BASE[16]
mult T116 4 T115
add T116 T116 4
assignw f45 T114[T116]
assignw f46 BASE[8]
sub f44 f45 f46
assignw T117 BASE[0]
assignw T118 BASE[16]
mult T119 4 T118
add T119 T119 4
assignw f48 T117[T119]
assignw f49 BASE[8]
sub f47 f48 f49
mult f50 f44 f47
assignw f52 BASE[12]
add f51 f52 f50
assignw BASE[12] f51
goto L14
@label B432
assignw f54 BASE[12]
assignw T120 BASE[4]
div f53 f54 T120
assignw lastbase BASE
return f53
@label Function7_end
assignw lastbase BASE
return 0
@endfunction 20
@function Function8 8
assignw T123 BASE[0]
assignw T124 T123[0]
assignw T125 4
mult T125 T125 T124
add T125 T125 4
malloc T122 T125
memcpy T122 T123 T125
param T126 0
assignw T126[0] T122
assignw T127 BASE[4]
param T128 4
assignw T128[0] T127
call f55 Function7 2
param T129 0
assignw T129[0] f55
assignb A4[0] 0
call f56 Function3 2
assignw lastbase BASE
return f56
@label Function8_end
assignw lastbase BASE
return 0
@endfunction 8
