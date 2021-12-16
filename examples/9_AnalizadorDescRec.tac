@staticv A0 5
@staticv A1 1
@staticv A12 2
@staticv A19 1
@string S0 "0000\n"
@string S1 "0000-"
@string S2 "0000."
@string S3 "0000%s  =>  %f%c"
@string S4 "0000abcdefghijklmnopqrstuvwxyz"
@string S5 "0000calc> "
@string S6 "0000quit"
@string S7 "0000$"
@string S8 "0000Numero maximo de tokens alcanzado."
@string S9 "0000("
@string S10 "0000$"
@string S11 "0000No se pudo reconocer la expresion."
@string S12 "0000No se pudo reconocer la expresion."
@string S13 "0000="
@string S14 "0000("
@string S15 "0000No se pudo reconocer la expresion."
@string S16 "0000("
@string S17 "0000+"
@string S18 "0000-"
@string S19 "0000+"
@string S20 "0000No se pudo reconocer la expresion."
@string S21 "0000("
@string S22 "0000*"
@string S23 "0000/"
@string S24 "0000+"
@string S25 "0000No se puede dividir entre 0."
@string S26 "0000No se pudo reconocer la expresion."
@string S27 "0000("
@string S28 "0000("
@string S29 "0000)"
@string S30 "0000No se pudo reconocer la expresion."
@string S31 "0000No se pudo reconocer la expresion."
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
malloc T602 12
assignw T603 T602
assignw T604 T603[0]
assignb T605 0
assignw T606 1
assignw T608 T606
assignw T609 1
mult T609 T609 T608
add T609 T609 4
malloc T607 T609
assignw T607[0] T608
assignb T607[4] T605
assignw T604[4] T607
@function Function11 16
assignb T611 A12[0]
goif L45 T611
assignw T612 1024
assignw BASE[0] T612
@label L45
assignb T613 A12[1]
goif L46 T613
assignw T614 31
assignw BASE[4] T614
@label L46
malloc T615 12
assignw BASE[8] T615
assignw T616 BASE[8]
assignw T617 T616[0]
assignw T619 BASE[0]
assignw T620 4
mult T620 T620 T619
add T620 T620 4
malloc T618 T620
assignw T618[0] T619
assignw T617[0] T618
assignw T621 BASE[8]
assignw T622 T621[0]
assignw T623 BASE[0]
assignw T622[4] T623
assignw T624 BASE[8]
assignw T625 T624[0]
assignw T626 BASE[4]
assignw T625[8] T626
assignw T627 0
assignw BASE[12] T627
@label L47
assignw T628 BASE[12]
assignw T629 BASE[0]
lt test T628 T629
goif B1412 test
goto B1422
@label B1412
assignw T630 BASE[8]
assignw T631 T630[0]
assignw T632 T631[0]
assignw T633 T632[0]
assignw T634 BASE[12]
mult T635 4 T634
add T635 T635 4
assignw T636 BASE[16]
assignw T633[T635] T636
goto L47
@label B1422
assignw T637 BASE[8]
assignw lastbase BASE
return T637
@label Function11_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function12 16
assignw T638 0
assignw BASE[12] T638
@label L48
assignw T639 BASE[0]
assignw T640 T639[0]
assignw T641 BASE[12]
assignw T642 T640[4]
lt test T641 T642
goif B1440 test
goto B1486
@label B1440
assignw T643 BASE[0]
assignw T644 T643[0]
assignw T645 T644[0]
assignw T646 T645[0]
assignw T647 BASE[12]
mult T648 4 T647
add T648 T648 4
assignw T649 T646[T648]
assignw BASE[4] T649
@label L49
assignw T650 BASE[4]
assignw T651 T650[0]
assignw T653 T651[4]
assignw T654 T653[0]
assignw T655 1
mult T655 T655 T654
add T655 T655 4
malloc T652 T655
memcpy T652 T653 T655
param T656 0
assignw T656[0] T652
assignw T658 BASE[4]
assignw T659 T658[0]
assignw T660 1
mult T660 T660 T659
add T660 T660 4
malloc T657 T660
memcpy T657 T658 T660
param T661 4
assignw T661[0] T657
call T662 Function1 2
@label L50
assignw T663 0
neq test T662 T663
goif B1476 test
goto L48
@label B1476
assignw T664 BASE[4]
assignw T665 T664[0]
assignw T666 T665[0]
assignw BASE[8] T666
assignw T667 BASE[4]
free T667
assignw T668 BASE[8]
assignw BASE[4] T668
goto L49
goto L48
@label B1486
assignw T669 BASE[0]
assignw T670 T669[0]
assignw T671 T670[0]
free T671
assignw T672 BASE[0]
free T672
@label Function12_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function13 16
assignw T674 0
assignw T675 0
assignw BASE[8] T674
assignw BASE[12] T675
@label L51
assignw T676 BASE[4]
assignw T677 BASE[12]
mult T678 1 T677
add T678 T678 4
@label L52
assignb T679 0
assignb T680 T676[T678]
neq test T680 T679
goif B1512 test
goto B1532
@label B1512
assignw T681 BASE[4]
assignw T682 BASE[12]
mult T683 1 T682
add T683 T683 4
assignb T684 T681[T683]
param T685 0
assignb T685[0] T684
call T686 CTOI 1
assignw T687 BASE[0]
assignw T688 T687[0]
assignw T690 BASE[8]
assignw T691 T688[8]
mult T689 T690 T691
add T692 T686 T689
assignw BASE[8] T692
assignw T693 1
assignw T695 BASE[12]
add T694 T695 T693
assignw BASE[12] T694
goto L51
@label B1532
assignw T696 BASE[0]
assignw T697 T696[0]
assignw T699 BASE[8]
assignw T700 T697[4]
mod T698 T699 T700
assignw lastbase BASE
return T698
@label Function13_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function14 16
assignw T702 BASE[0]
assignw T703 T702[0]
assignw T704 T703[0]
assignw T705 BASE[0]
param T706 0
assignw T706[0] T705
assignw T708 BASE[4]
assignw T709 T708[0]
assignw T710 1
mult T710 T710 T709
add T710 T710 4
malloc T707 T710
memcpy T707 T708 T710
param T711 4
assignw T711[0] T707
call T712 Function13 2
assignw T713 T704[0]
mult T714 4 T712
add T714 T714 4
assignw T715 T713[T714]
assignw BASE[12] T715
@label L53
assignw T716 BASE[12]
assignw T717 T716[0]
assignw T718 0
assignw T719 T717[4]
mult T720 1 T718
add T720 T720 4
@label L54
assignb T721 0
assignb T722 T719[T720]
neq test T722 T721
goif B1578 test
goto B1621
@label B1578
assignw T723 BASE[12]
assignw T724 T723[0]
assignw T726 T724[4]
assignw T727 T726[0]
assignw T728 1
mult T728 T728 T727
add T728 T728 4
malloc T725 T728
memcpy T725 T726 T728
param T729 0
assignw T729[0] T725
assignw T731 BASE[4]
assignw T732 T731[0]
assignw T733 1
mult T733 T733 T732
add T733 T733 4
malloc T730 T733
memcpy T730 T731 T733
param T734 4
assignw T734[0] T730
call T735 Function1 2
@label L55
assignw T736 0
eq test T735 T736
goif B1604 test
goto B1616
@label B1604
assignw T737 BASE[12]
assignw T738 T737[0]
assignw f17 T738[8]
assignw BASE[8] f17
goto B1609
@label B1609
assignb T739 True
goto Bool1612
assignb T739 False
@label Bool1612
assignw lastbase BASE
return T739
goto L53
@label B1616
assignw T740 BASE[12]
assignw T741 T740[0]
assignw T742 T741[0]
assignw BASE[12] T742
goto L53
@label B1621
goto B1624
assignb T743 True
goto Bool1625
@label B1624
assignb T743 False
@label Bool1625
assignw lastbase BASE
return T743
@label Function14_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function15 24
assignw T745 BASE[0]
param T746 0
assignw T746[0] T745
assignw T748 BASE[4]
assignw T749 T748[0]
assignw T750 1
mult T750 T750 T749
add T750 T750 4
malloc T747 T750
memcpy T747 T748 T750
param T751 4
assignw T751[0] T747
assignw f18 BASE[20]
param T752 8
assignw T752[0] f18
call T753 Function14 3
assignw f19 lastbase[8]
assignw BASE[20] f19
goif B1653 T753
goto B1690
@label B1653
malloc T754 12
assignw BASE[12] T754
assignw T755 BASE[0]
param T756 0
assignw T756[0] T755
assignw T758 BASE[4]
assignw T759 T758[0]
assignw T760 1
mult T760 T760 T759
add T760 T760 4
malloc T757 T760
memcpy T757 T758 T760
param T761 4
assignw T761[0] T757
call T762 Function13 2
assignw BASE[16] T762
assignw T763 BASE[12]
assignw T764 T763[0]
assignw T765 BASE[0]
assignw T766 T765[0]
assignw T767 T766[0]
assignw T768 T767[0]
assignw T769 BASE[16]
mult T770 4 T769
add T770 T770 4
assignw T771 T768[T770]
assignw T764[0] T771
assignw T772 BASE[0]
assignw T773 T772[0]
assignw T774 T773[0]
assignw T775 T774[0]
assignw T776 BASE[16]
mult T777 4 T776
add T777 T777 4
assignw T778 BASE[12]
assignw T775[T777] T778
goto B1690
@label B1690
assignw T779 BASE[12]
assignw T780 T779[0]
assignw f20 BASE[8]
assignw T780[8] f20
@label Function15_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function16 28
assignw T781 0
assignw BASE[4] T781
assignw T782 32
assignw T783 T782
assignw T784 BASE[12]
assignw T785 1
mult T785 T785 T783
add T785 T785 4
malloc T784 T785
assignw T784[0] T783
assignw T784[0] T784
@label L56
assignw T786 BASE[0]
assignw T787 T786[0]
assignw T788 BASE[4]
assignw T789 T787[4]
lt test T788 T789
goif B1718 test
goto Function16_end
@label B1718
assignw T790 BASE[0]
assignw T791 T790[0]
assignw T792 T791[0]
assignw T793 T792[0]
assignw T794 BASE[4]
mult T795 4 T794
add T795 T795 4
assignw T796 T793[T795]
assignw BASE[8] T796
@label L57
assignw T797 BASE[8]
assignw T798 T797[0]
assignw T799 0
assignw T800 T798[4]
mult T801 1 T799
add T801 T801 4
@label L58
assignb T802 0
assignb T803 T800[T801]
neq test T803 T802
goif B1740 test
goto B1842
@label B1740
assignw S3[0] 12
assignw T805 BASE[8]
assignw T806 T805[0]
assignw T807 1
assignw T808 T807
assignw T809 BASE[16]
assignw T810 4
mult T810 T810 T808
add T810 T810 4
malloc T809 T810
assignw T809[0] T808
assignw T809[0] T809
@label L59
sub T810 T810 4
lt test T810 0
goif L59_end test
goto L59
@label L59_end
assignw T811 BASE[16]
assignw T812 T806[4]
assignw T811[4] T812
assignw T813 BASE[8]
assignw T814 T813[0]
assignw T815 1
assignw T816 T815
assignw T817 BASE[20]
assignw T818 4
mult T818 T818 T816
add T818 T818 4
malloc T817 T818
assignw T817[0] T816
assignw T817[0] T817
assignw T819 BASE[20]
assignw f21 T814[8]
assignw T819[4] f21
assignb T820 10
assignw T821 1
assignw T822 T821
assignw T823 BASE[24]
assignw T824 1
mult T824 T824 T822
add T824 T824 4
malloc T823 T824
assignw T823[0] T822
assignw T823[0] T823
assignw T825 BASE[24]
assignb T825[4] T820
param T826 0
assignw T826[0] S3
assignw T828 BASE[24]
assignw T829 T828[0]
assignw T830 1
mult T830 T830 T829
add T830 T830 4
malloc T827 T830
memcpy T827 T828 T830
param T831 4
assignw T831[0] T827
assignb A0[0] 1
assignb A0[1] 0
assignw T833 BASE[20]
assignw T834 T833[0]
assignw T835 4
mult T835 T835 T834
add T835 T835 4
malloc T832 T835
memcpy T832 T833 T835
param T836 12
assignw T836[0] T832
assignb A0[2] 1
assignw T838 BASE[16]
assignw T839 T838[0]
assignw T840 4
mult T840 T840 T839
add T840 T840 4
malloc T837 T840
assignw T841 T840
@label L60
sub T841 T841 4
lt test T841 0
goif L60_end test
assignw T842 T838[T841]
assignw T843 T837[T841]
assignw T844 T842[0]
assignw T845 1
mult T845 T845 T844
add T845 T845 4
malloc T843 T845
assignw T843[0] T843
memcpy T843 T842 T845
goto L60
@label L60_end
param T846 16
assignw T846[0] T837
assignb A0[3] 1
assignb A0[4] 0
call T847 PRINT 6
assignw T848 BASE[8]
assignw T849 T848[0]
assignw T850 T849[0]
assignw BASE[8] T850
goto L57
@label B1842
assignw T851 1
assignw T853 BASE[4]
add T852 T853 T851
assignw BASE[4] T852
goto L56
@label Function16_end
assignw lastbase BASE
return 0
@endfunction 28
assignw T854 33792
assignw T855 T854
assignw T856 1024
assignw T857 T856
assignw T858 32
assignw T859 T858
assignw T860 0
assignw T861 0
assignw T862 1
minus T863 T862
assignb A12[0] 0
assignb A12[1] 0
call T864 Function11 2
assignw T865 T864
assignw S4[0] 26
assignw T868 S4
assignw T870 T868[0]
assignw T871 1
mult T871 T871 T870
add T871 T871 4
malloc T869 T871
memcpy T869 T868 T871
param T872 0
assignw T872[0] T869
assignb A1[0] 0
call T873 Function0 2
assignw T874 T873
assignw T875 0
assignw T877 T875
@label L61
geq test T877 T874
goif L61_end test
assignw T876 T877
mult T878 1 T876
add T878 T878 4
assignw T879 1
assignw T881 T879
assignw T882 1
mult T882 T882 T881
add T882 T882 4
malloc T880 T882
assignw T880[0] T881
assignb T883 T868[T878]
assignb T880[4] T883
assignw f22 0.000000
param T884 0
assignw T884[0] T865
assignw T886 T880[0]
assignw T887 1
mult T887 T887 T886
add T887 T887 4
malloc T885 T887
memcpy T885 T880 T887
param T888 4
assignw T888[0] T885
param T889 8
assignw T889[0] f22
call T890 Function15 3
add T877 T877 1
goto L61
@label L61_end
assignw T893 T855
assignw T894 1
mult T894 T894 T893
add T894 T894 4
malloc T892 T894
assignw T892[0] T893
assignw T896 T859
assignw T897 1
mult T897 T897 T896
add T897 T897 4
malloc T895 T897
assignw T895[0] T896
malloc T899 24
assignw T900 T857
assignw T901 T899[0]
assignw T902 4
mult T902 T902 T900
add T902 T902 4
malloc T901 T902
assignw T901[0] T900
assignw T901[0] T901
@label L62
sub T902 T902 4
lt test T902 0
goif L62_end test
assignw T903 T859
assignw T904 T901[T902]
assignw T905 1
mult T905 T905 T903
add T905 T905 4
malloc T904 T905
assignw T904[0] T903
assignw T904[0] T904
goto L62
@label L62_end
assignw T906 T857
assignw T907 T899[12]
assignw T908 4
mult T908 T908 T906
add T908 T908 4
malloc T907 T908
assignw T907[0] T906
assignw T907[0] T907
assignw T909 T899
@label L63
goto B1958
@label B1958
assignw S5[0] 6
param T911 0
assignw T911[0] S5
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T912 PRINT 6
param T913 0
assignw T913[0] T892
call T914 READ 1
assignw S6[0] 4
assignw T917 T892[0]
assignw T918 1
mult T918 T918 T917
add T918 T918 4
malloc T916 T918
memcpy T916 T892 T918
param T919 0
assignw T919[0] T916
param T920 4
assignw T920[0] S6
call T921 Function1 2
@label L64
assignw T922 0
eq test T921 T922
goif B1987 test
goto B1989
@label B1987
goto B2058
goto B1989
@label B1989
assignw T923 T909[0]
assignb T924 32
assignw T926 T892[0]
assignw T927 1
mult T927 T927 T926
add T927 T927 4
malloc T925 T927
memcpy T925 T892 T927
param T928 0
assignw T928[0] T925
assignw T929 T923[0]
param T930 4
assignw T930[0] T929
param T931 8
assignb T931[0] T924
call T932 Function5 3
assignw T898 T932
assignw T933 T909[0]
assignw T934 T933[0]
mult T935 4 T898
add T935 T935 4
assignw S7[0] 1
assignw T937 T934[T935]
param T938 0
assignw T938[0] T937
param T939 4
assignw T939[0] S7
call T940 Function2 2
param T941 0
assignw T941[0] T909
assignw T943 T895[0]
assignw T944 1
mult T944 T944 T943
add T944 T944 4
malloc T942 T944
memcpy T942 T895 T944
param T945 4
assignw T945[0] T942
call T946 Function22  2
assignw T948 T895[0]
assignw T949 1
mult T949 T949 T948
add T949 T949 4
malloc T947 T949
memcpy T947 T895 T949
param T950 0
assignw T950[0] T947
assignb A1[0] 0
call T951 Function0 2
assignw T952 0
gt test T951 T952
goif B2042 test
goto L63
@label B2042
assignw T954 T895[0]
assignw T955 1
mult T955 T955 T954
add T955 T955 4
malloc T953 T955
memcpy T953 T895 T955
param T956 0
assignw T956[0] T953
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T957 PRINT 6
goto L63
goto L63
@label B2058
assignw T958 T909[0]
assignw T959 T958[0]
assignw T960 4
mult T960 T960 T959
@label L65
sub T960 T960 4
lt test T960 0
goif L65_end test
assignw T961 T958[T960]
free T961
goto L65
@label L65_end
free T958
assignw T962 T909[12]
free T962
free T909
@function Function17 8
assignw T964 BASE[0]
assignw T965 T964[0]
assignw T966 BASE[0]
assignw T967 T966[0]
assignw T968 T965[0]
assignw T969 T967[4]
mult T970 4 T969
add T970 T970 4
assignw T972 BASE[4]
assignw T973 T972[0]
assignw T974 1
mult T974 T974 T973
add T974 T974 4
malloc T971 T974
memcpy T971 T972 T974
param T975 0
assignw T975[0] T971
assignw T977 T968[T970]
assignw T978 T977[0]
assignw T979 1
mult T979 T979 T978
add T979 T979 4
malloc T976 T979
memcpy T976 T977 T979
param T980 4
assignw T980[0] T976
call T981 Function1 2
@label L66
assignw T982 0
eq test T981 T982
goif B2107 test
goto B2123
@label B2107
assignw T983 BASE[0]
assignw T984 T983[0]
assignw T985 BASE[0]
assignw T986 T985[0]
assignw T987 1
assignw T989 T986[4]
add T988 T989 T987
assignw T984[4] T988
goto B2116
@label B2116
assignb T990 True
goto Bool2119
assignb T990 False
@label Bool2119
assignw lastbase BASE
return T990
goto B2123
@label B2123
goto B2126
assignb T991 True
goto Bool2127
@label B2126
assignb T991 False
@label Bool2127
assignw lastbase BASE
return T991
@label Function17_end
assignw lastbase BASE
return 0
@endfunction 8
@function Function18 8
assignb T992 A19[0]
goif L67 T992
assignw T993 0
assignw BASE[4] T993
@label L67
assignw T995 BASE[0]
assignw T996 T995[0]
assignw T998 T996[4]
assignw T999 BASE[4]
add T997 T998 T999
assignw T1000 BASE[0]
assignw T1001 T1000[0]
assignw T1002 T1001[8]
lt test T997 T1002
goif B2151 test
goto B2165
@label B2151
assignw T1003 BASE[0]
assignw T1004 T1003[0]
assignw T1005 BASE[0]
assignw T1006 T1005[0]
assignw T1008 T1006[4]
assignw T1009 BASE[4]
add T1007 T1008 T1009
assignw T1010 T1004[0]
mult T1011 4 T1007
add T1011 T1011 4
assignw T1012 T1010[T1011]
assignw lastbase BASE
return T1012
goto B2165
@label B2165
assignw T1013 BASE[4]
assignw lastbase BASE
return T1013
@label Function18_end
assignw lastbase BASE
return 0
@endfunction 8
@function Function19 4
assignw T1014 BASE[0]
assignw T1015 T1014[0]
assignw T1016 T1015[16]
assignw T1017 BASE[28]
geq test T1016 T1017
goif B2180 test
goto B2192
@label B2180
assignw S8[0] 34
param T1019 0
assignw T1019[0] S8
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1020 PRINT 6
assignw T1021 1
exit T1021
goto B2192
@label B2192
assignw T1022 BASE[0]
assignw T1023 T1022[0]
assignw T1024 BASE[0]
assignw T1025 T1024[0]
assignw T1026 T1023[12]
assignw T1027 T1025[16]
mult T1028 4 T1027
add T1028 T1028 4
malloc T1029 8
assignw T1030 T859
assignw T1031 T1029[0]
assignw T1032 1
mult T1032 T1032 T1030
add T1032 T1032 4
malloc T1031 T1032
assignw T1031[0] T1030
assignw T1031[0] T1031
assignw T1033 T859
assignw T1034 T1029[4]
assignw T1035 1
mult T1035 T1035 T1033
add T1035 T1035 4
malloc T1034 T1035
assignw T1034[0] T1033
assignw T1034[0] T1034
assignw T1026[T1028] T1029
assignw T1036 BASE[0]
assignw T1037 T1036[0]
assignw T1038 BASE[0]
assignw T1039 T1038[0]
assignw T1040 1
assignw T1042 T1039[16]
add T1041 T1042 T1040
assignw T1037[16] T1041
@label Function19_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function20 4
assignw T1043 BASE[0]
assignw T1044 T1043[0]
assignw T1045 BASE[0]
assignw T1046 T1045[0]
assignw T1047 1
assignw T1049 T1046[16]
sub T1048 T1049 T1047
assignw T1050 T1044[12]
mult T1051 4 T1048
add T1051 T1051 4
assignw T1052 T1050[T1051]
assignw T1053 T1052[0]
free T1053
assignw T1054 T1052[4]
free T1054
free T1052
assignw T1055 BASE[0]
assignw T1056 T1055[0]
assignw T1057 BASE[0]
assignw T1058 T1057[0]
assignw T1059 1
assignw T1061 T1058[16]
sub T1060 T1061 T1059
assignw T1056[16] T1060
@label Function20_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function21 4
@label L68
assignw T1062 BASE[0]
assignw T1063 T1062[0]
assignw T1064 0
assignw T1065 T1063[4]
gt test T1065 T1064
goif B2268 test
goto Function21_end
@label B2268
assignw T1066 BASE[0]
param T1067 0
assignw T1067[0] T1066
call T1068 Function20 1
goto L68
@label Function21_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function22 12
assignw T1071 BASE[0]
param T1072 0
assignw T1072[0] T1071
assignb A19[0] 0
call T1073 Function18 2
assignw BASE[8] T1073
assignb T1074 48
assignw T1075 0
assignw T1076 BASE[8]
mult T1077 1 T1075
add T1077 T1077 4
assignw T1078 T1076[T1077]
leq test T1074 T1078
goif B2293 test
goto B2302
@label B2293
assignw T1079 0
assignw T1080 BASE[8]
mult T1081 1 T1079
add T1081 T1081 4
assignb T1082 57
assignw T1083 T1080[T1081]
leq test T1083 T1082
goif B2338 test
goto B2302
@label B2302
assignb T1084 97
assignw T1085 0
assignw T1086 BASE[8]
mult T1087 1 T1085
add T1087 T1087 4
assignw T1088 T1086[T1087]
leq test T1084 T1088
goif B2311 test
goto B2320
@label B2311
assignw T1089 0
assignw T1090 BASE[8]
mult T1091 1 T1089
add T1091 T1091 4
assignb T1092 122
assignw T1093 T1090[T1091]
leq test T1093 T1092
goif B2338 test
goto B2320
@label B2320
assignw S9[0] 1
assignw T1096 BASE[8]
assignw T1097 T1096[0]
assignw T1098 1
mult T1098 T1098 T1097
add T1098 T1098 4
malloc T1095 T1098
memcpy T1095 T1096 T1098
param T1099 0
assignw T1099[0] T1095
param T1100 4
assignw T1100[0] S9
call T1101 Function1 2
@label L69
assignw T1102 0
eq test T1101 T1102
goif B2338 test
goto B2418
@label B2338
assignw T1103 BASE[0]
param T1104 0
assignw T1104[0] T1103
call T1105 Function19 1
assignw T1106 BASE[0]
param T1107 0
assignw T1107[0] T1106
call T1108 Function23  1
goif B2359 T1108
goto B2348
@label B2348
assignw T1109 BASE[0]
param T1110 0
assignw T1110[0] T1109
call T1111 Function21 1
assignw T1112 0
assignw T1113 BASE[4]
mult T1114 1 T1112
add T1114 T1114 4
assignb T1115 0
assignb T1113[T1114] T1115
goto B2359
@label B2359
assignw S10[0] 1
assignw T1117 BASE[0]
param T1118 0
assignw T1118[0] T1117
param T1119 4
assignw T1119[0] S10
call T1120 Function17 2
goif B2388 T1120
goto B2368
@label B2368
assignw S11[0] 34
param T1122 0
assignw T1122[0] S11
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1123 PRINT 6
assignw T1124 BASE[0]
param T1125 0
assignw T1125[0] T1124
call T1126 Function21 1
assignw T1127 0
assignw T1128 BASE[4]
mult T1129 1 T1127
add T1129 T1129 4
assignb T1130 0
assignb T1128[T1129] T1130
goto B2388
@label B2388
assignw T1131 BASE[0]
assignw T1132 T1131[0]
assignw T1133 BASE[0]
assignw T1134 T1133[0]
assignw T1135 1
assignw T1137 T1134[16]
sub T1136 T1137 T1135
assignw T1138 T1132[12]
mult T1139 4 T1136
add T1139 T1139 4
assignw T1140 T1138[T1139]
assignw T1141 T1140[0]
assignw T1142 BASE[4]
param T1143 0
assignw T1143[0] T1142
assignw T1145 T1141[4]
assignw T1146 T1145[0]
assignw T1147 1
mult T1147 T1147 T1146
add T1147 T1147 4
malloc T1144 T1147
memcpy T1144 T1145 T1147
param T1148 4
assignw T1148[0] T1144
call T1149 Function2 2
assignw T1150 BASE[0]
param T1151 0
assignw T1151[0] T1150
call T1152 Function20 1
goto Function22_end
@label B2418
assignw S12[0] 34
param T1154 0
assignw T1154[0] S12
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1155 PRINT 6
assignw T1156 BASE[0]
param T1157 0
assignw T1157[0] T1156
call T1158 Function21 1
assignw T1159 0
assignw T1160 BASE[4]
mult T1161 1 T1159
add T1161 T1161 4
assignb T1162 0
assignb T1160[T1161] T1162
@label Function22_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function23 16
assignw T1164 BASE[0]
param T1165 0
assignw T1165[0] T1164
assignb A19[0] 0
call T1166 Function18 2
assignw T1167 1
assignw T1168 BASE[0]
param T1169 0
assignw T1169[0] T1168
param T1170 4
assignw T1170[0] T1167
assignb A19[0] 1
call T1171 Function18 2
assignw BASE[4] T1166
assignw BASE[8] T1171
assignb T1172 97
assignw T1173 0
assignw T1174 BASE[4]
mult T1175 1 T1173
add T1175 T1175 4
assignw T1176 T1174[T1175]
leq test T1172 T1176
goif B2466 test
goto B2642
@label B2466
assignw T1177 0
assignw T1178 BASE[4]
mult T1179 1 T1177
add T1179 T1179 4
assignb T1180 122
assignw T1181 T1178[T1179]
leq test T1181 T1180
goif B2475 test
goto B2642
@label B2475
assignw T1183 BASE[4]
assignw T1184 T1183[0]
assignw T1185 1
mult T1185 T1185 T1184
add T1185 T1185 4
malloc T1182 T1185
memcpy T1182 T1183 T1185
param T1186 0
assignw T1186[0] T1182
assignb A1[0] 0
call T1187 Function0 2
@label L70
assignw T1188 1
eq test T1187 T1188
goif B2491 test
goto B2642
@label B2491
assignw S13[0] 1
assignw T1191 BASE[8]
assignw T1192 T1191[0]
assignw T1193 1
mult T1193 T1193 T1192
add T1193 T1193 4
malloc T1190 T1193
memcpy T1190 T1191 T1193
param T1194 0
assignw T1194[0] T1190
param T1195 4
assignw T1195[0] S13
call T1196 Function1 2
@label L71
assignw T1197 0
eq test T1196 T1197
goif B2509 test
goto B2642
@label B2509
assignw T1198 BASE[0]
param T1199 0
assignw T1199[0] T1198
assignw T1201 BASE[4]
assignw T1202 T1201[0]
assignw T1203 1
mult T1203 T1203 T1202
add T1203 T1203 4
malloc T1200 T1203
memcpy T1200 T1201 T1203
param T1204 4
assignw T1204[0] T1200
call T1205 Function17 2
goif B2524 T1205
goto B2524
@label B2524
assignw T1206 BASE[0]
param T1207 0
assignw T1207[0] T1206
assignw T1209 BASE[8]
assignw T1210 T1209[0]
assignw T1211 1
mult T1211 T1211 T1210
add T1211 T1211 4
malloc T1208 T1211
memcpy T1208 T1209 T1211
param T1212 4
assignw T1212[0] T1208
call T1213 Function17 2
goif B2539 T1213
goto B2539
@label B2539
assignw T1214 BASE[0]
param T1215 0
assignw T1215[0] T1214
call T1216 Function19 1
assignw T1217 BASE[0]
param T1218 0
assignw T1218[0] T1217
call T1219 Function24  1
goif B2557 T1219
goto B2549
@label B2549
goto B2552
assignb T1220 True
goto Bool2553
@label B2552
assignb T1220 False
@label Bool2553
assignw lastbase BASE
return T1220
goto B2557
@label B2557
assignw T1221 BASE[0]
assignw T1222 T1221[0]
assignw T1223 BASE[0]
assignw T1224 T1223[0]
assignw T1225 1
assignw T1227 T1224[16]
sub T1226 T1227 T1225
assignw T1228 T1222[12]
mult T1229 4 T1226
add T1229 T1229 4
assignw T1230 T1228[T1229]
assignw T1231 T1230[0]
assignw T1233 T1231[4]
assignw T1234 T1233[0]
assignw T1235 1
mult T1235 T1235 T1234
add T1235 T1235 4
malloc T1232 T1235
memcpy T1232 T1233 T1235
param T1236 0
assignw T1236[0] T1232
assignw f23 BASE[12]
param T1237 4
assignw T1237[0] f23
call T1238 Function8 2
goif B2584 T1238
goto B2584
@label B2584
assignw T1239 BASE[0]
assignw T1240 T1239[0]
assignw T1241 BASE[0]
assignw T1242 T1241[0]
assignw T1243 2
assignw T1245 T1242[16]
sub T1244 T1245 T1243
assignw T1246 T1240[12]
mult T1247 4 T1244
add T1247 T1247 4
assignw T1248 T1246[T1247]
assignw T1249 T1248[0]
assignw T1250 BASE[0]
assignw T1251 T1250[0]
assignw T1252 BASE[0]
assignw T1253 T1252[0]
assignw T1254 1
assignw T1256 T1253[16]
sub T1255 T1256 T1254
assignw T1257 T1251[12]
mult T1258 4 T1255
add T1258 T1258 4
assignw T1259 T1257[T1258]
assignw T1260 T1259[0]
assignw T1261 T1249[4]
param T1262 0
assignw T1262[0] T1261
assignw T1264 T1260[4]
assignw T1265 T1264[0]
assignw T1266 1
mult T1266 T1266 T1265
add T1266 T1266 4
malloc T1263 T1266
memcpy T1263 T1264 T1266
param T1267 4
assignw T1267[0] T1263
call T1268 Function2 2
assignw T1269 BASE[36]
param T1270 0
assignw T1270[0] T1269
assignw T1272 BASE[4]
assignw T1273 T1272[0]
assignw T1274 1
mult T1274 T1274 T1273
add T1274 T1274 4
malloc T1271 T1274
memcpy T1271 T1272 T1274
param T1275 4
assignw T1275[0] T1271
assignw f24 BASE[12]
param T1276 8
assignw T1276[0] f24
call T1277 Function15 3
assignw T1278 BASE[0]
param T1279 0
assignw T1279[0] T1278
call T1280 Function20 1
goto B2772
@label B2642
assignb T1281 48
assignw T1282 0
assignw T1283 BASE[4]
mult T1284 1 T1282
add T1284 T1284 4
assignw T1285 T1283[T1284]
leq test T1281 T1285
goif B2651 test
goto B2660
@label B2651
assignw T1286 0
assignw T1287 BASE[4]
mult T1288 1 T1286
add T1288 T1288 4
assignb T1289 57
assignw T1290 T1287[T1288]
leq test T1290 T1289
goif B2696 test
goto B2660
@label B2660
assignb T1291 97
assignw T1292 0
assignw T1293 BASE[4]
mult T1294 1 T1292
add T1294 T1294 4
assignw T1295 T1293[T1294]
leq test T1291 T1295
goif B2669 test
goto B2678
@label B2669
assignw T1296 0
assignw T1297 BASE[4]
mult T1298 1 T1296
add T1298 T1298 4
assignb T1299 122
assignw T1300 T1297[T1298]
leq test T1300 T1299
goif B2696 test
goto B2678
@label B2678
assignw S14[0] 1
assignw T1303 BASE[4]
assignw T1304 T1303[0]
assignw T1305 1
mult T1305 T1305 T1304
add T1305 T1305 4
malloc T1302 T1305
memcpy T1302 T1303 T1305
param T1306 0
assignw T1306[0] T1302
param T1307 4
assignw T1307[0] S14
call T1308 Function1 2
@label L72
assignw T1309 0
eq test T1308 T1309
goif B2696 test
goto B2756
@label B2696
assignw T1310 BASE[0]
param T1311 0
assignw T1311[0] T1310
call T1312 Function19 1
assignw T1313 BASE[0]
param T1314 0
assignw T1314[0] T1313
call T1315 Function24  1
goif B2714 T1315
goto B2706
@label B2706
goto B2709
assignb T1316 True
goto Bool2710
@label B2709
assignb T1316 False
@label Bool2710
assignw lastbase BASE
return T1316
goto B2714
@label B2714
assignw T1317 BASE[0]
assignw T1318 T1317[0]
assignw T1319 BASE[0]
assignw T1320 T1319[0]
assignw T1321 2
assignw T1323 T1320[16]
sub T1322 T1323 T1321
assignw T1324 T1318[12]
mult T1325 4 T1322
add T1325 T1325 4
assignw T1326 T1324[T1325]
assignw T1327 T1326[0]
assignw T1328 BASE[0]
assignw T1329 T1328[0]
assignw T1330 BASE[0]
assignw T1331 T1330[0]
assignw T1332 1
assignw T1334 T1331[16]
sub T1333 T1334 T1332
assignw T1335 T1329[12]
mult T1336 4 T1333
add T1336 T1336 4
assignw T1337 T1335[T1336]
assignw T1338 T1337[0]
assignw T1339 T1327[4]
param T1340 0
assignw T1340[0] T1339
assignw T1342 T1338[4]
assignw T1343 T1342[0]
assignw T1344 1
mult T1344 T1344 T1343
add T1344 T1344 4
malloc T1341 T1344
memcpy T1341 T1342 T1344
param T1345 4
assignw T1345[0] T1341
call T1346 Function2 2
assignw T1347 BASE[0]
param T1348 0
assignw T1348[0] T1347
call T1349 Function20 1
goto B2772
@label B2756
assignw S15[0] 34
param T1351 0
assignw T1351[0] S15
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1352 PRINT 6
goto B2768
assignb T1353 True
goto Bool2769
@label B2768
assignb T1353 False
@label Bool2769
assignw lastbase BASE
return T1353
@label B2772
goto B2773
@label B2773
assignb T1354 True
goto Bool2776
assignb T1354 False
@label Bool2776
assignw lastbase BASE
return T1354
@label Function23_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function24 20
assignw T1356 BASE[0]
param T1357 0
assignw T1357[0] T1356
assignb A19[0] 0
call T1358 Function18 2
assignw BASE[4] T1358
assignb T1359 48
assignw T1360 0
assignw T1361 BASE[4]
mult T1362 1 T1360
add T1362 T1362 4
assignw T1363 T1361[T1362]
leq test T1359 T1363
goif B2799 test
goto B2808
@label B2799
assignw T1364 0
assignw T1365 BASE[4]
mult T1366 1 T1364
add T1366 T1366 4
assignb T1367 57
assignw T1368 T1365[T1366]
leq test T1368 T1367
goif B2844 test
goto B2808
@label B2808
assignb T1369 97
assignw T1370 0
assignw T1371 BASE[4]
mult T1372 1 T1370
add T1372 T1372 4
assignw T1373 T1371[T1372]
leq test T1369 T1373
goif B2817 test
goto B2826
@label B2817
assignw T1374 0
assignw T1375 BASE[4]
mult T1376 1 T1374
add T1376 T1376 4
assignb T1377 122
assignw T1378 T1375[T1376]
leq test T1378 T1377
goif B2844 test
goto B2826
@label B2826
assignw S16[0] 1
assignw T1381 BASE[4]
assignw T1382 T1381[0]
assignw T1383 1
mult T1383 T1383 T1382
add T1383 T1383 4
malloc T1380 T1383
memcpy T1380 T1381 T1383
param T1384 0
assignw T1384[0] T1380
param T1385 4
assignw T1385[0] S16
call T1386 Function1 2
@label L73
assignw T1387 0
eq test T1386 T1387
goif B2844 test
goto B3138
@label B2844
assignw T1388 BASE[0]
param T1389 0
assignw T1389[0] T1388
call T1390 Function19 1
assignw T1391 BASE[0]
param T1392 0
assignw T1392[0] T1391
call T1393 Function25  1
goif B2862 T1393
goto B2854
@label B2854
goto B2857
assignb T1394 True
goto Bool2858
@label B2857
assignb T1394 False
@label Bool2858
assignw lastbase BASE
return T1394
goto B2862
@label B2862
assignw T1395 BASE[0]
assignw T1396 T1395[0]
assignw T1397 BASE[0]
assignw T1398 T1397[0]
assignw T1399 2
assignw T1401 T1398[16]
sub T1400 T1401 T1399
assignw T1402 T1396[12]
mult T1403 4 T1400
add T1403 T1403 4
assignw T1404 T1402[T1403]
assignw T1405 T1404[0]
assignw T1406 BASE[0]
assignw T1407 T1406[0]
assignw T1408 BASE[0]
assignw T1409 T1408[0]
assignw T1410 1
assignw T1412 T1409[16]
sub T1411 T1412 T1410
assignw T1413 T1407[12]
mult T1414 4 T1411
add T1414 T1414 4
assignw T1415 T1413[T1414]
assignw T1416 T1415[0]
assignw T1417 T1405[4]
param T1418 0
assignw T1418[0] T1417
assignw T1420 T1416[4]
assignw T1421 T1420[0]
assignw T1422 1
mult T1422 T1422 T1421
add T1422 T1422 4
malloc T1419 T1422
memcpy T1419 T1420 T1422
param T1423 4
assignw T1423[0] T1419
call T1424 Function2 2
assignw T1425 BASE[0]
param T1426 0
assignw T1426[0] T1425
call T1427 Function20 1
assignw T1428 BASE[0]
param T1429 0
assignw T1429[0] T1428
assignb A19[0] 0
call T1430 Function18 2
assignw BASE[4] T1430
assignw S17[0] 1
assignw T1433 BASE[4]
assignw T1434 T1433[0]
assignw T1435 1
mult T1435 T1435 T1434
add T1435 T1435 4
malloc T1432 T1435
memcpy T1432 T1433 T1435
param T1436 0
assignw T1436[0] T1432
param T1437 4
assignw T1437[0] S17
call T1438 Function1 2
@label L74
assignw T1439 0
eq test T1438 T1439
goif B2945 test
goto B2927
@label B2927
assignw S18[0] 1
assignw T1442 BASE[4]
assignw T1443 T1442[0]
assignw T1444 1
mult T1444 T1444 T1443
add T1444 T1444 4
malloc T1441 T1444
memcpy T1441 T1442 T1444
param T1445 0
assignw T1445[0] T1441
param T1446 4
assignw T1446[0] S18
call T1447 Function1 2
@label L75
assignw T1448 0
eq test T1447 T1448
goif B2945 test
goto B3154
@label B2945
assignw T1449 BASE[0]
param T1450 0
assignw T1450[0] T1449
call T1451 Function19 1
assignw T1452 BASE[0]
param T1453 0
assignw T1453[0] T1452
assignw T1455 BASE[4]
assignw T1456 T1455[0]
assignw T1457 1
mult T1457 T1457 T1456
add T1457 T1457 4
malloc T1454 T1457
memcpy T1454 T1455 T1457
param T1458 4
assignw T1458[0] T1454
call T1459 Function17 2
goif B2964 T1459
goto B2964
@label B2964
assignw T1460 BASE[0]
param T1461 0
assignw T1461[0] T1460
call T1462 Function24 1
goif B2978 T1462
goto B2970
@label B2970
goto B2973
assignb T1463 True
goto Bool2974
@label B2973
assignb T1463 False
@label Bool2974
assignw lastbase BASE
return T1463
goto B2978
@label B2978
assignw S19[0] 1
assignw T1466 BASE[4]
assignw T1467 T1466[0]
assignw T1468 1
mult T1468 T1468 T1467
add T1468 T1468 4
malloc T1465 T1468
memcpy T1465 T1466 T1468
param T1469 0
assignw T1469[0] T1465
param T1470 4
assignw T1470[0] S19
call T1471 Function1 2
@label L76
assignw T1472 0
eq test T1471 T1472
goif B2996 test
goto B3055
@label B2996
assignw T1473 BASE[0]
assignw T1474 T1473[0]
assignw T1475 BASE[0]
assignw T1476 T1475[0]
assignw T1477 2
assignw T1479 T1476[16]
sub T1478 T1479 T1477
assignw T1480 T1474[12]
mult T1481 4 T1478
add T1481 T1481 4
assignw T1482 T1480[T1481]
assignw T1483 T1482[0]
assignw T1485 T1483[4]
assignw T1486 T1485[0]
assignw T1487 1
mult T1487 T1487 T1486
add T1487 T1487 4
malloc T1484 T1487
memcpy T1484 T1485 T1487
param T1488 0
assignw T1488[0] T1484
assignw f25 BASE[12]
param T1489 4
assignw T1489[0] f25
call T1490 Function8 2
goif B3023 T1490
goto B3023
@label B3023
assignw T1491 BASE[0]
assignw T1492 T1491[0]
assignw T1493 BASE[0]
assignw T1494 T1493[0]
assignw T1495 1
assignw T1497 T1494[16]
sub T1496 T1497 T1495
assignw T1498 T1492[12]
mult T1499 4 T1496
add T1499 T1499 4
assignw T1500 T1498[T1499]
assignw T1501 T1500[0]
assignw T1503 T1501[4]
assignw T1504 T1503[0]
assignw T1505 1
mult T1505 T1505 T1504
add T1505 T1505 4
malloc T1502 T1505
memcpy T1502 T1503 T1505
param T1506 0
assignw T1506[0] T1502
assignw f26 BASE[16]
param T1507 4
assignw T1507[0] f26
call T1508 Function8 2
goif B3050 T1508
goto B3050
@label B3050
assignw f28 BASE[12]
assignw f29 BASE[16]
add f27 f28 f29
assignw BASE[8] f27
goto B3113
@label B3055
assignw T1509 BASE[0]
assignw T1510 T1509[0]
assignw T1511 BASE[0]
assignw T1512 T1511[0]
assignw T1513 2
assignw T1515 T1512[16]
sub T1514 T1515 T1513
assignw T1516 T1510[12]
mult T1517 4 T1514
add T1517 T1517 4
assignw T1518 T1516[T1517]
assignw T1519 T1518[0]
assignw T1521 T1519[4]
assignw T1522 T1521[0]
assignw T1523 1
mult T1523 T1523 T1522
add T1523 T1523 4
malloc T1520 T1523
memcpy T1520 T1521 T1523
param T1524 0
assignw T1524[0] T1520
assignw f30 BASE[12]
param T1525 4
assignw T1525[0] f30
call T1526 Function8 2
goif B3082 T1526
goto B3082
@label B3082
assignw T1527 BASE[0]
assignw T1528 T1527[0]
assignw T1529 BASE[0]
assignw T1530 T1529[0]
assignw T1531 1
assignw T1533 T1530[16]
sub T1532 T1533 T1531
assignw T1534 T1528[12]
mult T1535 4 T1532
add T1535 T1535 4
assignw T1536 T1534[T1535]
assignw T1537 T1536[0]
assignw T1539 T1537[4]
assignw T1540 T1539[0]
assignw T1541 1
mult T1541 T1541 T1540
add T1541 T1541 4
malloc T1538 T1541
memcpy T1538 T1539 T1541
param T1542 0
assignw T1542[0] T1538
assignw f31 BASE[16]
param T1543 4
assignw T1543[0] f31
call T1544 Function8 2
goif B3109 T1544
goto B3109
@label B3109
assignw f33 BASE[12]
assignw f34 BASE[16]
sub f32 f33 f34
assignw BASE[8] f32
@label B3113
assignw T1545 BASE[0]
assignw T1546 T1545[0]
assignw T1547 BASE[0]
assignw T1548 T1547[0]
assignw T1549 2
assignw T1551 T1548[16]
sub T1550 T1551 T1549
assignw T1552 T1546[12]
mult T1553 4 T1550
add T1553 T1553 4
assignw T1554 T1552[T1553]
assignw T1555 T1554[0]
assignw T1556 T1555[4]
param T1557 0
assignw T1557[0] T1556
assignw f35 BASE[8]
param T1558 4
assignw T1558[0] f35
call T1559 Function10 2
assignw T1560 BASE[0]
param T1561 0
assignw T1561[0] T1560
call T1562 Function20 1
goto B3154
goto B3154
@label B3138
assignw S20[0] 34
param T1564 0
assignw T1564[0] S20
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1565 PRINT 6
goto B3150
assignb T1566 True
goto Bool3151
@label B3150
assignb T1566 False
@label Bool3151
assignw lastbase BASE
return T1566
@label B3154
goto B3155
@label B3155
assignb T1567 True
goto Bool3158
assignb T1567 False
@label Bool3158
assignw lastbase BASE
return T1567
@label Function24_end
assignw lastbase BASE
return 0
@endfunction 20
@function Function25 20
assignw T1569 BASE[0]
param T1570 0
assignw T1570[0] T1569
assignb A19[0] 0
call T1571 Function18 2
assignw BASE[4] T1571
assignb T1572 48
assignw T1573 0
assignw T1574 BASE[4]
mult T1575 1 T1573
add T1575 T1575 4
assignw T1576 T1574[T1575]
leq test T1572 T1576
goif B3181 test
goto B3190
@label B3181
assignw T1577 0
assignw T1578 BASE[4]
mult T1579 1 T1577
add T1579 T1579 4
assignb T1580 57
assignw T1581 T1578[T1579]
leq test T1581 T1580
goif B3226 test
goto B3190
@label B3190
assignb T1582 97
assignw T1583 0
assignw T1584 BASE[4]
mult T1585 1 T1583
add T1585 T1585 4
assignw T1586 T1584[T1585]
leq test T1582 T1586
goif B3199 test
goto B3208
@label B3199
assignw T1587 0
assignw T1588 BASE[4]
mult T1589 1 T1587
add T1589 T1589 4
assignb T1590 122
assignw T1591 T1588[T1589]
leq test T1591 T1590
goif B3226 test
goto B3208
@label B3208
assignw S21[0] 1
assignw T1594 BASE[4]
assignw T1595 T1594[0]
assignw T1596 1
mult T1596 T1596 T1595
add T1596 T1596 4
malloc T1593 T1596
memcpy T1593 T1594 T1596
param T1597 0
assignw T1597[0] T1593
param T1598 4
assignw T1598[0] S21
call T1599 Function1 2
@label L77
assignw T1600 0
eq test T1599 T1600
goif B3226 test
goto B3570
@label B3226
assignw T1601 BASE[0]
param T1602 0
assignw T1602[0] T1601
call T1603 Function19 1
assignw T1604 BASE[0]
param T1605 0
assignw T1605[0] T1604
call T1606 Function26  1
goif B3244 T1606
goto B3236
@label B3236
goto B3239
assignb T1607 True
goto Bool3240
@label B3239
assignb T1607 False
@label Bool3240
assignw lastbase BASE
return T1607
goto B3244
@label B3244
assignw T1608 BASE[0]
assignw T1609 T1608[0]
assignw T1610 BASE[0]
assignw T1611 T1610[0]
assignw T1612 2
assignw T1614 T1611[16]
sub T1613 T1614 T1612
assignw T1615 T1609[12]
mult T1616 4 T1613
add T1616 T1616 4
assignw T1617 T1615[T1616]
assignw T1618 T1617[0]
assignw T1619 BASE[0]
assignw T1620 T1619[0]
assignw T1621 BASE[0]
assignw T1622 T1621[0]
assignw T1623 1
assignw T1625 T1622[16]
sub T1624 T1625 T1623
assignw T1626 T1620[12]
mult T1627 4 T1624
add T1627 T1627 4
assignw T1628 T1626[T1627]
assignw T1629 T1628[0]
assignw T1630 T1618[4]
param T1631 0
assignw T1631[0] T1630
assignw T1633 T1629[4]
assignw T1634 T1633[0]
assignw T1635 1
mult T1635 T1635 T1634
add T1635 T1635 4
malloc T1632 T1635
memcpy T1632 T1633 T1635
param T1636 4
assignw T1636[0] T1632
call T1637 Function2 2
assignw T1638 BASE[0]
param T1639 0
assignw T1639[0] T1638
call T1640 Function20 1
assignw T1641 BASE[0]
param T1642 0
assignw T1642[0] T1641
assignb A19[0] 0
call T1643 Function18 2
assignw BASE[4] T1643
assignw S22[0] 1
assignw T1646 BASE[4]
assignw T1647 T1646[0]
assignw T1648 1
mult T1648 T1648 T1647
add T1648 T1648 4
malloc T1645 T1648
memcpy T1645 T1646 T1648
param T1649 0
assignw T1649[0] T1645
param T1650 4
assignw T1650[0] S22
call T1651 Function1 2
@label L78
assignw T1652 0
eq test T1651 T1652
goif B3327 test
goto B3309
@label B3309
assignw S23[0] 1
assignw T1655 BASE[4]
assignw T1656 T1655[0]
assignw T1657 1
mult T1657 T1657 T1656
add T1657 T1657 4
malloc T1654 T1657
memcpy T1654 T1655 T1657
param T1658 0
assignw T1658[0] T1654
param T1659 4
assignw T1659[0] S23
call T1660 Function1 2
@label L79
assignw T1661 0
eq test T1660 T1661
goif B3327 test
goto B3586
@label B3327
assignw T1662 BASE[0]
param T1663 0
assignw T1663[0] T1662
call T1664 Function19 1
assignw T1665 BASE[0]
param T1666 0
assignw T1666[0] T1665
assignw T1668 BASE[4]
assignw T1669 T1668[0]
assignw T1670 1
mult T1670 T1670 T1669
add T1670 T1670 4
malloc T1667 T1670
memcpy T1667 T1668 T1670
param T1671 4
assignw T1671[0] T1667
call T1672 Function17 2
goif B3346 T1672
goto B3346
@label B3346
assignw T1673 BASE[0]
param T1674 0
assignw T1674[0] T1673
call T1675 Function25 1
goif B3360 T1675
goto B3352
@label B3352
goto B3355
assignb T1676 True
goto Bool3356
@label B3355
assignb T1676 False
@label Bool3356
assignw lastbase BASE
return T1676
goto B3360
@label B3360
assignw S24[0] 1
assignw T1679 BASE[4]
assignw T1680 T1679[0]
assignw T1681 1
mult T1681 T1681 T1680
add T1681 T1681 4
malloc T1678 T1681
memcpy T1678 T1679 T1681
param T1682 0
assignw T1682[0] T1678
param T1683 4
assignw T1683[0] S24
call T1684 Function1 2
@label L80
assignw T1685 0
eq test T1684 T1685
goif B3378 test
goto B3437
@label B3378
assignw T1686 BASE[0]
assignw T1687 T1686[0]
assignw T1688 BASE[0]
assignw T1689 T1688[0]
assignw T1690 2
assignw T1692 T1689[16]
sub T1691 T1692 T1690
assignw T1693 T1687[12]
mult T1694 4 T1691
add T1694 T1694 4
assignw T1695 T1693[T1694]
assignw T1696 T1695[0]
assignw T1698 T1696[4]
assignw T1699 T1698[0]
assignw T1700 1
mult T1700 T1700 T1699
add T1700 T1700 4
malloc T1697 T1700
memcpy T1697 T1698 T1700
param T1701 0
assignw T1701[0] T1697
assignw f36 BASE[12]
param T1702 4
assignw T1702[0] f36
call T1703 Function8 2
goif B3405 T1703
goto B3405
@label B3405
assignw T1704 BASE[0]
assignw T1705 T1704[0]
assignw T1706 BASE[0]
assignw T1707 T1706[0]
assignw T1708 1
assignw T1710 T1707[16]
sub T1709 T1710 T1708
assignw T1711 T1705[12]
mult T1712 4 T1709
add T1712 T1712 4
assignw T1713 T1711[T1712]
assignw T1714 T1713[0]
assignw T1716 T1714[4]
assignw T1717 T1716[0]
assignw T1718 1
mult T1718 T1718 T1717
add T1718 T1718 4
malloc T1715 T1718
memcpy T1715 T1716 T1718
param T1719 0
assignw T1719[0] T1715
assignw f37 BASE[16]
param T1720 4
assignw T1720[0] f37
call T1721 Function8 2
goif B3432 T1721
goto B3432
@label B3432
assignw f39 BASE[12]
assignw f40 BASE[16]
mult f38 f39 f40
assignw BASE[8] f38
goto B3545
@label B3437
assignw T1722 BASE[0]
assignw T1723 T1722[0]
assignw T1724 BASE[0]
assignw T1725 T1724[0]
assignw T1726 1
assignw T1728 T1725[16]
sub T1727 T1728 T1726
assignw T1729 T1723[12]
mult T1730 4 T1727
add T1730 T1730 4
assignw T1731 T1729[T1730]
assignw T1732 T1731[0]
assignw T1734 T1732[4]
assignw T1735 T1734[0]
assignw T1736 1
mult T1736 T1736 T1735
add T1736 T1736 4
malloc T1733 T1736
memcpy T1733 T1734 T1736
param T1737 0
assignw T1737[0] T1733
assignw f41 BASE[8]
param T1738 4
assignw T1738[0] f41
call T1739 Function8 2
goif B3464 T1739
goto B3464
@label B3464
@label L81
assignw T1740 0
assignw T1741 BASE[8]
eq test T1741 T1740
goif B3470 test
goto B3487
@label B3470
assignw S25[0] 28
param T1743 0
assignw T1743[0] S25
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1744 PRINT 6
goto B3482
assignb T1745 True
goto Bool3483
@label B3482
assignb T1745 False
@label Bool3483
assignw lastbase BASE
return T1745
goto B3487
@label B3487
assignw T1746 BASE[0]
assignw T1747 T1746[0]
assignw T1748 BASE[0]
assignw T1749 T1748[0]
assignw T1750 2
assignw T1752 T1749[16]
sub T1751 T1752 T1750
assignw T1753 T1747[12]
mult T1754 4 T1751
add T1754 T1754 4
assignw T1755 T1753[T1754]
assignw T1756 T1755[0]
assignw T1758 T1756[4]
assignw T1759 T1758[0]
assignw T1760 1
mult T1760 T1760 T1759
add T1760 T1760 4
malloc T1757 T1760
memcpy T1757 T1758 T1760
param T1761 0
assignw T1761[0] T1757
assignw f42 BASE[12]
param T1762 4
assignw T1762[0] f42
call T1763 Function8 2
goif B3514 T1763
goto B3514
@label B3514
assignw T1764 BASE[0]
assignw T1765 T1764[0]
assignw T1766 BASE[0]
assignw T1767 T1766[0]
assignw T1768 1
assignw T1770 T1767[16]
sub T1769 T1770 T1768
assignw T1771 T1765[12]
mult T1772 4 T1769
add T1772 T1772 4
assignw T1773 T1771[T1772]
assignw T1774 T1773[0]
assignw T1776 T1774[4]
assignw T1777 T1776[0]
assignw T1778 1
mult T1778 T1778 T1777
add T1778 T1778 4
malloc T1775 T1778
memcpy T1775 T1776 T1778
param T1779 0
assignw T1779[0] T1775
assignw f43 BASE[16]
param T1780 4
assignw T1780[0] f43
call T1781 Function8 2
goif B3541 T1781
goto B3541
@label B3541
assignw f45 BASE[12]
assignw f46 BASE[16]
div f44 f45 f46
assignw BASE[8] f44
@label B3545
assignw T1782 BASE[0]
assignw T1783 T1782[0]
assignw T1784 BASE[0]
assignw T1785 T1784[0]
assignw T1786 2
assignw T1788 T1785[16]
sub T1787 T1788 T1786
assignw T1789 T1783[12]
mult T1790 4 T1787
add T1790 T1790 4
assignw T1791 T1789[T1790]
assignw T1792 T1791[0]
assignw T1793 T1792[4]
param T1794 0
assignw T1794[0] T1793
assignw f47 BASE[8]
param T1795 4
assignw T1795[0] f47
call T1796 Function10 2
assignw T1797 BASE[0]
param T1798 0
assignw T1798[0] T1797
call T1799 Function20 1
goto B3586
goto B3586
@label B3570
assignw S26[0] 34
param T1801 0
assignw T1801[0] S26
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1802 PRINT 6
goto B3582
assignb T1803 True
goto Bool3583
@label B3582
assignb T1803 False
@label Bool3583
assignw lastbase BASE
return T1803
@label B3586
goto B3587
@label B3587
assignb T1804 True
goto Bool3590
assignb T1804 False
@label Bool3590
assignw lastbase BASE
return T1804
@label Function25_end
assignw lastbase BASE
return 0
@endfunction 20
@function Function26 12
assignw T1806 BASE[0]
param T1807 0
assignw T1807[0] T1806
assignb A19[0] 0
call T1808 Function18 2
assignw BASE[4] T1808
assignw S27[0] 1
assignw T1811 BASE[4]
assignw T1812 T1811[0]
assignw T1813 1
mult T1813 T1813 T1812
add T1813 T1813 4
malloc T1810 T1813
memcpy T1810 T1811 T1813
param T1814 0
assignw T1814[0] T1810
param T1815 4
assignw T1815[0] S27
call T1816 Function1 2
@label L82
assignw T1817 0
eq test T1816 T1817
goif B3622 test
goto B3717
@label B3622
assignw S28[0] 1
assignw T1819 BASE[0]
param T1820 0
assignw T1820[0] T1819
param T1821 4
assignw T1821[0] S28
call T1822 Function17 2
goif B3631 T1822
goto B3631
@label B3631
assignw T1823 BASE[0]
param T1824 0
assignw T1824[0] T1823
call T1825 Function19 1
assignw T1826 BASE[0]
param T1827 0
assignw T1827[0] T1826
call T1828 Function24 1
goif B3649 T1828
goto B3641
@label B3641
goto B3644
assignb T1829 True
goto Bool3645
@label B3644
assignb T1829 False
@label Bool3645
assignw lastbase BASE
return T1829
goto B3649
@label B3649
assignw S29[0] 1
assignw T1831 BASE[0]
param T1832 0
assignw T1832[0] T1831
param T1833 4
assignw T1833[0] S29
call T1834 Function17 2
goif B3675 T1834
goto B3658
@label B3658
assignw S30[0] 34
param T1836 0
assignw T1836[0] S30
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1837 PRINT 6
goto B3670
assignb T1838 True
goto Bool3671
@label B3670
assignb T1838 False
@label Bool3671
assignw lastbase BASE
return T1838
goto B3675
@label B3675
assignw T1839 BASE[0]
assignw T1840 T1839[0]
assignw T1841 BASE[0]
assignw T1842 T1841[0]
assignw T1843 2
assignw T1845 T1842[16]
sub T1844 T1845 T1843
assignw T1846 T1840[12]
mult T1847 4 T1844
add T1847 T1847 4
assignw T1848 T1846[T1847]
assignw T1849 T1848[0]
assignw T1850 BASE[0]
assignw T1851 T1850[0]
assignw T1852 BASE[0]
assignw T1853 T1852[0]
assignw T1854 1
assignw T1856 T1853[16]
sub T1855 T1856 T1854
assignw T1857 T1851[12]
mult T1858 4 T1855
add T1858 T1858 4
assignw T1859 T1857[T1858]
assignw T1860 T1859[0]
assignw T1861 T1849[4]
param T1862 0
assignw T1862[0] T1861
assignw T1864 T1860[4]
assignw T1865 T1864[0]
assignw T1866 1
mult T1866 T1866 T1865
add T1866 T1866 4
malloc T1863 T1866
memcpy T1863 T1864 T1866
param T1867 4
assignw T1867[0] T1863
call T1868 Function2 2
assignw T1869 BASE[0]
param T1870 0
assignw T1870[0] T1869
call T1871 Function20 1
goto B3883
@label B3717
assignw T1873 BASE[4]
assignw T1874 T1873[0]
assignw T1875 1
mult T1875 T1875 T1874
add T1875 T1875 4
malloc T1872 T1875
memcpy T1872 T1873 T1875
param T1876 0
assignw T1876[0] T1872
call T1877 Function6 1
goif B3729 T1877
goto B3774
@label B3729
assignw T1878 BASE[0]
param T1879 0
assignw T1879[0] T1878
assignw T1881 BASE[4]
assignw T1882 T1881[0]
assignw T1883 1
mult T1883 T1883 T1882
add T1883 T1883 4
malloc T1880 T1883
memcpy T1880 T1881 T1883
param T1884 4
assignw T1884[0] T1880
call T1885 Function17 2
goif B3744 T1885
goto B3744
@label B3744
assignw T1886 BASE[0]
assignw T1887 T1886[0]
assignw T1888 BASE[0]
assignw T1889 T1888[0]
assignw T1890 2
assignw T1892 T1889[16]
sub T1891 T1892 T1890
assignw T1893 T1887[12]
mult T1894 4 T1891
add T1894 T1894 4
assignw T1895 T1893[T1894]
assignw T1896 T1895[0]
assignw T1897 T1896[4]
param T1898 0
assignw T1898[0] T1897
assignw T1900 BASE[4]
assignw T1901 T1900[0]
assignw T1902 1
mult T1902 T1902 T1901
add T1902 T1902 4
malloc T1899 T1902
memcpy T1899 T1900 T1902
param T1903 4
assignw T1903[0] T1899
call T1904 Function2 2
assignw T1905 BASE[0]
param T1906 0
assignw T1906[0] T1905
call T1907 Function20 1
goto B3883
@label B3774
assignb T1908 97
assignw T1909 0
assignw T1910 BASE[4]
mult T1911 1 T1909
add T1911 T1911 4
assignw T1912 T1910[T1911]
leq test T1908 T1912
goif B3783 test
goto B3867
@label B3783
assignw T1913 0
assignw T1914 BASE[4]
mult T1915 1 T1913
add T1915 T1915 4
assignb T1916 122
assignw T1917 T1914[T1915]
leq test T1917 T1916
goif B3792 test
goto B3867
@label B3792
assignw T1919 BASE[4]
assignw T1920 T1919[0]
assignw T1921 1
mult T1921 T1921 T1920
add T1921 T1921 4
malloc T1918 T1921
memcpy T1918 T1919 T1921
param T1922 0
assignw T1922[0] T1918
assignb A1[0] 0
call T1923 Function0 2
@label L83
assignw T1924 1
eq test T1923 T1924
goif B3808 test
goto B3867
@label B3808
assignw T1925 BASE[0]
param T1926 0
assignw T1926[0] T1925
assignw T1928 BASE[4]
assignw T1929 T1928[0]
assignw T1930 1
mult T1930 T1930 T1929
add T1930 T1930 4
malloc T1927 T1930
memcpy T1927 T1928 T1930
param T1931 4
assignw T1931[0] T1927
call T1932 Function17 2
goif B3823 T1932
goto B3823
@label B3823
assignw T1933 BASE[36]
param T1934 0
assignw T1934[0] T1933
assignw T1936 BASE[4]
assignw T1937 T1936[0]
assignw T1938 1
mult T1938 T1938 T1937
add T1938 T1938 4
malloc T1935 T1938
memcpy T1935 T1936 T1938
param T1939 4
assignw T1939[0] T1935
assignw f48 BASE[8]
param T1940 8
assignw T1940[0] f48
call T1941 Function14 3
assignw f49 lastbase[8]
assignw BASE[8] f49
goif B3843 T1941
goto B3843
@label B3843
assignw T1942 BASE[0]
assignw T1943 T1942[0]
assignw T1944 BASE[0]
assignw T1945 T1944[0]
assignw T1946 2
assignw T1948 T1945[16]
sub T1947 T1948 T1946
assignw T1949 T1943[12]
mult T1950 4 T1947
add T1950 T1950 4
assignw T1951 T1949[T1950]
assignw T1952 T1951[0]
assignw T1953 T1952[4]
param T1954 0
assignw T1954[0] T1953
assignw f50 BASE[8]
param T1955 4
assignw T1955[0] f50
call T1956 Function10 2
assignw T1957 BASE[0]
param T1958 0
assignw T1958[0] T1957
call T1959 Function20 1
goto B3883
@label B3867
assignw S31[0] 34
param T1961 0
assignw T1961[0] S31
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T1962 PRINT 6
goto B3879
assignb T1963 True
goto Bool3880
@label B3879
assignb T1963 False
@label Bool3880
assignw lastbase BASE
return T1963
@label B3883
goto B3884
@label B3884
assignb T1964 True
goto Bool3887
assignb T1964 False
@label Bool3887
assignw lastbase BASE
return T1964
@label Function26_end
assignw lastbase BASE
return 0
@endfunction 12
