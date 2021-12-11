@string S0 "0000\n"
@string S1 "0000No esta definido el factorial para numeros negativos."
@string S2 "0000No esta definido el factorial para numeros negativos."
@string S3 "0000No se puede calcular el minimo de un arreglo vacio."
@string S4 "0000No se puede calcular el maximo de un arreglo vacio."
@string S5 "0000-"
@string S6 "0000."
@string S7 "0000Indique el numero entero no negativo: "
@string S8 "0000El metodo para calcular el factorial debe ser iterativo? [Y/n] "
@string S9 "0000%i! = %i"
@string S10 "0000Desea calcular otro factorial? [Y/n] "
@string S11 "0000Hasta luego!"
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
goto B117
@label B100
assignw S1[0] 53
param T22 0
assignw T22[0] S1
param T23 4
assignw T23[0] 0
param T24 8
assignw T24[0] 0
param T25 12
assignw T25[0] 0
param T26 16
assignw T26[0] 0
param T27 20
assignw T27[0] S0
call T28 PRINT 6
assignw T29 1
exit T29
goto Function0_end
@label B117
@label L6
assignw T30 0
assignw T31 BASE[0]
eq test T31 T30
goif B123 test
goto B127
@label B123
assignw T32 1
assignw lastbase BASE
return T32
goto Function0_end
@label B127
assignw T33 1
assignw T35 BASE[0]
sub T34 T35 T33
param T36 0
assignw T36[0] T34
call T37 Function0 1
assignw T39 BASE[0]
mult T38 T39 T37
assignw lastbase BASE
return T38
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function1 8
assignw T40 0
assignw T41 BASE[0]
lt test T41 T40
goif B147 test
goto B164
@label B147
assignw S2[0] 53
param T43 0
assignw T43[0] S2
param T44 4
assignw T44[0] 0
param T45 8
assignw T45[0] 0
param T46 12
assignw T46[0] 0
param T47 16
assignw T47[0] 0
param T48 20
assignw T48[0] S0
call T49 PRINT 6
assignw T50 1
exit T50
goto B164
@label B164
assignw T51 1
assignw BASE[4] T51
@label L7
assignw T52 0
assignw T53 BASE[0]
gt test T53 T52
goif B172 test
goto B181
@label B172
assignw T55 BASE[4]
assignw T56 BASE[0]
mult T54 T55 T56
assignw BASE[4] T54
assignw T57 1
assignw T59 BASE[0]
sub T58 T59 T57
assignw BASE[0] T58
goto L7
@label B181
assignw T60 BASE[4]
assignw lastbase BASE
return T60
@label Function1_end
assignw lastbase BASE
return 0
@endfunction 8
@function Function2 4
assignw T61 0
assignw f4 BASE[0]
lt test f4 T61
goif B194 test
goto B199
@label B194
assignw f6 BASE[0]
minus f5 f6
assignw lastbase BASE
return f5
goto Function2_end
@label B199
assignw f7 BASE[0]
assignw lastbase BASE
return f7
@label Function2_end
assignw lastbase BASE
return 0
@endfunction 4
assignw f8 0.000001
@function Function3 20
assignw f9 1.000000
assignw f10 BASE[0]
assignw BASE[8] f10
assignw BASE[12] f9
@label L8
assignw f11 BASE[12]
assignw f12 BASE[4]
gt test f11 f12
goif B218 test
goto B236
@label B218
assignw f13 BASE[8]
assignw BASE[16] f13
assignw f15 BASE[0]
assignw f16 BASE[8]
div f14 f15 f16
assignw f18 BASE[8]
add f17 f18 f14
assignw T62 2
div f19 f17 T62
assignw BASE[8] f19
assignw f21 BASE[8]
assignw f22 BASE[16]
sub f20 f21 f22
param T63 0
assignw T63[0] f20
call f23 Function2 1
assignw BASE[12] f23
goto L8
@label B236
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
assignw T65 0
assignw BASE[12] T65
@label L9
assignw T66 BASE[12]
assignw T67 BASE[4]
lt test T66 T67
goif B254 test
goto B263
@label B254
assignw T68 BASE[0]
assignw T69 BASE[12]
mult T70 4 T69
add T70 T70 4
assignw f27 BASE[8]
assignw f28 T68[T70]
add f26 f27 f28
assignw BASE[8] f26
goto L9
@label B263
assignw f30 BASE[8]
assignw T71 BASE[4]
div f29 f30 T71
assignw lastbase BASE
return f29
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function5 16
assignw T73 1
assignw T74 BASE[4]
lt test T74 T73
goif B278 test
goto B295
@label B278
assignw S3[0] 51
param T76 0
assignw T76[0] S3
param T77 4
assignw T77[0] 0
param T78 8
assignw T78[0] 0
param T79 12
assignw T79[0] 0
param T80 16
assignw T80[0] 0
param T81 20
assignw T81[0] S0
call T82 PRINT 6
assignw T83 1
exit T83
goto B295
@label B295
assignw T84 0
assignw T85 BASE[0]
mult T86 4 T84
add T86 T86 4
assignw f31 T85[T86]
assignw BASE[8] f31
assignw T87 1
assignw BASE[12] T87
@label L10
assignw T88 BASE[12]
assignw T89 BASE[4]
lt test T88 T89
goif B309 test
goto B326
@label B309
assignw T90 BASE[0]
assignw T91 BASE[12]
mult T92 4 T91
add T92 T92 4
assignw f32 T90[T92]
assignw f33 BASE[8]
lt test f32 f33
goif B318 test
goto L10
@label B318
assignw T93 BASE[0]
assignw T94 BASE[12]
mult T95 4 T94
add T95 T95 4
assignw f34 T93[T95]
assignw BASE[8] f34
goto L10
goto L10
@label B326
assignw f35 BASE[8]
assignw lastbase BASE
return f35
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function6 16
assignw T97 1
assignw T98 BASE[4]
lt test T98 T97
goif B339 test
goto B356
@label B339
assignw S4[0] 51
param T100 0
assignw T100[0] S4
param T101 4
assignw T101[0] 0
param T102 8
assignw T102[0] 0
param T103 12
assignw T103[0] 0
param T104 16
assignw T104[0] 0
param T105 20
assignw T105[0] S0
call T106 PRINT 6
assignw T107 1
exit T107
goto B356
@label B356
assignw T108 0
assignw T109 BASE[0]
mult T110 4 T108
add T110 T110 4
assignw f36 T109[T110]
assignw BASE[8] f36
assignw T111 1
assignw BASE[12] T111
@label L11
assignw T112 BASE[12]
assignw T113 BASE[4]
lt test T112 T113
goif B370 test
goto B387
@label B370
assignw T114 BASE[0]
assignw T115 BASE[12]
mult T116 4 T115
add T116 T116 4
assignw f37 T114[T116]
assignw f38 BASE[8]
gt test f37 f38
goif B379 test
goto L11
@label B379
assignw T117 BASE[0]
assignw T118 BASE[12]
mult T119 4 T118
add T119 T119 4
assignw f39 T117[T119]
assignw BASE[8] f39
goto L11
goto L11
@label B387
assignw f40 BASE[8]
assignw lastbase BASE
return f40
@label Function6_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function7 20
@label L12
assignw T121 0
assignw T122 BASE[4]
eq test T122 T121
goif B401 test
goto B405
@label B401
assignw f41 0.000000
assignw lastbase BASE
return f41
goto B405
@label B405
assignw T124 BASE[0]
assignw T125 T124[0]
assignw T126 4
mult T126 T126 T125
add T126 T126 4
malloc T123 T126
memcpy T123 T124 T126
param T127 0
assignw T127[0] T123
assignw T128 BASE[4]
param T129 4
assignw T129[0] T128
call f42 Function4 2
assignw f43 0.000000
assignw BASE[8] f42
assignw BASE[12] f43
assignw T130 0
assignw BASE[16] T130
@label L13
assignw T131 BASE[16]
assignw T132 BASE[4]
lt test T131 T132
goif B429 test
goto B448
@label B429
assignw T133 BASE[0]
assignw T134 BASE[16]
mult T135 4 T134
add T135 T135 4
assignw f45 T133[T135]
assignw f46 BASE[8]
sub f44 f45 f46
assignw T136 BASE[0]
assignw T137 BASE[16]
mult T138 4 T137
add T138 T138 4
assignw f48 T136[T138]
assignw f49 BASE[8]
sub f47 f48 f49
mult f50 f44 f47
assignw f52 BASE[12]
add f51 f52 f50
assignw BASE[12] f51
goto L13
@label B448
assignw f54 BASE[12]
assignw T139 BASE[4]
div f53 f54 T139
assignw lastbase BASE
return f53
@label Function7_end
assignw lastbase BASE
return 0
@endfunction 20
@function Function8 8
assignw T142 BASE[0]
assignw T143 T142[0]
assignw T144 4
mult T144 T144 T143
add T144 T144 4
malloc T141 T144
memcpy T141 T142 T144
param T145 0
assignw T145[0] T141
assignw T146 BASE[4]
param T147 4
assignw T147[0] T146
call f55 Function7 2
param T148 0
assignw T148[0] f55
param T149 4
assignw T149[0] f8
call f56 Function3 2
assignw lastbase BASE
return f56
@label Function8_end
assignw lastbase BASE
return 0
@endfunction 8
assignb T151 0
assignw T152 1
assignw T154 T152
assignw T155 1
mult T155 T155 T154
add T155 T155 4
malloc T153 T155
assignw T153[0] T154
assignb T153[4] T151
assignw T156 T153
assignb T158 10
assignw T159 1
assignw T161 T159
assignw T162 1
mult T162 T162 T161
add T162 T162 4
malloc T160 T162
assignw T160[0] T161
assignb T160[4] T158
assignw T163 T160
assignb T165 0
@function Function9 12
assignw T166 0
assignw BASE[8] T166
@label L14
assignw T167 BASE[0]
assignw T168 BASE[8]
mult T169 1 T168
add T169 T169 4
@label L15
assignb T170 T167[T169]
assignb T171 BASE[4]
neq test T170 T171
goif B517 test
goto B522
@label B517
assignw T172 1
assignw T174 BASE[8]
add T173 T174 T172
assignw BASE[8] T173
goto L14
@label B522
assignw T175 BASE[8]
assignw lastbase BASE
return T175
@label Function9_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function10 12
assignw T178 0
assignw BASE[8] T178
@label L16
assignw T179 BASE[0]
assignw T180 BASE[8]
mult T181 1 T180
add T181 T181 4
@label L17
assignb T182 0
assignb T183 T179[T181]
neq test T183 T182
goif B543 test
goto B562
@label B543
assignw T184 BASE[0]
assignw T185 BASE[8]
mult T186 1 T185
add T186 T186 4
@label L18
assignw T187 BASE[4]
assignw T188 BASE[8]
mult T189 1 T188
add T189 T189 4
assignb T190 T184[T186]
assignb T191 T187[T189]
eq test T190 T191
goif B557 test
goto B562
@label B557
assignw T192 1
assignw T194 BASE[8]
add T193 T194 T192
assignw BASE[8] T193
goto L16
@label B562
assignw T195 BASE[0]
assignw T196 BASE[8]
mult T197 1 T196
add T197 T197 4
assignw T198 BASE[4]
assignw T199 BASE[8]
mult T200 1 T199
add T200 T200 4
assignw T201 T195[T197]
assignw T202 T198[T200]
gt test T201 T202
goif B575 test
goto B579
@label B575
assignw T203 1
assignw lastbase BASE
return T203
goto Function10_end
@label B579
assignw T204 BASE[4]
assignw T205 BASE[8]
mult T206 1 T205
add T206 T206 4
assignw T207 BASE[0]
assignw T208 BASE[8]
mult T209 1 T208
add T209 T209 4
assignw T210 T204[T206]
assignw T211 T207[T209]
gt test T210 T211
goif B592 test
goto B597
@label B592
assignw T212 1
minus T213 T212
assignw lastbase BASE
return T213
goto Function10_end
@label B597
assignw T214 0
assignw lastbase BASE
return T214
@label Function10_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function11 16
assignw T218 BASE[4]
assignw T219 T218[0]
assignw T220 1
mult T220 T220 T219
add T220 T220 4
malloc T217 T220
memcpy T217 T218 T220
param T221 0
assignw T221[0] T217
param T222 4
assignb T222[0] T165
call T223 Function9 2
assignw T224 1
add T225 T223 T224
assignw BASE[8] T225
assignw T226 0
assignw BASE[12] T226
@label L19
assignw T227 BASE[12]
assignw T228 BASE[8]
lt test T227 T228
goif B628 test
goto Function11_end
@label B628
assignw T229 BASE[0]
assignw T230 BASE[12]
mult T231 1 T230
add T231 T231 4
assignw T232 BASE[4]
assignw T233 BASE[12]
mult T234 1 T233
add T234 T234 4
assignb T235 T232[T234]
assignb T229[T231] T235
assignw T236 1
assignw T238 BASE[12]
add T237 T238 T236
assignw BASE[12] T237
goto L19
@label Function11_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function12 16
assignw T242 BASE[4]
assignw T243 T242[0]
assignw T244 1
mult T244 T244 T243
add T244 T244 4
malloc T241 T244
memcpy T241 T242 T244
param T245 0
assignw T245[0] T241
param T246 4
assignb T246[0] T165
call T247 Function9 2
assignw BASE[8] T247
assignw T248 0
assignw T250 T248
@label L20
assignw T251 BASE[8]
geq test T250 T251
goif L20_end test
assignw T249 T250
assignw T253 BASE[8]
assignw T254 BASE[12]
sub T252 T253 T254
assignw T255 1
sub T256 T252 T255
assignw T257 BASE[0]
mult T258 1 T256
add T258 T258 4
assignw T259 BASE[4]
assignw T260 BASE[12]
mult T261 1 T260
add T261 T261 4
assignb T262 T259[T261]
assignb T257[T258] T262
add T250 T250 1
goto L20
@label L20_end
@label Function12_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function13 28
assignw T266 0
assignw T267 0
assignw BASE[12] T266
assignw BASE[16] T267
@label L21
assignw T268 BASE[12]
assignw T269 BASE[4]
lt test T268 T269
goif B700 test
goto B753
@label B700
assignw T270 BASE[0]
assignw T271 BASE[12]
mult T272 4 T271
add T272 T272 4
assignw T274 T270[T272]
assignw T275 T274[0]
assignw T276 1
mult T276 T276 T275
add T276 T276 4
malloc T273 T276
memcpy T273 T274 T276
param T277 0
assignw T277[0] T273
param T278 4
assignb T278[0] T165
call T279 Function9 2
assignw BASE[24] T279
assignw T280 0
assignw BASE[20] T280
@label L22
assignw T281 BASE[20]
assignw T282 BASE[24]
lt test T281 T282
goif B725 test
goto B748
@label B725
assignw T283 BASE[8]
assignw T284 BASE[16]
mult T285 1 T284
add T285 T285 4
assignw T286 BASE[0]
assignw T287 BASE[12]
mult T288 4 T287
add T288 T288 4
assignw T289 T286[T288]
assignw T290 BASE[20]
mult T291 1 T290
add T291 T291 4
assignb T292 T289[T291]
assignb T283[T285] T292
assignw T293 1
assignw T295 BASE[20]
add T294 T295 T293
assignw BASE[20] T294
assignw T296 1
assignw T298 BASE[16]
add T297 T298 T296
assignw BASE[16] T297
goto L22
@label B748
assignw T299 1
assignw T301 BASE[12]
add T300 T301 T299
assignw BASE[12] T300
goto L21
@label B753
assignw T302 BASE[8]
assignw T303 BASE[16]
mult T304 1 T303
add T304 T304 4
assignb T305 0
assignb T302[T304] T305
@label Function13_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function14 29
assignw T309 0
assignw T310 0
assignw T311 0
assignw T313 BASE[0]
assignw T314 T313[0]
assignw T315 1
mult T315 T315 T314
add T315 T315 4
malloc T312 T315
memcpy T312 T313 T315
param T316 0
assignw T316[0] T312
param T317 4
assignb T317[0] T165
call T318 Function9 2
assignw BASE[12] T309
assignw BASE[16] T310
assignw BASE[20] T311
assignw BASE[24] T318
goto B784
@label B784
assignb BASE[28] True
goto Bool787
assignb BASE[28] False
@label Bool787
@label L23
assignw T319 BASE[0]
assignw T320 BASE[12]
mult T321 1 T320
add T321 T321 4
@label L24
assignb T322 0
assignb T323 T319[T321]
neq test T323 T322
goif B799 test
goto B879
@label B799
assignw T324 BASE[0]
assignw T325 BASE[12]
mult T326 1 T325
add T326 T326 4
@label L25
assignb T327 T324[T326]
assignb T328 BASE[8]
eq test T327 T328
goif B809 test
goto B837
@label B809
assignb T329 BASE[28]
goif B837 T329
goto B812
@label B812
assignb T330 BASE[28]


goto B816
@label B816
assignb BASE[28] True
goto Bool819
assignb BASE[28] False
@label Bool819
assignw T331 BASE[4]
assignw T332 BASE[20]
mult T333 4 T332
add T333 T333 4
assignw T334 T331[T333]
assignw T335 BASE[16]
mult T336 1 T335
add T336 T336 4
assignb T337 0
assignb T334[T336] T337
assignw T338 1
assignw T340 BASE[20]
add T339 T340 T338
assignw BASE[20] T339
assignw T341 0
assignw BASE[16] T341
goto B874
@label B837
assignw T342 BASE[0]
assignw T343 BASE[12]
mult T344 1 T343
add T344 T344 4
@label L26
assignb T345 T342[T344]
assignb T346 BASE[8]
neq test T345 T346
goif B847 test
goto B874
@label B847
assignb T347 BASE[28]


goto B853
assignb BASE[28] True
goto Bool854
@label B853
assignb BASE[28] False
@label Bool854
assignw T348 BASE[4]
assignw T349 BASE[20]
mult T350 4 T349
add T350 T350 4
assignw T351 T348[T350]
assignw T352 BASE[16]
mult T353 1 T352
add T353 T353 4
assignw T354 BASE[0]
assignw T355 BASE[12]
mult T356 1 T355
add T356 T356 4
assignb T357 T354[T356]
assignb T351[T353] T357
assignw T358 1
assignw T360 BASE[16]
add T359 T360 T358
assignw BASE[16] T359
goto B874
@label B874
assignw T361 1
assignw T363 BASE[12]
add T362 T363 T361
assignw BASE[12] T362
goto L23
@label B879
assignb T364 BASE[28]
goif B897 T364
goto B882
@label B882
assignw T365 BASE[4]
assignw T366 BASE[20]
mult T367 4 T366
add T367 T367 4
assignw T368 T365[T367]
assignw T369 BASE[16]
mult T370 1 T369
add T370 T370 4
assignb T371 0
assignb T368[T370] T371
assignw T372 1
assignw T374 BASE[20]
add T373 T374 T372
assignw BASE[20] T373
goto B897
@label B897
assignw T375 BASE[20]
assignw lastbase BASE
return T375
@label Function14_end
assignw lastbase BASE
return 0
@endfunction 29
@function Function15 16
goto B909
goto B913
assignb BASE[4] True
goto Bool910
@label B909
assignb BASE[4] False
@label Bool910
assignb BASE[5] True
goto Bool914
@label B913
assignb BASE[5] False
@label Bool914
assignw T378 BASE[0]
assignw T379 T378[0]
assignw T380 1
mult T380 T380 T379
add T380 T380 4
malloc T377 T380
memcpy T377 T378 T380
param T381 0
assignw T381[0] T377
param T382 4
assignb T382[0] T165
call T383 Function9 2
assignw T384 0
assignw BASE[8] T383
assignw BASE[12] T384
@label L27
assignw T385 BASE[12]
assignw T386 BASE[8]
lt test T385 T386
goif B936 test
goto B1022
@label B936
assignw T387 BASE[0]
assignw T388 BASE[12]
mult T389 1 T388
add T389 T389 4
@label L28
assignb T390 46
assignb T391 T387[T389]
eq test T391 T390
goif B946 test
goto B958
@label B946
assignb T392 BASE[4]
goif B958 T392
goto B949
@label B949
assignb T393 BASE[4]


goto B953
@label B953
assignb BASE[4] True
goto Bool956
assignb BASE[4] False
@label Bool956
goto B1017
@label B958
assignw T394 BASE[0]
assignw T395 BASE[12]
mult T396 1 T395
add T396 T396 4
@label L29
assignb T397 46
assignb T398 T394[T396]
eq test T398 T397
goif B968 test
goto B976
@label B968
goto B971
assignb T399 True
goto Bool972
@label B971
assignb T399 False
@label Bool972
assignw lastbase BASE
return T399
goto B1017
@label B976
assignw T400 BASE[0]
assignw T401 BASE[12]
mult T402 1 T401
add T402 T402 4
assignb T403 48
assignw T404 T400[T402]
lt test T404 T403
goif B994 test
goto B985
@label B985
assignw T405 BASE[0]
assignw T406 BASE[12]
mult T407 1 T406
add T407 T407 4
assignb T408 57
assignw T409 T405[T407]
gt test T409 T408
goif B994 test
goto B1002
@label B994
goto B997
assignb T410 True
goto Bool998
@label B997
assignb T410 False
@label Bool998
assignw lastbase BASE
return T410
goto B1017
@label B1002
assignb T411 BASE[4]
goif B1005 T411
goto B1017
@label B1005
assignb T412 BASE[5]
goif B1017 T412
goto B1008
@label B1008
assignb T413 BASE[5]


goto B1012
@label B1012
assignb BASE[5] True
goto Bool1015
assignb BASE[5] False
@label Bool1015
goto B1017
@label B1017
assignw T414 1
assignw T416 BASE[12]
add T415 T416 T414
assignw BASE[12] T415
goto L27
@label B1022
assignb T417 BASE[4]
goif B1025 T417
goto B1030
@label B1025
assignb T418 BASE[5]
goif B1028 T418
goto B1030
@label B1028
assignb T419 True
goto Bool1031
@label B1030
assignb T419 False
@label Bool1031
assignw lastbase BASE
return T419
@label Function15_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function16 24
assignw T422 BASE[0]
assignw T423 T422[0]
assignw T424 1
mult T424 T424 T423
add T424 T424 4
malloc T421 T424
memcpy T421 T422 T424
param T425 0
assignw T425[0] T421
param T426 4
assignb T426[0] T165
call T427 Function9 2
assignw BASE[8] T427
assignw T428 0
assignw BASE[4] T428
@label L30
assignw T429 0
assignw T430 BASE[8]
eq test T430 T429
goif B1076 test
goto B1060
@label B1060
assignw T431 0
assignw T432 BASE[0]
mult T433 1 T431
add T433 T433 4
@label L31
assignb T434 45
assignb T435 T432[T433]
eq test T435 T434
goif B1070 test
goto B1084
@label B1070
@label L32
assignw T436 1
assignw T437 BASE[8]
eq test T437 T436
goif B1076 test
goto B1084
@label B1076
goto B1079
assignb T438 True
goto Bool1080
@label B1079
assignb T438 False
@label Bool1080
assignw lastbase BASE
return T438
goto B1104
@label B1084
assignw T439 0
assignw T440 BASE[0]
mult T441 1 T439
add T441 T441 4
@label L33
assignb T442 45
assignb T443 T440[T441]
eq test T443 T442
goif B1094 test
goto B1100
@label B1094
assignw T444 1
minus T445 T444
assignw BASE[16] T445
assignw T446 1
assignw BASE[12] T446
goto B1104
@label B1100
assignw T447 1
assignw BASE[16] T447
assignw T448 0
assignw BASE[12] T448
@label B1104
assignw T449 1
assignw T451 BASE[8]
sub T450 T451 T449
assignw T452 1
assignw T454 BASE[12]
sub T453 T454 T452
assignw T455 1
minus T456 T455
assignw T458 T450
@label L34
lt test T456 0
goif L34_neg test
geq test T458 T453
goif L34_end test
goto L34_body
@label L34_neg
leq test T458 T453
goif L34_end test
@label L34_body
assignw T457 T458
assignw T459 BASE[0]
assignw T460 BASE[20]
mult T461 1 T460
add T461 T461 4
assignb T462 48
assignw T463 T459[T461]
lt test T463 T462
goif B1142 test
goto B1133
@label B1133
assignw T464 BASE[0]
assignw T465 BASE[20]
mult T466 1 T465
add T466 T466 4
assignb T467 57
assignw T468 T464[T466]
gt test T468 T467
goif B1142 test
goto B1152
@label B1142
assignw T469 0
assignw BASE[4] T469
goto B1147
assignb T470 True
goto Bool1148
@label B1147
assignb T470 False
@label Bool1148
assignw lastbase BASE
return T470
goto B1152
@label B1152
assignw T471 BASE[0]
assignw T472 BASE[20]
mult T473 1 T472
add T473 T473 4
assignb T474 T471[T473]
param T475 0
assignb T475[0] T474
call T476 CTOI 1
assignb T477 48
param T478 0
assignb T478[0] T477
call T479 CTOI 1
sub T480 T476 T479
assignw T482 BASE[16]
mult T481 T482 T480
assignw T484 BASE[4]
add T483 T484 T481
assignw BASE[4] T483
assignw T485 10
assignw T487 BASE[16]
mult T486 T487 T485
assignw BASE[16] T486
add T458 T458 T456
goto L34
@label L34_end
goto B1178
@label B1178
assignb T488 True
goto Bool1181
assignb T488 False
@label Bool1181
assignw lastbase BASE
return T488
@label Function16_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function17 36
assignw T491 BASE[0]
assignw T492 T491[0]
assignw T493 1
mult T493 T493 T492
add T493 T493 4
malloc T490 T493
memcpy T490 T491 T493
param T494 0
assignw T494[0] T490
param T495 4
assignb T495[0] T165
call T496 Function9 2
assignw BASE[8] T496
assignw T497 BASE[8]
assignw T498 BASE[12]
assignw T499 1
mult T499 T499 T497
add T499 T499 4
malloc T498 T499
assignw T498[0] T497
assignw T498[0] T498
assignw T500 BASE[8]
assignw T501 BASE[16]
assignw T502 1
mult T502 T502 T500
add T502 T502 4
malloc T501 T502
assignw T501[0] T500
assignw T501[0] T501
assignw T503 0
assignw BASE[32] T503
@label L35
assignw T504 BASE[0]
assignw T505 BASE[32]
mult T506 1 T505
add T506 T506 4
@label L36
assignb T507 46
assignb T508 T504[T506]
neq test T508 T507
goif B1231 test
goto B1256
@label B1231
assignw T509 BASE[0]
assignw T510 BASE[32]
mult T511 1 T510
add T511 T511 4
@label L37
assignb T512 0
assignb T513 T509[T511]
neq test T513 T512
goif B1241 test
goto B1256
@label B1241
assignw T514 BASE[12]
assignw T515 BASE[32]
mult T516 1 T515
add T516 T516 4
assignw T517 BASE[0]
assignw T518 BASE[32]
mult T519 1 T518
add T519 T519 4
assignb T520 T517[T519]
assignb T514[T516] T520
assignw T521 1
assignw T523 BASE[32]
add T522 T523 T521
assignw BASE[32] T522
goto L35
@label B1256
@label L38
assignw T524 0
assignw T525 BASE[32]
eq test T525 T524
goif B1262 test
goto B1265
@label B1262
assignw T526 0
assignw BASE[24] T526
goto B1290
@label B1265
assignw T528 BASE[12]
assignw T529 T528[0]
assignw T530 1
mult T530 T530 T529
add T530 T530 4
malloc T527 T530
memcpy T527 T528 T530
param T531 0
assignw T531[0] T527
assignw T532 BASE[24]
param T533 4
assignw T533[0] T532
call T534 Function16 2
assignw T535 lastbase[4]
assignw BASE[24] T535
goif B1290 T534
goto B1282
@label B1282
goto B1285
assignb T536 True
goto Bool1286
@label B1285
assignb T536 False
@label Bool1286
assignw lastbase BASE
return T536
goto B1290
@label B1290
assignw T537 BASE[0]
assignw T538 BASE[32]
mult T539 1 T538
add T539 T539 4
@label L39
assignb T540 0
assignb T541 T537[T539]
eq test T541 T540
goif B1300 test
goto B1313
@label B1300
assignw T542 BASE[24]
param T543 0
assignw T543[0] T542
call f57 ITOF 1
assignw BASE[4] f57
goto B1306
@label B1306
assignb T544 True
goto Bool1309
assignb T544 False
@label Bool1309
assignw lastbase BASE
return T544
goto B1313
@label B1313
assignw T545 1
assignw T547 BASE[32]
add T546 T547 T545
assignw BASE[32] T546
assignw T548 0
assignw BASE[20] T548
@label L40
assignw T549 BASE[0]
assignw T550 BASE[32]
mult T551 1 T550
add T551 T551 4
@label L41
assignb T552 0
assignb T553 T549[T551]
neq test T553 T552
goif B1330 test
goto B1349
@label B1330
assignw T554 BASE[16]
assignw T555 BASE[20]
mult T556 1 T555
add T556 T556 4
assignw T557 BASE[0]
assignw T558 BASE[32]
mult T559 1 T558
add T559 T559 4
assignb T560 T557[T559]
assignb T554[T556] T560
assignw T561 1
assignw T563 BASE[32]
add T562 T563 T561
assignw BASE[32] T562
assignw T564 1
assignw T566 BASE[20]
add T565 T566 T564
assignw BASE[20] T565
goto L40
@label B1349
@label L42
assignw T567 0
assignw T568 BASE[20]
eq test T568 T567
goif B1355 test
goto B1368
@label B1355
assignw T569 BASE[24]
param T570 0
assignw T570[0] T569
call f58 ITOF 1
assignw BASE[4] f58
goto B1361
@label B1361
assignb T571 True
goto Bool1364
assignb T571 False
@label Bool1364
assignw lastbase BASE
return T571
goto B1393
@label B1368
assignw T573 BASE[16]
assignw T574 T573[0]
assignw T575 1
mult T575 T575 T574
add T575 T575 4
malloc T572 T575
memcpy T572 T573 T575
param T576 0
assignw T576[0] T572
assignw T577 BASE[28]
param T578 4
assignw T578[0] T577
call T579 Function16 2
assignw T580 lastbase[4]
assignw BASE[28] T580
goif B1393 T579
goto B1385
@label B1385
goto B1388
assignb T581 True
goto Bool1389
@label B1388
assignb T581 False
@label Bool1389
assignw lastbase BASE
return T581
goto B1393
@label B1393
assignw T582 BASE[24]
param T583 0
assignw T583[0] T582
call f59 ITOF 1
assignw T584 BASE[28]
param T585 0
assignw T585[0] T584
call f60 ITOF 1
assignw T586 10
assignw T588 T586
assignw T589 BASE[20]
assignw T587 1
lt test T589 0
goif L43_neg test
@label L43_pos
eq test T589 0
goif L43_end test
mult T587 T587 T588
sub T589 T589 1
goto L43_pos
@label L43_neg
div T587 T587 T588
add T589 T589 1
neq test T589 0
goif L43_neg test
@label L43_end
div f61 f60 T587
add f62 f59 f61
assignw BASE[4] f62
goto B1423
@label B1423
assignb T590 True
goto Bool1426
assignb T590 False
@label Bool1426
assignw lastbase BASE
return T590
@label Function17_end
assignw lastbase BASE
return 0
@endfunction 36
@function Function18 32
@label L44
assignw T592 0
assignw T593 BASE[4]
eq test T593 T592
goif B1440 test
goto B1453
@label B1440
assignw T594 0
assignw T595 BASE[0]
mult T596 1 T594
add T596 T596 4
assignb T597 48
assignb T595[T596] T597
assignw T598 1
assignw T599 BASE[0]
mult T600 1 T598
add T600 T600 4
assignb T601 0
assignb T599[T600] T601
goto B1453
@label B1453
assignw T602 0
assignw BASE[16] T602
assignw T604 BASE[0]
assignw T605 T604[0]
assignw T606 1
mult T606 T606 T605
add T606 T606 4
malloc T603 T606
memcpy T603 T604 T606
param T607 0
assignw T607[0] T603
param T608 4
assignb T608[0] T165
call T609 Function9 2
assignw T610 T609
assignw T611 BASE[20]
assignw T612 1
mult T612 T612 T610
add T612 T612 4
malloc T611 T612
assignw T611[0] T610
assignw T611[0] T611
assignw T613 T609
assignw T614 BASE[24]
assignw T615 1
mult T615 T615 T613
add T615 T615 4
malloc T614 T615
assignw T614[0] T613
assignw T614[0] T614
assignw T616 0
assignw T617 BASE[4]
lt test T617 T616
goif B1488 test
goto B1492
@label B1488
assignw T619 BASE[4]
minus T618 T619
assignw BASE[8] T618
goto B1494
@label B1492
assignw T620 BASE[4]
assignw BASE[8] T620
@label B1494
@label L45
assignw T621 0
assignw T622 BASE[8]
gt test T622 T621
goif B1500 test
goto B1521
@label B1500
assignw T623 BASE[20]
assignw T624 BASE[16]
mult T625 1 T624
add T625 T625 4
assignw T626 10
assignw T628 BASE[8]
mod T627 T628 T626
assignb T629 48
param T630 0
assignb T630[0] T629
call T631 CTOI 1
add T632 T627 T631
param T633 0
assignw T633[0] T632
call T634 ITOC 1
assignb T623[T625] T634
assignw T635 10
assignw T637 BASE[8]
div T636 T637 T635
assignw BASE[8] T636
goto L45
@label B1521
assignw T638 BASE[24]
param T639 0
assignw T639[0] T638
assignw T641 BASE[20]
assignw T642 T641[0]
assignw T643 1
mult T643 T643 T642
add T643 T643 4
malloc T640 T643
memcpy T640 T641 T643
param T644 4
assignw T644[0] T640
call T645 Function12 2
assignw T646 0
assignw T647 BASE[4]
lt test T647 T646
goif B1539 test
goto B1599
@label B1539
assignw S5[0] 1
assignw T649 2
assignw T650 T649
assignw T651 BASE[28]
assignw T652 4
mult T652 T652 T650
add T652 T652 4
malloc T651 T652
assignw T651[0] T650
assignw T651[0] T651
@label L46
sub T652 T652 4
lt test T652 0
goif L46_end test
assignw T653 T609
assignw T654 T651[T652]
assignw T655 1
mult T655 T655 T653
add T655 T655 4
malloc T654 T655
assignw T654[0] T653
assignw T654[0] T654
goto L46
@label L46_end
assignw T656 BASE[28]
assignw T657 BASE[24]
assignw T656[8] T657
assignw T656[4] S5
assignw T658 2
assignw T660 BASE[28]
assignw T661 T660[0]
assignw T662 4
mult T662 T662 T661
add T662 T662 4
malloc T659 T662
assignw T663 T662
@label L47
sub T663 T663 4
lt test T663 0
goif L47_end test
assignw T664 T660[T663]
assignw T665 T659[T663]
assignw T666 T664[0]
assignw T667 1
mult T667 T667 T666
add T667 T667 4
malloc T665 T667
assignw T665[0] T665
memcpy T665 T664 T667
goto L47
@label L47_end
param T668 0
assignw T668[0] T659
param T669 4
assignw T669[0] T658
assignw T670 BASE[0]
param T671 8
assignw T671[0] T670
call T672 Function13 3
goto Function18_end
@label B1599
assignw T673 BASE[0]
param T674 0
assignw T674[0] T673
assignw T676 BASE[24]
assignw T677 T676[0]
assignw T678 1
mult T678 T678 T677
add T678 T678 4
malloc T675 T678
memcpy T675 T676 T678
param T679 4
assignw T679[0] T675
call T680 Function11 2
@label Function18_end
assignw lastbase BASE
return 0
@endfunction 32
@function Function19 32
assignw T683 BASE[0]
assignw T684 T683[0]
assignw T685 1
mult T685 T685 T684
add T685 T685 4
malloc T682 T685
memcpy T682 T683 T685
param T686 0
assignw T686[0] T682
param T687 4
assignb T687[0] T165
call T688 Function9 2
assignw T689 T688
assignw T690 BASE[20]
assignw T691 1
mult T691 T691 T689
add T691 T691 4
malloc T690 T691
assignw T690[0] T689
assignw T690[0] T690
assignw T692 T688
assignw T693 BASE[24]
assignw T694 1
mult T694 T694 T692
add T694 T694 4
malloc T693 T694
assignw T693[0] T692
assignw T693[0] T693
assignw f63 BASE[4]
param T695 0
assignw T695[0] f63
call T696 FTOI 1
assignw BASE[8] T696
assignw f65 BASE[4]
assignw T697 BASE[8]
sub f64 f65 T697
assignw BASE[16] f64
@label L48
@label L49
assignw f66 BASE[16]
param T698 0
assignw T698[0] f66
call T699 FTOI 1
assignw T700 BASE[16]
neq test T700 T699
goif B1664 test
goto B1669
@label B1664
assignw T701 10
assignw f68 BASE[16]
mult f67 f68 T701
assignw BASE[16] f67
goto L48
@label B1669
assignw f69 BASE[16]
param T702 0
assignw T702[0] f69
call T703 FTOI 1
assignw BASE[12] T703
assignw T704 BASE[20]
param T705 0
assignw T705[0] T704
assignw T706 BASE[8]
param T707 4
assignw T707[0] T706
call T708 Function18 2
assignw T709 BASE[24]
param T710 0
assignw T710[0] T709
assignw T711 BASE[12]
param T712 4
assignw T712[0] T711
call T713 Function18 2
assignw S6[0] 1
assignw T715 3
assignw T716 T715
assignw T717 BASE[28]
assignw T718 4
mult T718 T718 T716
add T718 T718 4
malloc T717 T718
assignw T717[0] T716
assignw T717[0] T717
@label L50
sub T718 T718 4
lt test T718 0
goif L50_end test
assignw T719 T688
assignw T720 T717[T718]
assignw T721 1
mult T721 T721 T719
add T721 T721 4
malloc T720 T721
assignw T720[0] T719
assignw T720[0] T720
goto L50
@label L50_end
assignw T722 BASE[28]
assignw T723 BASE[24]
assignw T722[12] T723
assignw T722[8] S6
assignw T724 BASE[20]
assignw T722[4] T724
assignw T725 3
assignw T727 BASE[28]
assignw T728 T727[0]
assignw T729 4
mult T729 T729 T728
add T729 T729 4
malloc T726 T729
assignw T730 T729
@label L51
sub T730 T730 4
lt test T730 0
goif L51_end test
assignw T731 T727[T730]
assignw T732 T726[T730]
assignw T733 T731[0]
assignw T734 1
mult T734 T734 T733
add T734 T734 4
malloc T732 T734
assignw T732[0] T732
memcpy T732 T731 T734
goto L51
@label L51_end
param T735 0
assignw T735[0] T726
param T736 4
assignw T736[0] T725
assignw T737 BASE[0]
param T738 8
assignw T738[0] T737
call T739 Function13 3
@label Function19_end
assignw lastbase BASE
return 0
@endfunction 32
@label L52
goto B1755
@label B1755
assignw S7[0] 38
param T745 0
assignw T745[0] S7
param T746 4
assignw T746[0] 0
param T747 8
assignw T747[0] 0
param T748 12
assignw T748[0] 0
param T749 16
assignw T749[0] 0
param T750 20
assignw T750[0] S0
call T751 PRINT 6
call T752 READI 0
assignw T740 T752
assignw S8[0] 63
param T754 0
assignw T754[0] S8
param T755 4
assignw T755[0] 0
param T756 8
assignw T756[0] 0
param T757 12
assignw T757[0] 0
param T758 16
assignw T758[0] 0
param T759 20
assignw T759[0] S0
call T760 PRINT 6
call T761 READC 0
assignb T743 T761
@label L53
assignb T762 110
eq test T743 T762
goif B1797 test
goto B1792
@label B1792
@label L54
assignb T763 78
eq test T743 T763
goif B1797 test
goto B1802
@label B1797
param T764 0
assignw T764[0] T740
call T765 Function0 1
assignw T741 T765
goto B1806
@label B1802
param T766 0
assignw T766[0] T740
call T767 Function1 1
assignw T741 T767
@label B1806
assignw S9[0] 8
assignw T769 2
assignw T771 T769
assignw T772 4
mult T772 T772 T771
add T772 T772 4
malloc T770 T772
assignw T770[0] T771
assignw T770[8] T741
assignw T770[4] T740
param T773 0
assignw T773[0] S9
param T774 4
assignw T774[0] 0
assignw T776 T770[0]
assignw T777 4
mult T777 T777 T776
add T777 T777 4
malloc T775 T777
memcpy T775 T770 T777
param T778 8
assignw T778[0] T775
param T779 12
assignw T779[0] 0
param T780 16
assignw T780[0] 0
param T781 20
assignw T781[0] S0
call T782 PRINT 6
assignw S10[0] 37
param T784 0
assignw T784[0] S10
param T785 4
assignw T785[0] 0
param T786 8
assignw T786[0] 0
param T787 12
assignw T787[0] 0
param T788 16
assignw T788[0] 0
param T789 20
assignw T789[0] S0
call T790 PRINT 6
call T791 READC 0
assignb T743 T791
@label L55
assignb T792 110
eq test T743 T792
goif B1861 test
goto B1856
@label B1856
@label L56
assignb T793 78
eq test T743 T793
goif B1861 test
goto L52
@label B1861
assignw S11[0] 12
param T795 0
assignw T795[0] S11
param T796 4
assignw T796[0] 0
param T797 8
assignw T797[0] 0
param T798 12
assignw T798[0] 0
param T799 16
assignw T799[0] 0
param T800 20
assignw T800[0] S0
call T801 PRINT 6
goto B1878
goto L52
goto L52
@label B1878
