@staticv A0 1
@staticv A1 1
@staticv A2 20
@string S0 "No esta definido el factorial para numeros negativos"
@string S1 "No esta definido el factorial para numeros negativos"
@string S2 "No se puede calcular el minimo de un arreglo vacio."
@string S3 "No se puede calcular el maximo de un arreglo vacio."
@string S4 "Indique el numero en punto flotante no negativo: "
@string S5 "sqrt("
@string S6 ") = "
@string S7 "Desea calcular otra raiz? [Y/n] "
@string S8 "n"
@string S9 "N"
@string S10 "Hasta luego!"
goto F0_out
@function F0 4
assign T0 0
lt test base[0] T0
goif B6 test
goto B11
@label B6
param S0
call T1 PRINT 1
assign T2 1
exit T2
goto F0_end
@label B11
@label L0
assign T3 0
eq test base[0] T3
goif B16 test
goto B19
@label B16
assign T4 1
return T4
goto F0_end
@label B19
assign T5 1
sub T6 base[0] T5
param T6
call T7 F0 1
mult T8 base[0] T7
return T8
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 8
assign T9 0
lt test base[0] T9
goif B35 test
goto B40
@label B35
param S1
call T10 PRINT 1
assign T11 1
exit T11
goto B40
@label B40
assign T12 1
assign base[4] T12
@label L1
assign T13 0
gt test base[0] T13
goif B47 test
goto B53
@label B47
mult T14 base[4] base[0]
assign base[4] T14
assign T15 1
sub T16 base[0] T15
assign base[0] T16
goto L1
@label B53
return base[4]
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 4
assign T17 0
lt test base[0] T17
goif B64 test
goto B67
@label B64
minus T18 base[0]
return T18
goto F2_end
@label B67
return base[0]
@label F2_end
assign lastbase base
@endfunction
@label F2_out
goto F3_out
@function F3 16
assign T19 1.000000
assign base[4] base[0]
assign base[8] T19
@label L2
assign T20 0.000001
gt test base[8] T20
goif B82 test
goto B93
@label B82
assign base[12] base[4]
div T21 base[0] base[4]
add T22 base[4] T21
assign T23 2
div T24 T22 T23
assign base[4] T24
sub T25 base[4] base[12]
param T25
call T26 F2 1
assign base[8] T26
goto L2
@label B93
return base[4]
@label F3_end
assign lastbase base
@endfunction
@label F3_out
goto F4_out
@function F4 16
assign T27 0.000000
assign base[8] T27
assign T28 0
assign base[12] T28
@label L3
lt test base[12] base[4]
goif B108 test
goto B112
@label B108
mult T30 base[12] 4
add T31 base[8] base[0][T30]
assign base[8] T31
goto L3
@label B112
div T32 base[8] base[4]
return T32
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 16
assign T33 1
lt test base[4] T33
goif B124 test
goto B129
@label B124
param S2
call T34 PRINT 1
assign T35 1
exit T35
goto B129
@label B129
assign T36 0
mult T38 T36 4
assign base[8] base[0][T38]
assign T39 1
assign base[12] T39
@label L4
lt test base[12] base[4]
goif B138 test
goto B146
@label B138
mult T41 base[12] 4
lt test base[0][T41] base[8]
goif B142 test
goto L4
@label B142
mult T43 base[12] 4
assign base[8] base[0][T43]
goto L4
goto L4
@label B146
return base[8]
@label F5_end
assign lastbase base
@endfunction
@label F5_out
goto F6_out
@function F6 16
assign T44 1
lt test base[4] T44
goif B157 test
goto B162
@label B157
param S3
call T45 PRINT 1
assign T46 1
exit T46
goto B162
@label B162
assign T47 0
mult T49 T47 4
assign base[8] base[0][T49]
assign T50 1
assign base[12] T50
@label L5
lt test base[12] base[4]
goif B171 test
goto B179
@label B171
mult T52 base[12] 4
gt test base[0][T52] base[8]
goif B175 test
goto L5
@label B175
mult T54 base[12] 4
assign base[8] base[0][T54]
goto L5
goto L5
@label B179
return base[8]
@label F6_end
assign lastbase base
@endfunction
@label F6_out
goto F7_out
@function F7 20
@label L6
assign T55 0
eq test base[4] T55
goif B191 test
goto B194
@label B191
assign T56 0.000000
return T56
goto B194
@label B194
param base[0]
param base[4]
call T57 F4 2
assign T58 0.000000
assign base[8] T57
assign base[12] T58
assign T59 0
assign base[16] T59
@label L7
lt test base[16] base[4]
goif B206 test
goto B214
@label B206
mult T61 base[16] 4
sub T62 base[0][T61] base[8]
mult T64 base[16] 4
sub T65 base[0][T64] base[8]
mult T66 T62 T65
add T67 base[12] T66
assign base[12] T67
goto L7
@label B214
div T68 base[12] base[4]
return T68
@label F7_end
assign lastbase base
@endfunction
@label F7_out
goto F8_out
@function F8 8
param base[0]
param base[4]
call T69 F7 2
param T69
call T70 F3 1
return T70
@label F8_end
assign lastbase base
@endfunction
@label F8_out
assign T71 0
assign A0[0] T71
assign T72 A0
assign T73 10
assign A1[0] T73
assign T74 A1
assign T75 0
goto F9_out
@function F9 12
assign T76 0
assign base[8] T76
@label L8
mult T78 base[8] 1
@label L9
neq test base[0][T78] base[4]
goif B249 test
goto B253
@label B249
assign T79 1
add T80 base[8] T79
assign base[8] T80
goto L8
@label B253
return base[8]
@label F9_end
assign lastbase base
@endfunction
@label F9_out
goto F10_out
@function F10 12
assign T81 0
assign base[8] T81
@label L10
mult T83 base[8] 1
@label L11
assign T84 0
neq test base[0][T83] T84
goif B269 test
goto B279
@label B269
mult T86 base[8] 1
@label L12
mult T88 base[8] 1
eq test base[0][T86] base[4][T88]
goif B275 test
goto B279
@label B275
assign T89 1
add T90 base[8] T89
assign base[8] T90
goto L10
@label B279
mult T92 base[8] 1
mult T94 base[8] 1
gt test base[0][T92] base[4][T94]
goif B284 test
goto B287
@label B284
assign T95 1
return T95
goto F10_end
@label B287
mult T97 base[8] 1
mult T99 base[8] 1
gt test base[4][T97] base[0][T99]
goif B292 test
goto B296
@label B292
assign T100 1
minus T101 T100
return T101
goto F10_end
@label B296
assign T102 0
return T102
@label F10_end
assign lastbase base
@endfunction
@label F10_out
goto F11_out
@function F11 16
param base[4]
param T75
call T103 F9 2
assign T104 1
add T105 T103 T104
assign base[8] T105
assign T106 0
assign base[12] T106
@label L13
lt test base[12] base[8]
goif B316 test
goto F11_end
@label B316
mult T108 base[12] 1
mult T110 base[12] 1
assign base[0][T108] base[4][T110]
assign T111 1
add T112 base[12] T111
assign base[12] T112
goto L13
@label F11_end
assign lastbase base
@endfunction
@label F11_out
goto F12_out
@function F12 28
assign T113 0
assign T114 0
assign base[12] T113
assign base[16] T114
@label L14
lt test base[12] base[4]
goif B337 test
goto B363
@label B337
mult T116 base[12] 4
param base[0][T116]
param T75
call T117 F9 2
assign base[24] T117
assign T118 0
assign base[20] T118
@label L15
lt test base[20] base[24]
goif B348 test
goto B359
@label B348
mult T120 base[16] 1
mult T122 base[12] 4
mult T124 base[20] 1
assign base[8][T120] base[0][T122][T124]
assign T125 1
add T126 base[20] T125
assign base[20] T126
assign T127 1
add T128 base[16] T127
assign base[16] T128
goto L15
@label B359
assign T129 1
add T130 base[12] T129
assign base[12] T130
goto L14
@label B363
mult T132 base[16] 1
assign T133 0
assign base[8][T132] T133
@label F12_end
assign lastbase base
@endfunction
@label F12_out
goto F13_out
@function F13 29
assign T134 0
assign T135 0
assign T136 0
param base[0]
param T75
call T137 F9 2
assign base[12] T134
assign base[16] T135
assign base[20] T136
assign base[24] T137
goto B383
@label B383
assign base[28] True
goto Bool386
assign base[28] False
@label Bool386
@label L16
mult T139 base[12] 1
@label L17
assign T140 0
neq test base[0][T139] T140
goif B394 test
goto B442
@label B394
mult T142 base[12] 1
@label L18
eq test base[0][T142] base[8]
goif B399 test
goto B418
@label B399
goif B418 base[28]
goto B401
@label B401


goto B404
@label B404
assign base[28] True
goto Bool407
assign base[28] False
@label Bool407
mult T144 base[20] 4
mult T146 base[16] 1
assign T147 0
assign base[4][T144][T146] T147
assign T148 1
add T149 base[20] T148
assign base[20] T149
assign T150 0
assign base[16] T150
goto B438
@label B418
mult T152 base[12] 1
@label L19
neq test base[0][T152] base[8]
goif B423 test
goto B438
@label B423


goto B428
assign base[28] True
goto Bool429
@label B428
assign base[28] False
@label Bool429
mult T154 base[20] 4
mult T156 base[16] 1
mult T158 base[12] 1
assign base[4][T154][T156] base[0][T158]
assign T159 1
add T160 base[16] T159
assign base[16] T160
goto B438
@label B438
assign T161 1
add T162 base[12] T161
assign base[12] T162
goto L16
@label B442
goif B452 base[28]
goto B444
@label B444
mult T164 base[20] 4
mult T166 base[16] 1
assign T167 0
assign base[4][T164][T166] T167
assign T168 1
add T169 base[20] T168
assign base[20] T169
goto B452
@label B452
return base[20]
@label F13_end
assign lastbase base
@endfunction
@label F13_out
goto F14_out
@function F14 22
goto B463
goto B467
assign base[4] True
goto Bool464
@label B463
assign base[4] False
@label Bool464
assign base[5] True
goto Bool468
@label B467
assign base[5] False
@label Bool468
param base[0]
param T75
call T170 F9 2
assign T171 0
assign base[10] T170
assign base[18] T171
@label L20
lt test base[18] base[10]
goif B479 test
goto B541
@label B479
mult T173 base[18] 1
@label L21
assign T174 46
eq test base[0][T173] T174
goif B485 test
goto B495
@label B485
goif B495 base[4]
goto B487
@label B487


goto B490
@label B490
assign base[4] True
goto Bool493
assign base[4] False
@label Bool493
goto B537
@label B495
mult T176 base[18] 1
@label L22
assign T177 46
eq test base[0][T176] T177
goif B501 test
goto B508
@label B501
goto B504
assign T178 True
goto Bool505
@label B504
assign T178 False
@label Bool505
return T178
goto B537
@label B508
mult T180 base[18] 1
assign T181 48
lt test base[0][T180] T181
goif B518 test
goto B513
@label B513
mult T183 base[18] 1
assign T184 57
gt test base[0][T183] T184
goif B518 test
goto B525
@label B518
goto B521
assign T185 True
goto Bool522
@label B521
assign T185 False
@label Bool522
return T185
goto B537
@label B525
goif B527 base[4]
goto B537
@label B527
goif B537 base[5]
goto B529
@label B529


goto B532
@label B532
assign base[5] True
goto Bool535
assign base[5] False
@label Bool535
goto B537
@label B537
assign T186 1
add T187 base[18] T186
assign base[18] T187
goto L20
@label B541
goif B543 base[4]
goto B547
@label B543
goif B545 base[5]
goto B547
@label B545
assign T188 True
goto Bool548
@label B547
assign T188 False
@label Bool548
return T188
@label F14_end
assign lastbase base
@endfunction
@label F14_out
assign T189 512
assign T190 T189
assign T191 32
assign T192 T191
assign T194 1
mult T194 T194 T190
malloc T193 T194
assign T196 1
mult T196 T196 T190
malloc T195 T196
assign T198 1
mult T198 T198 T192
malloc T197 T198
assign T200 1
mult T200 T200 T192
malloc T199 T200
@label L23
goto B572
@label B572
param S4
call T202 PRINT 1
param T193
call T203 READ 1
param T193
call T204 STOF 1
assign T201 T204
param T197
param T201
call T205 FTOS 2
param T201
call T206 F3 1
param T199
param T206
call T207 FTOS 2
assign A2[16] T74
assign A2[12] T199
assign A2[8] S6
assign A2[4] T197
assign A2[0] S5
assign T208 5
param A2
param T208
param T195
call T209 F12 3
param T195
call T210 PRINT 1
param S7
call T211 PRINT 1
param T193
call T212 READ 1
param T193
param S8
call T213 F10 2
@label L24
assign T214 0
eq test T213 T214
goif B619 test
goto B611
@label B611
param T193
param S9
call T215 F10 2
@label L25
assign T216 0
eq test T215 T216
goif B619 test
goto L23
@label B619
param S10
call T217 PRINT 1
goto L23
goto L23
free T193
free T195
free T197
free T199
