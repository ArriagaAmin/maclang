@string S0 "No esta definido el factorial para numeros negativos"
@string S1 "No esta definido el factorial para numeros negativos"
@string S2 "No se puede calcular el minimo de un arreglo vacio."
@string S3 "No se puede calcular el maximo de un arreglo vacio."
@string S4 "Indique el numero entero no negativo: "
@string S5 "El metodo para calcular el factorial debe ser iterativo? [Y/n] "
@string S6 "n"
@string S7 "N"
@string S8 "! = "
@string S9 "Desea calcular otro factorial? [Y/n] "
@string S10 "n"
@string S11 "N"
@string S12 "Hasta luego!"
goto F0_out
@function F0 4
assign T0 0
lt test base[0] T0
goif B6 test
goto B11
@label B6
param T1
call T2 PRINT 1
assign T3 1
exit T3
goto F0_end
@label B11
@label L0
assign T4 0
eq test base[0] T4
goif B16 test
goto B19
@label B16
assign T5 1
return T5
goto F0_end
@label B19
assign T6 1
sub T7 base[0] T6
param T7
call T8 F0 1
mult T9 base[0] T8
return T9
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 8
assign T10 0
lt test base[0] T10
goif B35 test
goto B40
@label B35
param T11
call T12 PRINT 1
assign T13 1
exit T13
goto B40
@label B40
assign T14 1
assign base[4] T14
@label L1
assign T15 0
gt test base[0] T15
goif B47 test
goto B53
@label B47
mult T16 base[4] base[0]
assign base[4] T16
assign T17 1
sub T18 base[0] T17
assign base[0] T18
goto L1
@label B53
return base[4]
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 4
assign T19 0
lt test base[0] T19
goif B64 test
goto B67
@label B64
minus T20 base[0]
return T20
goto F2_end
@label B67
return base[0]
@label F2_end
assign lastbase base
@endfunction
@label F2_out
goto F3_out
@function F3 16
assign T21 1.000000
assign base[4] base[0]
assign base[8] T21
@label L2
assign T22 0.000001
gt test base[8] T22
goif B82 test
goto B93
@label B82
assign base[12] base[4]
div T23 base[0] base[4]
add T24 base[4] T23
assign T25 2
div T26 T24 T25
assign base[4] T26
sub T27 base[4] base[12]
param T27
call T28 F2 1
assign base[8] T28
goto L2
@label B93
return base[4]
@label F3_end
assign lastbase base
@endfunction
@label F3_out
goto F4_out
@function F4 16
assign T29 0.000000
assign base[8] T29
assign T30 0
assign base[12] T30
@label L3
lt test base[12] base[4]
goif B108 test
goto B112
@label B108
mult T32 base[12] 4
add T33 base[8] base[0][T32]
assign base[8] T33
goto L3
@label B112
div T34 base[8] base[4]
return T34
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 16
assign T35 1
lt test base[4] T35
goif B124 test
goto B129
@label B124
param T36
call T37 PRINT 1
assign T38 1
exit T38
goto B129
@label B129
assign T39 0
mult T41 T39 4
assign base[8] base[0][T41]
assign T42 1
assign base[12] T42
@label L4
lt test base[12] base[4]
goif B138 test
goto B146
@label B138
mult T44 base[12] 4
lt test base[0][T44] base[8]
goif B142 test
goto L4
@label B142
mult T46 base[12] 4
assign base[8] base[0][T46]
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
assign T47 1
lt test base[4] T47
goif B157 test
goto B162
@label B157
param T48
call T49 PRINT 1
assign T50 1
exit T50
goto B162
@label B162
assign T51 0
mult T53 T51 4
assign base[8] base[0][T53]
assign T54 1
assign base[12] T54
@label L5
lt test base[12] base[4]
goif B171 test
goto B179
@label B171
mult T56 base[12] 4
gt test base[0][T56] base[8]
goif B175 test
goto L5
@label B175
mult T58 base[12] 4
assign base[8] base[0][T58]
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
assign T59 0
eq test base[4] T59
goif B191 test
goto B194
@label B191
assign T60 0.000000
return T60
goto B194
@label B194
assign T62 4
mult T62 T62 
malloc T61 T62
memcpy T61 base[0]
param T61
param base[4]
call T63 F4 2
assign T64 0.000000
assign base[8] T63
assign base[12] T64
assign T65 0
assign base[16] T65
@label L7
lt test base[16] base[4]
goif B210 test
goto B218
@label B210
mult T67 base[16] 4
sub T68 base[0][T67] base[8]
mult T70 base[16] 4
sub T71 base[0][T70] base[8]
mult T72 T68 T71
add T73 base[12] T72
assign base[12] T73
goto L7
@label B218
div T74 base[12] base[4]
return T74
@label F7_end
assign lastbase base
@endfunction
@label F7_out
goto F8_out
@function F8 8
assign T76 4
mult T76 T76 
malloc T75 T76
memcpy T75 base[0]
param T75
param base[4]
call T77 F7 2
param T77
call T78 F3 1
return T78
@label F8_end
assign lastbase base
@endfunction
@label F8_out
assign T79 0
assign T81 1
mult T81 T81 
malloc T80 T81
assign T80[0] T79
assign T82 T80
assign T83 10
assign T85 1
mult T85 T85 
malloc T84 T85
assign T84[0] T83
assign T86 T84
assign T87 0
goto F9_out
@function F9 12
assign T88 0
assign base[8] T88
@label L8
mult T90 base[8] 1
@label L9
neq test base[0][T90] base[4]
goif B263 test
goto B267
@label B263
assign T91 1
add T92 base[8] T91
assign base[8] T92
goto L8
@label B267
return base[8]
@label F9_end
assign lastbase base
@endfunction
@label F9_out
goto F10_out
@function F10 12
assign T93 0
assign base[8] T93
@label L10
mult T95 base[8] 1
@label L11
assign T96 0
neq test base[0][T95] T96
goif B283 test
goto B293
@label B283
mult T98 base[8] 1
@label L12
mult T100 base[8] 1
eq test base[0][T98] base[4][T100]
goif B289 test
goto B293
@label B289
assign T101 1
add T102 base[8] T101
assign base[8] T102
goto L10
@label B293
mult T104 base[8] 1
mult T106 base[8] 1
gt test base[0][T104] base[4][T106]
goif B298 test
goto B301
@label B298
assign T107 1
return T107
goto F10_end
@label B301
mult T109 base[8] 1
mult T111 base[8] 1
gt test base[4][T109] base[0][T111]
goif B306 test
goto B310
@label B306
assign T112 1
minus T113 T112
return T113
goto F10_end
@label B310
assign T114 0
return T114
@label F10_end
assign lastbase base
@endfunction
@label F10_out
goto F11_out
@function F11 16
param T115
param T87
call T116 F9 2
assign T117 1
add T118 T116 T117
assign base[8] T118
assign T119 0
assign base[12] T119
@label L13
lt test base[12] base[8]
goif B330 test
goto F11_end
@label B330
mult T121 base[12] 1
mult T123 base[12] 1
assign base[0][T121] base[4][T123]
assign T124 1
add T125 base[12] T124
assign base[12] T125
goto L13
@label F11_end
assign lastbase base
@endfunction
@label F11_out
goto F12_out
@function F12 28
assign T126 0
assign T127 0
assign base[12] T126
assign base[16] T127
@label L14
lt test base[12] base[4]
goif B351 test
goto B377
@label B351
mult T129 base[12] 4
param T130
param T87
call T131 F9 2
assign base[24] T131
assign T132 0
assign base[20] T132
@label L15
lt test base[20] base[24]
goif B362 test
goto B373
@label B362
mult T134 base[16] 1
mult T136 base[12] 4
mult T138 base[20] 1
assign base[8][T134] base[0][T136][T138]
assign T139 1
add T140 base[20] T139
assign base[20] T140
assign T141 1
add T142 base[16] T141
assign base[16] T142
goto L15
@label B373
assign T143 1
add T144 base[12] T143
assign base[12] T144
goto L14
@label B377
mult T146 base[16] 1
assign T147 0
assign base[8][T146] T147
@label F12_end
assign lastbase base
@endfunction
@label F12_out
goto F13_out
@function F13 29
assign T148 0
assign T149 0
assign T150 0
param T151
param T87
call T152 F9 2
assign base[12] T148
assign base[16] T149
assign base[20] T150
assign base[24] T152
goto B397
@label B397
assign base[28] True
goto Bool400
assign base[28] False
@label Bool400
@label L16
mult T154 base[12] 1
@label L17
assign T155 0
neq test base[0][T154] T155
goif B408 test
goto B456
@label B408
mult T157 base[12] 1
@label L18
eq test base[0][T157] base[8]
goif B413 test
goto B432
@label B413
goif B432 base[28]
goto B415
@label B415


goto B418
@label B418
assign base[28] True
goto Bool421
assign base[28] False
@label Bool421
mult T159 base[20] 4
mult T161 base[16] 1
assign T162 0
assign base[4][T159][T161] T162
assign T163 1
add T164 base[20] T163
assign base[20] T164
assign T165 0
assign base[16] T165
goto B452
@label B432
mult T167 base[12] 1
@label L19
neq test base[0][T167] base[8]
goif B437 test
goto B452
@label B437


goto B442
assign base[28] True
goto Bool443
@label B442
assign base[28] False
@label Bool443
mult T169 base[20] 4
mult T171 base[16] 1
mult T173 base[12] 1
assign base[4][T169][T171] base[0][T173]
assign T174 1
add T175 base[16] T174
assign base[16] T175
goto B452
@label B452
assign T176 1
add T177 base[12] T176
assign base[12] T177
goto L16
@label B456
goif B466 base[28]
goto B458
@label B458
mult T179 base[20] 4
mult T181 base[16] 1
assign T182 0
assign base[4][T179][T181] T182
assign T183 1
add T184 base[20] T183
assign base[20] T184
goto B466
@label B466
return base[20]
@label F13_end
assign lastbase base
@endfunction
@label F13_out
goto F14_out
@function F14 16
goto B477
goto B481
assign base[4] True
goto Bool478
@label B477
assign base[4] False
@label Bool478
assign base[5] True
goto Bool482
@label B481
assign base[5] False
@label Bool482
param T185
param T87
call T186 F9 2
assign T187 0
assign base[8] T186
assign base[12] T187
@label L20
lt test base[12] base[8]
goif B493 test
goto B555
@label B493
mult T189 base[12] 1
@label L21
assign T190 46
eq test base[0][T189] T190
goif B499 test
goto B509
@label B499
goif B509 base[4]
goto B501
@label B501


goto B504
@label B504
assign base[4] True
goto Bool507
assign base[4] False
@label Bool507
goto B551
@label B509
mult T192 base[12] 1
@label L22
assign T193 46
eq test base[0][T192] T193
goif B515 test
goto B522
@label B515
goto B518
assign T194 True
goto Bool519
@label B518
assign T194 False
@label Bool519
return T194
goto B551
@label B522
mult T196 base[12] 1
assign T197 48
lt test base[0][T196] T197
goif B532 test
goto B527
@label B527
mult T199 base[12] 1
assign T200 57
gt test base[0][T199] T200
goif B532 test
goto B539
@label B532
goto B535
assign T201 True
goto Bool536
@label B535
assign T201 False
@label Bool536
return T201
goto B551
@label B539
goif B541 base[4]
goto B551
@label B541
goif B551 base[5]
goto B543
@label B543


goto B546
@label B546
assign base[5] True
goto Bool549
assign base[5] False
@label Bool549
goto B551
@label B551
assign T202 1
add T203 base[12] T202
assign base[12] T203
goto L20
@label B555
goif B557 base[4]
goto B561
@label B557
goif B559 base[5]
goto B561
@label B559
assign T204 True
goto Bool562
@label B561
assign T204 False
@label Bool562
return T204
@label F14_end
assign lastbase base
@endfunction
@label F14_out
assign T205 512
assign T206 T205
assign T207 16
assign T208 T207
assign T210 1
mult T210 T210 T206
malloc T209 T210
assign T212 1
mult T212 T212 T206
malloc T211 T212
assign T214 1
mult T214 T214 T208
malloc T213 T214
assign T216 1
mult T216 T216 T208
malloc T215 T216
@label L23
goto B586
@label B586
param T220
call T221 PRINT 1
assign T223 1
mult T223 T223 T206
malloc T222 T223
memcpy T222 T211
param T222
call T224 READ 1
assign T226 1
mult T226 T226 T206
malloc T225 T226
memcpy T225 T211
param T225
call T227 STOI 1
assign T217 T227
param T228
call T229 PRINT 1
assign T231 1
mult T231 T231 T206
malloc T230 T231
memcpy T230 T211
param T230
call T232 READ 1


assign T234 1
mult T234 T234 T206
malloc T233 T234
memcpy T233 T211
param T233
param T235
call T236 F10 2
@label L24
assign T237 0
eq test T236 T237
goif B635 test
goto B623
@label B623
assign T239 1
mult T239 T239 T206
malloc T238 T239
memcpy T238 T211
param T238
param T240
call T241 F10 2
@label L25
assign T242 0
eq test T241 T242
goif B635 test
goto B637
@label B635
assign T219 True
goto Bool638
@label B637
assign T219 False
@label Bool638
goif B641 T219
goto B645
@label B641
param T217
call T243 F0 1
assign T218 T243
goto B648
@label B645
param T217
call T244 F1 1
assign T218 T244
@label B648
assign T246 1
mult T246 T246 T208
malloc T245 T246
memcpy T245 T213
param T245
param T217
call T247 ITOS 2
assign T249 1
mult T249 T249 T208
malloc T248 T249
memcpy T248 T215
param T248
param T218
call T250 ITOS 2
assign T252 4
mult T252 T252 
malloc T251 T252
@label L26
sub T252 T252 4
lt test T252 0
goif L26_end test
goto L26
@label L26_end
assign T251[12] T86
assign T251[8] T215
assign T251[4] S8
assign T251[0] T213
assign T253 4
assign T255 4
mult T255 T255 
malloc T254 T255
@label L27
sub T255 T255 4
lt test T255 0
goif L27_end test
goto L27
@label L27_end
param T254
param T253
assign T257 1
mult T257 T257 T206
malloc T256 T257
memcpy T256 T209
param T256
call T258 F12 3
assign T260 1
mult T260 T260 T206
malloc T259 T260
memcpy T259 T209
param T259
call T261 PRINT 1
param T262
call T263 PRINT 1
assign T265 1
mult T265 T265 T206
malloc T264 T265
memcpy T264 T211
param T264
call T266 READ 1
assign T268 1
mult T268 T268 T206
malloc T267 T268
memcpy T267 T211
param T267
param T269
call T270 F10 2
@label L28
assign T271 0
eq test T270 T271
goif B731 test
goto B719
@label B719
assign T273 1
mult T273 T273 T206
malloc T272 T273
memcpy T272 T211
param T272
param T274
call T275 F10 2
@label L29
assign T276 0
eq test T275 T276
goif B731 test
goto L23
@label B731
param T277
call T278 PRINT 1
goto L23
goto L23
assign T279 1
assign T280 8
assign T281 4
mult T282 T280 T281
assign T283 2
div T284 T282 T283
add T285 T279 T284
assign T286 4
assign T287 16
assign T288 2
assign T289 1
@label L30
leq test T288 0
goif L30_end test
mult T289 T289 T287
sub T288 T288 1
goto L30
@label L30_end
mult T290 T286 T289
add T291 T285 T290
