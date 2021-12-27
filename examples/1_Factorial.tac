@staticv A0 5
@staticv A4 1
@staticv A10 1
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
@function Function0 4
assignw T19 0
assignw T20 BASE[0]
lt test T20 T19
goif B101 test
goto B113
@label B101
assignw S1[0] 53
param T22 0
assignw T22[0] S1
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T23 PRINT 6
assignw T24 1
exit T24
goto Function0_end
@label B113
@label L6
assignw T25 0
assignw T26 BASE[0]
eq test T26 T25
goif B119 test
goto B123
@label B119
assignw T27 1
assignw lastbase BASE
return T27
goto Function0_end
@label B123
assignw T28 1
assignw T30 BASE[0]
sub T29 T30 T28
param T31 0
assignw T31[0] T29
call T32 Function0 1
assignw T34 BASE[0]
mult T33 T34 T32
assignw lastbase BASE
return T33
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function1 8
assignw T35 0
assignw T36 BASE[0]
lt test T36 T35
goif B143 test
goto B155
@label B143
assignw S2[0] 53
param T38 0
assignw T38[0] S2
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T39 PRINT 6
assignw T40 1
exit T40
goto B155
@label B155
assignw T41 1
assignw BASE[4] T41
@label L7
assignw T42 0
assignw T43 BASE[0]
gt test T43 T42
goif B163 test
goto B172
@label B163
assignw T45 BASE[4]
assignw T46 BASE[0]
mult T44 T45 T46
assignw BASE[4] T44
assignw T47 1
assignw T49 BASE[0]
sub T48 T49 T47
assignw BASE[0] T48
goto L7
@label B172
assignw T50 BASE[4]
assignw lastbase BASE
return T50
@label Function1_end
assignw lastbase BASE
return 0
@endfunction 8
@function Function2 4
assignw T51 0
assignw f4 BASE[0]
lt test f4 T51
goif B185 test
goto B190
@label B185
assignw f6 BASE[0]
minus f5 f6
assignw lastbase BASE
return f5
goto Function2_end
@label B190
assignw f7 BASE[0]
assignw lastbase BASE
return f7
@label Function2_end
assignw lastbase BASE
return 0
@endfunction 4
@function Function3 20
assignb T52 A4[0]
goif L8 T52
assignw f8 0.000001
assignw BASE[4] f8
@label L8
assignw f9 1.000000
assignw f10 BASE[0]
assignw BASE[8] f10
assignw BASE[12] f9
@label L9
assignw f11 BASE[12]
assignw f12 BASE[4]
gt test f11 f12
goif B213 test
goto B231
@label B213
assignw f13 BASE[8]
assignw BASE[16] f13
assignw f15 BASE[0]
assignw f16 BASE[8]
div f14 f15 f16
assignw f18 BASE[8]
add f17 f18 f14
assignw T53 2
div f19 f17 T53
assignw BASE[8] f19
assignw f21 BASE[8]
assignw f22 BASE[16]
sub f20 f21 f22
param T54 0
assignw T54[0] f20
call f23 Function2 1
assignw BASE[12] f23
goto L9
@label B231
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
assignw T56 0
assignw BASE[12] T56
@label L10
assignw T57 BASE[12]
assignw T58 BASE[4]
lt test T57 T58
goif B249 test
goto B258
@label B249
assignw T59 BASE[0]
assignw T60 BASE[12]
mult T61 4 T60
add T61 T61 4
assignw f27 BASE[8]
assignw f28 T59[T61]
add f26 f27 f28
assignw BASE[8] f26
goto L10
@label B258
assignw f30 BASE[8]
assignw T62 BASE[4]
div f29 f30 T62
assignw lastbase BASE
return f29
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function5 16
assignw T64 1
assignw T65 BASE[4]
lt test T65 T64
goif B273 test
goto B285
@label B273
assignw S3[0] 51
param T67 0
assignw T67[0] S3
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T68 PRINT 6
assignw T69 1
exit T69
goto B285
@label B285
assignw T70 0
assignw T71 BASE[0]
mult T72 4 T70
add T72 T72 4
assignw f31 T71[T72]
assignw BASE[8] f31
assignw T73 1
assignw BASE[12] T73
@label L11
assignw T74 BASE[12]
assignw T75 BASE[4]
lt test T74 T75
goif B299 test
goto B316
@label B299
assignw T76 BASE[0]
assignw T77 BASE[12]
mult T78 4 T77
add T78 T78 4
assignw f32 T76[T78]
assignw f33 BASE[8]
lt test f32 f33
goif B308 test
goto L11
@label B308
assignw T79 BASE[0]
assignw T80 BASE[12]
mult T81 4 T80
add T81 T81 4
assignw f34 T79[T81]
assignw BASE[8] f34
goto L11
goto L11
@label B316
assignw f35 BASE[8]
assignw lastbase BASE
return f35
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function6 16
assignw T83 1
assignw T84 BASE[4]
lt test T84 T83
goif B329 test
goto B341
@label B329
assignw S4[0] 51
param T86 0
assignw T86[0] S4
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T87 PRINT 6
assignw T88 1
exit T88
goto B341
@label B341
assignw T89 0
assignw T90 BASE[0]
mult T91 4 T89
add T91 T91 4
assignw f36 T90[T91]
assignw BASE[8] f36
assignw T92 1
assignw BASE[12] T92
@label L12
assignw T93 BASE[12]
assignw T94 BASE[4]
lt test T93 T94
goif B355 test
goto B372
@label B355
assignw T95 BASE[0]
assignw T96 BASE[12]
mult T97 4 T96
add T97 T97 4
assignw f37 T95[T97]
assignw f38 BASE[8]
gt test f37 f38
goif B364 test
goto L12
@label B364
assignw T98 BASE[0]
assignw T99 BASE[12]
mult T100 4 T99
add T100 T100 4
assignw f39 T98[T100]
assignw BASE[8] f39
goto L12
goto L12
@label B372
assignw f40 BASE[8]
assignw lastbase BASE
return f40
@label Function6_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function7 20
@label L13
assignw T102 0
assignw T103 BASE[4]
eq test T103 T102
goif B386 test
goto B390
@label B386
assignw f41 0.000000
assignw lastbase BASE
return f41
goto B390
@label B390
assignw T105 BASE[0]
assignw T106 T105[0]
assignw T107 4
mult T107 T107 T106
add T107 T107 4
malloc T104 T107
memcpy T104 T105 T107
param T108 0
assignw T108[0] T104
assignw T109 BASE[4]
param T110 4
assignw T110[0] T109
call f42 Function4 2
assignw f43 0.000000
assignw BASE[8] f42
assignw BASE[12] f43
assignw T111 0
assignw BASE[16] T111
@label L14
assignw T112 BASE[16]
assignw T113 BASE[4]
lt test T112 T113
goif B414 test
goto B433
@label B414
assignw T114 BASE[0]
assignw T115 BASE[16]
mult T116 4 T115
add T116 T116 4
assignw f45 T114[T116]
assignw f46 BASE[8]
sub f44 f45 f46
assignw T117 BASE[0]
assignw T118 BASE[16]
mult T119 4 T118
add T119 T119 4
assignw f48 T117[T119]
assignw f49 BASE[8]
sub f47 f48 f49
mult f50 f44 f47
assignw f52 BASE[12]
add f51 f52 f50
assignw BASE[12] f51
goto L14
@label B433
assignw f54 BASE[12]
assignw T120 BASE[4]
div f53 f54 T120
assignw lastbase BASE
return f53
@label Function7_end
assignw lastbase BASE
return 0
@endfunction 20
@function Function8 8
assignw T123 BASE[0]
assignw T124 T123[0]
assignw T125 4
mult T125 T125 T124
add T125 T125 4
malloc T122 T125
memcpy T122 T123 T125
param T126 0
assignw T126[0] T122
assignw T127 BASE[4]
param T128 4
assignw T128[0] T127
call f55 Function7 2
param T129 0
assignw T129[0] f55
assignb A4[0] 0
call f56 Function3 2
assignw lastbase BASE
return f56
@label Function8_end
assignw lastbase BASE
return 0
@endfunction 8
assignb T131 0
assignw T132 1
assignw T134 T132
assignw T135 1
mult T135 T135 T134
add T135 T135 4
malloc T133 T135
assignw T133[0] T134
assignb T133[4] T131
assignw T136 T133
assignb T138 10
assignw T139 1
assignw T141 T139
assignw T142 1
mult T142 T142 T141
add T142 T142 4
malloc T140 T142
assignw T140[0] T141
assignb T140[4] T138
assignw T143 T140
@function Function9 12
assignb T145 A10[0]
goif L15 T145
assignb T146 0
assignb BASE[4] T146
@label L15
assignw T147 0
assignw BASE[8] T147
@label L16
assignw T148 BASE[0]
assignw T149 BASE[8]
mult T150 1 T149
add T150 T150 4
@label L17
assignb T151 T148[T150]
assignb T152 BASE[4]
neq test T151 T152
goif B505 test
goto B510
@label B505
assignw T153 1
assignw T155 BASE[8]
add T154 T155 T153
assignw BASE[8] T154
goto L16
@label B510
assignw T156 BASE[8]
assignw lastbase BASE
return T156
@label Function9_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function10 12
assignw T159 0
assignw BASE[8] T159
@label L18
assignw T160 BASE[0]
assignw T161 BASE[8]
mult T162 1 T161
add T162 T162 4
@label L19
assignb T163 0
assignb T164 T160[T162]
neq test T164 T163
goif B531 test
goto B550
@label B531
assignw T165 BASE[0]
assignw T166 BASE[8]
mult T167 1 T166
add T167 T167 4
@label L20
assignw T168 BASE[4]
assignw T169 BASE[8]
mult T170 1 T169
add T170 T170 4
assignb T171 T165[T167]
assignb T172 T168[T170]
eq test T171 T172
goif B545 test
goto B550
@label B545
assignw T173 1
assignw T175 BASE[8]
add T174 T175 T173
assignw BASE[8] T174
goto L18
@label B550
assignw T176 BASE[0]
assignw T177 BASE[8]
mult T178 1 T177
add T178 T178 4
assignw T179 BASE[4]
assignw T180 BASE[8]
mult T181 1 T180
add T181 T181 4
assignw T182 T176[T178]
assignw T183 T179[T181]
gt test T182 T183
goif B563 test
goto B567
@label B563
assignw T184 1
assignw lastbase BASE
return T184
goto Function10_end
@label B567
assignw T185 BASE[4]
assignw T186 BASE[8]
mult T187 1 T186
add T187 T187 4
assignw T188 BASE[0]
assignw T189 BASE[8]
mult T190 1 T189
add T190 T190 4
assignw T191 T185[T187]
assignw T192 T188[T190]
gt test T191 T192
goif B580 test
goto B585
@label B580
assignw T193 1
minus T194 T193
assignw lastbase BASE
return T194
goto Function10_end
@label B585
assignw T195 0
assignw lastbase BASE
return T195
@label Function10_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function11 16
assignw T199 BASE[4]
assignw T200 T199[0]
assignw T201 1
mult T201 T201 T200
add T201 T201 4
malloc T198 T201
memcpy T198 T199 T201
param T202 0
assignw T202[0] T198
assignb A10[0] 0
call T203 Function9 2
assignw T204 1
add T205 T203 T204
assignw BASE[8] T205
assignw T206 0
assignw BASE[12] T206
@label L21
assignw T207 BASE[12]
assignw T208 BASE[8]
lt test T207 T208
goif B615 test
goto Function11_end
@label B615
assignw T209 BASE[0]
assignw T210 BASE[12]
mult T211 1 T210
add T211 T211 4
assignw T212 BASE[4]
assignw T213 BASE[12]
mult T214 1 T213
add T214 T214 4
assignb T215 T212[T214]
assignb T209[T211] T215
assignw T216 1
assignw T218 BASE[12]
add T217 T218 T216
assignw BASE[12] T217
goto L21
@label Function11_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function12 16
assignw T222 BASE[4]
assignw T223 T222[0]
assignw T224 1
mult T224 T224 T223
add T224 T224 4
malloc T221 T224
memcpy T221 T222 T224
param T225 0
assignw T225[0] T221
assignb A10[0] 0
call T226 Function9 2
assignw BASE[8] T226
assignw T227 0
assignw T229 T227
@label L22
assignw T230 BASE[8]
geq test T229 T230
goif L22_end test
assignw T228 T229
assignw T232 BASE[8]
assignw T233 BASE[12]
sub T231 T232 T233
assignw T234 1
sub T235 T231 T234
assignw T236 BASE[0]
mult T237 1 T235
add T237 T237 4
assignw T238 BASE[4]
assignw T239 BASE[12]
mult T240 1 T239
add T240 T240 4
assignb T241 T238[T240]
assignb T236[T237] T241
add T229 T229 1
goto L22
@label L22_end
@label Function12_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function13 28
assignw T245 0
assignw T246 0
assignw BASE[12] T245
assignw BASE[16] T246
@label L23
assignw T247 BASE[12]
assignw T248 BASE[4]
lt test T247 T248
goif B686 test
goto B738
@label B686
assignw T249 BASE[0]
assignw T250 BASE[12]
mult T251 4 T250
add T251 T251 4
assignw T253 T249[T251]
assignw T254 T253[0]
assignw T255 1
mult T255 T255 T254
add T255 T255 4
malloc T252 T255
memcpy T252 T253 T255
param T256 0
assignw T256[0] T252
assignb A10[0] 0
call T257 Function9 2
assignw BASE[24] T257
assignw T258 0
assignw BASE[20] T258
@label L24
assignw T259 BASE[20]
assignw T260 BASE[24]
lt test T259 T260
goif B710 test
goto B733
@label B710
assignw T261 BASE[8]
assignw T262 BASE[16]
mult T263 1 T262
add T263 T263 4
assignw T264 BASE[0]
assignw T265 BASE[12]
mult T266 4 T265
add T266 T266 4
assignw T267 T264[T266]
assignw T268 BASE[20]
mult T269 1 T268
add T269 T269 4
assignb T270 T267[T269]
assignb T261[T263] T270
assignw T271 1
assignw T273 BASE[20]
add T272 T273 T271
assignw BASE[20] T272
assignw T274 1
assignw T276 BASE[16]
add T275 T276 T274
assignw BASE[16] T275
goto L24
@label B733
assignw T277 1
assignw T279 BASE[12]
add T278 T279 T277
assignw BASE[12] T278
goto L23
@label B738
assignw T280 BASE[8]
assignw T281 BASE[16]
mult T282 1 T281
add T282 T282 4
assignb T283 0
assignb T280[T282] T283
@label Function13_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function14 29
assignw T287 0
assignw T288 0
assignw T289 0
assignw T291 BASE[0]
assignw T292 T291[0]
assignw T293 1
mult T293 T293 T292
add T293 T293 4
malloc T290 T293
memcpy T290 T291 T293
param T294 0
assignw T294[0] T290
assignb A10[0] 0
call T295 Function9 2
assignw BASE[12] T287
assignw BASE[16] T288
assignw BASE[20] T289
assignw BASE[24] T295
goto B768
@label B768
assignb BASE[28] True
goto Bool771
assignb BASE[28] False
@label Bool771
@label L25
assignw T296 BASE[0]
assignw T297 BASE[12]
mult T298 1 T297
add T298 T298 4
@label L26
assignb T299 0
assignb T300 T296[T298]
neq test T300 T299
goif B783 test
goto B863
@label B783
assignw T301 BASE[0]
assignw T302 BASE[12]
mult T303 1 T302
add T303 T303 4
@label L27
assignb T304 T301[T303]
assignb T305 BASE[8]
eq test T304 T305
goif B793 test
goto B821
@label B793
assignb T306 BASE[28]
goif B821 T306
goto B796
@label B796
assignb T307 BASE[28]


goto B800
@label B800
assignb BASE[28] True
goto Bool803
assignb BASE[28] False
@label Bool803
assignw T308 BASE[4]
assignw T309 BASE[20]
mult T310 4 T309
add T310 T310 4
assignw T311 T308[T310]
assignw T312 BASE[16]
mult T313 1 T312
add T313 T313 4
assignb T314 0
assignb T311[T313] T314
assignw T315 1
assignw T317 BASE[20]
add T316 T317 T315
assignw BASE[20] T316
assignw T318 0
assignw BASE[16] T318
goto B858
@label B821
assignw T319 BASE[0]
assignw T320 BASE[12]
mult T321 1 T320
add T321 T321 4
@label L28
assignb T322 T319[T321]
assignb T323 BASE[8]
neq test T322 T323
goif B831 test
goto B858
@label B831
assignb T324 BASE[28]


goto B837
assignb BASE[28] True
goto Bool838
@label B837
assignb BASE[28] False
@label Bool838
assignw T325 BASE[4]
assignw T326 BASE[20]
mult T327 4 T326
add T327 T327 4
assignw T328 T325[T327]
assignw T329 BASE[16]
mult T330 1 T329
add T330 T330 4
assignw T331 BASE[0]
assignw T332 BASE[12]
mult T333 1 T332
add T333 T333 4
assignb T334 T331[T333]
assignb T328[T330] T334
assignw T335 1
assignw T337 BASE[16]
add T336 T337 T335
assignw BASE[16] T336
goto B858
@label B858
assignw T338 1
assignw T340 BASE[12]
add T339 T340 T338
assignw BASE[12] T339
goto L25
@label B863
assignb T341 BASE[28]
goif B881 T341
goto B866
@label B866
assignw T342 BASE[4]
assignw T343 BASE[20]
mult T344 4 T343
add T344 T344 4
assignw T345 T342[T344]
assignw T346 BASE[16]
mult T347 1 T346
add T347 T347 4
assignb T348 0
assignb T345[T347] T348
assignw T349 1
assignw T351 BASE[20]
add T350 T351 T349
assignw BASE[20] T350
goto B881
@label B881
assignw T352 BASE[20]
assignw lastbase BASE
return T352
@label Function14_end
assignw lastbase BASE
return 0
@endfunction 29
@function Function15 16
goto B893
goto B897
assignb BASE[4] True
goto Bool894
@label B893
assignb BASE[4] False
@label Bool894
assignb BASE[5] True
goto Bool898
@label B897
assignb BASE[5] False
@label Bool898
assignw T355 BASE[0]
assignw T356 T355[0]
assignw T357 1
mult T357 T357 T356
add T357 T357 4
malloc T354 T357
memcpy T354 T355 T357
param T358 0
assignw T358[0] T354
assignb A10[0] 0
call T359 Function9 2
assignw T360 0
assignw BASE[8] T359
assignw BASE[12] T360
@label L29
assignw T361 BASE[12]
assignw T362 BASE[8]
lt test T361 T362
goif B919 test
goto B1005
@label B919
assignw T363 BASE[0]
assignw T364 BASE[12]
mult T365 1 T364
add T365 T365 4
@label L30
assignb T366 46
assignb T367 T363[T365]
eq test T367 T366
goif B929 test
goto B941
@label B929
assignb T368 BASE[4]
goif B941 T368
goto B932
@label B932
assignb T369 BASE[4]


goto B936
@label B936
assignb BASE[4] True
goto Bool939
assignb BASE[4] False
@label Bool939
goto B1000
@label B941
assignw T370 BASE[0]
assignw T371 BASE[12]
mult T372 1 T371
add T372 T372 4
@label L31
assignb T373 46
assignb T374 T370[T372]
eq test T374 T373
goif B951 test
goto B959
@label B951
goto B954
assignb T375 True
goto Bool955
@label B954
assignb T375 False
@label Bool955
assignw lastbase BASE
return T375
goto B1000
@label B959
assignw T376 BASE[0]
assignw T377 BASE[12]
mult T378 1 T377
add T378 T378 4
assignb T379 48
assignw T380 T376[T378]
lt test T380 T379
goif B977 test
goto B968
@label B968
assignw T381 BASE[0]
assignw T382 BASE[12]
mult T383 1 T382
add T383 T383 4
assignb T384 57
assignw T385 T381[T383]
gt test T385 T384
goif B977 test
goto B985
@label B977
goto B980
assignb T386 True
goto Bool981
@label B980
assignb T386 False
@label Bool981
assignw lastbase BASE
return T386
goto B1000
@label B985
assignb T387 BASE[4]
goif B988 T387
goto B1000
@label B988
assignb T388 BASE[5]
goif B1000 T388
goto B991
@label B991
assignb T389 BASE[5]


goto B995
@label B995
assignb BASE[5] True
goto Bool998
assignb BASE[5] False
@label Bool998
goto B1000
@label B1000
assignw T390 1
assignw T392 BASE[12]
add T391 T392 T390
assignw BASE[12] T391
goto L29
@label B1005
assignb T393 BASE[4]
goif B1008 T393
goto B1013
@label B1008
assignb T394 BASE[5]
goif B1011 T394
goto B1013
@label B1011
assignb T395 True
goto Bool1014
@label B1013
assignb T395 False
@label Bool1014
assignw lastbase BASE
return T395
@label Function15_end
assignw lastbase BASE
return 0
@endfunction 16
@function Function16 24
assignw T398 BASE[0]
assignw T399 T398[0]
assignw T400 1
mult T400 T400 T399
add T400 T400 4
malloc T397 T400
memcpy T397 T398 T400
param T401 0
assignw T401[0] T397
assignb A10[0] 0
call T402 Function9 2
assignw BASE[8] T402
assignw T403 0
assignw BASE[4] T403
@label L32
assignw T404 0
assignw T405 BASE[8]
eq test T405 T404
goif B1058 test
goto B1042
@label B1042
assignw T406 0
assignw T407 BASE[0]
mult T408 1 T406
add T408 T408 4
@label L33
assignb T409 45
assignb T410 T407[T408]
eq test T410 T409
goif B1052 test
goto B1066
@label B1052
@label L34
assignw T411 1
assignw T412 BASE[8]
eq test T412 T411
goif B1058 test
goto B1066
@label B1058
goto B1061
assignb T413 True
goto Bool1062
@label B1061
assignb T413 False
@label Bool1062
assignw lastbase BASE
return T413
goto B1086
@label B1066
assignw T414 0
assignw T415 BASE[0]
mult T416 1 T414
add T416 T416 4
@label L35
assignb T417 45
assignb T418 T415[T416]
eq test T418 T417
goif B1076 test
goto B1082
@label B1076
assignw T419 1
minus T420 T419
assignw BASE[16] T420
assignw T421 1
assignw BASE[12] T421
goto B1086
@label B1082
assignw T422 1
assignw BASE[16] T422
assignw T423 0
assignw BASE[12] T423
@label B1086
assignw T424 1
assignw T426 BASE[8]
sub T425 T426 T424
assignw T427 1
assignw T429 BASE[12]
sub T428 T429 T427
assignw T430 1
minus T431 T430
assignw T433 T425
@label L36
lt test T431 0
goif L36_neg test
geq test T433 T428
goif L36_end test
goto L36_body
@label L36_neg
leq test T433 T428
goif L36_end test
@label L36_body
assignw T432 T433
assignw T434 BASE[0]
assignw T435 BASE[20]
mult T436 1 T435
add T436 T436 4
assignb T437 48
assignw T438 T434[T436]
lt test T438 T437
goif B1124 test
goto B1115
@label B1115
assignw T439 BASE[0]
assignw T440 BASE[20]
mult T441 1 T440
add T441 T441 4
assignb T442 57
assignw T443 T439[T441]
gt test T443 T442
goif B1124 test
goto B1134
@label B1124
assignw T444 0
assignw BASE[4] T444
goto B1129
assignb T445 True
goto Bool1130
@label B1129
assignb T445 False
@label Bool1130
assignw lastbase BASE
return T445
goto B1134
@label B1134
assignw T446 BASE[0]
assignw T447 BASE[20]
mult T448 1 T447
add T448 T448 4
assignb T449 T446[T448]
param T450 0
assignb T450[0] T449
call T451 CTOI 1
assignb T452 48
param T453 0
assignb T453[0] T452
call T454 CTOI 1
sub T455 T451 T454
assignw T457 BASE[16]
mult T456 T457 T455
assignw T459 BASE[4]
add T458 T459 T456
assignw BASE[4] T458
assignw T460 10
assignw T462 BASE[16]
mult T461 T462 T460
assignw BASE[16] T461
add T433 T433 T431
goto L36
@label L36_end
goto B1160
@label B1160
assignb T463 True
goto Bool1163
assignb T463 False
@label Bool1163
assignw lastbase BASE
return T463
@label Function16_end
assignw lastbase BASE
return 0
@endfunction 24
@function Function17 36
assignw T466 BASE[0]
assignw T467 T466[0]
assignw T468 1
mult T468 T468 T467
add T468 T468 4
malloc T465 T468
memcpy T465 T466 T468
param T469 0
assignw T469[0] T465
assignb A10[0] 0
call T470 Function9 2
assignw BASE[8] T470
assignw T471 BASE[8]
assignw T472 BASE[12]
assignw T473 1
mult T473 T473 T471
add T473 T473 4
malloc T472 T473
assignw T472[0] T471
assignw T472[0] T472
assignw T474 BASE[8]
assignw T475 BASE[16]
assignw T476 1
mult T476 T476 T474
add T476 T476 4
malloc T475 T476
assignw T475[0] T474
assignw T475[0] T475
assignw T477 0
assignw BASE[32] T477
@label L37
assignw T478 BASE[0]
assignw T479 BASE[32]
mult T480 1 T479
add T480 T480 4
@label L38
assignb T481 46
assignb T482 T478[T480]
neq test T482 T481
goif B1212 test
goto B1237
@label B1212
assignw T483 BASE[0]
assignw T484 BASE[32]
mult T485 1 T484
add T485 T485 4
@label L39
assignb T486 0
assignb T487 T483[T485]
neq test T487 T486
goif B1222 test
goto B1237
@label B1222
assignw T488 BASE[12]
assignw T489 BASE[32]
mult T490 1 T489
add T490 T490 4
assignw T491 BASE[0]
assignw T492 BASE[32]
mult T493 1 T492
add T493 T493 4
assignb T494 T491[T493]
assignb T488[T490] T494
assignw T495 1
assignw T497 BASE[32]
add T496 T497 T495
assignw BASE[32] T496
goto L37
@label B1237
@label L40
assignw T498 0
assignw T499 BASE[32]
eq test T499 T498
goif B1243 test
goto B1246
@label B1243
assignw T500 0
assignw BASE[24] T500
goto B1271
@label B1246
assignw T502 BASE[12]
assignw T503 T502[0]
assignw T504 1
mult T504 T504 T503
add T504 T504 4
malloc T501 T504
memcpy T501 T502 T504
param T505 0
assignw T505[0] T501
assignw T506 BASE[24]
param T507 4
assignw T507[0] T506
call T508 Function16 2
assignw T509 lastbase[4]
assignw BASE[24] T509
goif B1271 T508
goto B1263
@label B1263
goto B1266
assignb T510 True
goto Bool1267
@label B1266
assignb T510 False
@label Bool1267
assignw lastbase BASE
return T510
goto B1271
@label B1271
assignw T511 BASE[0]
assignw T512 BASE[32]
mult T513 1 T512
add T513 T513 4
@label L41
assignb T514 0
assignb T515 T511[T513]
eq test T515 T514
goif B1281 test
goto B1294
@label B1281
assignw T516 BASE[24]
param T517 0
assignw T517[0] T516
call f57 ITOF 1
assignw BASE[4] f57
goto B1287
@label B1287
assignb T518 True
goto Bool1290
assignb T518 False
@label Bool1290
assignw lastbase BASE
return T518
goto B1294
@label B1294
assignw T519 1
assignw T521 BASE[32]
add T520 T521 T519
assignw BASE[32] T520
assignw T522 0
assignw BASE[20] T522
@label L42
assignw T523 BASE[0]
assignw T524 BASE[32]
mult T525 1 T524
add T525 T525 4
@label L43
assignb T526 0
assignb T527 T523[T525]
neq test T527 T526
goif B1311 test
goto B1330
@label B1311
assignw T528 BASE[16]
assignw T529 BASE[20]
mult T530 1 T529
add T530 T530 4
assignw T531 BASE[0]
assignw T532 BASE[32]
mult T533 1 T532
add T533 T533 4
assignb T534 T531[T533]
assignb T528[T530] T534
assignw T535 1
assignw T537 BASE[32]
add T536 T537 T535
assignw BASE[32] T536
assignw T538 1
assignw T540 BASE[20]
add T539 T540 T538
assignw BASE[20] T539
goto L42
@label B1330
@label L44
assignw T541 0
assignw T542 BASE[20]
eq test T542 T541
goif B1336 test
goto B1349
@label B1336
assignw T543 BASE[24]
param T544 0
assignw T544[0] T543
call f58 ITOF 1
assignw BASE[4] f58
goto B1342
@label B1342
assignb T545 True
goto Bool1345
assignb T545 False
@label Bool1345
assignw lastbase BASE
return T545
goto B1374
@label B1349
assignw T547 BASE[16]
assignw T548 T547[0]
assignw T549 1
mult T549 T549 T548
add T549 T549 4
malloc T546 T549
memcpy T546 T547 T549
param T550 0
assignw T550[0] T546
assignw T551 BASE[28]
param T552 4
assignw T552[0] T551
call T553 Function16 2
assignw T554 lastbase[4]
assignw BASE[28] T554
goif B1374 T553
goto B1366
@label B1366
goto B1369
assignb T555 True
goto Bool1370
@label B1369
assignb T555 False
@label Bool1370
assignw lastbase BASE
return T555
goto B1374
@label B1374
assignw T556 BASE[24]
param T557 0
assignw T557[0] T556
call f59 ITOF 1
assignw T558 BASE[28]
param T559 0
assignw T559[0] T558
call f60 ITOF 1
assignw T560 10
assignw T562 T560
assignw T563 BASE[20]
assignw T561 1
lt test T563 0
goif L45_neg test
@label L45_pos
eq test T563 0
goif L45_end test
mult T561 T561 T562
sub T563 T563 1
goto L45_pos
@label L45_neg
div T561 T561 T562
add T563 T563 1
neq test T563 0
goif L45_neg test
@label L45_end
div f61 f60 T561
add f62 f59 f61
assignw BASE[4] f62
goto B1404
@label B1404
assignb T564 True
goto Bool1407
assignb T564 False
@label Bool1407
assignw lastbase BASE
return T564
@label Function17_end
assignw lastbase BASE
return 0
@endfunction 36
@function Function18 32
@label L46
assignw T566 0
assignw T567 BASE[4]
eq test T567 T566
goif B1421 test
goto B1434
@label B1421
assignw T568 0
assignw T569 BASE[0]
mult T570 1 T568
add T570 T570 4
assignb T571 48
assignb T569[T570] T571
assignw T572 1
assignw T573 BASE[0]
mult T574 1 T572
add T574 T574 4
assignb T575 0
assignb T573[T574] T575
goto B1434
@label B1434
assignw T576 0
assignw BASE[16] T576
assignw T578 BASE[0]
assignw T579 T578[0]
assignw T580 1
mult T580 T580 T579
add T580 T580 4
malloc T577 T580
memcpy T577 T578 T580
param T581 0
assignw T581[0] T577
assignb A10[0] 0
call T582 Function9 2
assignw T583 T582
assignw T584 BASE[20]
assignw T585 1
mult T585 T585 T583
add T585 T585 4
malloc T584 T585
assignw T584[0] T583
assignw T584[0] T584
assignw T586 T582
assignw T587 BASE[24]
assignw T588 1
mult T588 T588 T586
add T588 T588 4
malloc T587 T588
assignw T587[0] T586
assignw T587[0] T587
assignw T589 0
assignw T590 BASE[4]
lt test T590 T589
goif B1468 test
goto B1472
@label B1468
assignw T592 BASE[4]
minus T591 T592
assignw BASE[8] T591
goto B1474
@label B1472
assignw T593 BASE[4]
assignw BASE[8] T593
@label B1474
@label L47
assignw T594 0
assignw T595 BASE[8]
gt test T595 T594
goif B1480 test
goto B1501
@label B1480
assignw T596 BASE[20]
assignw T597 BASE[16]
mult T598 1 T597
add T598 T598 4
assignw T599 10
assignw T601 BASE[8]
mod T600 T601 T599
assignb T602 48
param T603 0
assignb T603[0] T602
call T604 CTOI 1
add T605 T600 T604
param T606 0
assignw T606[0] T605
call T607 ITOC 1
assignb T596[T598] T607
assignw T608 10
assignw T610 BASE[8]
div T609 T610 T608
assignw BASE[8] T609
goto L47
@label B1501
assignw T611 BASE[24]
param T612 0
assignw T612[0] T611
assignw T614 BASE[20]
assignw T615 T614[0]
assignw T616 1
mult T616 T616 T615
add T616 T616 4
malloc T613 T616
memcpy T613 T614 T616
param T617 4
assignw T617[0] T613
call T618 Function12 2
assignw T619 0
assignw T620 BASE[4]
lt test T620 T619
goif B1519 test
goto B1579
@label B1519
assignw S5[0] 1
assignw T622 2
assignw T623 T622
assignw T624 BASE[28]
assignw T625 4
mult T625 T625 T623
add T625 T625 4
malloc T624 T625
assignw T624[0] T623
assignw T624[0] T624
@label L48
sub T625 T625 4
lt test T625 0
goif L48_end test
assignw T626 T582
assignw T627 T624[T625]
assignw T628 1
mult T628 T628 T626
add T628 T628 4
malloc T627 T628
assignw T627[0] T626
assignw T627[0] T627
goto L48
@label L48_end
assignw T629 BASE[28]
assignw T630 BASE[24]
assignw T629[8] T630
assignw T629[4] S5
assignw T631 2
assignw T633 BASE[28]
assignw T634 T633[0]
assignw T635 4
mult T635 T635 T634
add T635 T635 4
malloc T632 T635
assignw T636 T635
@label L49
sub T636 T636 4
lt test T636 0
goif L49_end test
assignw T637 T633[T636]
assignw T638 T632[T636]
assignw T639 T637[0]
assignw T640 1
mult T640 T640 T639
add T640 T640 4
malloc T638 T640
assignw T638[0] T638
memcpy T638 T637 T640
goto L49
@label L49_end
param T641 0
assignw T641[0] T632
param T642 4
assignw T642[0] T631
assignw T643 BASE[0]
param T644 8
assignw T644[0] T643
call T645 Function13 3
goto Function18_end
@label B1579
assignw T646 BASE[0]
param T647 0
assignw T647[0] T646
assignw T649 BASE[24]
assignw T650 T649[0]
assignw T651 1
mult T651 T651 T650
add T651 T651 4
malloc T648 T651
memcpy T648 T649 T651
param T652 4
assignw T652[0] T648
call T653 Function11 2
@label Function18_end
assignw lastbase BASE
return 0
@endfunction 32
@function Function19 32
assignw T656 BASE[0]
assignw T657 T656[0]
assignw T658 1
mult T658 T658 T657
add T658 T658 4
malloc T655 T658
memcpy T655 T656 T658
param T659 0
assignw T659[0] T655
assignb A10[0] 0
call T660 Function9 2
assignw T661 T660
assignw T662 BASE[20]
assignw T663 1
mult T663 T663 T661
add T663 T663 4
malloc T662 T663
assignw T662[0] T661
assignw T662[0] T662
assignw T664 T660
assignw T665 BASE[24]
assignw T666 1
mult T666 T666 T664
add T666 T666 4
malloc T665 T666
assignw T665[0] T664
assignw T665[0] T665
assignw f63 BASE[4]
param T667 0
assignw T667[0] f63
call T668 FTOI 1
assignw BASE[8] T668
assignw f65 BASE[4]
assignw T669 BASE[8]
sub f64 f65 T669
assignw BASE[16] f64
@label L50
@label L51
assignw f66 BASE[16]
param T670 0
assignw T670[0] f66
call T671 FTOI 1
assignw T672 BASE[16]
neq test T672 T671
goif B1643 test
goto B1648
@label B1643
assignw T673 10
assignw f68 BASE[16]
mult f67 f68 T673
assignw BASE[16] f67
goto L50
@label B1648
assignw f69 BASE[16]
param T674 0
assignw T674[0] f69
call T675 FTOI 1
assignw BASE[12] T675
assignw T676 BASE[20]
param T677 0
assignw T677[0] T676
assignw T678 BASE[8]
param T679 4
assignw T679[0] T678
call T680 Function18 2
assignw T681 BASE[24]
param T682 0
assignw T682[0] T681
assignw T683 BASE[12]
param T684 4
assignw T684[0] T683
call T685 Function18 2
assignw S6[0] 1
assignw T687 3
assignw T688 T687
assignw T689 BASE[28]
assignw T690 4
mult T690 T690 T688
add T690 T690 4
malloc T689 T690
assignw T689[0] T688
assignw T689[0] T689
@label L52
sub T690 T690 4
lt test T690 0
goif L52_end test
assignw T691 T660
assignw T692 T689[T690]
assignw T693 1
mult T693 T693 T691
add T693 T693 4
malloc T692 T693
assignw T692[0] T691
assignw T692[0] T692
goto L52
@label L52_end
assignw T694 BASE[28]
assignw T695 BASE[24]
assignw T694[12] T695
assignw T694[8] S6
assignw T696 BASE[20]
assignw T694[4] T696
assignw T697 3
assignw T699 BASE[28]
assignw T700 T699[0]
assignw T701 4
mult T701 T701 T700
add T701 T701 4
malloc T698 T701
assignw T702 T701
@label L53
sub T702 T702 4
lt test T702 0
goif L53_end test
assignw T703 T699[T702]
assignw T704 T698[T702]
assignw T705 T703[0]
assignw T706 1
mult T706 T706 T705
add T706 T706 4
malloc T704 T706
assignw T704[0] T704
memcpy T704 T703 T706
goto L53
@label L53_end
param T707 0
assignw T707[0] T698
param T708 4
assignw T708[0] T697
assignw T709 BASE[0]
param T710 8
assignw T710[0] T709
call T711 Function13 3
@label Function19_end
assignw lastbase BASE
return 0
@endfunction 32
@label L54
goto B1734
@label B1734
assignw S7[0] 38
param T717 0
assignw T717[0] S7
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T718 PRINT 6
call T719 READI 0
assignw T712 T719
assignw S8[0] 63
param T721 0
assignw T721[0] S8
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T722 PRINT 6
call T723 READC 0
assignb T715 T723
@label L55
assignb T724 110
eq test T715 T724
goif B1766 test
goto B1761
@label B1761
@label L56
assignb T725 78
eq test T715 T725
goif B1766 test
goto B1771
@label B1766
param T726 0
assignw T726[0] T712
call T727 Function0 1
assignw T713 T727
goto B1775
@label B1771
param T728 0
assignw T728[0] T712
call T729 Function1 1
assignw T713 T729
@label B1775
assignw S9[0] 8
assignw T731 2
assignw T733 T731
assignw T734 4
mult T734 T734 T733
add T734 T734 4
malloc T732 T734
assignw T732[0] T733
assignw T732[8] T713
assignw T732[4] T712
param T735 0
assignw T735[0] S9
assignb A0[0] 0
assignw T737 T732[0]
assignw T738 4
mult T738 T738 T737
add T738 T738 4
malloc T736 T738
memcpy T736 T732 T738
param T739 8
assignw T739[0] T736
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T740 PRINT 6
assignw S10[0] 37
param T742 0
assignw T742[0] S10
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T743 PRINT 6
call T744 READC 0
assignb T715 T744
@label L57
assignb T745 110
eq test T715 T745
goif B1822 test
goto B1817
@label B1817
@label L58
assignb T746 78
eq test T715 T746
goif B1822 test
goto L54
@label B1822
assignw S11[0] 12
param T748 0
assignw T748[0] S11
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T749 PRINT 6
goto B1834
goto L54
goto L54
@label B1834
