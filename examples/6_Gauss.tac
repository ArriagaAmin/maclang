@string S0 "0000\n"
@string S1 "0000-"
@string S2 "0000."
@string S3 "0000Desea resolver un sistema de ecuaciones? [Y/n] "
@string S4 "0000Hasta luego!"
@string S5 "0000Indique el numero de ecuaciones. Debe ser entre 1 y 10: "
@string S6 "0000Indique los %i coeficientes flotantes de la %i-esima ecuacion:"
@string S7 "0000El valor de las variables es: "
@string S8 "0000X%i = %f"
@string S9 "0000El sistema de ecuaciones no tiene solucion."
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
assignb T34 0
@function Function0 12
assignw T35 0
assignw BASE[8] T35
@label L6
assignw T36 BASE[0]
assignw T37 BASE[8]
mult T38 1 T37
add T38 T38 4
@label L7
assignb T39 T36[T38]
assignb T40 BASE[4]
neq test T39 T40
goif B129 test
goto B134
@label B129
assignw T41 1
assignw T43 BASE[8]
add T42 T43 T41
assignw BASE[8] T42
goto L6
@label B134
assignw T44 BASE[8]
assignw lastbase BASE
return T44
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function1 12
assignw T47 0
assignw BASE[8] T47
@label L8
assignw T48 BASE[0]
assignw T49 BASE[8]
mult T50 1 T49
add T50 T50 4
@label L9
assignb T51 0
assignb T52 T48[T50]
neq test T52 T51
goif B155 test
goto B174
@label B155
assignw T53 BASE[0]
assignw T54 BASE[8]
mult T55 1 T54
add T55 T55 4
@label L10
assignw T56 BASE[4]
assignw T57 BASE[8]
mult T58 1 T57
add T58 T58 4
assignb T59 T53[T55]
assignb T60 T56[T58]
eq test T59 T60
goif B169 test
goto B174
@label B169
assignw T61 1
assignw T63 BASE[8]
add T62 T63 T61
assignw BASE[8] T62
goto L8
@label B174
assignw T64 BASE[0]
assignw T65 BASE[8]
mult T66 1 T65
add T66 T66 4
assignw T67 BASE[4]
assignw T68 BASE[8]
mult T69 1 T68
add T69 T69 4
assignw T70 T64[T66]
assignw T71 T67[T69]
gt test T70 T71
goif B187 test
goto B191
@label B187
assignw T72 1
assignw lastbase BASE
return T72
goto Function1_end
@label B191
assignw T73 BASE[4]
assignw T74 BASE[8]
mult T75 1 T74
add T75 T75 4
assignw T76 BASE[0]
assignw T77 BASE[8]
mult T78 1 T77
add T78 T78 4
assignw T79 T73[T75]
assignw T80 T76[T78]
gt test T79 T80
goif B204 test
goto B209
@label B204
assignw T81 1
minus T82 T81
assignw lastbase BASE
return T82
goto Function1_end
@label B209
assignw T83 0
assignw lastbase BASE
return T83
@label Function1_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function2 16
assignw T87 BASE[4]
assignw T88 T87[0]
assignw T89 1
mult T89 T89 T88
add T89 T89 4
malloc T86 T89
memcpy T86 T87 T89
param T90 0
assignw T90[0] T86
param T91 4
assignb T91[0] T34
call T92 Function0 2
assignw T93 1
add T94 T92 T93
assignw BASE[8] T94
assignw T95 0
assignw BASE[12] T95
@label L11
assignw T96 BASE[12]
assignw T97 BASE[8]
lt test T96 T97
goif B240 test
goto Function2_end
@label B240
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
goto L11
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
param T115 4
assignb T115[0] T34
call T116 Function0 2
assignw BASE[8] T116
assignw T117 0
assignw T119 T117
@label L12
assignw T120 BASE[8]
geq test T119 T120
goif L12_end test
assignw T118 T119
assignw T122 BASE[8]
assignw T123 BASE[12]
sub T121 T122 T123
assignw T124 1
sub T125 T121 T124
assignw T126 BASE[0]
mult T127 1 T125
add T127 T127 4
assignw T128 BASE[4]
assignw T129 BASE[12]
mult T130 1 T129
add T130 T130 4
assignb T131 T128[T130]
assignb T126[T127] T131
add T119 T119 1
goto L12
@label L12_end
@label Function3_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function4 28
assignw T135 0
assignw T136 0
assignw BASE[12] T135
assignw BASE[16] T136
@label L13
assignw T137 BASE[12]
assignw T138 BASE[4]
lt test T137 T138
goif B312 test
goto B365
@label B312
assignw T139 BASE[0]
assignw T140 BASE[12]
mult T141 4 T140
add T141 T141 4
assignw T143 T139[T141]
assignw T144 T143[0]
assignw T145 1
mult T145 T145 T144
add T145 T145 4
malloc T142 T145
memcpy T142 T143 T145
param T146 0
assignw T146[0] T142
param T147 4
assignb T147[0] T34
call T148 Function0 2
assignw BASE[24] T148
assignw T149 0
assignw BASE[20] T149
@label L14
assignw T150 BASE[20]
assignw T151 BASE[24]
lt test T150 T151
goif B337 test
goto B360
@label B337
assignw T152 BASE[8]
assignw T153 BASE[16]
mult T154 1 T153
add T154 T154 4
assignw T155 BASE[0]
assignw T156 BASE[12]
mult T157 4 T156
add T157 T157 4
assignw T158 T155[T157]
assignw T159 BASE[20]
mult T160 1 T159
add T160 T160 4
assignb T161 T158[T160]
assignb T152[T154] T161
assignw T162 1
assignw T164 BASE[20]
add T163 T164 T162
assignw BASE[20] T163
assignw T165 1
assignw T167 BASE[16]
add T166 T167 T165
assignw BASE[16] T166
goto L14
@label B360
assignw T168 1
assignw T170 BASE[12]
add T169 T170 T168
assignw BASE[12] T169
goto L13
@label B365
assignw T171 BASE[8]
assignw T172 BASE[16]
mult T173 1 T172
add T173 T173 4
assignb T174 0
assignb T171[T173] T174
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function5 29
assignw T178 0
assignw T179 0
assignw T180 0
assignw T182 BASE[0]
assignw T183 T182[0]
assignw T184 1
mult T184 T184 T183
add T184 T184 4
malloc T181 T184
memcpy T181 T182 T184
param T185 0
assignw T185[0] T181
param T186 4
assignb T186[0] T34
call T187 Function0 2
assignw BASE[12] T178
assignw BASE[16] T179
assignw BASE[20] T180
assignw BASE[24] T187
goto B396
@label B396
assignb BASE[28] True
goto Bool399
assignb BASE[28] False
@label Bool399
@label L15
assignw T188 BASE[0]
assignw T189 BASE[12]
mult T190 1 T189
add T190 T190 4
@label L16
assignb T191 0
assignb T192 T188[T190]
neq test T192 T191
goif B411 test
goto B491
@label B411
assignw T193 BASE[0]
assignw T194 BASE[12]
mult T195 1 T194
add T195 T195 4
@label L17
assignb T196 T193[T195]
assignb T197 BASE[8]
eq test T196 T197
goif B421 test
goto B449
@label B421
assignb T198 BASE[28]
goif B449 T198
goto B424
@label B424
assignb T199 BASE[28]


goto B428
@label B428
assignb BASE[28] True
goto Bool431
assignb BASE[28] False
@label Bool431
assignw T200 BASE[4]
assignw T201 BASE[20]
mult T202 4 T201
add T202 T202 4
assignw T203 T200[T202]
assignw T204 BASE[16]
mult T205 1 T204
add T205 T205 4
assignb T206 0
assignb T203[T205] T206
assignw T207 1
assignw T209 BASE[20]
add T208 T209 T207
assignw BASE[20] T208
assignw T210 0
assignw BASE[16] T210
goto B486
@label B449
assignw T211 BASE[0]
assignw T212 BASE[12]
mult T213 1 T212
add T213 T213 4
@label L18
assignb T214 T211[T213]
assignb T215 BASE[8]
neq test T214 T215
goif B459 test
goto B486
@label B459
assignb T216 BASE[28]


goto B465
assignb BASE[28] True
goto Bool466
@label B465
assignb BASE[28] False
@label Bool466
assignw T217 BASE[4]
assignw T218 BASE[20]
mult T219 4 T218
add T219 T219 4
assignw T220 T217[T219]
assignw T221 BASE[16]
mult T222 1 T221
add T222 T222 4
assignw T223 BASE[0]
assignw T224 BASE[12]
mult T225 1 T224
add T225 T225 4
assignb T226 T223[T225]
assignb T220[T222] T226
assignw T227 1
assignw T229 BASE[16]
add T228 T229 T227
assignw BASE[16] T228
goto B486
@label B486
assignw T230 1
assignw T232 BASE[12]
add T231 T232 T230
assignw BASE[12] T231
goto L15
@label B491
assignb T233 BASE[28]
goif B509 T233
goto B494
@label B494
assignw T234 BASE[4]
assignw T235 BASE[20]
mult T236 4 T235
add T236 T236 4
assignw T237 T234[T236]
assignw T238 BASE[16]
mult T239 1 T238
add T239 T239 4
assignb T240 0
assignb T237[T239] T240
assignw T241 1
assignw T243 BASE[20]
add T242 T243 T241
assignw BASE[20] T242
goto B509
@label B509
assignw T244 BASE[20]
assignw lastbase BASE
return T244
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 29
@function Function6 16
goto B521
goto B525
assignb BASE[4] True
goto Bool522
@label B521
assignb BASE[4] False
@label Bool522
assignb BASE[5] True
goto Bool526
@label B525
assignb BASE[5] False
@label Bool526
assignw T247 BASE[0]
assignw T248 T247[0]
assignw T249 1
mult T249 T249 T248
add T249 T249 4
malloc T246 T249
memcpy T246 T247 T249
param T250 0
assignw T250[0] T246
param T251 4
assignb T251[0] T34
call T252 Function0 2
assignw T253 0
assignw BASE[8] T252
assignw BASE[12] T253
@label L19
assignw T254 BASE[12]
assignw T255 BASE[8]
lt test T254 T255
goif B548 test
goto B634
@label B548
assignw T256 BASE[0]
assignw T257 BASE[12]
mult T258 1 T257
add T258 T258 4
@label L20
assignb T259 46
assignb T260 T256[T258]
eq test T260 T259
goif B558 test
goto B570
@label B558
assignb T261 BASE[4]
goif B570 T261
goto B561
@label B561
assignb T262 BASE[4]


goto B565
@label B565
assignb BASE[4] True
goto Bool568
assignb BASE[4] False
@label Bool568
goto B629
@label B570
assignw T263 BASE[0]
assignw T264 BASE[12]
mult T265 1 T264
add T265 T265 4
@label L21
assignb T266 46
assignb T267 T263[T265]
eq test T267 T266
goif B580 test
goto B588
@label B580
goto B583
assignb T268 True
goto Bool584
@label B583
assignb T268 False
@label Bool584
assignw lastbase BASE
return T268
goto B629
@label B588
assignw T269 BASE[0]
assignw T270 BASE[12]
mult T271 1 T270
add T271 T271 4
assignb T272 48
assignw T273 T269[T271]
lt test T273 T272
goif B606 test
goto B597
@label B597
assignw T274 BASE[0]
assignw T275 BASE[12]
mult T276 1 T275
add T276 T276 4
assignb T277 57
assignw T278 T274[T276]
gt test T278 T277
goif B606 test
goto B614
@label B606
goto B609
assignb T279 True
goto Bool610
@label B609
assignb T279 False
@label Bool610
assignw lastbase BASE
return T279
goto B629
@label B614
assignb T280 BASE[4]
goif B617 T280
goto B629
@label B617
assignb T281 BASE[5]
goif B629 T281
goto B620
@label B620
assignb T282 BASE[5]


goto B624
@label B624
assignb BASE[5] True
goto Bool627
assignb BASE[5] False
@label Bool627
goto B629
@label B629
assignw T283 1
assignw T285 BASE[12]
add T284 T285 T283
assignw BASE[12] T284
goto L19
@label B634
assignb T286 BASE[4]
goif B637 T286
goto B642
@label B637
assignb T287 BASE[5]
goif B640 T287
goto B642
@label B640
assignb T288 True
goto Bool643
@label B642
assignb T288 False
@label Bool643
assignw lastbase BASE
return T288
@label Function6_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function7 24
assignw T291 BASE[0]
assignw T292 T291[0]
assignw T293 1
mult T293 T293 T292
add T293 T293 4
malloc T290 T293
memcpy T290 T291 T293
param T294 0
assignw T294[0] T290
param T295 4
assignb T295[0] T34
call T296 Function0 2
assignw BASE[8] T296
assignw T297 0
assignw BASE[4] T297
@label L22
assignw T298 0
assignw T299 BASE[8]
eq test T299 T298
goif B688 test
goto B672
@label B672
assignw T300 0
assignw T301 BASE[0]
mult T302 1 T300
add T302 T302 4
@label L23
assignb T303 45
assignb T304 T301[T302]
eq test T304 T303
goif B682 test
goto B696
@label B682
@label L24
assignw T305 1
assignw T306 BASE[8]
eq test T306 T305
goif B688 test
goto B696
@label B688
goto B691
assignb T307 True
goto Bool692
@label B691
assignb T307 False
@label Bool692
assignw lastbase BASE
return T307
goto B716
@label B696
assignw T308 0
assignw T309 BASE[0]
mult T310 1 T308
add T310 T310 4
@label L25
assignb T311 45
assignb T312 T309[T310]
eq test T312 T311
goif B706 test
goto B712
@label B706
assignw T313 1
minus T314 T313
assignw BASE[16] T314
assignw T315 1
assignw BASE[12] T315
goto B716
@label B712
assignw T316 1
assignw BASE[16] T316
assignw T317 0
assignw BASE[12] T317
@label B716
assignw T318 1
assignw T320 BASE[8]
sub T319 T320 T318
assignw T321 1
assignw T323 BASE[12]
sub T322 T323 T321
assignw T324 1
minus T325 T324
assignw T327 T319
@label L26
lt test T325 0
goif L26_neg test
geq test T327 T322
goif L26_end test
goto L26_body
@label L26_neg
leq test T327 T322
goif L26_end test
@label L26_body
assignw T326 T327
assignw T328 BASE[0]
assignw T329 BASE[20]
mult T330 1 T329
add T330 T330 4
assignb T331 48
assignw T332 T328[T330]
lt test T332 T331
goif B754 test
goto B745
@label B745
assignw T333 BASE[0]
assignw T334 BASE[20]
mult T335 1 T334
add T335 T335 4
assignb T336 57
assignw T337 T333[T335]
gt test T337 T336
goif B754 test
goto B764
@label B754
assignw T338 0
assignw BASE[4] T338
goto B759
assignb T339 True
goto Bool760
@label B759
assignb T339 False
@label Bool760
assignw lastbase BASE
return T339
goto B764
@label B764
assignw T340 BASE[0]
assignw T341 BASE[20]
mult T342 1 T341
add T342 T342 4
assignb T343 T340[T342]
param T344 0
assignb T344[0] T343
call T345 CTOI 1
assignb T346 48
param T347 0
assignb T347[0] T346
call T348 CTOI 1
sub T349 T345 T348
assignw T351 BASE[16]
mult T350 T351 T349
assignw T353 BASE[4]
add T352 T353 T350
assignw BASE[4] T352
assignw T354 10
assignw T356 BASE[16]
mult T355 T356 T354
assignw BASE[16] T355
add T327 T327 T325
goto L26
@label L26_end
goto B790
@label B790
assignb T357 True
goto Bool793
assignb T357 False
@label Bool793
assignw lastbase BASE
return T357
@label Function7_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function8 36
assignw T360 BASE[0]
assignw T361 T360[0]
assignw T362 1
mult T362 T362 T361
add T362 T362 4
malloc T359 T362
memcpy T359 T360 T362
param T363 0
assignw T363[0] T359
param T364 4
assignb T364[0] T34
call T365 Function0 2
assignw BASE[8] T365
assignw T366 BASE[8]
assignw T367 BASE[12]
assignw T368 1
mult T368 T368 T366
add T368 T368 4
malloc T367 T368
assignw T367[0] T366
assignw T367[0] T367
assignw T369 BASE[8]
assignw T370 BASE[16]
assignw T371 1
mult T371 T371 T369
add T371 T371 4
malloc T370 T371
assignw T370[0] T369
assignw T370[0] T370
assignw T372 0
assignw BASE[32] T372
@label L27
assignw T373 BASE[0]
assignw T374 BASE[32]
mult T375 1 T374
add T375 T375 4
@label L28
assignb T376 46
assignb T377 T373[T375]
neq test T377 T376
goif B843 test
goto B868
@label B843
assignw T378 BASE[0]
assignw T379 BASE[32]
mult T380 1 T379
add T380 T380 4
@label L29
assignb T381 0
assignb T382 T378[T380]
neq test T382 T381
goif B853 test
goto B868
@label B853
assignw T383 BASE[12]
assignw T384 BASE[32]
mult T385 1 T384
add T385 T385 4
assignw T386 BASE[0]
assignw T387 BASE[32]
mult T388 1 T387
add T388 T388 4
assignb T389 T386[T388]
assignb T383[T385] T389
assignw T390 1
assignw T392 BASE[32]
add T391 T392 T390
assignw BASE[32] T391
goto L27
@label B868
@label L30
assignw T393 0
assignw T394 BASE[32]
eq test T394 T393
goif B874 test
goto B877
@label B874
assignw T395 0
assignw BASE[24] T395
goto B902
@label B877
assignw T397 BASE[12]
assignw T398 T397[0]
assignw T399 1
mult T399 T399 T398
add T399 T399 4
malloc T396 T399
memcpy T396 T397 T399
param T400 0
assignw T400[0] T396
assignw T401 BASE[24]
param T402 4
assignw T402[0] T401
call T403 Function7 2
assignw T404 lastbase[4]
assignw BASE[24] T404
goif B902 T403
goto B894
@label B894
goto B897
assignb T405 True
goto Bool898
@label B897
assignb T405 False
@label Bool898
assignw lastbase BASE
return T405
goto B902
@label B902
assignw T406 BASE[0]
assignw T407 BASE[32]
mult T408 1 T407
add T408 T408 4
@label L31
assignb T409 0
assignb T410 T406[T408]
eq test T410 T409
goif B912 test
goto B925
@label B912
assignw T411 BASE[24]
param T412 0
assignw T412[0] T411
call f4 ITOF 1
assignw BASE[4] f4
goto B918
@label B918
assignb T413 True
goto Bool921
assignb T413 False
@label Bool921
assignw lastbase BASE
return T413
goto B925
@label B925
assignw T414 1
assignw T416 BASE[32]
add T415 T416 T414
assignw BASE[32] T415
assignw T417 0
assignw BASE[20] T417
@label L32
assignw T418 BASE[0]
assignw T419 BASE[32]
mult T420 1 T419
add T420 T420 4
@label L33
assignb T421 0
assignb T422 T418[T420]
neq test T422 T421
goif B942 test
goto B961
@label B942
assignw T423 BASE[16]
assignw T424 BASE[20]
mult T425 1 T424
add T425 T425 4
assignw T426 BASE[0]
assignw T427 BASE[32]
mult T428 1 T427
add T428 T428 4
assignb T429 T426[T428]
assignb T423[T425] T429
assignw T430 1
assignw T432 BASE[32]
add T431 T432 T430
assignw BASE[32] T431
assignw T433 1
assignw T435 BASE[20]
add T434 T435 T433
assignw BASE[20] T434
goto L32
@label B961
@label L34
assignw T436 0
assignw T437 BASE[20]
eq test T437 T436
goif B967 test
goto B980
@label B967
assignw T438 BASE[24]
param T439 0
assignw T439[0] T438
call f5 ITOF 1
assignw BASE[4] f5
goto B973
@label B973
assignb T440 True
goto Bool976
assignb T440 False
@label Bool976
assignw lastbase BASE
return T440
goto B1005
@label B980
assignw T442 BASE[16]
assignw T443 T442[0]
assignw T444 1
mult T444 T444 T443
add T444 T444 4
malloc T441 T444
memcpy T441 T442 T444
param T445 0
assignw T445[0] T441
assignw T446 BASE[28]
param T447 4
assignw T447[0] T446
call T448 Function7 2
assignw T449 lastbase[4]
assignw BASE[28] T449
goif B1005 T448
goto B997
@label B997
goto B1000
assignb T450 True
goto Bool1001
@label B1000
assignb T450 False
@label Bool1001
assignw lastbase BASE
return T450
goto B1005
@label B1005
assignw T451 BASE[24]
param T452 0
assignw T452[0] T451
call f6 ITOF 1
assignw T453 BASE[28]
param T454 0
assignw T454[0] T453
call f7 ITOF 1
assignw T455 10
assignw T457 T455
assignw T458 BASE[20]
assignw T456 1
lt test T458 0
goif L35_neg test
@label L35_pos
eq test T458 0
goif L35_end test
mult T456 T456 T457
sub T458 T458 1
goto L35_pos
@label L35_neg
div T456 T456 T457
add T458 T458 1
neq test T458 0
goif L35_neg test
@label L35_end
div f8 f7 T456
add f9 f6 f8
assignw BASE[4] f9
goto B1035
@label B1035
assignb T459 True
goto Bool1038
assignb T459 False
@label Bool1038
assignw lastbase BASE
return T459
@label Function8_end
assignw lastbase BASE
return 0
@endfunction 36
@function Function9 32
@label L36
assignw T461 0
assignw T462 BASE[4]
eq test T462 T461
goif B1052 test
goto B1065
@label B1052
assignw T463 0
assignw T464 BASE[0]
mult T465 1 T463
add T465 T465 4
assignb T466 48
assignb T464[T465] T466
assignw T467 1
assignw T468 BASE[0]
mult T469 1 T467
add T469 T469 4
assignb T470 0
assignb T468[T469] T470
goto B1065
@label B1065
assignw T471 0
assignw BASE[16] T471
assignw T473 BASE[0]
assignw T474 T473[0]
assignw T475 1
mult T475 T475 T474
add T475 T475 4
malloc T472 T475
memcpy T472 T473 T475
param T476 0
assignw T476[0] T472
param T477 4
assignb T477[0] T34
call T478 Function0 2
assignw T479 T478
assignw T480 BASE[20]
assignw T481 1
mult T481 T481 T479
add T481 T481 4
malloc T480 T481
assignw T480[0] T479
assignw T480[0] T480
assignw T482 T478
assignw T483 BASE[24]
assignw T484 1
mult T484 T484 T482
add T484 T484 4
malloc T483 T484
assignw T483[0] T482
assignw T483[0] T483
assignw T485 0
assignw T486 BASE[4]
lt test T486 T485
goif B1100 test
goto B1104
@label B1100
assignw T488 BASE[4]
minus T487 T488
assignw BASE[8] T487
goto B1106
@label B1104
assignw T489 BASE[4]
assignw BASE[8] T489
@label B1106
@label L37
assignw T490 0
assignw T491 BASE[8]
gt test T491 T490
goif B1112 test
goto B1133
@label B1112
assignw T492 BASE[20]
assignw T493 BASE[16]
mult T494 1 T493
add T494 T494 4
assignw T495 10
assignw T497 BASE[8]
mod T496 T497 T495
assignb T498 48
param T499 0
assignb T499[0] T498
call T500 CTOI 1
add T501 T496 T500
param T502 0
assignw T502[0] T501
call T503 ITOC 1
assignb T492[T494] T503
assignw T504 10
assignw T506 BASE[8]
div T505 T506 T504
assignw BASE[8] T505
goto L37
@label B1133
assignw T507 BASE[24]
param T508 0
assignw T508[0] T507
assignw T510 BASE[20]
assignw T511 T510[0]
assignw T512 1
mult T512 T512 T511
add T512 T512 4
malloc T509 T512
memcpy T509 T510 T512
param T513 4
assignw T513[0] T509
call T514 Function3 2
assignw T515 0
assignw T516 BASE[4]
lt test T516 T515
goif B1151 test
goto B1211
@label B1151
assignw S1[0] 1
assignw T518 2
assignw T519 T518
assignw T520 BASE[28]
assignw T521 4
mult T521 T521 T519
add T521 T521 4
malloc T520 T521
assignw T520[0] T519
assignw T520[0] T520
@label L38
sub T521 T521 4
lt test T521 0
goif L38_end test
assignw T522 T478
assignw T523 T520[T521]
assignw T524 1
mult T524 T524 T522
add T524 T524 4
malloc T523 T524
assignw T523[0] T522
assignw T523[0] T523
goto L38
@label L38_end
assignw T525 BASE[28]
assignw T526 BASE[24]
assignw T525[8] T526
assignw T525[4] S1
assignw T527 2
assignw T529 BASE[28]
assignw T530 T529[0]
assignw T531 4
mult T531 T531 T530
add T531 T531 4
malloc T528 T531
assignw T532 T531
@label L39
sub T532 T532 4
lt test T532 0
goif L39_end test
assignw T533 T529[T532]
assignw T534 T528[T532]
assignw T535 T533[0]
assignw T536 1
mult T536 T536 T535
add T536 T536 4
malloc T534 T536
assignw T534[0] T534
memcpy T534 T533 T536
goto L39
@label L39_end
param T537 0
assignw T537[0] T528
param T538 4
assignw T538[0] T527
assignw T539 BASE[0]
param T540 8
assignw T540[0] T539
call T541 Function4 3
goto Function9_end
@label B1211
assignw T542 BASE[0]
param T543 0
assignw T543[0] T542
assignw T545 BASE[24]
assignw T546 T545[0]
assignw T547 1
mult T547 T547 T546
add T547 T547 4
malloc T544 T547
memcpy T544 T545 T547
param T548 4
assignw T548[0] T544
call T549 Function2 2
@label Function9_end
assignw lastbase BASE
return 0
@endfunction 32
@function Function10 32
assignw T552 BASE[0]
assignw T553 T552[0]
assignw T554 1
mult T554 T554 T553
add T554 T554 4
malloc T551 T554
memcpy T551 T552 T554
param T555 0
assignw T555[0] T551
param T556 4
assignb T556[0] T34
call T557 Function0 2
assignw T558 T557
assignw T559 BASE[20]
assignw T560 1
mult T560 T560 T558
add T560 T560 4
malloc T559 T560
assignw T559[0] T558
assignw T559[0] T559
assignw T561 T557
assignw T562 BASE[24]
assignw T563 1
mult T563 T563 T561
add T563 T563 4
malloc T562 T563
assignw T562[0] T561
assignw T562[0] T562
assignw f10 BASE[4]
param T564 0
assignw T564[0] f10
call T565 FTOI 1
assignw BASE[8] T565
assignw f12 BASE[4]
assignw T566 BASE[8]
sub f11 f12 T566
assignw BASE[16] f11
@label L40
@label L41
assignw f13 BASE[16]
param T567 0
assignw T567[0] f13
call T568 FTOI 1
assignw T569 BASE[16]
neq test T569 T568
goif B1276 test
goto B1281
@label B1276
assignw T570 10
assignw f15 BASE[16]
mult f14 f15 T570
assignw BASE[16] f14
goto L40
@label B1281
assignw f16 BASE[16]
param T571 0
assignw T571[0] f16
call T572 FTOI 1
assignw BASE[12] T572
assignw T573 BASE[20]
param T574 0
assignw T574[0] T573
assignw T575 BASE[8]
param T576 4
assignw T576[0] T575
call T577 Function9 2
assignw T578 BASE[24]
param T579 0
assignw T579[0] T578
assignw T580 BASE[12]
param T581 4
assignw T581[0] T580
call T582 Function9 2
assignw S2[0] 1
assignw T584 3
assignw T585 T584
assignw T586 BASE[28]
assignw T587 4
mult T587 T587 T585
add T587 T587 4
malloc T586 T587
assignw T586[0] T585
assignw T586[0] T586
@label L42
sub T587 T587 4
lt test T587 0
goif L42_end test
assignw T588 T557
assignw T589 T586[T587]
assignw T590 1
mult T590 T590 T588
add T590 T590 4
malloc T589 T590
assignw T589[0] T588
assignw T589[0] T589
goto L42
@label L42_end
assignw T591 BASE[28]
assignw T592 BASE[24]
assignw T591[12] T592
assignw T591[8] S2
assignw T593 BASE[20]
assignw T591[4] T593
assignw T594 3
assignw T596 BASE[28]
assignw T597 T596[0]
assignw T598 4
mult T598 T598 T597
add T598 T598 4
malloc T595 T598
assignw T599 T598
@label L43
sub T599 T599 4
lt test T599 0
goif L43_end test
assignw T600 T596[T599]
assignw T601 T595[T599]
assignw T602 T600[0]
assignw T603 1
mult T603 T603 T602
add T603 T603 4
malloc T601 T603
assignw T601[0] T601
memcpy T601 T600 T603
goto L43
@label L43_end
param T604 0
assignw T604[0] T595
param T605 4
assignw T605[0] T594
assignw T606 BASE[0]
param T607 8
assignw T607[0] T606
call T608 Function4 3
@label Function10_end
assignw lastbase BASE
return 0
@endfunction 32
assignw T611 10
assignw T612 11
assignw T614 T612
assignw T615 4
mult T615 T615 T614
add T615 T615 4
malloc T613 T615
assignw T613[0] T614
@label L44
sub T615 T615 4
lt test T615 0
goif L44_end test
assignw T616 T611
assignw T617 T613[T615]
assignw T618 4
mult T618 T618 T616
add T618 T618 4
malloc T617 T618
assignw T617[0] T616
assignw T617[0] T617
goto L44
@label L44_end
@label L45
goto B1389
@label B1389
assignw S3[0] 47
param T622 0
assignw T622[0] S3
param T623 4
assignw T623[0] 0
param T624 8
assignw T624[0] 0
param T625 12
assignw T625[0] 0
param T626 16
assignw T626[0] 0
param T627 20
assignw T627[0] S0
call T628 PRINT 6
call T629 READC 0
assignb T620 T629
@label L46
assignb T630 110
eq test T620 T630
goif B1415 test
goto B1410
@label B1410
@label L47
assignb T631 78
eq test T620 T631
goif B1415 test
goto B1431
@label B1415
assignw S4[0] 12
param T633 0
assignw T633[0] S4
param T634 4
assignw T634[0] 0
param T635 8
assignw T635[0] 0
param T636 12
assignw T636[0] 0
param T637 16
assignw T637[0] 0
param T638 20
assignw T638[0] S0
call T639 PRINT 6
goto B1639
goto B1431
@label B1431
assignw S5[0] 56
param T641 0
assignw T641[0] S5
param T642 4
assignw T642[0] 0
param T643 8
assignw T643[0] 0
param T644 12
assignw T644[0] 0
param T645 16
assignw T645[0] 0
param T646 20
assignw T646[0] S0
call T647 PRINT 6
call T648 READI 0
assignw T619 T648
assignw T649 0
assignw T651 T649
@label L48
geq test T651 T619
goif L48_end test
assignw T650 T651
assignw S6[0] 62
assignw T653 1
add T654 T619 T653
assignw T655 2
assignw T657 T655
assignw T658 4
mult T658 T658 T657
add T658 T658 4
malloc T656 T658
assignw T656[0] T657
assignw T656[8] T650
assignw T656[4] T654
param T659 0
assignw T659[0] S6
param T660 4
assignw T660[0] 0
assignw T662 T656[0]
assignw T663 4
mult T663 T663 T662
add T663 T663 4
malloc T661 T663
memcpy T661 T656 T663
param T664 8
assignw T664[0] T661
param T665 12
assignw T665[0] 0
param T666 16
assignw T666[0] 0
param T667 20
assignw T667[0] S0
call T668 PRINT 6
assignw T669 0
assignw T670 1
add T671 T619 T670
assignw T673 T669
@label L49
geq test T673 T671
goif L49_end test
assignw T672 T673
mult T674 4 T650
add T674 T674 4
assignw T675 T613[T674]
mult T676 4 T672
add T676 T676 4
call f17 READF 0
assignw T675[T676] f17
add T673 T673 1
goto L49
@label L49_end
add T651 T651 1
goto L48
@label L48_end
assignw T678 T613[0]
assignw T679 4
mult T679 T679 T678
add T679 T679 4
malloc T677 T679
assignw T680 T679
@label L50
sub T680 T680 4
lt test T680 0
goif L50_end test
assignw T681 T613[T680]
assignw T682 T677[T680]
assignw T683 T681[0]
assignw T684 4
mult T684 T684 T683
add T684 T684 4
malloc T682 T684
assignw T682[0] T682
memcpy T682 T681 T684
goto L50
@label L50_end
param T685 0
assignw T685[0] T677
param T686 4
assignw T686[0] T619
call T687 Function14  2
goif B1533 T687
goto B1605
@label B1533
assignw S7[0] 30
param T689 0
assignw T689[0] S7
param T690 4
assignw T690[0] 0
param T691 8
assignw T691[0] 0
param T692 12
assignw T692[0] 0
param T693 16
assignw T693[0] 0
param T694 20
assignw T694[0] S0
call T695 PRINT 6
assignw T696 0
assignw T698 T696
@label L51
geq test T698 T619
goif L51_end test
assignw T697 T698
assignw S8[0] 8
assignw T700 1
assignw T702 T700
assignw T703 4
mult T703 T703 T702
add T703 T703 4
malloc T701 T703
assignw T701[0] T702
assignw T701[4] T697
mult T704 4 T697
add T704 T704 4
assignw T705 T613[T704]
mult T706 4 T619
add T706 T706 4
assignw T707 1
assignw T709 T707
assignw T710 4
mult T710 T710 T709
add T710 T710 4
malloc T708 T710
assignw T708[0] T709
assignw f18 T705[T706]
assignw T708[4] f18
param T711 0
assignw T711[0] S8
param T712 4
assignw T712[0] 0
assignw T714 T701[0]
assignw T715 4
mult T715 T715 T714
add T715 T715 4
malloc T713 T715
memcpy T713 T701 T715
param T716 8
assignw T716[0] T713
assignw T718 T708[0]
assignw T719 4
mult T719 T719 T718
add T719 T719 4
malloc T717 T719
memcpy T717 T708 T719
param T720 12
assignw T720[0] T717
param T721 16
assignw T721[0] 0
param T722 20
assignw T722[0] S0
call T723 PRINT 6
add T698 T698 1
goto L51
@label L51_end
goto B1619
@label B1605
assignw S9[0] 43
param T725 0
assignw T725[0] S9
param T726 4
assignw T726[0] 0
param T727 8
assignw T727[0] 0
param T728 12
assignw T728[0] 0
param T729 16
assignw T729[0] 0
param T730 20
assignw T730[0] S0
call T731 PRINT 6
@label B1619
assignw T733 T32[0]
assignw T734 1
mult T734 T734 T733
add T734 T734 4
malloc T732 T734
memcpy T732 T32 T734
param T735 0
assignw T735[0] T732
param T736 4
assignw T736[0] 0
param T737 8
assignw T737[0] 0
param T738 12
assignw T738[0] 0
param T739 16
assignw T739[0] 0
param T740 20
assignw T740[0] S0
call T741 PRINT 6
goto L45
@label B1639
@function Function11 4
assignw T742 0
assignw f19 BASE[0]
lt test f19 T742
goif B1645 test
goto B1650
@label B1645
assignw f21 BASE[0]
minus f20 f21
assignw lastbase BASE
return f20
goto Function11_end
@label B1650
assignw f22 BASE[0]
assignw lastbase BASE
return f22
@label Function11_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function12 24
assignw T745 0
assignw T746 BASE[0]
mult T747 4 T745
add T747 T747 4
assignw T748 T746[T747]
assignw T749 BASE[8]
mult T750 4 T749
add T750 T750 4
assignw f23 T748[T750]
param T751 0
assignw T751[0] f23
call f24 Function11 1
assignw BASE[12] f24
assignw T752 0
assignw BASE[16] T752
assignw T753 1
assignw T755 T753
@label L52
assignw T756 BASE[4]
geq test T755 T756
goif L52_end test
assignw T754 T755
assignw T757 BASE[0]
assignw T758 BASE[20]
mult T759 4 T758
add T759 T759 4
assignw T760 T757[T759]
assignw T761 BASE[8]
mult T762 4 T761
add T762 T762 4
assignw f25 T760[T762]
param T763 0
assignw T763[0] f25
call f26 Function11 1
assignw f27 BASE[12]
gt test f26 f27
goif B1696 test
goto B1712
@label B1696
assignw T764 BASE[0]
assignw T765 BASE[20]
mult T766 4 T765
add T766 T766 4
assignw T767 T764[T766]
assignw T768 BASE[8]
mult T769 4 T768
add T769 T769 4
assignw f28 T767[T769]
param T770 0
assignw T770[0] f28
call f29 Function11 1
assignw BASE[12] f29
assignw T771 BASE[20]
assignw BASE[16] T771
goto B1712
@label B1712
add T755 T755 1
goto L52
@label L52_end
assignw T772 BASE[16]
assignw lastbase BASE
return T772
@label Function12_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function13 24
assignw T775 0
assignw T777 T775
@label L53
assignw T778 BASE[4]
geq test T777 T778
goif L53_end test
assignw T776 T777
assignw T779 BASE[0]
assignw T780 BASE[8]
mult T781 4 T780
add T781 T781 4
assignw T782 T779[T781]
assignw T783 BASE[20]
mult T784 4 T783
add T784 T784 4
assignw f30 T782[T784]
assignw BASE[16] f30
assignw T785 BASE[0]
assignw T786 BASE[8]
mult T787 4 T786
add T787 T787 4
assignw T788 T785[T787]
assignw T789 BASE[20]
mult T790 4 T789
add T790 T790 4
assignw T791 BASE[0]
assignw T792 BASE[12]
mult T793 4 T792
add T793 T793 4
assignw T794 T791[T793]
assignw T795 BASE[20]
mult T796 4 T795
add T796 T796 4
assignw f31 T794[T796]
assignw T788[T790] f31
assignw T797 BASE[0]
assignw T798 BASE[12]
mult T799 4 T798
add T799 T799 4
assignw T800 T797[T799]
assignw T801 BASE[20]
mult T802 4 T801
add T802 T802 4
assignw f32 BASE[16]
assignw T800[T802] f32
add T777 T777 1
goto L53
@label L53_end
@label Function13_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function14 36
assignw T805 0
assignw T807 T805
@label L54
assignw T808 BASE[4]
geq test T807 T808
goif L54_end test
assignw T806 T807
assignw T810 BASE[0]
assignw T811 T810[0]
assignw T812 4
mult T812 T812 T811
add T812 T812 4
malloc T809 T812
assignw T813 T812
@label L55
sub T813 T813 4
lt test T813 0
goif L55_end test
assignw T814 T810[T813]
assignw T815 T809[T813]
assignw T816 T814[0]
assignw T817 4
mult T817 T817 T816
add T817 T817 4
malloc T815 T817
assignw T815[0] T815
memcpy T815 T814 T817
goto L55
@label L55_end
param T818 0
assignw T818[0] T809
assignw T819 BASE[4]
param T820 4
assignw T820[0] T819
assignw T821 BASE[16]
param T822 8
assignw T822[0] T821
call T823 Function12 3
assignw BASE[8] T823
assignw T824 BASE[0]
assignw T825 BASE[8]
mult T826 4 T825
add T826 T826 4
assignw T827 T824[T826]
assignw T828 BASE[16]
mult T829 4 T828
add T829 T829 4
@label L56
assignw T830 0
assignw T831 T827[T829]
eq test T831 T830
goif B1829 test
goto B1837
@label B1829
goto B1832
assignb T832 True
goto Bool1833
@label B1832
assignb T832 False
@label Bool1833
assignw lastbase BASE
return T832
goto B1837
@label B1837
assignw T833 1
assignw T835 BASE[4]
add T834 T835 T833
assignw T837 BASE[0]
assignw T838 T837[0]
assignw T839 4
mult T839 T839 T838
add T839 T839 4
malloc T836 T839
assignw T840 T839
@label L57
sub T840 T840 4
lt test T840 0
goif L57_end test
assignw T841 T837[T840]
assignw T842 T836[T840]
assignw T843 T841[0]
assignw T844 4
mult T844 T844 T843
add T844 T844 4
malloc T842 T844
assignw T842[0] T842
memcpy T842 T841 T844
goto L57
@label L57_end
param T845 0
assignw T845[0] T836
param T846 4
assignw T846[0] T834
assignw T847 BASE[16]
param T848 8
assignw T848[0] T847
assignw T849 BASE[8]
param T850 12
assignw T850[0] T849
call T851 Function13 4
assignw T852 1
assignw T854 BASE[16]
add T853 T854 T852
assignw T856 T853
@label L58
assignw T857 BASE[4]
geq test T856 T857
goif L58_end test
assignw T855 T856
assignw T858 BASE[0]
assignw T859 BASE[20]
mult T860 4 T859
add T860 T860 4
assignw T861 T858[T860]
assignw T862 BASE[16]
mult T863 4 T862
add T863 T863 4
assignw T864 BASE[0]
assignw T865 BASE[16]
mult T866 4 T865
add T866 T866 4
assignw T867 T864[T866]
assignw T868 BASE[16]
mult T869 4 T868
add T869 T869 4
assignw f34 T861[T863]
assignw f35 T867[T869]
div f33 f34 f35
assignw BASE[12] f33
assignw T870 1
assignw T872 BASE[16]
add T871 T872 T870
assignw T873 1
assignw T875 BASE[4]
add T874 T875 T873
assignw T877 T871
@label L59
geq test T877 T874
goif L59_end test
assignw T876 T877
assignw T878 BASE[0]
assignw T879 BASE[20]
mult T880 4 T879
add T880 T880 4
assignw T881 T878[T880]
assignw T882 BASE[24]
mult T883 4 T882
add T883 T883 4
assignw T884 BASE[0]
assignw T885 BASE[20]
mult T886 4 T885
add T886 T886 4
assignw T887 T884[T886]
assignw T888 BASE[24]
mult T889 4 T888
add T889 T889 4
assignw T890 BASE[0]
assignw T891 BASE[16]
mult T892 4 T891
add T892 T892 4
assignw T893 T890[T892]
assignw T894 BASE[24]
mult T895 4 T894
add T895 T895 4
assignw f37 T893[T895]
assignw f38 BASE[12]
mult f36 f37 f38
assignw f40 T887[T889]
sub f39 f40 f36
assignw T881[T883] f39
add T877 T877 1
goto L59
@label L59_end
add T856 T856 1
goto L58
@label L58_end
add T807 T807 1
goto L54
@label L54_end
assignw T896 1
assignw T898 BASE[4]
sub T897 T898 T896
assignw T899 1
minus T900 T899
assignw T901 1
minus T902 T901
assignw T904 T897
@label L60
lt test T902 0
goif L60_neg test
geq test T904 T900
goif L60_end test
goto L60_body
@label L60_neg
leq test T904 T900
goif L60_end test
@label L60_body
assignw T903 T904
assignw T905 0
assignw T907 T905
@label L61
assignw T908 BASE[28]
geq test T907 T908
goif L61_end test
assignw T906 T907
assignw T909 BASE[0]
assignw T910 BASE[32]
mult T911 4 T910
add T911 T911 4
assignw T912 T909[T911]
assignw T913 BASE[4]
mult T914 4 T913
add T914 T914 4
assignw T915 BASE[0]
assignw T916 BASE[32]
mult T917 4 T916
add T917 T917 4
assignw T918 T915[T917]
assignw T919 BASE[4]
mult T920 4 T919
add T920 T920 4
assignw T921 BASE[0]
assignw T922 BASE[28]
mult T923 4 T922
add T923 T923 4
assignw T924 T921[T923]
assignw T925 BASE[4]
mult T926 4 T925
add T926 T926 4
assignw T927 BASE[0]
assignw T928 BASE[32]
mult T929 4 T928
add T929 T929 4
assignw T930 T927[T929]
assignw T931 BASE[28]
mult T932 4 T931
add T932 T932 4
assignw f42 T924[T926]
assignw f43 T930[T932]
mult f41 f42 f43
assignw T933 BASE[0]
assignw T934 BASE[28]
mult T935 4 T934
add T935 T935 4
assignw T936 T933[T935]
assignw T937 BASE[28]
mult T938 4 T937
add T938 T938 4
assignw f45 T936[T938]
div f44 f41 f45
assignw f47 T918[T920]
sub f46 f47 f44
assignw T912[T914] f46
add T907 T907 1
goto L61
@label L61_end
assignw T939 BASE[0]
assignw T940 BASE[28]
mult T941 4 T940
add T941 T941 4
assignw T942 T939[T941]
assignw T943 BASE[4]
mult T944 4 T943
add T944 T944 4
assignw T945 BASE[0]
assignw T946 BASE[28]
mult T947 4 T946
add T947 T947 4
assignw T948 T945[T947]
assignw T949 BASE[4]
mult T950 4 T949
add T950 T950 4
assignw T951 BASE[0]
assignw T952 BASE[28]
mult T953 4 T952
add T953 T953 4
assignw T954 T951[T953]
assignw T955 BASE[28]
mult T956 4 T955
add T956 T956 4
assignw f49 T948[T950]
assignw f50 T954[T956]
div f48 f49 f50
assignw T942[T944] f48
add T904 T904 T902
goto L60
@label L60_end
@label Function14_end
assignw lastbase BASE
return 0
@endfunction 36
