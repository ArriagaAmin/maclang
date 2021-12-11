@string S0 "0000\n"
@string S1 "0000Menu principal. Escoja una de las siguientes opciones: "
@string S2 "00001. Ordenar numeros enteros. "
@string S3 "00002. Ordenar numeros en punto flotante. "
@string S4 "00003. Ordenar caracteres. "
@string S5 "00004. Salir. "
@string S6 "0000Indique el numero de elementos a ordenar. Recuerde que debe estar entre 1 y 100: "
@string S7 "0000Numero de elementos invalido."
@string S8 "0000Indique los elementos: "
@string S9 "0000%cEl arreglo ordenado de enteros es:%c["
@string S10 "0000%i, "
@string S11 "0000%i]%c"
@string S12 "0000%cEl arreglo ordenado de flotantes es:%c["
@string S13 "0000%f, "
@string S14 "0000%f]%c"
@string S15 "0000%cEl arreglo ordenado de caracteres es:%c["
@string S16 "0000%c, "
@string S17 "0000%c]%c"
@string S18 "0000Hasta luego!"
@string S19 "0000Opcion invalida."
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
assignb T20 10
assignw T21 1
assignw T23 T21
assignw T24 1
mult T24 T24 T23
add T24 T24 4
malloc T22 T24
assignw T22[0] T23
assignb T22[4] T20
assignw T25 T22
assignw T32 100
assignw T34 T32
assignw T35 4
mult T35 T35 T34
add T35 T35 4
malloc T33 T35
assignw T33[0] T34
assignw T36 100
assignw T38 T36
assignw T39 4
mult T39 T39 T38
add T39 T39 4
malloc T37 T39
assignw T37[0] T38
assignw T40 100
assignw T42 T40
assignw T43 1
mult T43 T43 T42
add T43 T43 4
malloc T41 T43
assignw T41[0] T42
@label L6
goto B127
@label B127
assignw S1[0] 55
param T45 0
assignw T45[0] S1
param T46 4
assignw T46[0] 0
param T47 8
assignw T47[0] 0
param T48 12
assignw T48[0] 0
param T49 16
assignw T49[0] 0
param T50 20
assignw T50[0] S0
call T51 PRINT 6
assignw S2[0] 28
param T53 0
assignw T53[0] S2
param T54 4
assignw T54[0] 0
param T55 8
assignw T55[0] 0
param T56 12
assignw T56[0] 0
param T57 16
assignw T57[0] 0
param T58 20
assignw T58[0] S0
call T59 PRINT 6
assignw S3[0] 38
param T61 0
assignw T61[0] S3
param T62 4
assignw T62[0] 0
param T63 8
assignw T63[0] 0
param T64 12
assignw T64[0] 0
param T65 16
assignw T65[0] 0
param T66 20
assignw T66[0] S0
call T67 PRINT 6
assignw S4[0] 23
param T69 0
assignw T69[0] S4
param T70 4
assignw T70[0] 0
param T71 8
assignw T71[0] 0
param T72 12
assignw T72[0] 0
param T73 16
assignw T73[0] 0
param T74 20
assignw T74[0] S0
call T75 PRINT 6
assignw S5[0] 10
param T77 0
assignw T77[0] S5
param T78 4
assignw T78[0] 0
param T79 8
assignw T79[0] 0
param T80 12
assignw T80[0] 0
param T81 16
assignw T81[0] 0
param T82 20
assignw T82[0] S0
call T83 PRINT 6
call T84 READI 0
assignw T29 T84
assignw T85 0
lt test T85 T29
goif B203 test
goto B711
@label B203
assignw T86 4
lt test T29 T86
goif B207 test
goto B711
@label B207
assignw S6[0] 81
param T88 0
assignw T88[0] S6
param T89 4
assignw T89[0] 0
param T90 8
assignw T90[0] 0
param T91 12
assignw T91[0] 0
param T92 16
assignw T92[0] 0
param T93 20
assignw T93[0] S0
call T94 PRINT 6
call T95 READI 0
assignw T30 T95
assignw T96 1
lt test T30 T96
goif B231 test
goto B227
@label B227
assignw T97 100
gt test T30 T97
goif B231 test
goto B247
@label B231
assignw S7[0] 29
param T99 0
assignw T99[0] S7
param T100 4
assignw T100[0] 0
param T101 8
assignw T101[0] 0
param T102 12
assignw T102[0] 0
param T103 16
assignw T103[0] 0
param T104 20
assignw T104[0] S0
call T105 PRINT 6
goto L6
goto B247
@label B247
assignw S8[0] 23
param T107 0
assignw T107[0] S8
param T108 4
assignw T108[0] 0
param T109 8
assignw T109[0] 0
param T110 12
assignw T110[0] 0
param T111 16
assignw T111[0] 0
param T112 20
assignw T112[0] S0
call T113 PRINT 6
@label L7
assignw T114 1
eq test T29 T114
goif B266 test
goto B415
@label B266
assignw T115 0
assignw T117 T115
@label L8
geq test T117 T30
goif L8_end test
assignw T116 T117
mult T118 4 T116
add T118 T118 4
call T119 READI 0
assignw T33[T118] T119
add T117 T117 1
goto L8
@label L8_end
assignw T120 0
assignw T122 T33[0]
assignw T123 4
mult T123 T123 T122
add T123 T123 4
malloc T121 T123
memcpy T121 T33 T123
param T124 0
assignw T124[0] T121
param T125 4
assignw T125[0] T120
param T126 8
assignw T126[0] T30
call T127 Function1  3
assignw S9[0] 39
assignb T129 10
assignb T130 91
assignw T131 2
assignw T133 T131
assignw T134 1
mult T134 T134 T133
add T134 T134 4
malloc T132 T134
assignw T132[0] T133
assignb T132[5] T130
assignb T132[4] T129
param T135 0
assignw T135[0] S9
assignw T137 T132[0]
assignw T138 1
mult T138 T138 T137
add T138 T138 4
malloc T136 T138
memcpy T136 T132 T138
param T139 4
assignw T139[0] T136
param T140 8
assignw T140[0] 0
param T141 12
assignw T141[0] 0
param T142 16
assignw T142[0] 0
param T143 20
assignw T143[0] S0
call T144 PRINT 6
assignw T145 0
assignw T146 1
sub T147 T30 T146
assignw T149 T145
@label L9
geq test T149 T147
goif L9_end test
assignw T148 T149
assignw S10[0] 4
mult T151 4 T148
add T151 T151 4
assignw T152 1
assignw T154 T152
assignw T155 4
mult T155 T155 T154
add T155 T155 4
malloc T153 T155
assignw T153[0] T154
assignw T156 T33[T151]
assignw T153[4] T156
param T157 0
assignw T157[0] S10
param T158 4
assignw T158[0] 0
assignw T160 T153[0]
assignw T161 4
mult T161 T161 T160
add T161 T161 4
malloc T159 T161
memcpy T159 T153 T161
param T162 8
assignw T162[0] T159
param T163 12
assignw T163[0] 0
param T164 16
assignw T164[0] 0
param T165 20
assignw T165[0] S0
call T166 PRINT 6
add T149 T149 1
goto L9
@label L9_end
assignw S11[0] 5
assignw T168 1
sub T169 T30 T168
mult T170 4 T169
add T170 T170 4
assignw T171 1
assignw T173 T171
assignw T174 4
mult T174 T174 T173
add T174 T174 4
malloc T172 T174
assignw T172[0] T173
assignw T175 T33[T170]
assignw T172[4] T175
assignb T176 10
assignw T177 1
assignw T179 T177
assignw T180 1
mult T180 T180 T179
add T180 T180 4
malloc T178 T180
assignw T178[0] T179
assignb T178[4] T176
param T181 0
assignw T181[0] S11
assignw T183 T178[0]
assignw T184 1
mult T184 T184 T183
add T184 T184 4
malloc T182 T184
memcpy T182 T178 T184
param T185 4
assignw T185[0] T182
assignw T187 T172[0]
assignw T188 4
mult T188 T188 T187
add T188 T188 4
malloc T186 T188
memcpy T186 T172 T188
param T189 8
assignw T189[0] T186
param T190 12
assignw T190[0] 0
param T191 16
assignw T191[0] 0
param T192 20
assignw T192[0] S0
call T193 PRINT 6
goto L6
@label B415
@label L10
assignw T194 2
eq test T29 T194
goif B420 test
goto B569
@label B420
assignw T195 0
assignw T197 T195
@label L11
geq test T197 T30
goif L11_end test
assignw T196 T197
mult T198 4 T196
add T198 T198 4
call f4 READF 0
assignw T37[T198] f4
add T197 T197 1
goto L11
@label L11_end
assignw T199 0
assignw T201 T37[0]
assignw T202 4
mult T202 T202 T201
add T202 T202 4
malloc T200 T202
memcpy T200 T37 T202
param T203 0
assignw T203[0] T200
param T204 4
assignw T204[0] T199
param T205 8
assignw T205[0] T30
call T206 Function3  3
assignw S12[0] 41
assignb T208 10
assignb T209 91
assignw T210 2
assignw T212 T210
assignw T213 1
mult T213 T213 T212
add T213 T213 4
malloc T211 T213
assignw T211[0] T212
assignb T211[5] T209
assignb T211[4] T208
param T214 0
assignw T214[0] S12
assignw T216 T211[0]
assignw T217 1
mult T217 T217 T216
add T217 T217 4
malloc T215 T217
memcpy T215 T211 T217
param T218 4
assignw T218[0] T215
param T219 8
assignw T219[0] 0
param T220 12
assignw T220[0] 0
param T221 16
assignw T221[0] 0
param T222 20
assignw T222[0] S0
call T223 PRINT 6
assignw T224 0
assignw T225 1
sub T226 T30 T225
assignw T228 T224
@label L12
geq test T228 T226
goif L12_end test
assignw T227 T228
assignw S13[0] 4
mult T230 4 T227
add T230 T230 4
assignw T231 1
assignw T233 T231
assignw T234 4
mult T234 T234 T233
add T234 T234 4
malloc T232 T234
assignw T232[0] T233
assignw f5 T37[T230]
assignw T232[4] f5
param T235 0
assignw T235[0] S13
param T236 4
assignw T236[0] 0
param T237 8
assignw T237[0] 0
assignw T239 T232[0]
assignw T240 4
mult T240 T240 T239
add T240 T240 4
malloc T238 T240
memcpy T238 T232 T240
param T241 12
assignw T241[0] T238
param T242 16
assignw T242[0] 0
param T243 20
assignw T243[0] S0
call T244 PRINT 6
add T228 T228 1
goto L12
@label L12_end
assignw S14[0] 5
assignw T246 1
sub T247 T30 T246
mult T248 4 T247
add T248 T248 4
assignw T249 1
assignw T251 T249
assignw T252 4
mult T252 T252 T251
add T252 T252 4
malloc T250 T252
assignw T250[0] T251
assignw f6 T37[T248]
assignw T250[4] f6
assignb T253 10
assignw T254 1
assignw T256 T254
assignw T257 1
mult T257 T257 T256
add T257 T257 4
malloc T255 T257
assignw T255[0] T256
assignb T255[4] T253
param T258 0
assignw T258[0] S14
assignw T260 T255[0]
assignw T261 1
mult T261 T261 T260
add T261 T261 4
malloc T259 T261
memcpy T259 T255 T261
param T262 4
assignw T262[0] T259
param T263 8
assignw T263[0] 0
assignw T265 T250[0]
assignw T266 4
mult T266 T266 T265
add T266 T266 4
malloc T264 T266
memcpy T264 T250 T266
param T267 12
assignw T267[0] T264
param T268 16
assignw T268[0] 0
param T269 20
assignw T269[0] S0
call T270 PRINT 6
goto L6
@label B569
@label L13
assignw T271 2
eq test T29 T271
goif B574 test
goto L6
@label B574
assignw T272 0
assignw T274 T272
@label L14
geq test T274 T30
goif L14_end test
assignw T273 T274
mult T275 1 T273
add T275 T275 4
call T276 READC 0
assignb T41[T275] T276
add T274 T274 1
goto L14
@label L14_end
assignw T277 0
assignw T279 T41[0]
assignw T280 1
mult T280 T280 T279
add T280 T280 4
malloc T278 T280
memcpy T278 T41 T280
param T281 0
assignw T281[0] T278
param T282 4
assignw T282[0] T277
param T283 8
assignw T283[0] T30
call T284 Function5  3
assignw S15[0] 42
assignb T286 10
assignb T287 91
assignw T288 2
assignw T290 T288
assignw T291 1
mult T291 T291 T290
add T291 T291 4
malloc T289 T291
assignw T289[0] T290
assignb T289[5] T287
assignb T289[4] T286
param T292 0
assignw T292[0] S15
assignw T294 T289[0]
assignw T295 1
mult T295 T295 T294
add T295 T295 4
malloc T293 T295
memcpy T293 T289 T295
param T296 4
assignw T296[0] T293
param T297 8
assignw T297[0] 0
param T298 12
assignw T298[0] 0
param T299 16
assignw T299[0] 0
param T300 20
assignw T300[0] S0
call T301 PRINT 6
assignw T302 0
assignw T303 1
sub T304 T30 T303
assignw T306 T302
@label L15
geq test T306 T304
goif L15_end test
assignw T305 T306
assignw S16[0] 4
mult T308 1 T305
add T308 T308 4
assignw T309 1
assignw T311 T309
assignw T312 1
mult T312 T312 T311
add T312 T312 4
malloc T310 T312
assignw T310[0] T311
assignb T313 T41[T308]
assignb T310[4] T313
param T314 0
assignw T314[0] S16
assignw T316 T310[0]
assignw T317 1
mult T317 T317 T316
add T317 T317 4
malloc T315 T317
memcpy T315 T310 T317
param T318 4
assignw T318[0] T315
param T319 8
assignw T319[0] 0
param T320 12
assignw T320[0] 0
param T321 16
assignw T321[0] 0
param T322 20
assignw T322[0] S0
call T323 PRINT 6
add T306 T306 1
goto L15
@label L15_end
assignw S17[0] 5
assignw T325 1
sub T326 T30 T325
mult T327 1 T326
add T327 T327 4
assignb T328 10
assignw T329 2
assignw T331 T329
assignw T332 1
mult T332 T332 T331
add T332 T332 4
malloc T330 T332
assignw T330[0] T331
assignb T330[5] T328
assignb T333 T41[T327]
assignb T330[4] T333
param T334 0
assignw T334[0] S17
assignw T336 T330[0]
assignw T337 1
mult T337 T337 T336
add T337 T337 4
malloc T335 T337
memcpy T335 T330 T337
param T338 4
assignw T338[0] T335
param T339 8
assignw T339[0] 0
param T340 12
assignw T340[0] 0
param T341 16
assignw T341[0] 0
param T342 20
assignw T342[0] S0
call T343 PRINT 6
goto L6
goto L6
@label B711
@label L16
assignw T344 4
eq test T29 T344
goif B716 test
goto B732
@label B716
assignw S18[0] 12
param T346 0
assignw T346[0] S18
param T347 4
assignw T347[0] 0
param T348 8
assignw T348[0] 0
param T349 12
assignw T349[0] 0
param T350 16
assignw T350[0] 0
param T351 20
assignw T351[0] S0
call T352 PRINT 6
goto B764
goto L6
@label B732
assignw S19[0] 16
assignb T354 10
assignb T355 10
assignw T356 2
assignw T358 T356
assignw T359 1
mult T359 T359 T358
add T359 T359 4
malloc T357 T359
assignw T357[0] T358
assignb T357[5] T355
assignb T357[4] T354
param T360 0
assignw T360[0] S19
param T361 4
assignw T361[0] 0
param T362 8
assignw T362[0] 0
param T363 12
assignw T363[0] 0
param T364 16
assignw T364[0] 0
assignw T366 T357[0]
assignw T367 1
mult T367 T367 T366
add T367 T367 4
malloc T365 T367
memcpy T365 T357 T367
param T368 20
assignw T368[0] T365
call T369 PRINT 6
goto L6
@label B764
@function Function0 12
assignw T370 BASE[0]
assignw BASE[8] T370
assignw T371 BASE[4]
assignw BASE[0] T371
assignw T372 BASE[8]
assignw BASE[4] T372
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function1 28
assignw T374 BASE[8]
assignw T375 BASE[4]
leq test T374 T375
goif B781 test
goto B784
@label B781
assignw lastbase BASE
return 0
goto B784
@label B784
assignw T376 BASE[4]
assignw BASE[12] T376
assignw T377 1
assignw T379 BASE[8]
sub T378 T379 T377
assignw BASE[16] T378
assignw T380 BASE[0]
assignw T381 BASE[8]
mult T382 4 T381
add T382 T382 4
assignw T383 T380[T382]
assignw BASE[20] T383
@label L17
goto B798
@label B798
@label L18
assignw T384 BASE[0]
assignw T385 BASE[12]
mult T386 4 T385
add T386 T386 4
assignw T387 T384[T386]
assignw T388 BASE[20]
lt test T387 T388
goif B808 test
goto B813
@label B808
assignw T389 1
assignw T391 BASE[12]
add T390 T391 T389
assignw BASE[12] T390
goto L18
@label B813
@label L19
assignw T392 BASE[0]
assignw T393 BASE[16]
mult T394 4 T393
add T394 T394 4
assignw T395 T392[T394]
assignw T396 BASE[20]
gt test T395 T396
goif B823 test
goto B828
@label B823
assignw T397 1
assignw T399 BASE[16]
sub T398 T399 T397
assignw BASE[16] T398
goto L19
@label B828
assignw T400 BASE[12]
assignw T401 BASE[16]
geq test T400 T401
goif B833 test
goto B835
@label B833
goto B855
goto B835
@label B835
assignw T402 BASE[0]
assignw T403 BASE[12]
mult T404 4 T403
add T404 T404 4
assignw T405 BASE[0]
assignw T406 BASE[16]
mult T407 4 T406
add T407 T407 4
assignw T408 T402[T404]
param T409 0
assignw T409[0] T408
assignw T410 T405[T407]
param T411 4
assignw T411[0] T410
call T412 Function0 2
assignw T413 lastbase[0]
assignw T402[T404] T413
assignw T414 lastbase[4]
assignw T405[T407] T414
goto L17
@label B855
assignw T415 BASE[0]
assignw T416 BASE[12]
mult T417 4 T416
add T417 T417 4
assignw T418 BASE[0]
assignw T419 BASE[8]
mult T420 4 T419
add T420 T420 4
assignw T421 T415[T417]
param T422 0
assignw T422[0] T421
assignw T423 T418[T420]
param T424 4
assignw T424[0] T423
call T425 Function0 2
assignw T426 lastbase[0]
assignw T415[T417] T426
assignw T427 lastbase[4]
assignw T418[T420] T427
assignw T429 BASE[0]
assignw T430 T429[0]
assignw T431 4
mult T431 T431 T430
add T431 T431 4
malloc T428 T431
memcpy T428 T429 T431
param T432 0
assignw T432[0] T428
assignw T433 BASE[4]
param T434 4
assignw T434[0] T433
assignw T435 BASE[16]
param T436 8
assignw T436[0] T435
call T437 Function1 3
assignw T438 1
assignw T440 BASE[12]
add T439 T440 T438
assignw T442 BASE[0]
assignw T443 T442[0]
assignw T444 4
mult T444 T444 T443
add T444 T444 4
malloc T441 T444
memcpy T441 T442 T444
param T445 0
assignw T445[0] T441
param T446 4
assignw T446[0] T439
assignw T447 BASE[8]
param T448 8
assignw T448[0] T447
call T449 Function1 3
@label Function1_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function2 12
assignw f7 BASE[0]
assignw BASE[8] f7
assignw f8 BASE[4]
assignw BASE[0] f8
assignw f9 BASE[8]
assignw BASE[4] f9
@label Function2_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function3 28
assignw T451 BASE[8]
assignw T452 BASE[4]
leq test T451 T452
goif B929 test
goto B932
@label B929
assignw lastbase BASE
return 0
goto B932
@label B932
assignw T453 BASE[4]
assignw BASE[12] T453
assignw T454 1
assignw T456 BASE[8]
sub T455 T456 T454
assignw BASE[16] T455
assignw T457 BASE[0]
assignw T458 BASE[8]
mult T459 4 T458
add T459 T459 4
assignw f10 T457[T459]
assignw BASE[20] f10
@label L20
goto B946
@label B946
@label L21
assignw T460 BASE[0]
assignw T461 BASE[12]
mult T462 4 T461
add T462 T462 4
assignw f11 T460[T462]
assignw f12 BASE[20]
lt test f11 f12
goif B956 test
goto B961
@label B956
assignw T463 1
assignw T465 BASE[12]
add T464 T465 T463
assignw BASE[12] T464
goto L21
@label B961
@label L22
assignw T466 BASE[0]
assignw T467 BASE[16]
mult T468 4 T467
add T468 T468 4
assignw f13 T466[T468]
assignw f14 BASE[20]
gt test f13 f14
goif B971 test
goto B976
@label B971
assignw T469 1
assignw T471 BASE[16]
sub T470 T471 T469
assignw BASE[16] T470
goto L22
@label B976
assignw T472 BASE[12]
assignw T473 BASE[16]
geq test T472 T473
goif B981 test
goto B983
@label B981
goto B1003
goto B983
@label B983
assignw T474 BASE[0]
assignw T475 BASE[12]
mult T476 4 T475
add T476 T476 4
assignw T477 BASE[0]
assignw T478 BASE[16]
mult T479 4 T478
add T479 T479 4
assignw f15 T474[T476]
param T480 0
assignw T480[0] f15
assignw f16 T477[T479]
param T481 4
assignw T481[0] f16
call T482 Function2 2
assignw f17 lastbase[0]
assignw T474[T476] f17
assignw f18 lastbase[4]
assignw T477[T479] f18
goto L20
@label B1003
assignw T483 BASE[0]
assignw T484 BASE[12]
mult T485 4 T484
add T485 T485 4
assignw T486 BASE[0]
assignw T487 BASE[8]
mult T488 4 T487
add T488 T488 4
assignw f19 T483[T485]
param T489 0
assignw T489[0] f19
assignw f20 T486[T488]
param T490 4
assignw T490[0] f20
call T491 Function2 2
assignw f21 lastbase[0]
assignw T483[T485] f21
assignw f22 lastbase[4]
assignw T486[T488] f22
assignw T493 BASE[0]
assignw T494 T493[0]
assignw T495 4
mult T495 T495 T494
add T495 T495 4
malloc T492 T495
memcpy T492 T493 T495
param T496 0
assignw T496[0] T492
assignw T497 BASE[4]
param T498 4
assignw T498[0] T497
assignw T499 BASE[16]
param T500 8
assignw T500[0] T499
call T501 Function3 3
assignw T502 1
assignw T504 BASE[12]
add T503 T504 T502
assignw T506 BASE[0]
assignw T507 T506[0]
assignw T508 4
mult T508 T508 T507
add T508 T508 4
malloc T505 T508
memcpy T505 T506 T508
param T509 0
assignw T509[0] T505
param T510 4
assignw T510[0] T503
assignw T511 BASE[8]
param T512 8
assignw T512[0] T511
call T513 Function3 3
@label Function3_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function4 3
assignb T514 BASE[0]
assignb BASE[2] T514
assignb T515 BASE[1]
assignb BASE[0] T515
assignb T516 BASE[2]
assignb BASE[1] T516
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 3
@function Function5 22
assignw T518 BASE[8]
assignw T519 BASE[4]
leq test T518 T519
goif B1077 test
goto B1080
@label B1077
assignw lastbase BASE
return 0
goto B1080
@label B1080
assignw T520 BASE[4]
assignw BASE[12] T520
assignw T521 1
assignw T523 BASE[8]
sub T522 T523 T521
assignw BASE[16] T522
assignw T524 BASE[0]
assignw T525 BASE[8]
mult T526 1 T525
add T526 T526 4
assignb T527 T524[T526]
assignb BASE[20] T527
@label L23
goto B1094
@label B1094
@label L24
assignw T528 BASE[0]
assignw T529 BASE[12]
mult T530 1 T529
add T530 T530 4
assignw T531 T528[T530]
assignw T532 BASE[20]
lt test T531 T532
goif B1104 test
goto B1109
@label B1104
assignw T533 1
assignw T535 BASE[12]
add T534 T535 T533
assignw BASE[12] T534
goto L24
@label B1109
@label L25
assignw T536 BASE[0]
assignw T537 BASE[16]
mult T538 1 T537
add T538 T538 4
assignw T539 T536[T538]
assignw T540 BASE[20]
gt test T539 T540
goif B1119 test
goto B1124
@label B1119
assignw T541 1
assignw T543 BASE[16]
sub T542 T543 T541
assignw BASE[16] T542
goto L25
@label B1124
assignw T544 BASE[12]
assignw T545 BASE[16]
geq test T544 T545
goif B1129 test
goto B1131
@label B1129
goto B1151
goto B1131
@label B1131
assignw T546 BASE[0]
assignw T547 BASE[12]
mult T548 1 T547
add T548 T548 4
assignw T549 BASE[0]
assignw T550 BASE[16]
mult T551 1 T550
add T551 T551 4
assignb T552 T546[T548]
param T553 0
assignb T553[0] T552
assignb T554 T549[T551]
param T555 1
assignb T555[0] T554
call T556 Function4 2
assignb T557 lastbase[0]
assignb T546[T548] T557
assignb T558 lastbase[1]
assignb T549[T551] T558
goto L23
@label B1151
assignw T559 BASE[0]
assignw T560 BASE[12]
mult T561 1 T560
add T561 T561 4
assignw T562 BASE[0]
assignw T563 BASE[8]
mult T564 1 T563
add T564 T564 4
assignb T565 T559[T561]
param T566 0
assignb T566[0] T565
assignb T567 T562[T564]
param T568 1
assignb T568[0] T567
call T569 Function4 2
assignb T570 lastbase[0]
assignb T559[T561] T570
assignb T571 lastbase[1]
assignb T562[T564] T571
assignw T573 BASE[0]
assignw T574 T573[0]
assignw T575 1
mult T575 T575 T574
add T575 T575 4
malloc T572 T575
memcpy T572 T573 T575
param T576 0
assignw T576[0] T572
assignw T577 BASE[4]
param T578 4
assignw T578[0] T577
assignw T579 BASE[16]
param T580 8
assignw T580[0] T579
call T581 Function5 3
assignw T582 1
assignw T584 BASE[12]
add T583 T584 T582
assignw T586 BASE[0]
assignw T587 T586[0]
assignw T588 1
mult T588 T588 T587
add T588 T588 4
malloc T585 T588
memcpy T585 T586 T588
param T589 0
assignw T589[0] T585
param T590 4
assignw T590[0] T583
assignw T591 BASE[8]
param T592 8
assignw T592[0] T591
call T593 Function5 3
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 22
