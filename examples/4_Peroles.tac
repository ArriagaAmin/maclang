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
assignw T610 20
assignw T612 T610
assignw T613 8
mult T613 T613 T612
add T613 T613 4
malloc T611 T613
assignw T611[0] T612
@label L44
sub T613 T613 8
lt test T613 0
goif L44_end test
assignw T614 T611[T613]
malloc T614 8
assignw T614[0] T614
assignw T615 T614[4]
malloc T615 4
assignw T615[0] T615
goto L44
@label L44_end
@label L45
goto B1386
@label B1386
assignw S3[0] 35
param T620 0
assignw T620[0] S3
param T621 4
assignw T621[0] 0
param T622 8
assignw T622[0] 0
param T623 12
assignw T623[0] 0
param T624 16
assignw T624[0] 0
param T625 20
assignw T625[0] S0
call T626 PRINT 6
call T627 READC 0
assignb T618 T627
@label L46
assignb T628 110
eq test T618 T628
goif B1412 test
goto B1407
@label B1407
@label L47
assignb T629 78
eq test T618 T629
goif B1412 test
goto B1428
@label B1412
assignw S4[0] 12
param T631 0
assignw T631[0] S4
param T632 4
assignw T632[0] 0
param T633 8
assignw T633[0] 0
param T634 12
assignw T634[0] 0
param T635 16
assignw T635[0] 0
param T636 20
assignw T636[0] S0
call T637 PRINT 6
goto B1937
goto B1428
@label B1428
assignw S5[0] 42
param T639 0
assignw T639[0] S5
param T640 4
assignw T640[0] 0
param T641 8
assignw T641[0] 0
param T642 12
assignw T642[0] 0
param T643 16
assignw T643[0] 0
param T644 20
assignw T644[0] S0
call T645 PRINT 6
call T646 READI 0
assignw T616 T646
assignw T647 20
gt test T616 T647
goif B1448 test
goto B1464
@label B1448
assignw S6[0] 41
param T649 0
assignw T649[0] S6
param T650 4
assignw T650[0] 0
param T651 8
assignw T651[0] 0
param T652 12
assignw T652[0] 0
param T653 16
assignw T653[0] 0
param T654 20
assignw T654[0] S0
call T655 PRINT 6
goto L45
goto B1464
@label B1464
assignw T656 0
assignw T617 T656
@label L48
lt test T617 T616
goif B1470 test
goto B1691
@label B1470
assignw S7[0] 27
param T658 0
assignw T658[0] S7
param T659 4
assignw T659[0] 0
param T660 8
assignw T660[0] 0
param T661 12
assignw T661[0] 0
param T662 16
assignw T662[0] 0
param T663 20
assignw T663[0] S0
call T664 PRINT 6
assignw S8[0] 11
param T666 0
assignw T666[0] S8
param T667 4
assignw T667[0] 0
param T668 8
assignw T668[0] 0
param T669 12
assignw T669[0] 0
param T670 16
assignw T670[0] 0
param T671 20
assignw T671[0] S0
call T672 PRINT 6
assignw S9[0] 11
param T674 0
assignw T674[0] S9
param T675 4
assignw T675[0] 0
param T676 8
assignw T676[0] 0
param T677 12
assignw T677[0] 0
param T678 16
assignw T678[0] 0
param T679 20
assignw T679[0] S0
call T680 PRINT 6
assignw S10[0] 9
param T682 0
assignw T682[0] S10
param T683 4
assignw T683[0] 0
param T684 8
assignw T684[0] 0
param T685 12
assignw T685[0] 0
param T686 16
assignw T686[0] 0
param T687 20
assignw T687[0] S0
call T688 PRINT 6
assignw S11[0] 20
param T690 0
assignw T690[0] S11
param T691 4
assignw T691[0] 0
param T692 8
assignw T692[0] 0
param T693 12
assignw T693[0] 0
param T694 16
assignw T694[0] 0
param T695 20
assignw T695[0] S0
call T696 PRINT 6
call T697 READI 0
assignw T616 T697
mult T698 8 T617
add T698 T698 4
assignw T699 T611[T698]
assignw T699[0] T616
@label L49
assignw T700 1
eq test T616 T700
goif B1551 test
goto B1592
@label B1551
assignw S12[0] 34
param T702 0
assignw T702[0] S12
param T703 4
assignw T703[0] 0
param T704 8
assignw T704[0] 0
param T705 12
assignw T705[0] 0
param T706 16
assignw T706[0] 0
param T707 20
assignw T707[0] S0
call T708 PRINT 6
@label L50
call T709 READC 0
eq test T618 T709
goif B1570 test
goto B1570
@label B1570
mult T710 8 T617
add T710 T710 4
assignw T711 T611[T710]
assignw T712 T711[4]
assignb T713 T712[0]


@label L51
assignb T714 110
neq test T618 T714
goif B1582 test
goto B1589
@label B1582
@label L52
assignb T715 78
neq test T618 T715
goif B1587 test
goto B1589
@label B1587
assignb T712[0] True
goto Bool1590
@label B1589
assignb T712[0] False
@label Bool1590
goto B1687
@label B1592
@label L53
assignw T716 2
eq test T616 T716
goif B1597 test
goto B1618
@label B1597
assignw S13[0] 21
param T718 0
assignw T718[0] S13
param T719 4
assignw T719[0] 0
param T720 8
assignw T720[0] 0
param T721 12
assignw T721[0] 0
param T722 16
assignw T722[0] 0
param T723 20
assignw T723[0] S0
call T724 PRINT 6
mult T725 8 T617
add T725 T725 4
assignw T726 T611[T725]
assignw T727 T726[4]
call T728 READC 0
assignb T727[0] T728
goto B1687
@label B1618
@label L54
assignw T729 3
eq test T616 T729
goif B1623 test
goto B1644
@label B1623
assignw S14[0] 19
param T731 0
assignw T731[0] S14
param T732 4
assignw T732[0] 0
param T733 8
assignw T733[0] 0
param T734 12
assignw T734[0] 0
param T735 16
assignw T735[0] 0
param T736 20
assignw T736[0] S0
call T737 PRINT 6
mult T738 8 T617
add T738 T738 4
assignw T739 T611[T738]
assignw T740 T739[4]
call T741 READI 0
assignw T740[0] T741
goto B1687
@label B1644
@label L55
assignw T742 4
eq test T616 T742
goif B1649 test
goto B1670
@label B1649
assignw S15[0] 21
param T744 0
assignw T744[0] S15
param T745 4
assignw T745[0] 0
param T746 8
assignw T746[0] 0
param T747 12
assignw T747[0] 0
param T748 16
assignw T748[0] 0
param T749 20
assignw T749[0] S0
call T750 PRINT 6
mult T751 8 T617
add T751 T751 4
assignw T752 T611[T751]
assignw T753 T752[4]
call f17 READF 0
assignw T753[0] f17
goto B1687
@label B1670
assignw S16[0] 13
param T755 0
assignw T755[0] S16
param T756 4
assignw T756[0] 0
param T757 8
assignw T757[0] 0
param T758 12
assignw T758[0] 0
param T759 16
assignw T759[0] 0
param T760 20
assignw T760[0] S0
call T761 PRINT 6
assignw T762 1
sub T763 T617 T762
assignw T617 T763
@label B1687
assignw T764 1
add T765 T617 T764
assignw T617 T765
goto L48
@label B1691
assignw T767 T611[0]
assignw T768 8
mult T768 T768 T767
add T768 T768 4
malloc T766 T768
assignw T769 T768
@label L56
sub T769 T769 8
lt test T769 0
goif L56_end test
assignw T770 T766[T769]
malloc T770 8
assignw T770[0] T770
assignw T771 T611[T769]
memcpy T770 T771 8
assignw T772 T770[4]
malloc T772 4
assignw T772[0] T772
assignw T773 T771[4]
memcpy T772 T773 4
goto L56
@label L56_end
param T774 0
assignw T774[0] T766
param T775 4
assignw T775[0] T616
call T776 Function11  2
assignw S17[0] 35
assignb T778 10
assignw T779 1
assignw T781 T779
assignw T782 1
mult T782 T782 T781
add T782 T782 4
malloc T780 T782
assignw T780[0] T781
assignb T780[4] T778
param T783 0
assignw T783[0] S17
assignw T785 T780[0]
assignw T786 1
mult T786 T786 T785
add T786 T786 4
malloc T784 T786
memcpy T784 T780 T786
param T787 4
assignw T787[0] T784
param T788 8
assignw T788[0] 0
param T789 12
assignw T789[0] 0
param T790 16
assignw T790[0] 0
param T791 20
assignw T791[0] S0
call T792 PRINT 6
assignw T793 0
assignw T795 T793
@label L57
geq test T795 T616
goif L57_end test
assignw T794 T795
mult T796 8 T794
add T796 T796 4
assignw T797 T611[T796]
@label L58
assignw T798 1
assignw T799 T797[0]
eq test T799 T798
goif B1762 test
goto B1814
@label B1762
assignw S18[0] 6
assignw S19[0] 0
param T802 0
assignw T802[0] S18
param T803 4
assignw T803[0] 0
param T804 8
assignw T804[0] 0
param T805 12
assignw T805[0] 0
param T806 16
assignw T806[0] 0
param T807 20
assignw T807[0] S19
call T808 PRINT 6
mult T809 8 T794
add T809 T809 4
assignw T810 T611[T809]
assignw T811 T810[4]
assignb T812 T811[0]
goif B1784 T812
goto B1799
@label B1784
assignw S20[0] 4
param T814 0
assignw T814[0] S20
param T815 4
assignw T815[0] 0
param T816 8
assignw T816[0] 0
param T817 12
assignw T817[0] 0
param T818 16
assignw T818[0] 0
param T819 20
assignw T819[0] S0
call T820 PRINT 6
goto B1799
@label B1799
assignw S21[0] 5
param T822 0
assignw T822[0] S21
param T823 4
assignw T823[0] 0
param T824 8
assignw T824[0] 0
param T825 12
assignw T825[0] 0
param T826 16
assignw T826[0] 0
param T827 20
assignw T827[0] S0
call T828 PRINT 6
goto B1933
@label B1814
mult T829 8 T794
add T829 T829 4
assignw T830 T611[T829]
@label L59
assignw T831 2
assignw T832 T830[0]
eq test T832 T831
goif B1823 test
goto B1857
@label B1823
assignw S22[0] 8
mult T834 8 T794
add T834 T834 4
assignw T835 T611[T834]
assignw T836 T835[4]
assignw T837 1
assignw T839 T837
assignw T840 1
mult T840 T840 T839
add T840 T840 4
malloc T838 T840
assignw T838[0] T839
assignb T841 T836[0]
assignb T838[4] T841
param T842 0
assignw T842[0] S22
assignw T844 T838[0]
assignw T845 1
mult T845 T845 T844
add T845 T845 4
malloc T843 T845
memcpy T843 T838 T845
param T846 4
assignw T846[0] T843
param T847 8
assignw T847[0] 0
param T848 12
assignw T848[0] 0
param T849 16
assignw T849[0] 0
param T850 20
assignw T850[0] S0
call T851 PRINT 6
goto B1933
@label B1857
mult T852 8 T794
add T852 T852 4
assignw T853 T611[T852]
@label L60
assignw T854 3
assignw T855 T853[0]
eq test T855 T854
goif B1866 test
goto B1900
@label B1866
assignw S23[0] 7
mult T857 8 T794
add T857 T857 4
assignw T858 T611[T857]
assignw T859 T858[4]
assignw T860 1
assignw T862 T860
assignw T863 4
mult T863 T863 T862
add T863 T863 4
malloc T861 T863
assignw T861[0] T862
assignw T864 T859[0]
assignw T861[4] T864
param T865 0
assignw T865[0] S23
param T866 4
assignw T866[0] 0
assignw T868 T861[0]
assignw T869 4
mult T869 T869 T868
add T869 T869 4
malloc T867 T869
memcpy T867 T861 T869
param T870 8
assignw T870[0] T867
param T871 12
assignw T871[0] 0
param T872 16
assignw T872[0] 0
param T873 20
assignw T873[0] S0
call T874 PRINT 6
goto B1933
@label B1900
assignw S24[0] 9
mult T876 8 T794
add T876 T876 4
assignw T877 T611[T876]
assignw T878 T877[4]
assignw T879 1
assignw T881 T879
assignw T882 4
mult T882 T882 T881
add T882 T882 4
malloc T880 T882
assignw T880[0] T881
assignw f18 T878[0]
assignw T880[4] f18
param T883 0
assignw T883[0] S24
param T884 4
assignw T884[0] 0
param T885 8
assignw T885[0] 0
assignw T887 T880[0]
assignw T888 4
mult T888 T888 T887
add T888 T888 4
malloc T886 T888
memcpy T886 T880 T888
param T889 12
assignw T889[0] T886
param T890 16
assignw T890[0] 0
param T891 20
assignw T891[0] S0
call T892 PRINT 6
@label B1933
add T795 T795 1
goto L57
@label L57_end
goto L45
@label B1937
@function Function11 24
assignw T894 0
assignw T895 0
assignw T896 1
assignw T898 BASE[4]
sub T897 T898 T896
assignw BASE[8] T894
assignw BASE[12] T895
assignw BASE[16] T897
assignw T899 BASE[20]
malloc T899 8
assignw T899[0] T899
assignw T900 T899[4]
malloc T900 4
assignw T900[0] T900
@label L61
assignw T901 BASE[12]
assignw T902 BASE[16]
leq test T901 T902
goif B1958 test
goto B2043
@label B1958
assignw T903 BASE[0]
assignw T904 BASE[12]
mult T905 8 T904
add T905 T905 4
assignw T906 T903[T905]
@label L62
assignw T907 1
assignw T908 T906[0]
eq test T908 T907
goif B1969 test
goto B2000
@label B1969
assignw T909 BASE[0]
assignw T910 BASE[12]
mult T911 8 T910
add T911 T911 4
assignw T912 T909[T911]
assignw BASE[20] T912
assignw T913 BASE[0]
assignw T914 BASE[12]
mult T915 8 T914
add T915 T915 4
assignw T916 BASE[0]
assignw T917 BASE[8]
mult T918 8 T917
add T918 T918 4
assignw T919 T916[T918]
assignw T913[T915] T919
assignw T920 BASE[0]
assignw T921 BASE[8]
mult T922 8 T921
add T922 T922 4
assignw T923 BASE[20]
assignw T920[T922] T923
assignw T924 1
assignw T926 BASE[8]
add T925 T926 T924
assignw BASE[8] T925
assignw T927 1
assignw T929 BASE[12]
add T928 T929 T927
assignw BASE[12] T928
goto L61
@label B2000
assignw T930 BASE[0]
assignw T931 BASE[12]
mult T932 8 T931
add T932 T932 4
assignw T933 T930[T932]
@label L63
assignw T934 4
assignw T935 T933[0]
eq test T935 T934
goif B2011 test
goto B2038
@label B2011
assignw T936 BASE[0]
assignw T937 BASE[12]
mult T938 8 T937
add T938 T938 4
assignw T939 T936[T938]
assignw BASE[20] T939
assignw T940 BASE[0]
assignw T941 BASE[12]
mult T942 8 T941
add T942 T942 4
assignw T943 BASE[0]
assignw T944 BASE[16]
mult T945 8 T944
add T945 T945 4
assignw T946 T943[T945]
assignw T940[T942] T946
assignw T947 BASE[0]
assignw T948 BASE[16]
mult T949 8 T948
add T949 T949 4
assignw T950 BASE[20]
assignw T947[T949] T950
assignw T951 1
assignw T953 BASE[16]
sub T952 T953 T951
assignw BASE[16] T952
goto L61
@label B2038
assignw T954 1
assignw T956 BASE[12]
add T955 T956 T954
assignw BASE[12] T955
goto L61
@label B2043
@label L64
assignw T957 BASE[8]
assignw T958 BASE[16]
leq test T957 T958
goif B2049 test
goto Function11_end
@label B2049
assignw T959 BASE[0]
assignw T960 BASE[8]
mult T961 8 T960
add T961 T961 4
assignw T962 T959[T961]
@label L65
assignw T963 2
assignw T964 T962[0]
eq test T964 T963
goif B2060 test
goto B2065
@label B2060
assignw T965 1
assignw T967 BASE[8]
add T966 T967 T965
assignw BASE[8] T966
goto L64
@label B2065
assignw T968 BASE[0]
assignw T969 BASE[8]
mult T970 8 T969
add T970 T970 4
assignw T971 T968[T970]
assignw BASE[20] T971
assignw T972 BASE[0]
assignw T973 BASE[8]
mult T974 8 T973
add T974 T974 4
assignw T975 BASE[0]
assignw T976 BASE[16]
mult T977 8 T976
add T977 T977 4
assignw T978 T975[T977]
assignw T972[T974] T978
assignw T979 BASE[0]
assignw T980 BASE[16]
mult T981 8 T980
add T981 T981 4
assignw T982 BASE[20]
assignw T979[T981] T982
assignw T983 1
assignw T985 BASE[16]
sub T984 T985 T983
assignw BASE[16] T984
goto L64
@label Function11_end
assignw lastbase BASE
return 0
@endfunction 24
