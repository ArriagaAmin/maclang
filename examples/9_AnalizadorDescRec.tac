@string S0 "0000\n"
@string S1 "0000%s  =>  %f%c"
@string S2 "0000abcdefghijklmnopqrstuvwxyz"
@string S3 "0000calc> "
@string S4 "0000quit"
@string S5 "0000$"
@string S6 "0000Numero maximo de tokens alcanzado."
@string S7 "0000("
@string S8 "0000$"
@string S9 "0000No se pudo reconocer la expresion."
@string S10 "0000No se pudo reconocer la expresion."
@string S11 "0000="
@string S12 "0000("
@string S13 "0000No se pudo reconocer la expresion."
@string S14 "0000("
@string S15 "0000+"
@string S16 "0000-"
@string S17 "0000+"
@string S18 "0000No se pudo reconocer la expresion."
@string S19 "0000("
@string S20 "0000*"
@string S21 "0000/"
@string S22 "0000+"
@string S23 "0000No se puede dividir entre 0."
@string S24 "0000No se pudo reconocer la expresion."
@string S25 "0000("
@string S26 "0000("
@string S27 "0000)"
@string S28 "0000No se pudo reconocer la expresion."
@string S29 "0000No se pudo reconocer la expresion."
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
readf T4
return T4
@endfunction 0
@function CTOI 1
assignw T5 BASE[0]
return T5
@endfunction 1
@function ITOS 8
assignw T6 BASE[0]
assignw T7 BASE[4]
neq test T7 0
goif L0 test
assignb T6[0] 48
assignb T6[1] 0
return 1
@label L0
assignw T8 0
geq test T7 0
goif L1 test
mult T7 T7 -1
assignb T6[0] 45
add T8 T8 1
@label L1
assignw T9 8
@label L2
leq test T7 0
goif L3 test
mod T10 T7 10
div T7 T7 10
add T11 T10 48
assignb BASE[T9] T11
add T9 T9 1
goto L2
@label L3
leq test T9 8
goif L3_end test
sub T9 T9 1
assignb T12 BASE[T9]
assignb T6[T8] T12
add T8 T8 1
goto L3
@label L3_end
assignb T6[T8] 0
return T8
@endfunction 8
@function PRINT 24
assignw T13 0
assignw T14 0
assignw T15 0
assignw T16 0
assignw T17 0
assignw T18 BASE[0]
@label L4
assignb T19 T18[T13]
eq test T19 0
goif L4_end test
eq test T19 '%'
goif L5 test
printc T19
add T13 T13 1
goto L4
@label L5
assignb T19 T18[T13]
add T13 T13 1
eq test T19 'c'
goif L6 test
eq test T19 'i'
goif L7 test
eq test T19 'f'
goif L8 test
eq test T19 's'
goif L9 test
goto L4
@label L6
assignw T20 BASE[4]
assignb T21 T20[T14]
printc T21
add T14 T14 1
goto L4
@label L7
assignw T20 BASE[8]
assignw T22 T20[T15]
printi T22
add T15 T15 1
goto L4
@label L8
assignw T20 BASE[12]
assignw T23 T20[T16]
printf T23
add T16 T16 1
goto L4
@label L9
assignw T20 BASE[16]
assignw T24 T20[T17]
print T24
add T17 T17 1
goto L4
@label L4_end
assignw T20 BASE[20]
print T20
return 0
@endfunction 24
assignb T26 0
assignw T27 1
assignw T29 T27
assignw T30 1
mult T30 T30 T29
add T30 T30 4
malloc T28 T30
assignw T28[0] T29
assignb T28[4] T26
assignw T31 T28
assignb T33 10
assignw T34 1
assignw T36 T34
assignw T37 1
mult T37 T37 T36
add T37 T37 4
malloc T35 T37
assignw T35[0] T36
assignb T35[4] T33
assignw T38 T35
assignb T40 0
@function F0 12
assignw T41 0
assignw BASE[8] T41
@label L10
assignw T42 BASE[0]
assignw T43 BASE[8]
mult T44 1 T43
add T44 T44 4
@label L11
assignb T45 T42[T44]
assignb T46 BASE[4]
neq test T45 T46
goif B153 test
goto B158
@label B153
assignw T47 1
assignw T49 BASE[8]
add T48 T49 T47
assignw BASE[8] T48
goto L10
@label B158
assignw T50 BASE[8]
assignw lastbase BASE
return T50
@label F0_end
assignw lastbase BASE
return 0
@endfunction 12
@function F1 12
assignw T53 0
assignw BASE[8] T53
@label L12
assignw T54 BASE[0]
assignw T55 BASE[8]
mult T56 1 T55
add T56 T56 4
@label L13
assignb T57 0
assignb T58 T54[T56]
neq test T58 T57
goif B179 test
goto B198
@label B179
assignw T59 BASE[0]
assignw T60 BASE[8]
mult T61 1 T60
add T61 T61 4
@label L14
assignw T62 BASE[4]
assignw T63 BASE[8]
mult T64 1 T63
add T64 T64 4
assignb T65 T59[T61]
assignb T66 T62[T64]
eq test T65 T66
goif B193 test
goto B198
@label B193
assignw T67 1
assignw T69 BASE[8]
add T68 T69 T67
assignw BASE[8] T68
goto L12
@label B198
assignw T70 BASE[0]
assignw T71 BASE[8]
mult T72 1 T71
add T72 T72 4
assignw T73 BASE[4]
assignw T74 BASE[8]
mult T75 1 T74
add T75 T75 4
assignw T76 T70[T72]
assignw T77 T73[T75]
gt test T76 T77
goif B211 test
goto B215
@label B211
assignw T78 1
assignw lastbase BASE
return T78
goto F1_end
@label B215
assignw T79 BASE[4]
assignw T80 BASE[8]
mult T81 1 T80
add T81 T81 4
assignw T82 BASE[0]
assignw T83 BASE[8]
mult T84 1 T83
add T84 T84 4
assignw T85 T79[T81]
assignw T86 T82[T84]
gt test T85 T86
goif B228 test
goto B233
@label B228
assignw T87 1
minus T88 T87
assignw lastbase BASE
return T88
goto F1_end
@label B233
assignw T89 0
assignw lastbase BASE
return T89
@label F1_end
assignw lastbase BASE
return 0
@endfunction 12
@function F2 16
assignw T93 BASE[4]
assignw T94 T93[0]
assignw T95 1
mult T95 T95 T94
add T95 T95 4
malloc T92 T95
memcpy T92 T93 T95
param T96 0
assignw T96[0] T92
param T97 4
assignb T97[0] T40
call T98 F0 2
assignw T99 1
add T100 T98 T99
assignw BASE[8] T100
assignw T101 0
assignw BASE[12] T101
@label L15
assignw T102 BASE[12]
assignw T103 BASE[8]
lt test T102 T103
goif B264 test
goto F2_end
@label B264
assignw T104 BASE[0]
assignw T105 BASE[12]
mult T106 1 T105
add T106 T106 4
assignw T107 BASE[4]
assignw T108 BASE[12]
mult T109 1 T108
add T109 T109 4
assignb T110 T107[T109]
assignb T104[T106] T110
assignw T111 1
assignw T113 BASE[12]
add T112 T113 T111
assignw BASE[12] T112
goto L15
@label F2_end
assignw lastbase BASE
return 0
@endfunction 16
@function F3 28
assignw T117 0
assignw T118 0
assignw BASE[12] T117
assignw BASE[16] T118
@label L16
assignw T119 BASE[12]
assignw T120 BASE[4]
lt test T119 T120
goif B294 test
goto B347
@label B294
assignw T121 BASE[0]
assignw T122 BASE[12]
mult T123 4 T122
add T123 T123 4
assignw T125 T121[T123]
assignw T126 T125[0]
assignw T127 1
mult T127 T127 T126
add T127 T127 4
malloc T124 T127
memcpy T124 T125 T127
param T128 0
assignw T128[0] T124
param T129 4
assignb T129[0] T40
call T130 F0 2
assignw BASE[24] T130
assignw T131 0
assignw BASE[20] T131
@label L17
assignw T132 BASE[20]
assignw T133 BASE[24]
lt test T132 T133
goif B319 test
goto B342
@label B319
assignw T134 BASE[8]
assignw T135 BASE[16]
mult T136 1 T135
add T136 T136 4
assignw T137 BASE[0]
assignw T138 BASE[12]
mult T139 4 T138
add T139 T139 4
assignw T140 T137[T139]
assignw T141 BASE[20]
mult T142 1 T141
add T142 T142 4
assignb T143 T140[T142]
assignb T134[T136] T143
assignw T144 1
assignw T146 BASE[20]
add T145 T146 T144
assignw BASE[20] T145
assignw T147 1
assignw T149 BASE[16]
add T148 T149 T147
assignw BASE[16] T148
goto L17
@label B342
assignw T150 1
assignw T152 BASE[12]
add T151 T152 T150
assignw BASE[12] T151
goto L16
@label B347
assignw T153 BASE[8]
assignw T154 BASE[16]
mult T155 1 T154
add T155 T155 4
assignb T156 0
assignb T153[T155] T156
@label F3_end
assignw lastbase BASE
return 0
@endfunction 28
@function F4 29
assignw T160 0
assignw T161 0
assignw T162 0
assignw T164 BASE[0]
assignw T165 T164[0]
assignw T166 1
mult T166 T166 T165
add T166 T166 4
malloc T163 T166
memcpy T163 T164 T166
param T167 0
assignw T167[0] T163
param T168 4
assignb T168[0] T40
call T169 F0 2
assignw BASE[12] T160
assignw BASE[16] T161
assignw BASE[20] T162
assignw BASE[24] T169
goto B378
@label B378
assignb BASE[28] True
goto Bool381
assignb BASE[28] False
@label Bool381
@label L18
assignw T170 BASE[0]
assignw T171 BASE[12]
mult T172 1 T171
add T172 T172 4
@label L19
assignb T173 0
assignb T174 T170[T172]
neq test T174 T173
goif B393 test
goto B473
@label B393
assignw T175 BASE[0]
assignw T176 BASE[12]
mult T177 1 T176
add T177 T177 4
@label L20
assignb T178 T175[T177]
assignb T179 BASE[8]
eq test T178 T179
goif B403 test
goto B431
@label B403
assignb T180 BASE[28]
goif B431 T180
goto B406
@label B406
assignb T181 BASE[28]


goto B410
@label B410
assignb BASE[28] True
goto Bool413
assignb BASE[28] False
@label Bool413
assignw T182 BASE[4]
assignw T183 BASE[20]
mult T184 4 T183
add T184 T184 4
assignw T185 T182[T184]
assignw T186 BASE[16]
mult T187 1 T186
add T187 T187 4
assignb T188 0
assignb T185[T187] T188
assignw T189 1
assignw T191 BASE[20]
add T190 T191 T189
assignw BASE[20] T190
assignw T192 0
assignw BASE[16] T192
goto B468
@label B431
assignw T193 BASE[0]
assignw T194 BASE[12]
mult T195 1 T194
add T195 T195 4
@label L21
assignb T196 T193[T195]
assignb T197 BASE[8]
neq test T196 T197
goif B441 test
goto B468
@label B441
assignb T198 BASE[28]


goto B447
assignb BASE[28] True
goto Bool448
@label B447
assignb BASE[28] False
@label Bool448
assignw T199 BASE[4]
assignw T200 BASE[20]
mult T201 4 T200
add T201 T201 4
assignw T202 T199[T201]
assignw T203 BASE[16]
mult T204 1 T203
add T204 T204 4
assignw T205 BASE[0]
assignw T206 BASE[12]
mult T207 1 T206
add T207 T207 4
assignb T208 T205[T207]
assignb T202[T204] T208
assignw T209 1
assignw T211 BASE[16]
add T210 T211 T209
assignw BASE[16] T210
goto B468
@label B468
assignw T212 1
assignw T214 BASE[12]
add T213 T214 T212
assignw BASE[12] T213
goto L18
@label B473
assignb T215 BASE[28]
goif B491 T215
goto B476
@label B476
assignw T216 BASE[4]
assignw T217 BASE[20]
mult T218 4 T217
add T218 T218 4
assignw T219 T216[T218]
assignw T220 BASE[16]
mult T221 1 T220
add T221 T221 4
assignb T222 0
assignb T219[T221] T222
assignw T223 1
assignw T225 BASE[20]
add T224 T225 T223
assignw BASE[20] T224
goto B491
@label B491
assignw T226 BASE[20]
assignw lastbase BASE
return T226
@label F4_end
assignw lastbase BASE
return 0
@endfunction 29
@function F5 16
goto B503
goto B507
assignb BASE[4] True
goto Bool504
@label B503
assignb BASE[4] False
@label Bool504
assignb BASE[5] True
goto Bool508
@label B507
assignb BASE[5] False
@label Bool508
assignw T229 BASE[0]
assignw T230 T229[0]
assignw T231 1
mult T231 T231 T230
add T231 T231 4
malloc T228 T231
memcpy T228 T229 T231
param T232 0
assignw T232[0] T228
param T233 4
assignb T233[0] T40
call T234 F0 2
assignw T235 0
assignw BASE[8] T234
assignw BASE[12] T235
@label L22
assignw T236 BASE[12]
assignw T237 BASE[8]
lt test T236 T237
goif B530 test
goto B616
@label B530
assignw T238 BASE[0]
assignw T239 BASE[12]
mult T240 1 T239
add T240 T240 4
@label L23
assignb T241 46
assignb T242 T238[T240]
eq test T242 T241
goif B540 test
goto B552
@label B540
assignb T243 BASE[4]
goif B552 T243
goto B543
@label B543
assignb T244 BASE[4]


goto B547
@label B547
assignb BASE[4] True
goto Bool550
assignb BASE[4] False
@label Bool550
goto B611
@label B552
assignw T245 BASE[0]
assignw T246 BASE[12]
mult T247 1 T246
add T247 T247 4
@label L24
assignb T248 46
assignb T249 T245[T247]
eq test T249 T248
goif B562 test
goto B570
@label B562
goto B565
assignb T250 True
goto Bool566
@label B565
assignb T250 False
@label Bool566
assignw lastbase BASE
return T250
goto B611
@label B570
assignw T251 BASE[0]
assignw T252 BASE[12]
mult T253 1 T252
add T253 T253 4
assignb T254 48
assignw T255 T251[T253]
lt test T255 T254
goif B588 test
goto B579
@label B579
assignw T256 BASE[0]
assignw T257 BASE[12]
mult T258 1 T257
add T258 T258 4
assignb T259 57
assignw T260 T256[T258]
gt test T260 T259
goif B588 test
goto B596
@label B588
goto B591
assignb T261 True
goto Bool592
@label B591
assignb T261 False
@label Bool592
assignw lastbase BASE
return T261
goto B611
@label B596
assignb T262 BASE[4]
goif B599 T262
goto B611
@label B599
assignb T263 BASE[5]
goif B611 T263
goto B602
@label B602
assignb T264 BASE[5]


goto B606
@label B606
assignb BASE[5] True
goto Bool609
assignb BASE[5] False
@label Bool609
goto B611
@label B611
assignw T265 1
assignw T267 BASE[12]
add T266 T267 T265
assignw BASE[12] T266
goto L22
@label B616
assignb T268 BASE[4]
goif B619 T268
goto B624
@label B619
assignb T269 BASE[5]
goif B622 T269
goto B624
@label B622
assignb T270 True
goto Bool625
@label B624
assignb T270 False
@label Bool625
assignw lastbase BASE
return T270
@label F5_end
assignw lastbase BASE
return 0
@endfunction 16
malloc T272 12
assignw T273 T272
assignw T274 T273[0]
assignb T275 0
assignw T276 1
assignw T278 T276
assignw T279 1
mult T279 T279 T278
add T279 T279 4
malloc T277 T279
assignw T277[0] T278
assignb T277[4] T275
assignw T274[4] T277
assignw T281 1024
assignw T282 31
@function F6 16
malloc T283 12
assignw BASE[8] T283
assignw T284 BASE[8]
assignw T285 T284[0]
assignw T287 BASE[0]
assignw T288 4
mult T288 T288 T287
add T288 T288 4
malloc T286 T288
assignw T286[0] T287
assignw T285[0] T286
assignw T289 BASE[8]
assignw T290 T289[0]
assignw T291 BASE[0]
assignw T290[4] T291
assignw T292 BASE[8]
assignw T293 T292[0]
assignw T294 BASE[4]
assignw T293[8] T294
assignw T295 0
assignw BASE[12] T295
@label L25
assignw T296 BASE[12]
assignw T297 BASE[0]
lt test T296 T297
goif B675 test
goto B685
@label B675
assignw T298 BASE[8]
assignw T299 T298[0]
assignw T300 T299[0]
assignw T301 T300[0]
assignw T302 BASE[12]
mult T303 4 T302
add T303 T303 4
assignw T304 BASE[16]
assignw T301[T303] T304
goto L25
@label B685
assignw T305 BASE[8]
assignw lastbase BASE
return T305
@label F6_end
assignw lastbase BASE
return 0
@endfunction 16
@function F7 16
assignw T306 0
assignw BASE[12] T306
@label L26
assignw T307 BASE[0]
assignw T308 T307[0]
assignw T309 BASE[12]
assignw T310 T308[4]
lt test T309 T310
goif B703 test
goto B749
@label B703
assignw T311 BASE[0]
assignw T312 T311[0]
assignw T313 T312[0]
assignw T314 T313[0]
assignw T315 BASE[12]
mult T316 4 T315
add T316 T316 4
assignw T317 T314[T316]
assignw BASE[4] T317
@label L27
assignw T318 BASE[4]
assignw T319 T318[0]
assignw T321 T319[4]
assignw T322 T321[0]
assignw T323 1
mult T323 T323 T322
add T323 T323 4
malloc T320 T323
memcpy T320 T321 T323
param T324 0
assignw T324[0] T320
assignw T326 BASE[4]
assignw T327 T326[0]
assignw T328 1
mult T328 T328 T327
add T328 T328 4
malloc T325 T328
memcpy T325 T326 T328
param T329 4
assignw T329[0] T325
call T330 F1 2
@label L28
assignw T331 0
neq test T330 T331
goif B739 test
goto L26
@label B739
assignw T332 BASE[4]
assignw T333 T332[0]
assignw T334 T333[0]
assignw BASE[8] T334
assignw T335 BASE[4]
free T335
assignw T336 BASE[8]
assignw BASE[4] T336
goto L27
goto L26
@label B749
assignw T337 BASE[0]
assignw T338 T337[0]
assignw T339 T338[0]
free T339
assignw T340 BASE[0]
free T340
@label F7_end
assignw lastbase BASE
return 0
@endfunction 16
@function F8 16
assignw T342 0
assignw T343 0
assignw BASE[8] T342
assignw BASE[12] T343
@label L29
assignw T344 BASE[4]
assignw T345 BASE[12]
mult T346 1 T345
add T346 T346 4
@label L30
assignb T347 0
assignb T348 T344[T346]
neq test T348 T347
goif B775 test
goto B795
@label B775
assignw T349 BASE[4]
assignw T350 BASE[12]
mult T351 1 T350
add T351 T351 4
assignb T352 T349[T351]
param T353 0
assignb T353[0] T352
call T354 CTOI 1
assignw T355 BASE[0]
assignw T356 T355[0]
assignw T358 BASE[8]
assignw T359 T356[8]
mult T357 T358 T359
add T360 T354 T357
assignw BASE[8] T360
assignw T361 1
assignw T363 BASE[12]
add T362 T363 T361
assignw BASE[12] T362
goto L29
@label B795
assignw T364 BASE[0]
assignw T365 T364[0]
assignw T367 BASE[8]
assignw T368 T365[4]
mod T366 T367 T368
assignw lastbase BASE
return T366
@label F8_end
assignw lastbase BASE
return 0
@endfunction 16
@function F9 16
assignw T370 BASE[0]
assignw T371 T370[0]
assignw T372 T371[0]
assignw T373 BASE[0]
param T374 0
assignw T374[0] T373
assignw T376 BASE[4]
assignw T377 T376[0]
assignw T378 1
mult T378 T378 T377
add T378 T378 4
malloc T375 T378
memcpy T375 T376 T378
param T379 4
assignw T379[0] T375
call T380 F8 2
assignw T381 T372[0]
mult T382 4 T380
add T382 T382 4
assignw T383 T381[T382]
assignw BASE[12] T383
@label L31
assignw T384 BASE[12]
assignw T385 T384[0]
assignw T386 0
assignw T387 T385[4]
mult T388 1 T386
add T388 T388 4
@label L32
assignb T389 0
assignb T390 T387[T388]
neq test T390 T389
goif B841 test
goto B884
@label B841
assignw T391 BASE[12]
assignw T392 T391[0]
assignw T394 T392[4]
assignw T395 T394[0]
assignw T396 1
mult T396 T396 T395
add T396 T396 4
malloc T393 T396
memcpy T393 T394 T396
param T397 0
assignw T397[0] T393
assignw T399 BASE[4]
assignw T400 T399[0]
assignw T401 1
mult T401 T401 T400
add T401 T401 4
malloc T398 T401
memcpy T398 T399 T401
param T402 4
assignw T402[0] T398
call T403 F1 2
@label L33
assignw T404 0
eq test T403 T404
goif B867 test
goto B879
@label B867
assignw T405 BASE[12]
assignw T406 T405[0]
assignw T407 T406[8]
assignw BASE[8] T407
goto B872
@label B872
assignb T408 True
goto Bool875
assignb T408 False
@label Bool875
assignw lastbase BASE
return T408
goto L31
@label B879
assignw T409 BASE[12]
assignw T410 T409[0]
assignw T411 T410[0]
assignw BASE[12] T411
goto L31
@label B884
goto B887
assignb T412 True
goto Bool888
@label B887
assignb T412 False
@label Bool888
assignw lastbase BASE
return T412
@label F9_end
assignw lastbase BASE
return 0
@endfunction 16
@function F10 24
assignw T414 BASE[0]
param T415 0
assignw T415[0] T414
assignw T417 BASE[4]
assignw T418 T417[0]
assignw T419 1
mult T419 T419 T418
add T419 T419 4
malloc T416 T419
memcpy T416 T417 T419
param T420 4
assignw T420[0] T416
assignw T421 BASE[20]
param T422 8
assignw T422[0] T421
call T423 F9 3
assignw T424 lastbase[8]
assignw BASE[20] T424
goif B916 T423
goto B953
@label B916
malloc T425 12
assignw BASE[12] T425
assignw T426 BASE[0]
param T427 0
assignw T427[0] T426
assignw T429 BASE[4]
assignw T430 T429[0]
assignw T431 1
mult T431 T431 T430
add T431 T431 4
malloc T428 T431
memcpy T428 T429 T431
param T432 4
assignw T432[0] T428
call T433 F8 2
assignw BASE[16] T433
assignw T434 BASE[12]
assignw T435 T434[0]
assignw T436 BASE[0]
assignw T437 T436[0]
assignw T438 T437[0]
assignw T439 T438[0]
assignw T440 BASE[16]
mult T441 4 T440
add T441 T441 4
assignw T442 T439[T441]
assignw T435[0] T442
assignw T443 BASE[0]
assignw T444 T443[0]
assignw T445 T444[0]
assignw T446 T445[0]
assignw T447 BASE[16]
mult T448 4 T447
add T448 T448 4
assignw T449 BASE[12]
assignw T446[T448] T449
goto B953
@label B953
assignw T450 BASE[12]
assignw T451 T450[0]
assignw T452 BASE[8]
assignw T451[8] T452
@label F10_end
assignw lastbase BASE
return 0
@endfunction 24
@function F11 28
assignw T453 0
assignw BASE[4] T453
assignw T454 32
assignw T455 T454
assignw T456 BASE[12]
assignw T457 1
mult T457 T457 T455
add T457 T457 4
malloc T456 T457
assignw T456[0] T455
assignw T456[0] T456
@label L34
assignw T458 BASE[0]
assignw T459 T458[0]
assignw T460 BASE[4]
assignw T461 T459[4]
lt test T460 T461
goif B981 test
goto F11_end
@label B981
assignw T462 BASE[0]
assignw T463 T462[0]
assignw T464 T463[0]
assignw T465 T464[0]
assignw T466 BASE[4]
mult T467 4 T466
add T467 T467 4
assignw T468 T465[T467]
assignw BASE[8] T468
@label L35
assignw T469 BASE[8]
assignw T470 T469[0]
assignw T471 0
assignw T472 T470[4]
mult T473 1 T471
add T473 T473 4
@label L36
assignb T474 0
assignb T475 T472[T473]
neq test T475 T474
goif B1003 test
goto B1104
@label B1003
assignw S1[0] 12
assignw T477 BASE[8]
assignw T478 T477[0]
assignw T479 1
assignw T480 T479
assignw T481 BASE[16]
assignw T482 4
mult T482 T482 T480
add T482 T482 4
malloc T481 T482
assignw T481[0] T480
assignw T481[0] T481
@label L37
sub T482 T482 4
lt test T482 0
goif L37_end test
goto L37
@label L37_end
assignw T483 BASE[16]
assignw T484 T478[4]
assignw T483[4] T484
assignw T485 BASE[8]
assignw T486 T485[0]
assignw T487 1
assignw T488 T487
assignw T489 BASE[20]
assignw T490 4
mult T490 T490 T488
add T490 T490 4
malloc T489 T490
assignw T489[0] T488
assignw T489[0] T489
assignw T491 BASE[20]
assignw T492 T486[8]
assignw T491[4] T492
assignb T493 10
assignw T494 1
assignw T495 T494
assignw T496 BASE[24]
assignw T497 1
mult T497 T497 T495
add T497 T497 4
malloc T496 T497
assignw T496[0] T495
assignw T496[0] T496
assignw T498 BASE[24]
assignb T498[4] T493
param T499 0
assignw T499[0] S1
assignw T501 BASE[24]
assignw T502 T501[0]
assignw T503 1
mult T503 T503 T502
add T503 T503 4
malloc T500 T503
memcpy T500 T501 T503
param T504 4
assignw T504[0] T500
param T505 8
assignw T505[0] 0
assignw T507 BASE[20]
assignw T508 T507[0]
assignw T509 4
mult T509 T509 T508
add T509 T509 4
malloc T506 T509
memcpy T506 T507 T509
param T510 12
assignw T510[0] T506
assignw T512 BASE[16]
assignw T513 T512[0]
assignw T514 4
mult T514 T514 T513
add T514 T514 4
malloc T511 T514
assignw T515 T514
@label L38
sub T515 T515 4
lt test T515 0
goif L38_end test
assignw T516 T512[T515]
assignw T517 T511[T515]
assignw T518 T516[0]
assignw T519 1
mult T519 T519 T518
add T519 T519 4
malloc T517 T519
assignw T517[0] T517
memcpy T517 T516 T519
goto L38
@label L38_end
param T520 16
assignw T520[0] T511
param T521 20
assignw T521[0] S0
call T522 PRINT 6
assignw T523 BASE[8]
assignw T524 T523[0]
assignw T525 T524[0]
assignw BASE[8] T525
goto L35
@label B1104
assignw T526 1
assignw T528 BASE[4]
add T527 T528 T526
assignw BASE[4] T527
goto L34
@label F11_end
assignw lastbase BASE
return 0
@endfunction 28
assignw T529 33792
assignw T530 T529
assignw T531 1024
assignw T532 T531
assignw T533 32
assignw T534 T533
assignw T535 0
assignw T536 0
assignw T537 1
minus T538 T537
param T539 0
assignw T539[0] T281
param T540 4
assignw T540[0] T282
call T541 F6 2
assignw T542 T541
assignw S2[0] 26
assignw T545 S2
assignw T547 T545[0]
assignw T548 1
mult T548 T548 T547
add T548 T548 4
malloc T546 T548
memcpy T546 T545 T548
param T549 0
assignw T549[0] T546
param T550 4
assignb T550[0] T40
call T551 F0 2
assignw T552 T551
assignw T553 0
assignw T555 T553
@label L39
geq test T555 T552
goif L39_end test
assignw T554 T555
mult T556 1 T554
add T556 T556 4
assignw T557 1
assignw T559 T557
assignw T560 1
mult T560 T560 T559
add T560 T560 4
malloc T558 T560
assignw T558[0] T559
assignb T561 T545[T556]
assignb T558[4] T561
assignw T562 0.000000
param T563 0
assignw T563[0] T542
assignw T565 T558[0]
assignw T566 1
mult T566 T566 T565
add T566 T566 4
malloc T564 T566
memcpy T564 T558 T566
param T567 4
assignw T567[0] T564
param T568 8
assignw T568[0] T562
call T569 F10 3
add T555 T555 1
goto L39
@label L39_end
assignw T572 T530
assignw T573 1
mult T573 T573 T572
add T573 T573 4
malloc T571 T573
assignw T571[0] T572
assignw T575 T534
assignw T576 1
mult T576 T576 T575
add T576 T576 4
malloc T574 T576
assignw T574[0] T575
malloc T578 24
assignw T579 T532
assignw T580 T578[0]
assignw T581 4
mult T581 T581 T579
add T581 T581 4
malloc T580 T581
assignw T580[0] T579
assignw T580[0] T580
@label L40
sub T581 T581 4
lt test T581 0
goif L40_end test
assignw T582 T534
assignw T583 T580[T581]
assignw T584 1
mult T584 T584 T582
add T584 T584 4
malloc T583 T584
assignw T583[0] T582
assignw T583[0] T583
goto L40
@label L40_end
assignw T585 T532
assignw T586 T578[12]
assignw T587 4
mult T587 T587 T585
add T587 T587 4
malloc T586 T587
assignw T586[0] T585
assignw T586[0] T586
assignw T588 T578
@label L41
goto B1223
@label B1223
assignw S3[0] 6
param T590 0
assignw T590[0] S3
param T591 4
assignw T591[0] 0
param T592 8
assignw T592[0] 0
param T593 12
assignw T593[0] 0
param T594 16
assignw T594[0] 0
param T595 20
assignw T595[0] S0
call T596 PRINT 6
param T597 0
assignw T597[0] T571
call T598 READ 1
assignw S4[0] 4
assignw T601 T571[0]
assignw T602 1
mult T602 T602 T601
add T602 T602 4
malloc T600 T602
memcpy T600 T571 T602
param T603 0
assignw T603[0] T600
param T604 4
assignw T604[0] S4
call T605 F1 2
@label L42
assignw T606 0
eq test T605 T606
goif B1257 test
goto B1259
@label B1257
goto B1361
goto B1259
@label B1259
assignw T607 T588[0]
assignb T608 32
assignw T610 T571[0]
assignw T611 1
mult T611 T611 T610
add T611 T611 4
malloc T609 T611
memcpy T609 T571 T611
param T612 0
assignw T612[0] T609
assignw T614 T607[0]
assignw T615 T614[0]
assignw T616 4
mult T616 T616 T615
add T616 T616 4
malloc T613 T616
assignw T617 T616
@label L43
sub T617 T617 4
lt test T617 0
goif L43_end test
assignw T618 T614[T617]
assignw T619 T613[T617]
assignw T620 T618[0]
assignw T621 1
mult T621 T621 T620
add T621 T621 4
malloc T619 T621
assignw T619[0] T619
memcpy T619 T618 T621
goto L43
@label L43_end
param T622 4
assignw T622[0] T613
param T623 8
assignb T623[0] T608
call T624 F4 3
assignw T577 T624
assignw T625 T588[0]
assignw T626 T625[0]
mult T627 4 T577
add T627 T627 4
assignw S5[0] 1
assignw T630 T626[T627]
assignw T631 T630[0]
assignw T632 1
mult T632 T632 T631
add T632 T632 4
malloc T629 T632
memcpy T629 T630 T632
param T633 0
assignw T633[0] T629
param T634 4
assignw T634[0] S5
call T635 F2 2
param T636 0
assignw T636[0] T588
assignw T638 T574[0]
assignw T639 1
mult T639 T639 T638
add T639 T639 4
malloc T637 T639
memcpy T637 T574 T639
param T640 4
assignw T640[0] T637
call T641 F17  2
assignw T643 T574[0]
assignw T644 1
mult T644 T644 T643
add T644 T644 4
malloc T642 T644
memcpy T642 T574 T644
param T645 0
assignw T645[0] T642
param T646 4
assignb T646[0] T40
call T647 F0 2
assignw T648 0
gt test T647 T648
goif B1340 test
goto L41
@label B1340
assignw T650 T574[0]
assignw T651 1
mult T651 T651 T650
add T651 T651 4
malloc T649 T651
memcpy T649 T574 T651
param T652 0
assignw T652[0] T649
param T653 4
assignw T653[0] 0
param T654 8
assignw T654[0] 0
param T655 12
assignw T655[0] 0
param T656 16
assignw T656[0] 0
param T657 20
assignw T657[0] S0
call T658 PRINT 6
goto L41
goto L41
@label B1361
assignw T659 T588[0]
assignw T660 T659[0]
assignw T661 4
mult T661 T661 T660
@label L44
sub T661 T661 4
lt test T661 0
goif L44_end test
assignw T662 T659[T661]
free T662
goto L44
@label L44_end
free T659
assignw T663 T588[12]
free T663
free T588
@function F12 8
assignw T665 BASE[0]
assignw T666 T665[0]
assignw T667 BASE[0]
assignw T668 T667[0]
assignw T669 T666[0]
assignw T670 T668[4]
mult T671 4 T670
add T671 T671 4
assignw T673 BASE[4]
assignw T674 T673[0]
assignw T675 1
mult T675 T675 T674
add T675 T675 4
malloc T672 T675
memcpy T672 T673 T675
param T676 0
assignw T676[0] T672
assignw T678 T669[T671]
assignw T679 T678[0]
assignw T680 1
mult T680 T680 T679
add T680 T680 4
malloc T677 T680
memcpy T677 T678 T680
param T681 4
assignw T681[0] T677
call T682 F1 2
@label L45
assignw T683 0
eq test T682 T683
goif B1410 test
goto B1426
@label B1410
assignw T684 BASE[0]
assignw T685 T684[0]
assignw T686 BASE[0]
assignw T687 T686[0]
assignw T688 1
assignw T690 T687[4]
add T689 T690 T688
assignw T685[4] T689
goto B1419
@label B1419
assignb T691 True
goto Bool1422
assignb T691 False
@label Bool1422
assignw lastbase BASE
return T691
goto B1426
@label B1426
goto B1429
assignb T692 True
goto Bool1430
@label B1429
assignb T692 False
@label Bool1430
assignw lastbase BASE
return T692
@label F12_end
assignw lastbase BASE
return 0
@endfunction 8
assignw T693 0
@function F13 8
assignw T695 BASE[0]
assignw T696 T695[0]
assignw T698 T696[4]
assignw T699 BASE[4]
add T697 T698 T699
assignw T700 BASE[0]
assignw T701 T700[0]
assignw T702 T701[8]
lt test T697 T702
goif B1450 test
goto B1464
@label B1450
assignw T703 BASE[0]
assignw T704 T703[0]
assignw T705 BASE[0]
assignw T706 T705[0]
assignw T708 T706[4]
assignw T709 BASE[4]
add T707 T708 T709
assignw T710 T704[0]
mult T711 4 T707
add T711 T711 4
assignw T712 T710[T711]
assignw lastbase BASE
return T712
goto B1464
@label B1464
assignw T713 BASE[4]
assignw lastbase BASE
return T713
@label F13_end
assignw lastbase BASE
return 0
@endfunction 8
@function F14 4
assignw T714 BASE[0]
assignw T715 T714[0]
assignw T716 T715[16]
assignw T717 BASE[28]
geq test T716 T717
goif B1479 test
goto B1496
@label B1479
assignw S6[0] 34
param T719 0
assignw T719[0] S6
param T720 4
assignw T720[0] 0
param T721 8
assignw T721[0] 0
param T722 12
assignw T722[0] 0
param T723 16
assignw T723[0] 0
param T724 20
assignw T724[0] S0
call T725 PRINT 6
assignw T726 1
exit T726
goto B1496
@label B1496
assignw T727 BASE[0]
assignw T728 T727[0]
assignw T729 BASE[0]
assignw T730 T729[0]
assignw T731 T728[12]
assignw T732 T730[16]
mult T733 4 T732
add T733 T733 4
malloc T734 8
assignw T735 T534
assignw T736 T734[0]
assignw T737 1
mult T737 T737 T735
add T737 T737 4
malloc T736 T737
assignw T736[0] T735
assignw T736[0] T736
assignw T738 T534
assignw T739 T734[4]
assignw T740 1
mult T740 T740 T738
add T740 T740 4
malloc T739 T740
assignw T739[0] T738
assignw T739[0] T739
assignw T731[T733] T734
assignw T741 BASE[0]
assignw T742 T741[0]
assignw T743 BASE[0]
assignw T744 T743[0]
assignw T745 1
assignw T747 T744[16]
add T746 T747 T745
assignw T742[16] T746
@label F14_end
assignw lastbase BASE
return 0
@endfunction 4
@function F15 4
assignw T748 BASE[0]
assignw T749 T748[0]
assignw T750 BASE[0]
assignw T751 T750[0]
assignw T752 1
assignw T754 T751[16]
sub T753 T754 T752
assignw T755 T749[12]
mult T756 4 T753
add T756 T756 4
assignw T757 T755[T756]
assignw T758 T757[0]
free T758
assignw T759 T757[4]
free T759
free T757
assignw T760 BASE[0]
assignw T761 T760[0]
assignw T762 BASE[0]
assignw T763 T762[0]
assignw T764 1
assignw T766 T763[16]
sub T765 T766 T764
assignw T761[16] T765
@label F15_end
assignw lastbase BASE
return 0
@endfunction 4
@function F16 4
@label L46
assignw T767 BASE[0]
assignw T768 T767[0]
assignw T769 0
assignw T770 T768[4]
gt test T770 T769
goif B1572 test
goto F16_end
@label B1572
assignw T771 BASE[0]
param T772 0
assignw T772[0] T771
call T773 F15 1
goto L46
@label F16_end
assignw lastbase BASE
return 0
@endfunction 4
@function F17 12
assignw T776 BASE[0]
param T777 0
assignw T777[0] T776
param T778 4
assignw T778[0] T693
call T779 F13 2
assignw BASE[8] T779
assignb T780 48
assignw T781 0
assignw T782 BASE[8]
mult T783 1 T781
add T783 T783 4
assignw T784 T782[T783]
leq test T780 T784
goif B1598 test
goto B1607
@label B1598
assignw T785 0
assignw T786 BASE[8]
mult T787 1 T785
add T787 T787 4
assignb T788 57
assignw T789 T786[T787]
leq test T789 T788
goif B1643 test
goto B1607
@label B1607
assignb T790 97
assignw T791 0
assignw T792 BASE[8]
mult T793 1 T791
add T793 T793 4
assignw T794 T792[T793]
leq test T790 T794
goif B1616 test
goto B1625
@label B1616
assignw T795 0
assignw T796 BASE[8]
mult T797 1 T795
add T797 T797 4
assignb T798 122
assignw T799 T796[T797]
leq test T799 T798
goif B1643 test
goto B1625
@label B1625
assignw S7[0] 1
assignw T802 BASE[8]
assignw T803 T802[0]
assignw T804 1
mult T804 T804 T803
add T804 T804 4
malloc T801 T804
memcpy T801 T802 T804
param T805 0
assignw T805[0] T801
param T806 4
assignw T806[0] S7
call T807 F1 2
@label L47
assignw T808 0
eq test T807 T808
goif B1643 test
goto B1734
@label B1643
assignw T809 BASE[0]
param T810 0
assignw T810[0] T809
call T811 F14 1
assignw T812 BASE[0]
param T813 0
assignw T813[0] T812
call T814 F18  1
goif B1664 T814
goto B1653
@label B1653
assignw T815 BASE[0]
param T816 0
assignw T816[0] T815
call T817 F16 1
assignw T818 0
assignw T819 BASE[4]
mult T820 1 T818
add T820 T820 4
assignb T821 0
assignb T819[T820] T821
goto B1664
@label B1664
assignw S8[0] 1
assignw T823 BASE[0]
param T824 0
assignw T824[0] T823
param T825 4
assignw T825[0] S8
call T826 F12 2
goif B1698 T826
goto B1673
@label B1673
assignw S9[0] 34
param T828 0
assignw T828[0] S9
param T829 4
assignw T829[0] 0
param T830 8
assignw T830[0] 0
param T831 12
assignw T831[0] 0
param T832 16
assignw T832[0] 0
param T833 20
assignw T833[0] S0
call T834 PRINT 6
assignw T835 BASE[0]
param T836 0
assignw T836[0] T835
call T837 F16 1
assignw T838 0
assignw T839 BASE[4]
mult T840 1 T838
add T840 T840 4
assignb T841 0
assignb T839[T840] T841
goto B1698
@label B1698
assignw T842 BASE[0]
assignw T843 T842[0]
assignw T844 BASE[0]
assignw T845 T844[0]
assignw T846 1
assignw T848 T845[16]
sub T847 T848 T846
assignw T849 T843[12]
mult T850 4 T847
add T850 T850 4
assignw T851 T849[T850]
assignw T852 T851[0]
assignw T854 BASE[4]
assignw T855 T854[0]
assignw T856 1
mult T856 T856 T855
add T856 T856 4
malloc T853 T856
memcpy T853 T854 T856
param T857 0
assignw T857[0] T853
assignw T859 T852[4]
assignw T860 T859[0]
assignw T861 1
mult T861 T861 T860
add T861 T861 4
malloc T858 T861
memcpy T858 T859 T861
param T862 4
assignw T862[0] T858
call T863 F2 2
assignw T864 BASE[0]
param T865 0
assignw T865[0] T864
call T866 F15 1
goto F17_end
@label B1734
assignw S10[0] 34
param T868 0
assignw T868[0] S10
param T869 4
assignw T869[0] 0
param T870 8
assignw T870[0] 0
param T871 12
assignw T871[0] 0
param T872 16
assignw T872[0] 0
param T873 20
assignw T873[0] S0
call T874 PRINT 6
assignw T875 BASE[0]
param T876 0
assignw T876[0] T875
call T877 F16 1
assignw T878 0
assignw T879 BASE[4]
mult T880 1 T878
add T880 T880 4
assignb T881 0
assignb T879[T880] T881
@label F17_end
assignw lastbase BASE
return 0
@endfunction 12
@function F18 16
assignw T883 BASE[0]
param T884 0
assignw T884[0] T883
param T885 4
assignw T885[0] T693
call T886 F13 2
assignw T887 1
assignw T888 BASE[0]
param T889 0
assignw T889[0] T888
param T890 4
assignw T890[0] T887
call T891 F13 2
assignw BASE[4] T886
assignw BASE[8] T891
assignb T892 97
assignw T893 0
assignw T894 BASE[4]
mult T895 1 T893
add T895 T895 4
assignw T896 T894[T895]
leq test T892 T896
goif B1787 test
goto B1966
@label B1787
assignw T897 0
assignw T898 BASE[4]
mult T899 1 T897
add T899 T899 4
assignb T900 122
assignw T901 T898[T899]
leq test T901 T900
goif B1796 test
goto B1966
@label B1796
assignw T903 BASE[4]
assignw T904 T903[0]
assignw T905 1
mult T905 T905 T904
add T905 T905 4
malloc T902 T905
memcpy T902 T903 T905
param T906 0
assignw T906[0] T902
param T907 4
assignb T907[0] T40
call T908 F0 2
@label L48
assignw T909 1
eq test T908 T909
goif B1813 test
goto B1966
@label B1813
assignw S11[0] 1
assignw T912 BASE[8]
assignw T913 T912[0]
assignw T914 1
mult T914 T914 T913
add T914 T914 4
malloc T911 T914
memcpy T911 T912 T914
param T915 0
assignw T915[0] T911
param T916 4
assignw T916[0] S11
call T917 F1 2
@label L49
assignw T918 0
eq test T917 T918
goif B1831 test
goto B1966
@label B1831
assignw T919 BASE[0]
param T920 0
assignw T920[0] T919
assignw T922 BASE[4]
assignw T923 T922[0]
assignw T924 1
mult T924 T924 T923
add T924 T924 4
malloc T921 T924
memcpy T921 T922 T924
param T925 4
assignw T925[0] T921
call T926 F12 2
goif B1846 T926
goto B1846
@label B1846
assignw T927 BASE[0]
param T928 0
assignw T928[0] T927
assignw T930 BASE[8]
assignw T931 T930[0]
assignw T932 1
mult T932 T932 T931
add T932 T932 4
malloc T929 T932
memcpy T929 T930 T932
param T933 4
assignw T933[0] T929
call T934 F12 2
goif B1861 T934
goto B1861
@label B1861
assignw T935 BASE[0]
param T936 0
assignw T936[0] T935
call T937 F14 1
assignw T938 BASE[0]
param T939 0
assignw T939[0] T938
call T940 F19  1
goif B1879 T940
goto B1871
@label B1871
goto B1874
assignb T941 True
goto Bool1875
@label B1874
assignb T941 False
@label Bool1875
assignw lastbase BASE
return T941
goto B1879
@label B1879
assignw T942 BASE[0]
assignw T943 T942[0]
assignw T944 BASE[0]
assignw T945 T944[0]
assignw T946 1
assignw T948 T945[16]
sub T947 T948 T946
assignw T949 T943[12]
mult T950 4 T947
add T950 T950 4
assignw T951 T949[T950]
assignw T952 T951[0]
assignw T954 T952[4]
assignw T955 T954[0]
assignw T956 1
mult T956 T956 T955
add T956 T956 4
malloc T953 T956
memcpy T953 T954 T956
param T957 0
assignw T957[0] T953
call T958 STOF 1
assignw BASE[12] T958
assignw T959 BASE[0]
assignw T960 T959[0]
assignw T961 BASE[0]
assignw T962 T961[0]
assignw T963 2
assignw T965 T962[16]
sub T964 T965 T963
assignw T966 T960[12]
mult T967 4 T964
add T967 T967 4
assignw T968 T966[T967]
assignw T969 T968[0]
assignw T970 BASE[0]
assignw T971 T970[0]
assignw T972 BASE[0]
assignw T973 T972[0]
assignw T974 1
assignw T976 T973[16]
sub T975 T976 T974
assignw T977 T971[12]
mult T978 4 T975
add T978 T978 4
assignw T979 T977[T978]
assignw T980 T979[0]
assignw T982 T969[4]
assignw T983 T982[0]
assignw T984 1
mult T984 T984 T983
add T984 T984 4
malloc T981 T984
memcpy T981 T982 T984
param T985 0
assignw T985[0] T981
assignw T987 T980[4]
assignw T988 T987[0]
assignw T989 1
mult T989 T989 T988
add T989 T989 4
malloc T986 T989
memcpy T986 T987 T989
param T990 4
assignw T990[0] T986
call T991 F2 2
assignw T992 BASE[36]
param T993 0
assignw T993[0] T992
assignw T995 BASE[4]
assignw T996 T995[0]
assignw T997 1
mult T997 T997 T996
add T997 T997 4
malloc T994 T997
memcpy T994 T995 T997
param T998 4
assignw T998[0] T994
assignw T999 BASE[12]
param T1000 8
assignw T1000[0] T999
call T1001 F10 3
assignw T1002 BASE[0]
param T1003 0
assignw T1003[0] T1002
call T1004 F15 1
goto B2107
@label B1966
assignb T1005 48
assignw T1006 0
assignw T1007 BASE[4]
mult T1008 1 T1006
add T1008 T1008 4
assignw T1009 T1007[T1008]
leq test T1005 T1009
goif B1975 test
goto B1984
@label B1975
assignw T1010 0
assignw T1011 BASE[4]
mult T1012 1 T1010
add T1012 T1012 4
assignb T1013 57
assignw T1014 T1011[T1012]
leq test T1014 T1013
goif B2020 test
goto B1984
@label B1984
assignb T1015 97
assignw T1016 0
assignw T1017 BASE[4]
mult T1018 1 T1016
add T1018 T1018 4
assignw T1019 T1017[T1018]
leq test T1015 T1019
goif B1993 test
goto B2002
@label B1993
assignw T1020 0
assignw T1021 BASE[4]
mult T1022 1 T1020
add T1022 T1022 4
assignb T1023 122
assignw T1024 T1021[T1022]
leq test T1024 T1023
goif B2020 test
goto B2002
@label B2002
assignw S12[0] 1
assignw T1027 BASE[4]
assignw T1028 T1027[0]
assignw T1029 1
mult T1029 T1029 T1028
add T1029 T1029 4
malloc T1026 T1029
memcpy T1026 T1027 T1029
param T1030 0
assignw T1030[0] T1026
param T1031 4
assignw T1031[0] S12
call T1032 F1 2
@label L50
assignw T1033 0
eq test T1032 T1033
goif B2020 test
goto B2086
@label B2020
assignw T1034 BASE[0]
param T1035 0
assignw T1035[0] T1034
call T1036 F14 1
assignw T1037 BASE[0]
param T1038 0
assignw T1038[0] T1037
call T1039 F19  1
goif B2038 T1039
goto B2030
@label B2030
goto B2033
assignb T1040 True
goto Bool2034
@label B2033
assignb T1040 False
@label Bool2034
assignw lastbase BASE
return T1040
goto B2038
@label B2038
assignw T1041 BASE[0]
assignw T1042 T1041[0]
assignw T1043 BASE[0]
assignw T1044 T1043[0]
assignw T1045 2
assignw T1047 T1044[16]
sub T1046 T1047 T1045
assignw T1048 T1042[12]
mult T1049 4 T1046
add T1049 T1049 4
assignw T1050 T1048[T1049]
assignw T1051 T1050[0]
assignw T1052 BASE[0]
assignw T1053 T1052[0]
assignw T1054 BASE[0]
assignw T1055 T1054[0]
assignw T1056 1
assignw T1058 T1055[16]
sub T1057 T1058 T1056
assignw T1059 T1053[12]
mult T1060 4 T1057
add T1060 T1060 4
assignw T1061 T1059[T1060]
assignw T1062 T1061[0]
assignw T1064 T1051[4]
assignw T1065 T1064[0]
assignw T1066 1
mult T1066 T1066 T1065
add T1066 T1066 4
malloc T1063 T1066
memcpy T1063 T1064 T1066
param T1067 0
assignw T1067[0] T1063
assignw T1069 T1062[4]
assignw T1070 T1069[0]
assignw T1071 1
mult T1071 T1071 T1070
add T1071 T1071 4
malloc T1068 T1071
memcpy T1068 T1069 T1071
param T1072 4
assignw T1072[0] T1068
call T1073 F2 2
assignw T1074 BASE[0]
param T1075 0
assignw T1075[0] T1074
call T1076 F15 1
goto B2107
@label B2086
assignw S13[0] 34
param T1078 0
assignw T1078[0] S13
param T1079 4
assignw T1079[0] 0
param T1080 8
assignw T1080[0] 0
param T1081 12
assignw T1081[0] 0
param T1082 16
assignw T1082[0] 0
param T1083 20
assignw T1083[0] S0
call T1084 PRINT 6
goto B2103
assignb T1085 True
goto Bool2104
@label B2103
assignb T1085 False
@label Bool2104
assignw lastbase BASE
return T1085
@label B2107
goto B2108
@label B2108
assignb T1086 True
goto Bool2111
assignb T1086 False
@label Bool2111
assignw lastbase BASE
return T1086
@label F18_end
assignw lastbase BASE
return 0
@endfunction 16
@function F19 12
assignw T1088 BASE[0]
param T1089 0
assignw T1089[0] T1088
param T1090 4
assignw T1090[0] T693
call T1091 F13 2
assignw BASE[4] T1091
assignb T1092 48
assignw T1093 0
assignw T1094 BASE[4]
mult T1095 1 T1093
add T1095 T1095 4
assignw T1096 T1094[T1095]
leq test T1092 T1096
goif B2135 test
goto B2144
@label B2135
assignw T1097 0
assignw T1098 BASE[4]
mult T1099 1 T1097
add T1099 T1099 4
assignb T1100 57
assignw T1101 T1098[T1099]
leq test T1101 T1100
goif B2180 test
goto B2144
@label B2144
assignb T1102 97
assignw T1103 0
assignw T1104 BASE[4]
mult T1105 1 T1103
add T1105 T1105 4
assignw T1106 T1104[T1105]
leq test T1102 T1106
goif B2153 test
goto B2162
@label B2153
assignw T1107 0
assignw T1108 BASE[4]
mult T1109 1 T1107
add T1109 T1109 4
assignb T1110 122
assignw T1111 T1108[T1109]
leq test T1111 T1110
goif B2180 test
goto B2162
@label B2162
assignw S14[0] 1
assignw T1114 BASE[4]
assignw T1115 T1114[0]
assignw T1116 1
mult T1116 T1116 T1115
add T1116 T1116 4
malloc T1113 T1116
memcpy T1113 T1114 T1116
param T1117 0
assignw T1117[0] T1113
param T1118 4
assignw T1118[0] S14
call T1119 F1 2
@label L51
assignw T1120 0
eq test T1119 T1120
goif B2180 test
goto B2463
@label B2180
assignw T1121 BASE[0]
param T1122 0
assignw T1122[0] T1121
call T1123 F14 1
assignw T1124 BASE[0]
param T1125 0
assignw T1125[0] T1124
call T1126 F20  1
goif B2198 T1126
goto B2190
@label B2190
goto B2193
assignb T1127 True
goto Bool2194
@label B2193
assignb T1127 False
@label Bool2194
assignw lastbase BASE
return T1127
goto B2198
@label B2198
assignw T1128 BASE[0]
assignw T1129 T1128[0]
assignw T1130 BASE[0]
assignw T1131 T1130[0]
assignw T1132 2
assignw T1134 T1131[16]
sub T1133 T1134 T1132
assignw T1135 T1129[12]
mult T1136 4 T1133
add T1136 T1136 4
assignw T1137 T1135[T1136]
assignw T1138 T1137[0]
assignw T1139 BASE[0]
assignw T1140 T1139[0]
assignw T1141 BASE[0]
assignw T1142 T1141[0]
assignw T1143 1
assignw T1145 T1142[16]
sub T1144 T1145 T1143
assignw T1146 T1140[12]
mult T1147 4 T1144
add T1147 T1147 4
assignw T1148 T1146[T1147]
assignw T1149 T1148[0]
assignw T1151 T1138[4]
assignw T1152 T1151[0]
assignw T1153 1
mult T1153 T1153 T1152
add T1153 T1153 4
malloc T1150 T1153
memcpy T1150 T1151 T1153
param T1154 0
assignw T1154[0] T1150
assignw T1156 T1149[4]
assignw T1157 T1156[0]
assignw T1158 1
mult T1158 T1158 T1157
add T1158 T1158 4
malloc T1155 T1158
memcpy T1155 T1156 T1158
param T1159 4
assignw T1159[0] T1155
call T1160 F2 2
assignw T1161 BASE[0]
param T1162 0
assignw T1162[0] T1161
call T1163 F15 1
assignw T1164 BASE[0]
param T1165 0
assignw T1165[0] T1164
param T1166 4
assignw T1166[0] T693
call T1167 F13 2
assignw BASE[4] T1167
assignw S15[0] 1
assignw T1170 BASE[4]
assignw T1171 T1170[0]
assignw T1172 1
mult T1172 T1172 T1171
add T1172 T1172 4
malloc T1169 T1172
memcpy T1169 T1170 T1172
param T1173 0
assignw T1173[0] T1169
param T1174 4
assignw T1174[0] S15
call T1175 F1 2
@label L52
assignw T1176 0
eq test T1175 T1176
goif B2288 test
goto B2270
@label B2270
assignw S16[0] 1
assignw T1179 BASE[4]
assignw T1180 T1179[0]
assignw T1181 1
mult T1181 T1181 T1180
add T1181 T1181 4
malloc T1178 T1181
memcpy T1178 T1179 T1181
param T1182 0
assignw T1182[0] T1178
param T1183 4
assignw T1183[0] S16
call T1184 F1 2
@label L53
assignw T1185 0
eq test T1184 T1185
goif B2288 test
goto B2484
@label B2288
assignw T1186 BASE[0]
param T1187 0
assignw T1187[0] T1186
call T1188 F14 1
assignw T1189 BASE[0]
param T1190 0
assignw T1190[0] T1189
assignw T1192 BASE[4]
assignw T1193 T1192[0]
assignw T1194 1
mult T1194 T1194 T1193
add T1194 T1194 4
malloc T1191 T1194
memcpy T1191 T1192 T1194
param T1195 4
assignw T1195[0] T1191
call T1196 F12 2
goif B2307 T1196
goto B2307
@label B2307
assignw T1197 BASE[0]
param T1198 0
assignw T1198[0] T1197
call T1199 F19 1
goif B2321 T1199
goto B2313
@label B2313
goto B2316
assignb T1200 True
goto Bool2317
@label B2316
assignb T1200 False
@label Bool2317
assignw lastbase BASE
return T1200
goto B2321
@label B2321
assignw S17[0] 1
assignw T1203 BASE[4]
assignw T1204 T1203[0]
assignw T1205 1
mult T1205 T1205 T1204
add T1205 T1205 4
malloc T1202 T1205
memcpy T1202 T1203 T1205
param T1206 0
assignw T1206[0] T1202
param T1207 4
assignw T1207[0] S17
call T1208 F1 2
@label L54
assignw T1209 0
eq test T1208 T1209
goif B2339 test
goto B2386
@label B2339
assignw T1210 BASE[0]
assignw T1211 T1210[0]
assignw T1212 BASE[0]
assignw T1213 T1212[0]
assignw T1214 2
assignw T1216 T1213[16]
sub T1215 T1216 T1214
assignw T1217 T1211[12]
mult T1218 4 T1215
add T1218 T1218 4
assignw T1219 T1217[T1218]
assignw T1220 T1219[0]
assignw T1222 T1220[4]
assignw T1223 T1222[0]
assignw T1224 1
mult T1224 T1224 T1223
add T1224 T1224 4
malloc T1221 T1224
memcpy T1221 T1222 T1224
param T1225 0
assignw T1225[0] T1221
call T1226 STOF 1
assignw T1227 BASE[0]
assignw T1228 T1227[0]
assignw T1229 BASE[0]
assignw T1230 T1229[0]
assignw T1231 1
assignw T1233 T1230[16]
sub T1232 T1233 T1231
assignw T1234 T1228[12]
mult T1235 4 T1232
add T1235 T1235 4
assignw T1236 T1234[T1235]
assignw T1237 T1236[0]
assignw T1239 T1237[4]
assignw T1240 T1239[0]
assignw T1241 1
mult T1241 T1241 T1240
add T1241 T1241 4
malloc T1238 T1241
memcpy T1238 T1239 T1241
param T1242 0
assignw T1242[0] T1238
call T1243 STOF 1
add T1244 T1226 T1243
assignw BASE[8] T1244
goto B2432
@label B2386
assignw T1245 BASE[0]
assignw T1246 T1245[0]
assignw T1247 BASE[0]
assignw T1248 T1247[0]
assignw T1249 2
assignw T1251 T1248[16]
sub T1250 T1251 T1249
assignw T1252 T1246[12]
mult T1253 4 T1250
add T1253 T1253 4
assignw T1254 T1252[T1253]
assignw T1255 T1254[0]
assignw T1257 T1255[4]
assignw T1258 T1257[0]
assignw T1259 1
mult T1259 T1259 T1258
add T1259 T1259 4
malloc T1256 T1259
memcpy T1256 T1257 T1259
param T1260 0
assignw T1260[0] T1256
call T1261 STOF 1
assignw T1262 BASE[0]
assignw T1263 T1262[0]
assignw T1264 BASE[0]
assignw T1265 T1264[0]
assignw T1266 1
assignw T1268 T1265[16]
sub T1267 T1268 T1266
assignw T1269 T1263[12]
mult T1270 4 T1267
add T1270 T1270 4
assignw T1271 T1269[T1270]
assignw T1272 T1271[0]
assignw T1274 T1272[4]
assignw T1275 T1274[0]
assignw T1276 1
mult T1276 T1276 T1275
add T1276 T1276 4
malloc T1273 T1276
memcpy T1273 T1274 T1276
param T1277 0
assignw T1277[0] T1273
call T1278 STOF 1
sub T1279 T1261 T1278
assignw BASE[8] T1279
@label B2432
assignw T1280 BASE[0]
assignw T1281 T1280[0]
assignw T1282 BASE[0]
assignw T1283 T1282[0]
assignw T1284 2
assignw T1286 T1283[16]
sub T1285 T1286 T1284
assignw T1287 T1281[12]
mult T1288 4 T1285
add T1288 T1288 4
assignw T1289 T1287[T1288]
assignw T1290 T1289[0]
assignw T1292 T1290[4]
assignw T1293 T1292[0]
assignw T1294 1
mult T1294 T1294 T1293
add T1294 T1294 4
malloc T1291 T1294
memcpy T1291 T1292 T1294
param T1295 0
assignw T1295[0] T1291
assignw T1296 BASE[8]
param T1297 4
assignw T1297[0] T1296
call T1298 FTOS 2
assignw T1299 BASE[0]
param T1300 0
assignw T1300[0] T1299
call T1301 F15 1
goto B2484
goto B2484
@label B2463
assignw S18[0] 34
param T1303 0
assignw T1303[0] S18
param T1304 4
assignw T1304[0] 0
param T1305 8
assignw T1305[0] 0
param T1306 12
assignw T1306[0] 0
param T1307 16
assignw T1307[0] 0
param T1308 20
assignw T1308[0] S0
call T1309 PRINT 6
goto B2480
assignb T1310 True
goto Bool2481
@label B2480
assignb T1310 False
@label Bool2481
assignw lastbase BASE
return T1310
@label B2484
goto B2485
@label B2485
assignb T1311 True
goto Bool2488
assignb T1311 False
@label Bool2488
assignw lastbase BASE
return T1311
@label F19_end
assignw lastbase BASE
return 0
@endfunction 12
@function F20 12
assignw T1313 BASE[0]
param T1314 0
assignw T1314[0] T1313
param T1315 4
assignw T1315[0] T693
call T1316 F13 2
assignw BASE[4] T1316
assignb T1317 48
assignw T1318 0
assignw T1319 BASE[4]
mult T1320 1 T1318
add T1320 T1320 4
assignw T1321 T1319[T1320]
leq test T1317 T1321
goif B2512 test
goto B2521
@label B2512
assignw T1322 0
assignw T1323 BASE[4]
mult T1324 1 T1322
add T1324 T1324 4
assignb T1325 57
assignw T1326 T1323[T1324]
leq test T1326 T1325
goif B2557 test
goto B2521
@label B2521
assignb T1327 97
assignw T1328 0
assignw T1329 BASE[4]
mult T1330 1 T1328
add T1330 T1330 4
assignw T1331 T1329[T1330]
leq test T1327 T1331
goif B2530 test
goto B2539
@label B2530
assignw T1332 0
assignw T1333 BASE[4]
mult T1334 1 T1332
add T1334 T1334 4
assignb T1335 122
assignw T1336 T1333[T1334]
leq test T1336 T1335
goif B2557 test
goto B2539
@label B2539
assignw S19[0] 1
assignw T1339 BASE[4]
assignw T1340 T1339[0]
assignw T1341 1
mult T1341 T1341 T1340
add T1341 T1341 4
malloc T1338 T1341
memcpy T1338 T1339 T1341
param T1342 0
assignw T1342[0] T1338
param T1343 4
assignw T1343[0] S19
call T1344 F1 2
@label L55
assignw T1345 0
eq test T1344 T1345
goif B2557 test
goto B2889
@label B2557
assignw T1346 BASE[0]
param T1347 0
assignw T1347[0] T1346
call T1348 F14 1
assignw T1349 BASE[0]
param T1350 0
assignw T1350[0] T1349
call T1351 F21  1
goif B2575 T1351
goto B2567
@label B2567
goto B2570
assignb T1352 True
goto Bool2571
@label B2570
assignb T1352 False
@label Bool2571
assignw lastbase BASE
return T1352
goto B2575
@label B2575
assignw T1353 BASE[0]
assignw T1354 T1353[0]
assignw T1355 BASE[0]
assignw T1356 T1355[0]
assignw T1357 2
assignw T1359 T1356[16]
sub T1358 T1359 T1357
assignw T1360 T1354[12]
mult T1361 4 T1358
add T1361 T1361 4
assignw T1362 T1360[T1361]
assignw T1363 T1362[0]
assignw T1364 BASE[0]
assignw T1365 T1364[0]
assignw T1366 BASE[0]
assignw T1367 T1366[0]
assignw T1368 1
assignw T1370 T1367[16]
sub T1369 T1370 T1368
assignw T1371 T1365[12]
mult T1372 4 T1369
add T1372 T1372 4
assignw T1373 T1371[T1372]
assignw T1374 T1373[0]
assignw T1376 T1363[4]
assignw T1377 T1376[0]
assignw T1378 1
mult T1378 T1378 T1377
add T1378 T1378 4
malloc T1375 T1378
memcpy T1375 T1376 T1378
param T1379 0
assignw T1379[0] T1375
assignw T1381 T1374[4]
assignw T1382 T1381[0]
assignw T1383 1
mult T1383 T1383 T1382
add T1383 T1383 4
malloc T1380 T1383
memcpy T1380 T1381 T1383
param T1384 4
assignw T1384[0] T1380
call T1385 F2 2
assignw T1386 BASE[0]
param T1387 0
assignw T1387[0] T1386
call T1388 F15 1
assignw T1389 BASE[0]
param T1390 0
assignw T1390[0] T1389
param T1391 4
assignw T1391[0] T693
call T1392 F13 2
assignw BASE[4] T1392
assignw S20[0] 1
assignw T1395 BASE[4]
assignw T1396 T1395[0]
assignw T1397 1
mult T1397 T1397 T1396
add T1397 T1397 4
malloc T1394 T1397
memcpy T1394 T1395 T1397
param T1398 0
assignw T1398[0] T1394
param T1399 4
assignw T1399[0] S20
call T1400 F1 2
@label L56
assignw T1401 0
eq test T1400 T1401
goif B2665 test
goto B2647
@label B2647
assignw S21[0] 1
assignw T1404 BASE[4]
assignw T1405 T1404[0]
assignw T1406 1
mult T1406 T1406 T1405
add T1406 T1406 4
malloc T1403 T1406
memcpy T1403 T1404 T1406
param T1407 0
assignw T1407[0] T1403
param T1408 4
assignw T1408[0] S21
call T1409 F1 2
@label L57
assignw T1410 0
eq test T1409 T1410
goif B2665 test
goto B2910
@label B2665
assignw T1411 BASE[0]
param T1412 0
assignw T1412[0] T1411
call T1413 F14 1
assignw T1414 BASE[0]
param T1415 0
assignw T1415[0] T1414
assignw T1417 BASE[4]
assignw T1418 T1417[0]
assignw T1419 1
mult T1419 T1419 T1418
add T1419 T1419 4
malloc T1416 T1419
memcpy T1416 T1417 T1419
param T1420 4
assignw T1420[0] T1416
call T1421 F12 2
goif B2684 T1421
goto B2684
@label B2684
assignw T1422 BASE[0]
param T1423 0
assignw T1423[0] T1422
call T1424 F20 1
goif B2698 T1424
goto B2690
@label B2690
goto B2693
assignb T1425 True
goto Bool2694
@label B2693
assignb T1425 False
@label Bool2694
assignw lastbase BASE
return T1425
goto B2698
@label B2698
assignw S22[0] 1
assignw T1428 BASE[4]
assignw T1429 T1428[0]
assignw T1430 1
mult T1430 T1430 T1429
add T1430 T1430 4
malloc T1427 T1430
memcpy T1427 T1428 T1430
param T1431 0
assignw T1431[0] T1427
param T1432 4
assignw T1432[0] S22
call T1433 F1 2
@label L58
assignw T1434 0
eq test T1433 T1434
goif B2716 test
goto B2763
@label B2716
assignw T1435 BASE[0]
assignw T1436 T1435[0]
assignw T1437 BASE[0]
assignw T1438 T1437[0]
assignw T1439 2
assignw T1441 T1438[16]
sub T1440 T1441 T1439
assignw T1442 T1436[12]
mult T1443 4 T1440
add T1443 T1443 4
assignw T1444 T1442[T1443]
assignw T1445 T1444[0]
assignw T1447 T1445[4]
assignw T1448 T1447[0]
assignw T1449 1
mult T1449 T1449 T1448
add T1449 T1449 4
malloc T1446 T1449
memcpy T1446 T1447 T1449
param T1450 0
assignw T1450[0] T1446
call T1451 STOF 1
assignw T1452 BASE[0]
assignw T1453 T1452[0]
assignw T1454 BASE[0]
assignw T1455 T1454[0]
assignw T1456 1
assignw T1458 T1455[16]
sub T1457 T1458 T1456
assignw T1459 T1453[12]
mult T1460 4 T1457
add T1460 T1460 4
assignw T1461 T1459[T1460]
assignw T1462 T1461[0]
assignw T1464 T1462[4]
assignw T1465 T1464[0]
assignw T1466 1
mult T1466 T1466 T1465
add T1466 T1466 4
malloc T1463 T1466
memcpy T1463 T1464 T1466
param T1467 0
assignw T1467[0] T1463
call T1468 STOF 1
mult T1469 T1451 T1468
assignw BASE[8] T1469
goto B2858
@label B2763
assignw T1470 BASE[0]
assignw T1471 T1470[0]
assignw T1472 BASE[0]
assignw T1473 T1472[0]
assignw T1474 1
assignw T1476 T1473[16]
sub T1475 T1476 T1474
assignw T1477 T1471[12]
mult T1478 4 T1475
add T1478 T1478 4
assignw T1479 T1477[T1478]
assignw T1480 T1479[0]
assignw T1482 T1480[4]
assignw T1483 T1482[0]
assignw T1484 1
mult T1484 T1484 T1483
add T1484 T1484 4
malloc T1481 T1484
memcpy T1481 T1482 T1484
param T1485 0
assignw T1485[0] T1481
call T1486 STOF 1
@label L59
assignw T1487 0
eq test T1486 T1487
goif B2790 test
goto B2812
@label B2790
assignw S23[0] 28
param T1489 0
assignw T1489[0] S23
param T1490 4
assignw T1490[0] 0
param T1491 8
assignw T1491[0] 0
param T1492 12
assignw T1492[0] 0
param T1493 16
assignw T1493[0] 0
param T1494 20
assignw T1494[0] S0
call T1495 PRINT 6
goto B2807
assignb T1496 True
goto Bool2808
@label B2807
assignb T1496 False
@label Bool2808
assignw lastbase BASE
return T1496
goto B2812
@label B2812
assignw T1497 BASE[0]
assignw T1498 T1497[0]
assignw T1499 BASE[0]
assignw T1500 T1499[0]
assignw T1501 2
assignw T1503 T1500[16]
sub T1502 T1503 T1501
assignw T1504 T1498[12]
mult T1505 4 T1502
add T1505 T1505 4
assignw T1506 T1504[T1505]
assignw T1507 T1506[0]
assignw T1509 T1507[4]
assignw T1510 T1509[0]
assignw T1511 1
mult T1511 T1511 T1510
add T1511 T1511 4
malloc T1508 T1511
memcpy T1508 T1509 T1511
param T1512 0
assignw T1512[0] T1508
call T1513 STOF 1
assignw T1514 BASE[0]
assignw T1515 T1514[0]
assignw T1516 BASE[0]
assignw T1517 T1516[0]
assignw T1518 1
assignw T1520 T1517[16]
sub T1519 T1520 T1518
assignw T1521 T1515[12]
mult T1522 4 T1519
add T1522 T1522 4
assignw T1523 T1521[T1522]
assignw T1524 T1523[0]
assignw T1526 T1524[4]
assignw T1527 T1526[0]
assignw T1528 1
mult T1528 T1528 T1527
add T1528 T1528 4
malloc T1525 T1528
memcpy T1525 T1526 T1528
param T1529 0
assignw T1529[0] T1525
call T1530 STOF 1
div T1531 T1513 T1530
assignw BASE[8] T1531
@label B2858
assignw T1532 BASE[0]
assignw T1533 T1532[0]
assignw T1534 BASE[0]
assignw T1535 T1534[0]
assignw T1536 2
assignw T1538 T1535[16]
sub T1537 T1538 T1536
assignw T1539 T1533[12]
mult T1540 4 T1537
add T1540 T1540 4
assignw T1541 T1539[T1540]
assignw T1542 T1541[0]
assignw T1544 T1542[4]
assignw T1545 T1544[0]
assignw T1546 1
mult T1546 T1546 T1545
add T1546 T1546 4
malloc T1543 T1546
memcpy T1543 T1544 T1546
param T1547 0
assignw T1547[0] T1543
assignw T1548 BASE[8]
param T1549 4
assignw T1549[0] T1548
call T1550 FTOS 2
assignw T1551 BASE[0]
param T1552 0
assignw T1552[0] T1551
call T1553 F15 1
goto B2910
goto B2910
@label B2889
assignw S24[0] 34
param T1555 0
assignw T1555[0] S24
param T1556 4
assignw T1556[0] 0
param T1557 8
assignw T1557[0] 0
param T1558 12
assignw T1558[0] 0
param T1559 16
assignw T1559[0] 0
param T1560 20
assignw T1560[0] S0
call T1561 PRINT 6
goto B2906
assignb T1562 True
goto Bool2907
@label B2906
assignb T1562 False
@label Bool2907
assignw lastbase BASE
return T1562
@label B2910
goto B2911
@label B2911
assignb T1563 True
goto Bool2914
assignb T1563 False
@label Bool2914
assignw lastbase BASE
return T1563
@label F20_end
assignw lastbase BASE
return 0
@endfunction 12
@function F21 12
assignw T1565 BASE[0]
param T1566 0
assignw T1566[0] T1565
param T1567 4
assignw T1567[0] T693
call T1568 F13 2
assignw BASE[4] T1568
assignw S25[0] 1
assignw T1571 BASE[4]
assignw T1572 T1571[0]
assignw T1573 1
mult T1573 T1573 T1572
add T1573 T1573 4
malloc T1570 T1573
memcpy T1570 T1571 T1573
param T1574 0
assignw T1574[0] T1570
param T1575 4
assignw T1575[0] S25
call T1576 F1 2
@label L60
assignw T1577 0
eq test T1576 T1577
goif B2947 test
goto B3053
@label B2947
assignw S26[0] 1
assignw T1579 BASE[0]
param T1580 0
assignw T1580[0] T1579
param T1581 4
assignw T1581[0] S26
call T1582 F12 2
goif B2956 T1582
goto B2956
@label B2956
assignw T1583 BASE[0]
param T1584 0
assignw T1584[0] T1583
call T1585 F14 1
assignw T1586 BASE[0]
param T1587 0
assignw T1587[0] T1586
call T1588 F19 1
goif B2974 T1588
goto B2966
@label B2966
goto B2969
assignb T1589 True
goto Bool2970
@label B2969
assignb T1589 False
@label Bool2970
assignw lastbase BASE
return T1589
goto B2974
@label B2974
assignw S27[0] 1
assignw T1591 BASE[0]
param T1592 0
assignw T1592[0] T1591
param T1593 4
assignw T1593[0] S27
call T1594 F12 2
goif B3005 T1594
goto B2983
@label B2983
assignw S28[0] 34
param T1596 0
assignw T1596[0] S28
param T1597 4
assignw T1597[0] 0
param T1598 8
assignw T1598[0] 0
param T1599 12
assignw T1599[0] 0
param T1600 16
assignw T1600[0] 0
param T1601 20
assignw T1601[0] S0
call T1602 PRINT 6
goto B3000
assignb T1603 True
goto Bool3001
@label B3000
assignb T1603 False
@label Bool3001
assignw lastbase BASE
return T1603
goto B3005
@label B3005
assignw T1604 BASE[0]
assignw T1605 T1604[0]
assignw T1606 BASE[0]
assignw T1607 T1606[0]
assignw T1608 2
assignw T1610 T1607[16]
sub T1609 T1610 T1608
assignw T1611 T1605[12]
mult T1612 4 T1609
add T1612 T1612 4
assignw T1613 T1611[T1612]
assignw T1614 T1613[0]
assignw T1615 BASE[0]
assignw T1616 T1615[0]
assignw T1617 BASE[0]
assignw T1618 T1617[0]
assignw T1619 1
assignw T1621 T1618[16]
sub T1620 T1621 T1619
assignw T1622 T1616[12]
mult T1623 4 T1620
add T1623 T1623 4
assignw T1624 T1622[T1623]
assignw T1625 T1624[0]
assignw T1627 T1614[4]
assignw T1628 T1627[0]
assignw T1629 1
mult T1629 T1629 T1628
add T1629 T1629 4
malloc T1626 T1629
memcpy T1626 T1627 T1629
param T1630 0
assignw T1630[0] T1626
assignw T1632 T1625[4]
assignw T1633 T1632[0]
assignw T1634 1
mult T1634 T1634 T1633
add T1634 T1634 4
malloc T1631 T1634
memcpy T1631 T1632 T1634
param T1635 4
assignw T1635[0] T1631
call T1636 F2 2
assignw T1637 BASE[0]
param T1638 0
assignw T1638[0] T1637
call T1639 F15 1
goto B3237
@label B3053
assignw T1641 BASE[4]
assignw T1642 T1641[0]
assignw T1643 1
mult T1643 T1643 T1642
add T1643 T1643 4
malloc T1640 T1643
memcpy T1640 T1641 T1643
param T1644 0
assignw T1644[0] T1640
call T1645 F5 1
goif B3065 T1645
goto B3116
@label B3065
assignw T1646 BASE[0]
param T1647 0
assignw T1647[0] T1646
assignw T1649 BASE[4]
assignw T1650 T1649[0]
assignw T1651 1
mult T1651 T1651 T1650
add T1651 T1651 4
malloc T1648 T1651
memcpy T1648 T1649 T1651
param T1652 4
assignw T1652[0] T1648
call T1653 F12 2
goif B3080 T1653
goto B3080
@label B3080
assignw T1654 BASE[0]
assignw T1655 T1654[0]
assignw T1656 BASE[0]
assignw T1657 T1656[0]
assignw T1658 2
assignw T1660 T1657[16]
sub T1659 T1660 T1658
assignw T1661 T1655[12]
mult T1662 4 T1659
add T1662 T1662 4
assignw T1663 T1661[T1662]
assignw T1664 T1663[0]
assignw T1666 T1664[4]
assignw T1667 T1666[0]
assignw T1668 1
mult T1668 T1668 T1667
add T1668 T1668 4
malloc T1665 T1668
memcpy T1665 T1666 T1668
param T1669 0
assignw T1669[0] T1665
assignw T1671 BASE[4]
assignw T1672 T1671[0]
assignw T1673 1
mult T1673 T1673 T1672
add T1673 T1673 4
malloc T1670 T1673
memcpy T1670 T1671 T1673
param T1674 4
assignw T1674[0] T1670
call T1675 F2 2
assignw T1676 BASE[0]
param T1677 0
assignw T1677[0] T1676
call T1678 F15 1
goto B3237
@label B3116
assignb T1679 97
assignw T1680 0
assignw T1681 BASE[4]
mult T1682 1 T1680
add T1682 T1682 4
assignw T1683 T1681[T1682]
leq test T1679 T1683
goif B3125 test
goto B3216
@label B3125
assignw T1684 0
assignw T1685 BASE[4]
mult T1686 1 T1684
add T1686 T1686 4
assignb T1687 122
assignw T1688 T1685[T1686]
leq test T1688 T1687
goif B3134 test
goto B3216
@label B3134
assignw T1690 BASE[4]
assignw T1691 T1690[0]
assignw T1692 1
mult T1692 T1692 T1691
add T1692 T1692 4
malloc T1689 T1692
memcpy T1689 T1690 T1692
param T1693 0
assignw T1693[0] T1689
param T1694 4
assignb T1694[0] T40
call T1695 F0 2
@label L61
assignw T1696 1
eq test T1695 T1696
goif B3151 test
goto B3216
@label B3151
assignw T1697 BASE[0]
param T1698 0
assignw T1698[0] T1697
assignw T1700 BASE[4]
assignw T1701 T1700[0]
assignw T1702 1
mult T1702 T1702 T1701
add T1702 T1702 4
malloc T1699 T1702
memcpy T1699 T1700 T1702
param T1703 4
assignw T1703[0] T1699
call T1704 F12 2
goif B3166 T1704
goto B3166
@label B3166
assignw T1705 BASE[36]
param T1706 0
assignw T1706[0] T1705
assignw T1708 BASE[4]
assignw T1709 T1708[0]
assignw T1710 1
mult T1710 T1710 T1709
add T1710 T1710 4
malloc T1707 T1710
memcpy T1707 T1708 T1710
param T1711 4
assignw T1711[0] T1707
assignw T1712 BASE[8]
param T1713 8
assignw T1713[0] T1712
call T1714 F9 3
assignw T1715 lastbase[8]
assignw BASE[8] T1715
goif B3186 T1714
goto B3186
@label B3186
assignw T1716 BASE[0]
assignw T1717 T1716[0]
assignw T1718 BASE[0]
assignw T1719 T1718[0]
assignw T1720 2
assignw T1722 T1719[16]
sub T1721 T1722 T1720
assignw T1723 T1717[12]
mult T1724 4 T1721
add T1724 T1724 4
assignw T1725 T1723[T1724]
assignw T1726 T1725[0]
assignw T1728 T1726[4]
assignw T1729 T1728[0]
assignw T1730 1
mult T1730 T1730 T1729
add T1730 T1730 4
malloc T1727 T1730
memcpy T1727 T1728 T1730
param T1731 0
assignw T1731[0] T1727
assignw T1732 BASE[8]
param T1733 4
assignw T1733[0] T1732
call T1734 FTOS 2
assignw T1735 BASE[0]
param T1736 0
assignw T1736[0] T1735
call T1737 F15 1
goto B3237
@label B3216
assignw S29[0] 34
param T1739 0
assignw T1739[0] S29
param T1740 4
assignw T1740[0] 0
param T1741 8
assignw T1741[0] 0
param T1742 12
assignw T1742[0] 0
param T1743 16
assignw T1743[0] 0
param T1744 20
assignw T1744[0] S0
call T1745 PRINT 6
goto B3233
assignb T1746 True
goto Bool3234
@label B3233
assignb T1746 False
@label Bool3234
assignw lastbase BASE
return T1746
@label B3237
goto B3238
@label B3238
assignb T1747 True
goto Bool3241
assignb T1747 False
@label Bool3241
assignw lastbase BASE
return T1747
@label F21_end
assignw lastbase BASE
return 0
@endfunction 12
