@staticv A0 1
@staticv A1 1
@staticv A2 160
@staticv A3 1
@string S0 "Desea organizar los peroles? [Y\n] "
@string S1 "n"
@string S2 "N"
@string S3 "Hasta luego!"
@string S4 "Indique el numero de peroles a organizar: "
@string S5 "No se pueden organizar mas de 20 peroles."
@string S6 "Indique el tipo del perol: "
@string S7 "1. Booleano"
@string S8 "2. Caracter"
@string S9 "3. Entero"
@string S10 "4. De punto flotante"
@string S11 "El valor del perol es True? [Y/n] "
@string S12 "n"
@string S13 "N"
@string S14 "Indique el caracter: "
@string S15 "Indique el entero: "
@string S16 "Indique el flotante: "
@string S17 "Tipo invalido"
@string S18 "Imprimimos los peroles ordenados:"
@string S19 "BOOL: "
@string S20 "True"
@string S21 "False"
@string S22 "CHAR: "
@string S23 "INT: "
@string S24 "FLOAT: "
assign T0 0
assign A0[0] T0
assign T1 A0
assign T2 10
assign A1[0] T2
assign T3 A1
assign T4 0
goto F0_out
@function F0 12
assign T5 0
assign base[8] T5
@label L0
mult T7 base[8] 1
@label L1
neq test base[0][T7] base[4]
goif B17 test
goto B21
@label B17
assign T8 1
add T9 base[8] T8
assign base[8] T9
goto L0
@label B21
return base[8]
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 12
assign T10 0
assign base[8] T10
@label L2
mult T12 base[8] 1
@label L3
assign T13 0
neq test base[0][T12] T13
goif B37 test
goto B47
@label B37
mult T15 base[8] 1
@label L4
mult T17 base[8] 1
eq test base[0][T15] base[4][T17]
goif B43 test
goto B47
@label B43
assign T18 1
add T19 base[8] T18
assign base[8] T19
goto L2
@label B47
mult T21 base[8] 1
mult T23 base[8] 1
gt test base[0][T21] base[4][T23]
goif B52 test
goto B55
@label B52
assign T24 1
return T24
goto F1_end
@label B55
mult T26 base[8] 1
mult T28 base[8] 1
gt test base[4][T26] base[0][T28]
goif B60 test
goto B64
@label B60
assign T29 1
minus T30 T29
return T30
goto F1_end
@label B64
assign T31 0
return T31
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 16
param base[4]
param T4
call T32 F0 2
assign T33 1
add T34 T32 T33
assign base[8] T34
assign T35 0
assign base[12] T35
@label L5
lt test base[12] base[8]
goif B84 test
goto F2_end
@label B84
mult T37 base[12] 1
mult T39 base[12] 1
assign base[0][T37] base[4][T39]
assign T40 1
add T41 base[12] T40
assign base[12] T41
goto L5
@label F2_end
assign lastbase base
@endfunction
@label F2_out
goto F3_out
@function F3 28
assign T42 0
assign T43 0
assign base[12] T42
assign base[16] T43
@label L6
lt test base[12] base[4]
goif B105 test
goto B131
@label B105
mult T45 base[12] 4
param base[0][T45]
param T4
call T46 F0 2
assign base[24] T46
assign T47 0
assign base[20] T47
@label L7
lt test base[20] base[24]
goif B116 test
goto B127
@label B116
mult T49 base[16] 1
mult T51 base[12] 4
mult T53 base[20] 1
assign base[8][T49] base[0][T51][T53]
assign T54 1
add T55 base[20] T54
assign base[20] T55
assign T56 1
add T57 base[16] T56
assign base[16] T57
goto L7
@label B127
assign T58 1
add T59 base[12] T58
assign base[12] T59
goto L6
@label B131
mult T61 base[16] 1
assign T62 0
assign base[8][T61] T62
@label F3_end
assign lastbase base
@endfunction
@label F3_out
goto F4_out
@function F4 29
assign T63 0
assign T64 0
assign T65 0
param base[0]
param T4
call T66 F0 2
assign base[12] T63
assign base[16] T64
assign base[20] T65
assign base[24] T66
goto B151
@label B151
assign base[28] True
goto Bool154
assign base[28] False
@label Bool154
@label L8
mult T68 base[12] 1
@label L9
assign T69 0
neq test base[0][T68] T69
goif B162 test
goto B210
@label B162
mult T71 base[12] 1
@label L10
eq test base[0][T71] base[8]
goif B167 test
goto B186
@label B167
goif B186 base[28]
goto B169
@label B169


goto B172
@label B172
assign base[28] True
goto Bool175
assign base[28] False
@label Bool175
mult T73 base[20] 4
mult T75 base[16] 1
assign T76 0
assign base[4][T73][T75] T76
assign T77 1
add T78 base[20] T77
assign base[20] T78
assign T79 0
assign base[16] T79
goto B206
@label B186
mult T81 base[12] 1
@label L11
neq test base[0][T81] base[8]
goif B191 test
goto B206
@label B191


goto B196
assign base[28] True
goto Bool197
@label B196
assign base[28] False
@label Bool197
mult T83 base[20] 4
mult T85 base[16] 1
mult T87 base[12] 1
assign base[4][T83][T85] base[0][T87]
assign T88 1
add T89 base[16] T88
assign base[16] T89
goto B206
@label B206
assign T90 1
add T91 base[12] T90
assign base[12] T91
goto L8
@label B210
goif B220 base[28]
goto B212
@label B212
mult T93 base[20] 4
mult T95 base[16] 1
assign T96 0
assign base[4][T93][T95] T96
assign T97 1
add T98 base[20] T97
assign base[20] T98
goto B220
@label B220
return base[20]
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 22
goto B231
goto B235
assign base[4] True
goto Bool232
@label B231
assign base[4] False
@label Bool232
assign base[5] True
goto Bool236
@label B235
assign base[5] False
@label Bool236
param base[0]
param T4
call T99 F0 2
assign T100 0
assign base[10] T99
assign base[18] T100
@label L12
lt test base[18] base[10]
goif B247 test
goto B309
@label B247
mult T102 base[18] 1
@label L13
assign T103 46
eq test base[0][T102] T103
goif B253 test
goto B263
@label B253
goif B263 base[4]
goto B255
@label B255


goto B258
@label B258
assign base[4] True
goto Bool261
assign base[4] False
@label Bool261
goto B305
@label B263
mult T105 base[18] 1
@label L14
assign T106 46
eq test base[0][T105] T106
goif B269 test
goto B276
@label B269
goto B272
assign T107 True
goto Bool273
@label B272
assign T107 False
@label Bool273
return T107
goto B305
@label B276
mult T109 base[18] 1
assign T110 48
lt test base[0][T109] T110
goif B286 test
goto B281
@label B281
mult T112 base[18] 1
assign T113 57
gt test base[0][T112] T113
goif B286 test
goto B293
@label B286
goto B289
assign T114 True
goto Bool290
@label B289
assign T114 False
@label Bool290
return T114
goto B305
@label B293
goif B295 base[4]
goto B305
@label B295
goif B305 base[5]
goto B297
@label B297


goto B300
@label B300
assign base[5] True
goto Bool303
assign base[5] False
@label Bool303
goto B305
@label B305
assign T115 1
add T116 base[18] T115
assign base[18] T116
goto L12
@label B309
goif B311 base[4]
goto B315
@label B311
goif B313 base[5]
goto B315
@label B313
assign T117 True
goto Bool316
@label B315
assign T117 False
@label Bool316
return T117
@label F5_end
assign lastbase base
@endfunction
@label F5_out
assign T118 512
assign T119 T118
assign T120 20
assign T121 8
mult T121 T121 T120
@label L15
sub T121 T121 8
lt test T121 0
goif L15_end test
goto L15
@label L15_end
assign T123 1
mult T123 T123 T119
malloc T122 T123
@label L16
goto B338
@label B338
param S0
call T126 PRINT 1
param T122
call T127 READ 1
param T122
param S1
call T128 F1 2
@label L17
assign T129 0
eq test T128 T129
goif B358 test
goto B350
@label B350
param T122
param S2
call T130 F1 2
@label L18
assign T131 0
eq test T130 T131
goif B358 test
goto B361
@label B358
param S3
call T132 PRINT 1
goto B361
@label B361
param S4
call T133 PRINT 1
param T122
call T134 READ 1
param T122
call T135 STOI 1
assign T124 T135
assign T136 20
gt test T124 T136
goif B372 test
goto B378
@label B372
param S5
call T137 PRINT 1
param T3
call T138 PRINT 1
goto L16
goto B378
@label B378
assign T139 0
assign T125 T139
@label L19
lt test T125 T124
goif B384 test
goto B497
@label B384
param S6
call T140 PRINT 1
param T3
call T141 PRINT 1
param S7
call T142 PRINT 1
param T3
call T143 PRINT 1
param S8
call T144 PRINT 1
param T3
call T145 PRINT 1
param S9
call T146 PRINT 1
param T3
call T147 PRINT 1
param S10
call T148 PRINT 1
param T3
call T149 PRINT 1
param T122
call T150 READ 1
param T122
call T151 STOI 1
assign T124 T151
mult T153 T125 8
assign A2[T153][0] T124
@label L20
assign T154 1
eq test T124 T154
goif B416 test
goto B444
@label B416
param S11
call T155 PRINT 1
param T122
call T156 READ 1
mult T158 T125 8


param T122
param S12
call T159 F1 2
@label L21
assign T160 0
eq test T159 T160
goif B439 test
goto B431
@label B431
param T122
param S13
call T161 F1 2
@label L22
assign T162 0
eq test T161 T162
goif B439 test
goto B441
@label B439
assign A2[T158][4][0] True
goto Bool442
@label B441
assign A2[T158][4][0] False
@label Bool442
goto B493
@label B444
@label L23
assign T163 2
eq test T124 T163
goif B449 test
goto B458
@label B449
param S14
call T164 PRINT 1
param T122
call T165 READ 1
mult T167 T125 8
assign T168 0
mult T170 T168 1
assign A2[T167][4][0] T122[T170]
goto B493
@label B458
@label L24
assign T171 3
eq test T124 T171
goif B463 test
goto B472
@label B463
param S15
call T172 PRINT 1
param T122
call T173 READ 1
mult T175 T125 8
param T122
call T176 STOI 1
assign A2[T175][4][0] T176
goto B493
@label B472
@label L25
assign T177 4
eq test T124 T177
goif B477 test
goto B486
@label B477
param S16
call T178 PRINT 1
param T122
call T179 READ 1
mult T181 T125 8
param T122
call T182 STOF 1
assign A2[T181][4][0] T182
goto B493
@label B486
param S17
call T183 PRINT 1
param T3
call T184 PRINT 1
assign T185 1
sub T186 T125 T185
assign T125 T186
@label B493
assign T187 1
add T188 T125 T187
assign T125 T188
goto L19
@label B497
param A2
param T124
call T189 F6 2
param T3
call T190 PRINT 1
param S18
call T191 PRINT 1
param T3
call T192 PRINT 1
assign T193 0
assign T125 T193
@label L26
lt test T125 T124
goif B512 test
goto L16
@label B512
mult T195 T125 8
@label L27
assign T196 1
eq test A2[T195][0] T196
goif B518 test
goto B529
@label B518
param S19
call T197 PRINT 1
mult T199 T125 8
goif B523 A2[T199][4][0]
goto B526
@label B523
param S20
call T200 PRINT 1
goto B526
@label B526
param S21
call T201 PRINT 1
goto B565
@label B529
mult T203 T125 8
@label L28
assign T204 2
eq test A2[T203][0] T204
goif B535 test
goto B542
@label B535
param S22
call T205 PRINT 1
mult T207 T125 8
assign A3[0] A2[T207][4][0]
param A3
call T208 PRINT 1
goto B565
@label B542
mult T210 T125 8
@label L29
assign T211 3
eq test A2[T210][0] T211
goif B548 test
goto B557
@label B548
param S23
call T212 PRINT 1
mult T214 T125 8
param T122
param A2[T214][4][0]
call T215 ITOS 2
param T122
call T216 PRINT 1
goto B565
@label B557
param S24
call T217 PRINT 1
mult T219 T125 8
param T122
param A2[T219][4][0]
call T220 FTOS 2
param T122
call T221 PRINT 1
@label B565
param T3
call T222 PRINT 1
assign T223 1
add T224 T125 T223
assign T125 T224
goto L26
goto L16
goto F6_out
@function F6 32
assign T225 0
assign T226 0
assign T227 1
sub T228 base[8] T227
assign base[12] T225
assign base[16] T226
assign base[20] T228
malloc base[24] 8
@label L30
leq test base[16] base[20]
goif B586 test
goto B627
@label B586
mult T230 base[16] 8
@label L31
assign T231 1
eq test base[0][T230][0] T231
goif B592 test
goto B606
@label B592
mult T233 base[16] 8
assign base[24] base[0][T233]
mult T235 base[16] 8
mult T237 base[12] 8
assign base[0][T235] base[0][T237]
mult T239 base[12] 8
assign base[0][T239] base[24]
assign T240 1
add T241 base[12] T240
assign base[12] T241
assign T242 1
add T243 base[16] T242
assign base[16] T243
goto L30
@label B606
mult T245 base[16] 8
@label L32
assign T246 4
eq test base[0][T245][0] T246
goif B612 test
goto B623
@label B612
mult T248 base[16] 8
assign base[24] base[0][T248]
mult T250 base[16] 8
mult T252 base[20] 8
assign base[0][T250] base[0][T252]
mult T254 base[20] 8
assign base[0][T254] base[24]
assign T255 1
sub T256 base[20] T255
assign base[20] T256
goto L30
@label B623
assign T257 1
add T258 base[16] T257
assign base[16] T258
goto L30
@label B627
@label L33
leq test base[12] base[20]
goif B631 test
goto F6_end
@label B631
mult T260 base[12] 8
@label L34
assign T261 2
eq test base[0][T260][0] T261
goif B637 test
goto B641
@label B637
assign T262 1
add T263 base[12] T262
assign base[12] T263
goto L33
@label B641
mult T265 base[12] 8
assign base[24] base[0][T265]
mult T267 base[12] 8
mult T269 base[20] 8
assign base[0][T267] base[0][T269]
mult T271 base[20] 8
assign base[0][T271] base[24]
assign T272 1
sub T273 base[20] T272
assign base[20] T273
goto L33
@label F6_end
assign lastbase base
@endfunction
@label F6_out
assign T274 8
mult T274 T274 T120
@label L35
sub T274 T274 8
lt test T274 0
goif L35_end test
goto L35
@label L35_end
free T122
