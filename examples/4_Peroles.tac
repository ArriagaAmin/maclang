@staticv A0 5
@staticv A1 1
@string S0 "0000\n"
@string S1 "0000-"
@string S2 "0000."
@string S3 "0000Desea organizar los peroles? [Y\n] "
@string S4 "0000Hasta luego!"
@string S5 "0000Indique el numero de peroles a organizar: "
@string S6 "0000No se pueden organizar mas de 20 peroles."
@string S7 "0000Indique el tipo del perol: "
@string S8 "00001. Booleano"
@string S9 "00002. Caracter"
@string S10 "00003. Entero"
@string S11 "00004. De punto flotante"
@string S12 "0000El valor del perol es True? [Y/n] "
@string S13 "0000Indique el caracter: "
@string S14 "0000Indique el entero: "
@string S15 "0000Indique el flotante: "
@string S16 "0000Tipo invalido"
@string S17 "0000%cImprimimos los peroles ordenados:"
@string S18 "0000BOOL: "
@string S19 "0000"
@string S20 "0000True"
@string S21 "0000False"
@string S22 "0000CHAR: %c"
@string S23 "0000INT: %i"
@string S24 "0000FLOAT: %f"
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
assignb test A0
assignw T8 4
assignw T9 4
assignw T10 4
assignw T11 4
assignw T12 4
assignw T13 BASE[0]
@label L0
assignb T14 T13[T8]
add T8 T8 1
eq test T14 0
goif L0_end test
eq test T14 37
goif L1 test
printc T14
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
assignb T20 0
assignw T21 1
assignw T23 T21
assignw T24 1
mult T24 T24 T23
add T24 T24 4
malloc T22 T24
assignw T22[0] T23
assignb T22[4] T20
assignw T25 T22
assignb T27 10
assignw T28 1
assignw T30 T28
assignw T31 1
mult T31 T31 T30
add T31 T31 4
malloc T29 T31
assignw T29[0] T30
assignb T29[4] T27
assignw T32 T29
@function Function0 12
assignb T34 A1[0]
goif L6 T34
assignb T35 0
assignb BASE[4] T35
@label L6
assignw T36 0
assignw BASE[8] T36
@label L7
assignw T37 BASE[0]
assignw T38 BASE[8]
mult T39 1 T38
add T39 T39 4
@label L8
assignb T40 T37[T39]
assignb T41 BASE[4]
neq test T40 T41
goif B134 test
goto B139
@label B134
assignw T42 1
assignw T44 BASE[8]
add T43 T44 T42
assignw BASE[8] T43
goto L7
@label B139
assignw T45 BASE[8]
assignw lastbase BASE
return T45
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function1 12
assignw T48 0
assignw BASE[8] T48
@label L9
assignw T49 BASE[0]
assignw T50 BASE[8]
mult T51 1 T50
add T51 T51 4
@label L10
assignb T52 0
assignb T53 T49[T51]
neq test T53 T52
goif B160 test
goto B179
@label B160
assignw T54 BASE[0]
assignw T55 BASE[8]
mult T56 1 T55
add T56 T56 4
@label L11
assignw T57 BASE[4]
assignw T58 BASE[8]
mult T59 1 T58
add T59 T59 4
assignb T60 T54[T56]
assignb T61 T57[T59]
eq test T60 T61
goif B174 test
goto B179
@label B174
assignw T62 1
assignw T64 BASE[8]
add T63 T64 T62
assignw BASE[8] T63
goto L9
@label B179
assignw T65 BASE[0]
assignw T66 BASE[8]
mult T67 1 T66
add T67 T67 4
assignw T68 BASE[4]
assignw T69 BASE[8]
mult T70 1 T69
add T70 T70 4
assignw T71 T65[T67]
assignw T72 T68[T70]
gt test T71 T72
goif B192 test
goto B196
@label B192
assignw T73 1
assignw lastbase BASE
return T73
goto Function1_end
@label B196
assignw T74 BASE[4]
assignw T75 BASE[8]
mult T76 1 T75
add T76 T76 4
assignw T77 BASE[0]
assignw T78 BASE[8]
mult T79 1 T78
add T79 T79 4
assignw T80 T74[T76]
assignw T81 T77[T79]
gt test T80 T81
goif B209 test
goto B214
@label B209
assignw T82 1
minus T83 T82
assignw lastbase BASE
return T83
goto Function1_end
@label B214
assignw T84 0
assignw lastbase BASE
return T84
@label Function1_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function2 16
assignw T88 BASE[4]
assignw T89 T88[0]
assignw T90 1
mult T90 T90 T89
add T90 T90 4
malloc T87 T90
memcpy T87 T88 T90
param T91 0
assignw T91[0] T87
assignb A1[0] 0
call T92 Function0 2
assignw T93 1
add T94 T92 T93
assignw BASE[8] T94
assignw T95 0
assignw BASE[12] T95
@label L12
assignw T96 BASE[12]
assignw T97 BASE[8]
lt test T96 T97
goif B244 test
goto Function2_end
@label B244
assignw T98 BASE[0]
assignw T99 BASE[12]
mult T100 1 T99
add T100 T100 4
assignw T101 BASE[4]
assignw T102 BASE[12]
mult T103 1 T102
add T103 T103 4
assignb T104 T101[T103]
assignb T98[T100] T104
assignw T105 1
assignw T107 BASE[12]
add T106 T107 T105
assignw BASE[12] T106
goto L12
@label Function2_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function3 16
assignw T111 BASE[4]
assignw T112 T111[0]
assignw T113 1
mult T113 T113 T112
add T113 T113 4
malloc T110 T113
memcpy T110 T111 T113
param T114 0
assignw T114[0] T110
assignb A1[0] 0
call T115 Function0 2
assignw BASE[8] T115
assignw T116 0
assignw T118 T116
@label L13
assignw T119 BASE[8]
geq test T118 T119
goif L13_end test
assignw T117 T118
assignw T121 BASE[8]
assignw T122 BASE[12]
sub T120 T121 T122
assignw T123 1
sub T124 T120 T123
assignw T125 BASE[0]
mult T126 1 T124
add T126 T126 4
assignw T127 BASE[4]
assignw T128 BASE[12]
mult T129 1 T128
add T129 T129 4
assignb T130 T127[T129]
assignb T125[T126] T130
add T118 T118 1
goto L13
@label L13_end
@label Function3_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function4 28
assignw T134 0
assignw T135 0
assignw BASE[12] T134
assignw BASE[16] T135
@label L14
assignw T136 BASE[12]
assignw T137 BASE[4]
lt test T136 T137
goif B315 test
goto B367
@label B315
assignw T138 BASE[0]
assignw T139 BASE[12]
mult T140 4 T139
add T140 T140 4
assignw T142 T138[T140]
assignw T143 T142[0]
assignw T144 1
mult T144 T144 T143
add T144 T144 4
malloc T141 T144
memcpy T141 T142 T144
param T145 0
assignw T145[0] T141
assignb A1[0] 0
call T146 Function0 2
assignw BASE[24] T146
assignw T147 0
assignw BASE[20] T147
@label L15
assignw T148 BASE[20]
assignw T149 BASE[24]
lt test T148 T149
goif B339 test
goto B362
@label B339
assignw T150 BASE[8]
assignw T151 BASE[16]
mult T152 1 T151
add T152 T152 4
assignw T153 BASE[0]
assignw T154 BASE[12]
mult T155 4 T154
add T155 T155 4
assignw T156 T153[T155]
assignw T157 BASE[20]
mult T158 1 T157
add T158 T158 4
assignb T159 T156[T158]
assignb T150[T152] T159
assignw T160 1
assignw T162 BASE[20]
add T161 T162 T160
assignw BASE[20] T161
assignw T163 1
assignw T165 BASE[16]
add T164 T165 T163
assignw BASE[16] T164
goto L15
@label B362
assignw T166 1
assignw T168 BASE[12]
add T167 T168 T166
assignw BASE[12] T167
goto L14
@label B367
assignw T169 BASE[8]
assignw T170 BASE[16]
mult T171 1 T170
add T171 T171 4
assignb T172 0
assignb T169[T171] T172
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function5 29
assignw T176 0
assignw T177 0
assignw T178 0
assignw T180 BASE[0]
assignw T181 T180[0]
assignw T182 1
mult T182 T182 T181
add T182 T182 4
malloc T179 T182
memcpy T179 T180 T182
param T183 0
assignw T183[0] T179
assignb A1[0] 0
call T184 Function0 2
assignw BASE[12] T176
assignw BASE[16] T177
assignw BASE[20] T178
assignw BASE[24] T184
goto B397
@label B397
assignb BASE[28] True
goto Bool400
assignb BASE[28] False
@label Bool400
@label L16
assignw T185 BASE[0]
assignw T186 BASE[12]
mult T187 1 T186
add T187 T187 4
@label L17
assignb T188 0
assignb T189 T185[T187]
neq test T189 T188
goif B412 test
goto B492
@label B412
assignw T190 BASE[0]
assignw T191 BASE[12]
mult T192 1 T191
add T192 T192 4
@label L18
assignb T193 T190[T192]
assignb T194 BASE[8]
eq test T193 T194
goif B422 test
goto B450
@label B422
assignb T195 BASE[28]
goif B450 T195
goto B425
@label B425
assignb T196 BASE[28]


goto B429
@label B429
assignb BASE[28] True
goto Bool432
assignb BASE[28] False
@label Bool432
assignw T197 BASE[4]
assignw T198 BASE[20]
mult T199 4 T198
add T199 T199 4
assignw T200 T197[T199]
assignw T201 BASE[16]
mult T202 1 T201
add T202 T202 4
assignb T203 0
assignb T200[T202] T203
assignw T204 1
assignw T206 BASE[20]
add T205 T206 T204
assignw BASE[20] T205
assignw T207 0
assignw BASE[16] T207
goto B487
@label B450
assignw T208 BASE[0]
assignw T209 BASE[12]
mult T210 1 T209
add T210 T210 4
@label L19
assignb T211 T208[T210]
assignb T212 BASE[8]
neq test T211 T212
goif B460 test
goto B487
@label B460
assignb T213 BASE[28]


goto B466
assignb BASE[28] True
goto Bool467
@label B466
assignb BASE[28] False
@label Bool467
assignw T214 BASE[4]
assignw T215 BASE[20]
mult T216 4 T215
add T216 T216 4
assignw T217 T214[T216]
assignw T218 BASE[16]
mult T219 1 T218
add T219 T219 4
assignw T220 BASE[0]
assignw T221 BASE[12]
mult T222 1 T221
add T222 T222 4
assignb T223 T220[T222]
assignb T217[T219] T223
assignw T224 1
assignw T226 BASE[16]
add T225 T226 T224
assignw BASE[16] T225
goto B487
@label B487
assignw T227 1
assignw T229 BASE[12]
add T228 T229 T227
assignw BASE[12] T228
goto L16
@label B492
assignb T230 BASE[28]
goif B510 T230
goto B495
@label B495
assignw T231 BASE[4]
assignw T232 BASE[20]
mult T233 4 T232
add T233 T233 4
assignw T234 T231[T233]
assignw T235 BASE[16]
mult T236 1 T235
add T236 T236 4
assignb T237 0
assignb T234[T236] T237
assignw T238 1
assignw T240 BASE[20]
add T239 T240 T238
assignw BASE[20] T239
goto B510
@label B510
assignw T241 BASE[20]
assignw lastbase BASE
return T241
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 29
@function Function6 16
goto B522
goto B526
assignb BASE[4] True
goto Bool523
@label B522
assignb BASE[4] False
@label Bool523
assignb BASE[5] True
goto Bool527
@label B526
assignb BASE[5] False
@label Bool527
assignw T244 BASE[0]
assignw T245 T244[0]
assignw T246 1
mult T246 T246 T245
add T246 T246 4
malloc T243 T246
memcpy T243 T244 T246
param T247 0
assignw T247[0] T243
assignb A1[0] 0
call T248 Function0 2
assignw T249 0
assignw BASE[8] T248
assignw BASE[12] T249
@label L20
assignw T250 BASE[12]
assignw T251 BASE[8]
lt test T250 T251
goif B548 test
goto B634
@label B548
assignw T252 BASE[0]
assignw T253 BASE[12]
mult T254 1 T253
add T254 T254 4
@label L21
assignb T255 46
assignb T256 T252[T254]
eq test T256 T255
goif B558 test
goto B570
@label B558
assignb T257 BASE[4]
goif B570 T257
goto B561
@label B561
assignb T258 BASE[4]


goto B565
@label B565
assignb BASE[4] True
goto Bool568
assignb BASE[4] False
@label Bool568
goto B629
@label B570
assignw T259 BASE[0]
assignw T260 BASE[12]
mult T261 1 T260
add T261 T261 4
@label L22
assignb T262 46
assignb T263 T259[T261]
eq test T263 T262
goif B580 test
goto B588
@label B580
goto B583
assignb T264 True
goto Bool584
@label B583
assignb T264 False
@label Bool584
assignw lastbase BASE
return T264
goto B629
@label B588
assignw T265 BASE[0]
assignw T266 BASE[12]
mult T267 1 T266
add T267 T267 4
assignb T268 48
assignw T269 T265[T267]
lt test T269 T268
goif B606 test
goto B597
@label B597
assignw T270 BASE[0]
assignw T271 BASE[12]
mult T272 1 T271
add T272 T272 4
assignb T273 57
assignw T274 T270[T272]
gt test T274 T273
goif B606 test
goto B614
@label B606
goto B609
assignb T275 True
goto Bool610
@label B609
assignb T275 False
@label Bool610
assignw lastbase BASE
return T275
goto B629
@label B614
assignb T276 BASE[4]
goif B617 T276
goto B629
@label B617
assignb T277 BASE[5]
goif B629 T277
goto B620
@label B620
assignb T278 BASE[5]


goto B624
@label B624
assignb BASE[5] True
goto Bool627
assignb BASE[5] False
@label Bool627
goto B629
@label B629
assignw T279 1
assignw T281 BASE[12]
add T280 T281 T279
assignw BASE[12] T280
goto L20
@label B634
assignb T282 BASE[4]
goif B637 T282
goto B642
@label B637
assignb T283 BASE[5]
goif B640 T283
goto B642
@label B640
assignb T284 True
goto Bool643
@label B642
assignb T284 False
@label Bool643
assignw lastbase BASE
return T284
@label Function6_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function7 24
assignw T287 BASE[0]
assignw T288 T287[0]
assignw T289 1
mult T289 T289 T288
add T289 T289 4
malloc T286 T289
memcpy T286 T287 T289
param T290 0
assignw T290[0] T286
assignb A1[0] 0
call T291 Function0 2
assignw BASE[8] T291
assignw T292 0
assignw BASE[4] T292
@label L23
assignw T293 0
assignw T294 BASE[8]
eq test T294 T293
goif B687 test
goto B671
@label B671
assignw T295 0
assignw T296 BASE[0]
mult T297 1 T295
add T297 T297 4
@label L24
assignb T298 45
assignb T299 T296[T297]
eq test T299 T298
goif B681 test
goto B695
@label B681
@label L25
assignw T300 1
assignw T301 BASE[8]
eq test T301 T300
goif B687 test
goto B695
@label B687
goto B690
assignb T302 True
goto Bool691
@label B690
assignb T302 False
@label Bool691
assignw lastbase BASE
return T302
goto B715
@label B695
assignw T303 0
assignw T304 BASE[0]
mult T305 1 T303
add T305 T305 4
@label L26
assignb T306 45
assignb T307 T304[T305]
eq test T307 T306
goif B705 test
goto B711
@label B705
assignw T308 1
minus T309 T308
assignw BASE[16] T309
assignw T310 1
assignw BASE[12] T310
goto B715
@label B711
assignw T311 1
assignw BASE[16] T311
assignw T312 0
assignw BASE[12] T312
@label B715
assignw T313 1
assignw T315 BASE[8]
sub T314 T315 T313
assignw T316 1
assignw T318 BASE[12]
sub T317 T318 T316
assignw T319 1
minus T320 T319
assignw T322 T314
@label L27
lt test T320 0
goif L27_neg test
geq test T322 T317
goif L27_end test
goto L27_body
@label L27_neg
leq test T322 T317
goif L27_end test
@label L27_body
assignw T321 T322
assignw T323 BASE[0]
assignw T324 BASE[20]
mult T325 1 T324
add T325 T325 4
assignb T326 48
assignw T327 T323[T325]
lt test T327 T326
goif B753 test
goto B744
@label B744
assignw T328 BASE[0]
assignw T329 BASE[20]
mult T330 1 T329
add T330 T330 4
assignb T331 57
assignw T332 T328[T330]
gt test T332 T331
goif B753 test
goto B763
@label B753
assignw T333 0
assignw BASE[4] T333
goto B758
assignb T334 True
goto Bool759
@label B758
assignb T334 False
@label Bool759
assignw lastbase BASE
return T334
goto B763
@label B763
assignw T335 BASE[0]
assignw T336 BASE[20]
mult T337 1 T336
add T337 T337 4
assignb T338 T335[T337]
param T339 0
assignb T339[0] T338
call T340 CTOI 1
assignb T341 48
param T342 0
assignb T342[0] T341
call T343 CTOI 1
sub T344 T340 T343
assignw T346 BASE[16]
mult T345 T346 T344
assignw T348 BASE[4]
add T347 T348 T345
assignw BASE[4] T347
assignw T349 10
assignw T351 BASE[16]
mult T350 T351 T349
assignw BASE[16] T350
add T322 T322 T320
goto L27
@label L27_end
goto B789
@label B789
assignb T352 True
goto Bool792
assignb T352 False
@label Bool792
assignw lastbase BASE
return T352
@label Function7_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function8 36
assignw T355 BASE[0]
assignw T356 T355[0]
assignw T357 1
mult T357 T357 T356
add T357 T357 4
malloc T354 T357
memcpy T354 T355 T357
param T358 0
assignw T358[0] T354
assignb A1[0] 0
call T359 Function0 2
assignw BASE[8] T359
assignw T360 BASE[8]
assignw T361 BASE[12]
assignw T362 1
mult T362 T362 T360
add T362 T362 4
malloc T361 T362
assignw T361[0] T360
assignw T361[0] T361
assignw T363 BASE[8]
assignw T364 BASE[16]
assignw T365 1
mult T365 T365 T363
add T365 T365 4
malloc T364 T365
assignw T364[0] T363
assignw T364[0] T364
assignw T366 0
assignw BASE[32] T366
@label L28
assignw T367 BASE[0]
assignw T368 BASE[32]
mult T369 1 T368
add T369 T369 4
@label L29
assignb T370 46
assignb T371 T367[T369]
neq test T371 T370
goif B841 test
goto B866
@label B841
assignw T372 BASE[0]
assignw T373 BASE[32]
mult T374 1 T373
add T374 T374 4
@label L30
assignb T375 0
assignb T376 T372[T374]
neq test T376 T375
goif B851 test
goto B866
@label B851
assignw T377 BASE[12]
assignw T378 BASE[32]
mult T379 1 T378
add T379 T379 4
assignw T380 BASE[0]
assignw T381 BASE[32]
mult T382 1 T381
add T382 T382 4
assignb T383 T380[T382]
assignb T377[T379] T383
assignw T384 1
assignw T386 BASE[32]
add T385 T386 T384
assignw BASE[32] T385
goto L28
@label B866
@label L31
assignw T387 0
assignw T388 BASE[32]
eq test T388 T387
goif B872 test
goto B875
@label B872
assignw T389 0
assignw BASE[24] T389
goto B900
@label B875
assignw T391 BASE[12]
assignw T392 T391[0]
assignw T393 1
mult T393 T393 T392
add T393 T393 4
malloc T390 T393
memcpy T390 T391 T393
param T394 0
assignw T394[0] T390
assignw T395 BASE[24]
param T396 4
assignw T396[0] T395
call T397 Function7 2
assignw T398 lastbase[4]
assignw BASE[24] T398
goif B900 T397
goto B892
@label B892
goto B895
assignb T399 True
goto Bool896
@label B895
assignb T399 False
@label Bool896
assignw lastbase BASE
return T399
goto B900
@label B900
assignw T400 BASE[0]
assignw T401 BASE[32]
mult T402 1 T401
add T402 T402 4
@label L32
assignb T403 0
assignb T404 T400[T402]
eq test T404 T403
goif B910 test
goto B923
@label B910
assignw T405 BASE[24]
param T406 0
assignw T406[0] T405
call f4 ITOF 1
assignw BASE[4] f4
goto B916
@label B916
assignb T407 True
goto Bool919
assignb T407 False
@label Bool919
assignw lastbase BASE
return T407
goto B923
@label B923
assignw T408 1
assignw T410 BASE[32]
add T409 T410 T408
assignw BASE[32] T409
assignw T411 0
assignw BASE[20] T411
@label L33
assignw T412 BASE[0]
assignw T413 BASE[32]
mult T414 1 T413
add T414 T414 4
@label L34
assignb T415 0
assignb T416 T412[T414]
neq test T416 T415
goif B940 test
goto B959
@label B940
assignw T417 BASE[16]
assignw T418 BASE[20]
mult T419 1 T418
add T419 T419 4
assignw T420 BASE[0]
assignw T421 BASE[32]
mult T422 1 T421
add T422 T422 4
assignb T423 T420[T422]
assignb T417[T419] T423
assignw T424 1
assignw T426 BASE[32]
add T425 T426 T424
assignw BASE[32] T425
assignw T427 1
assignw T429 BASE[20]
add T428 T429 T427
assignw BASE[20] T428
goto L33
@label B959
@label L35
assignw T430 0
assignw T431 BASE[20]
eq test T431 T430
goif B965 test
goto B978
@label B965
assignw T432 BASE[24]
param T433 0
assignw T433[0] T432
call f5 ITOF 1
assignw BASE[4] f5
goto B971
@label B971
assignb T434 True
goto Bool974
assignb T434 False
@label Bool974
assignw lastbase BASE
return T434
goto B1003
@label B978
assignw T436 BASE[16]
assignw T437 T436[0]
assignw T438 1
mult T438 T438 T437
add T438 T438 4
malloc T435 T438
memcpy T435 T436 T438
param T439 0
assignw T439[0] T435
assignw T440 BASE[28]
param T441 4
assignw T441[0] T440
call T442 Function7 2
assignw T443 lastbase[4]
assignw BASE[28] T443
goif B1003 T442
goto B995
@label B995
goto B998
assignb T444 True
goto Bool999
@label B998
assignb T444 False
@label Bool999
assignw lastbase BASE
return T444
goto B1003
@label B1003
assignw T445 BASE[24]
param T446 0
assignw T446[0] T445
call f6 ITOF 1
assignw T447 BASE[28]
param T448 0
assignw T448[0] T447
call f7 ITOF 1
assignw T449 10
assignw T451 T449
assignw T452 BASE[20]
assignw T450 1
lt test T452 0
goif L36_neg test
@label L36_pos
eq test T452 0
goif L36_end test
mult T450 T450 T451
sub T452 T452 1
goto L36_pos
@label L36_neg
div T450 T450 T451
add T452 T452 1
neq test T452 0
goif L36_neg test
@label L36_end
div f8 f7 T450
add f9 f6 f8
assignw BASE[4] f9
goto B1033
@label B1033
assignb T453 True
goto Bool1036
assignb T453 False
@label Bool1036
assignw lastbase BASE
return T453
@label Function8_end
assignw lastbase BASE
return 0
@endfunction 36
@function Function9 32
@label L37
assignw T455 0
assignw T456 BASE[4]
eq test T456 T455
goif B1050 test
goto B1063
@label B1050
assignw T457 0
assignw T458 BASE[0]
mult T459 1 T457
add T459 T459 4
assignb T460 48
assignb T458[T459] T460
assignw T461 1
assignw T462 BASE[0]
mult T463 1 T461
add T463 T463 4
assignb T464 0
assignb T462[T463] T464
goto B1063
@label B1063
assignw T465 0
assignw BASE[16] T465
assignw T467 BASE[0]
assignw T468 T467[0]
assignw T469 1
mult T469 T469 T468
add T469 T469 4
malloc T466 T469
memcpy T466 T467 T469
param T470 0
assignw T470[0] T466
assignb A1[0] 0
call T471 Function0 2
assignw T472 T471
assignw T473 BASE[20]
assignw T474 1
mult T474 T474 T472
add T474 T474 4
malloc T473 T474
assignw T473[0] T472
assignw T473[0] T473
assignw T475 T471
assignw T476 BASE[24]
assignw T477 1
mult T477 T477 T475
add T477 T477 4
malloc T476 T477
assignw T476[0] T475
assignw T476[0] T476
assignw T478 0
assignw T479 BASE[4]
lt test T479 T478
goif B1097 test
goto B1101
@label B1097
assignw T481 BASE[4]
minus T480 T481
assignw BASE[8] T480
goto B1103
@label B1101
assignw T482 BASE[4]
assignw BASE[8] T482
@label B1103
@label L38
assignw T483 0
assignw T484 BASE[8]
gt test T484 T483
goif B1109 test
goto B1130
@label B1109
assignw T485 BASE[20]
assignw T486 BASE[16]
mult T487 1 T486
add T487 T487 4
assignw T488 10
assignw T490 BASE[8]
mod T489 T490 T488
assignb T491 48
param T492 0
assignb T492[0] T491
call T493 CTOI 1
add T494 T489 T493
param T495 0
assignw T495[0] T494
call T496 ITOC 1
assignb T485[T487] T496
assignw T497 10
assignw T499 BASE[8]
div T498 T499 T497
assignw BASE[8] T498
goto L38
@label B1130
assignw T500 BASE[24]
param T501 0
assignw T501[0] T500
assignw T503 BASE[20]
assignw T504 T503[0]
assignw T505 1
mult T505 T505 T504
add T505 T505 4
malloc T502 T505
memcpy T502 T503 T505
param T506 4
assignw T506[0] T502
call T507 Function3 2
assignw T508 0
assignw T509 BASE[4]
lt test T509 T508
goif B1148 test
goto B1208
@label B1148
assignw S1[0] 1
assignw T511 2
assignw T512 T511
assignw T513 BASE[28]
assignw T514 4
mult T514 T514 T512
add T514 T514 4
malloc T513 T514
assignw T513[0] T512
assignw T513[0] T513
@label L39
sub T514 T514 4
lt test T514 0
goif L39_end test
assignw T515 T471
assignw T516 T513[T514]
assignw T517 1
mult T517 T517 T515
add T517 T517 4
malloc T516 T517
assignw T516[0] T515
assignw T516[0] T516
goto L39
@label L39_end
assignw T518 BASE[28]
assignw T519 BASE[24]
assignw T518[8] T519
assignw T518[4] S1
assignw T520 2
assignw T522 BASE[28]
assignw T523 T522[0]
assignw T524 4
mult T524 T524 T523
add T524 T524 4
malloc T521 T524
assignw T525 T524
@label L40
sub T525 T525 4
lt test T525 0
goif L40_end test
assignw T526 T522[T525]
assignw T527 T521[T525]
assignw T528 T526[0]
assignw T529 1
mult T529 T529 T528
add T529 T529 4
malloc T527 T529
assignw T527[0] T527
memcpy T527 T526 T529
goto L40
@label L40_end
param T530 0
assignw T530[0] T521
param T531 4
assignw T531[0] T520
assignw T532 BASE[0]
param T533 8
assignw T533[0] T532
call T534 Function4 3
goto Function9_end
@label B1208
assignw T535 BASE[0]
param T536 0
assignw T536[0] T535
assignw T538 BASE[24]
assignw T539 T538[0]
assignw T540 1
mult T540 T540 T539
add T540 T540 4
malloc T537 T540
memcpy T537 T538 T540
param T541 4
assignw T541[0] T537
call T542 Function2 2
@label Function9_end
assignw lastbase BASE
return 0
@endfunction 32
@function Function10 32
assignw T545 BASE[0]
assignw T546 T545[0]
assignw T547 1
mult T547 T547 T546
add T547 T547 4
malloc T544 T547
memcpy T544 T545 T547
param T548 0
assignw T548[0] T544
assignb A1[0] 0
call T549 Function0 2
assignw T550 T549
assignw T551 BASE[20]
assignw T552 1
mult T552 T552 T550
add T552 T552 4
malloc T551 T552
assignw T551[0] T550
assignw T551[0] T551
assignw T553 T549
assignw T554 BASE[24]
assignw T555 1
mult T555 T555 T553
add T555 T555 4
malloc T554 T555
assignw T554[0] T553
assignw T554[0] T554
assignw f10 BASE[4]
param T556 0
assignw T556[0] f10
call T557 FTOI 1
assignw BASE[8] T557
assignw f12 BASE[4]
assignw T558 BASE[8]
sub f11 f12 T558
assignw BASE[16] f11
@label L41
@label L42
assignw f13 BASE[16]
param T559 0
assignw T559[0] f13
call T560 FTOI 1
assignw T561 BASE[16]
neq test T561 T560
goif B1272 test
goto B1277
@label B1272
assignw T562 10
assignw f15 BASE[16]
mult f14 f15 T562
assignw BASE[16] f14
goto L41
@label B1277
assignw f16 BASE[16]
param T563 0
assignw T563[0] f16
call T564 FTOI 1
assignw BASE[12] T564
assignw T565 BASE[20]
param T566 0
assignw T566[0] T565
assignw T567 BASE[8]
param T568 4
assignw T568[0] T567
call T569 Function9 2
assignw T570 BASE[24]
param T571 0
assignw T571[0] T570
assignw T572 BASE[12]
param T573 4
assignw T573[0] T572
call T574 Function9 2
assignw S2[0] 1
assignw T576 3
assignw T577 T576
assignw T578 BASE[28]
assignw T579 4
mult T579 T579 T577
add T579 T579 4
malloc T578 T579
assignw T578[0] T577
assignw T578[0] T578
@label L43
sub T579 T579 4
lt test T579 0
goif L43_end test
assignw T580 T549
assignw T581 T578[T579]
assignw T582 1
mult T582 T582 T580
add T582 T582 4
malloc T581 T582
assignw T581[0] T580
assignw T581[0] T581
goto L43
@label L43_end
assignw T583 BASE[28]
assignw T584 BASE[24]
assignw T583[12] T584
assignw T583[8] S2
assignw T585 BASE[20]
assignw T583[4] T585
assignw T586 3
assignw T588 BASE[28]
assignw T589 T588[0]
assignw T590 4
mult T590 T590 T589
add T590 T590 4
malloc T587 T590
assignw T591 T590
@label L44
sub T591 T591 4
lt test T591 0
goif L44_end test
assignw T592 T588[T591]
assignw T593 T587[T591]
assignw T594 T592[0]
assignw T595 1
mult T595 T595 T594
add T595 T595 4
malloc T593 T595
assignw T593[0] T593
memcpy T593 T592 T595
goto L44
@label L44_end
param T596 0
assignw T596[0] T587
param T597 4
assignw T597[0] T586
assignw T598 BASE[0]
param T599 8
assignw T599[0] T598
call T600 Function4 3
@label Function10_end
assignw lastbase BASE
return 0
@endfunction 32
assignw T602 20
assignw T604 T602
assignw T605 8
mult T605 T605 T604
add T605 T605 4
malloc T603 T605
assignw T603[0] T604
@label L45
sub T605 T605 8
lt test T605 0
goif L45_end test
assignw T606 T603[T605]
malloc T606 8
assignw T606[0] T606
assignw T607 T606[4]
malloc T607 4
assignw T607[0] T607
goto L45
@label L45_end
@label L46
goto B1382
@label B1382
assignw S3[0] 35
param T612 0
assignw T612[0] S3
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T613 PRINT 6
call T614 READC 0
assignb T610 T614
@label L47
assignb T615 110
eq test T610 T615
goif B1403 test
goto B1398
@label B1398
@label L48
assignb T616 78
eq test T610 T616
goif B1403 test
goto B1414
@label B1403
assignw S4[0] 12
param T618 0
assignw T618[0] S4
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T619 PRINT 6
goto B1838
goto B1414
@label B1414
assignw S5[0] 42
param T621 0
assignw T621[0] S5
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T622 PRINT 6
call T623 READI 0
assignw T608 T623
assignw T624 20
gt test T608 T624
goif B1429 test
goto B1440
@label B1429
assignw S6[0] 41
param T626 0
assignw T626[0] S6
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T627 PRINT 6
goto L46
goto B1440
@label B1440
assignw T628 0
assignw T609 T628
@label L49
lt test T609 T608
goif B1446 test
goto B1617
@label B1446
assignw S7[0] 27
param T630 0
assignw T630[0] S7
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T631 PRINT 6
assignw S8[0] 11
param T633 0
assignw T633[0] S8
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T634 PRINT 6
assignw S9[0] 11
param T636 0
assignw T636[0] S9
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T637 PRINT 6
assignw S10[0] 9
param T639 0
assignw T639[0] S10
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T640 PRINT 6
assignw S11[0] 20
param T642 0
assignw T642[0] S11
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T643 PRINT 6
call T644 READI 0
assignw T608 T644
mult T645 8 T609
add T645 T645 4
assignw T646 T603[T645]
assignw T646[0] T608
@label L50
assignw T647 1
eq test T608 T647
goif B1502 test
goto B1538
@label B1502
assignw S12[0] 34
param T649 0
assignw T649[0] S12
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T650 PRINT 6
@label L51
call T651 READC 0
eq test T610 T651
goif B1516 test
goto B1516
@label B1516
mult T652 8 T609
add T652 T652 4
assignw T653 T603[T652]
assignw T654 T653[4]
assignb T655 T654[0]


@label L52
assignb T656 110
neq test T610 T656
goif B1528 test
goto B1535
@label B1528
@label L53
assignb T657 78
neq test T610 T657
goif B1533 test
goto B1535
@label B1533
assignb T654[0] True
goto Bool1536
@label B1535
assignb T654[0] False
@label Bool1536
goto B1613
@label B1538
@label L54
assignw T658 2
eq test T608 T658
goif B1543 test
goto B1559
@label B1543
assignw S13[0] 21
param T660 0
assignw T660[0] S13
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T661 PRINT 6
mult T662 8 T609
add T662 T662 4
assignw T663 T603[T662]
assignw T664 T663[4]
call T665 READC 0
assignb T664[0] T665
goto B1613
@label B1559
@label L55
assignw T666 3
eq test T608 T666
goif B1564 test
goto B1580
@label B1564
assignw S14[0] 19
param T668 0
assignw T668[0] S14
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T669 PRINT 6
mult T670 8 T609
add T670 T670 4
assignw T671 T603[T670]
assignw T672 T671[4]
call T673 READI 0
assignw T672[0] T673
goto B1613
@label B1580
@label L56
assignw T674 4
eq test T608 T674
goif B1585 test
goto B1601
@label B1585
assignw S15[0] 21
param T676 0
assignw T676[0] S15
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T677 PRINT 6
mult T678 8 T609
add T678 T678 4
assignw T679 T603[T678]
assignw T680 T679[4]
call f17 READF 0
assignw T680[0] f17
goto B1613
@label B1601
assignw S16[0] 13
param T682 0
assignw T682[0] S16
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T683 PRINT 6
assignw T684 1
sub T685 T609 T684
assignw T609 T685
@label B1613
assignw T686 1
add T687 T609 T686
assignw T609 T687
goto L49
@label B1617
assignw T689 T603[0]
assignw T690 8
mult T690 T690 T689
add T690 T690 4
malloc T688 T690
assignw T691 T690
@label L57
sub T691 T691 8
lt test T691 0
goif L57_end test
assignw T692 T688[T691]
malloc T692 8
assignw T692[0] T692
assignw T693 T603[T691]
memcpy T692 T693 8
assignw T694 T692[4]
malloc T694 4
assignw T694[0] T694
assignw T695 T693[4]
memcpy T694 T695 4
goto L57
@label L57_end
param T696 0
assignw T696[0] T688
param T697 4
assignw T697[0] T608
call T698 Function11  2
assignw S17[0] 35
assignb T700 10
assignw T701 1
assignw T703 T701
assignw T704 1
mult T704 T704 T703
add T704 T704 4
malloc T702 T704
assignw T702[0] T703
assignb T702[4] T700
param T705 0
assignw T705[0] S17
assignw T707 T702[0]
assignw T708 1
mult T708 T708 T707
add T708 T708 4
malloc T706 T708
memcpy T706 T702 T708
param T709 4
assignw T709[0] T706
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T710 PRINT 6
assignw T711 0
assignw T713 T711
@label L58
geq test T713 T608
goif L58_end test
assignw T712 T713
mult T714 8 T712
add T714 T714 4
assignw T715 T603[T714]
@label L59
assignw T716 1
assignw T717 T715[0]
eq test T717 T716
goif B1685 test
goto B1724
@label B1685
assignw S18[0] 6
assignw S19[0] 0
param T720 0
assignw T720[0] S18
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
param T721 20
assignw T721[0] S19
assignb A0[4] 1
call T722 PRINT 6
mult T723 8 T712
add T723 T723 4
assignw T724 T603[T723]
assignw T725 T724[4]
assignb T726 T725[0]
goif B1704 T726
goto B1714
@label B1704
assignw S20[0] 4
param T728 0
assignw T728[0] S20
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T729 PRINT 6
goto B1714
@label B1714
assignw S21[0] 5
param T731 0
assignw T731[0] S21
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T732 PRINT 6
goto B1834
@label B1724
mult T733 8 T712
add T733 T733 4
assignw T734 T603[T733]
@label L60
assignw T735 2
assignw T736 T734[0]
eq test T736 T735
goif B1733 test
goto B1764
@label B1733
assignw S22[0] 8
mult T738 8 T712
add T738 T738 4
assignw T739 T603[T738]
assignw T740 T739[4]
assignw T741 1
assignw T743 T741
assignw T744 1
mult T744 T744 T743
add T744 T744 4
malloc T742 T744
assignw T742[0] T743
assignb T745 T740[0]
assignb T742[4] T745
param T746 0
assignw T746[0] S22
assignw T748 T742[0]
assignw T749 1
mult T749 T749 T748
add T749 T749 4
malloc T747 T749
memcpy T747 T742 T749
param T750 4
assignw T750[0] T747
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T751 PRINT 6
goto B1834
@label B1764
mult T752 8 T712
add T752 T752 4
assignw T753 T603[T752]
@label L61
assignw T754 3
assignw T755 T753[0]
eq test T755 T754
goif B1773 test
goto B1804
@label B1773
assignw S23[0] 7
mult T757 8 T712
add T757 T757 4
assignw T758 T603[T757]
assignw T759 T758[4]
assignw T760 1
assignw T762 T760
assignw T763 4
mult T763 T763 T762
add T763 T763 4
malloc T761 T763
assignw T761[0] T762
assignw T764 T759[0]
assignw T761[4] T764
param T765 0
assignw T765[0] S23
assignb A0[0] 0
assignw T767 T761[0]
assignw T768 4
mult T768 T768 T767
add T768 T768 4
malloc T766 T768
memcpy T766 T761 T768
param T769 8
assignw T769[0] T766
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T770 PRINT 6
goto B1834
@label B1804
assignw S24[0] 9
mult T772 8 T712
add T772 T772 4
assignw T773 T603[T772]
assignw T774 T773[4]
assignw T775 1
assignw T777 T775
assignw T778 4
mult T778 T778 T777
add T778 T778 4
malloc T776 T778
assignw T776[0] T777
assignw f18 T774[0]
assignw T776[4] f18
param T779 0
assignw T779[0] S24
assignb A0[0] 0
assignb A0[1] 0
assignw T781 T776[0]
assignw T782 4
mult T782 T782 T781
add T782 T782 4
malloc T780 T782
memcpy T780 T776 T782
param T783 12
assignw T783[0] T780
assignb A0[2] 1
assignb A0[3] 0
assignb A0[4] 0
call T784 PRINT 6
@label B1834
add T713 T713 1
goto L58
@label L58_end
goto L46
@label B1838
@function Function11 24
assignw T786 0
assignw T787 0
assignw T788 1
assignw T790 BASE[4]
sub T789 T790 T788
assignw BASE[8] T786
assignw BASE[12] T787
assignw BASE[16] T789
assignw T791 BASE[20]
malloc T791 8
assignw T791[0] T791
assignw T792 T791[4]
malloc T792 4
assignw T792[0] T792
@label L62
assignw T793 BASE[12]
assignw T794 BASE[16]
leq test T793 T794
goif B1859 test
goto B1944
@label B1859
assignw T795 BASE[0]
assignw T796 BASE[12]
mult T797 8 T796
add T797 T797 4
assignw T798 T795[T797]
@label L63
assignw T799 1
assignw T800 T798[0]
eq test T800 T799
goif B1870 test
goto B1901
@label B1870
assignw T801 BASE[0]
assignw T802 BASE[12]
mult T803 8 T802
add T803 T803 4
assignw T804 T801[T803]
assignw BASE[20] T804
assignw T805 BASE[0]
assignw T806 BASE[12]
mult T807 8 T806
add T807 T807 4
assignw T808 BASE[0]
assignw T809 BASE[8]
mult T810 8 T809
add T810 T810 4
assignw T811 T808[T810]
assignw T805[T807] T811
assignw T812 BASE[0]
assignw T813 BASE[8]
mult T814 8 T813
add T814 T814 4
assignw T815 BASE[20]
assignw T812[T814] T815
assignw T816 1
assignw T818 BASE[8]
add T817 T818 T816
assignw BASE[8] T817
assignw T819 1
assignw T821 BASE[12]
add T820 T821 T819
assignw BASE[12] T820
goto L62
@label B1901
assignw T822 BASE[0]
assignw T823 BASE[12]
mult T824 8 T823
add T824 T824 4
assignw T825 T822[T824]
@label L64
assignw T826 4
assignw T827 T825[0]
eq test T827 T826
goif B1912 test
goto B1939
@label B1912
assignw T828 BASE[0]
assignw T829 BASE[12]
mult T830 8 T829
add T830 T830 4
assignw T831 T828[T830]
assignw BASE[20] T831
assignw T832 BASE[0]
assignw T833 BASE[12]
mult T834 8 T833
add T834 T834 4
assignw T835 BASE[0]
assignw T836 BASE[16]
mult T837 8 T836
add T837 T837 4
assignw T838 T835[T837]
assignw T832[T834] T838
assignw T839 BASE[0]
assignw T840 BASE[16]
mult T841 8 T840
add T841 T841 4
assignw T842 BASE[20]
assignw T839[T841] T842
assignw T843 1
assignw T845 BASE[16]
sub T844 T845 T843
assignw BASE[16] T844
goto L62
@label B1939
assignw T846 1
assignw T848 BASE[12]
add T847 T848 T846
assignw BASE[12] T847
goto L62
@label B1944
@label L65
assignw T849 BASE[8]
assignw T850 BASE[16]
leq test T849 T850
goif B1950 test
goto Function11_end
@label B1950
assignw T851 BASE[0]
assignw T852 BASE[8]
mult T853 8 T852
add T853 T853 4
assignw T854 T851[T853]
@label L66
assignw T855 2
assignw T856 T854[0]
eq test T856 T855
goif B1961 test
goto B1966
@label B1961
assignw T857 1
assignw T859 BASE[8]
add T858 T859 T857
assignw BASE[8] T858
goto L65
@label B1966
assignw T860 BASE[0]
assignw T861 BASE[8]
mult T862 8 T861
add T862 T862 4
assignw T863 T860[T862]
assignw BASE[20] T863
assignw T864 BASE[0]
assignw T865 BASE[8]
mult T866 8 T865
add T866 T866 4
assignw T867 BASE[0]
assignw T868 BASE[16]
mult T869 8 T868
add T869 T869 4
assignw T870 T867[T869]
assignw T864[T866] T870
assignw T871 BASE[0]
assignw T872 BASE[16]
mult T873 8 T872
add T873 T873 4
assignw T874 BASE[20]
assignw T871[T873] T874
assignw T875 1
assignw T877 BASE[16]
sub T876 T877 T875
assignw BASE[16] T876
goto L65
@label Function11_end
assignw lastbase BASE
return 0
@endfunction 24
