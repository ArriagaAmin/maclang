@staticv A0 5
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
goto B128
@label B128
assignw S1[0] 55
param T45 0
assignw T45[0] S1
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T46 PRINT 6
assignw S2[0] 28
param T48 0
assignw T48[0] S2
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T49 PRINT 6
assignw S3[0] 38
param T51 0
assignw T51[0] S3
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T52 PRINT 6
assignw S4[0] 23
param T54 0
assignw T54[0] S4
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T55 PRINT 6
assignw S5[0] 10
param T57 0
assignw T57[0] S5
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T58 PRINT 6
call T59 READI 0
assignw T29 T59
assignw T60 0
lt test T60 T29
goif B179 test
goto B649
@label B179
assignw T61 4
lt test T29 T61
goif B183 test
goto B649
@label B183
assignw S6[0] 81
param T63 0
assignw T63[0] S6
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T64 PRINT 6
call T65 READI 0
assignw T30 T65
assignw T66 1
lt test T30 T66
goif B202 test
goto B198
@label B198
assignw T67 100
gt test T30 T67
goif B202 test
goto B213
@label B202
assignw S7[0] 29
param T69 0
assignw T69[0] S7
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T70 PRINT 6
goto L6
goto B213
@label B213
assignw S8[0] 23
param T72 0
assignw T72[0] S8
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T73 PRINT 6
@label L7
assignw T74 1
eq test T29 T74
goif B227 test
goto B369
@label B227
assignw T75 0
assignw T77 T75
@label L8
geq test T77 T30
goif L8_end test
assignw T76 T77
mult T78 4 T76
add T78 T78 4
call T79 READI 0
assignw T33[T78] T79
add T77 T77 1
goto L8
@label L8_end
assignw T80 0
assignw T82 T33[0]
assignw T83 4
mult T83 T83 T82
add T83 T83 4
malloc T81 T83
memcpy T81 T33 T83
param T84 0
assignw T84[0] T81
param T85 4
assignw T85[0] T80
param T86 8
assignw T86[0] T30
call T87 Function1  3
assignw S9[0] 39
assignb T89 10
assignb T90 91
assignw T91 2
assignw T93 T91
assignw T94 1
mult T94 T94 T93
add T94 T94 4
malloc T92 T94
assignw T92[0] T93
assignb T92[5] T90
assignb T92[4] T89
param T95 0
assignw T95[0] S9
assignw T97 T92[0]
assignw T98 1
mult T98 T98 T97
add T98 T98 4
malloc T96 T98
memcpy T96 T92 T98
param T99 4
assignw T99[0] T96
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T100 PRINT 6
assignw T101 0
assignw T102 1
sub T103 T30 T102
assignw T105 T101
@label L9
geq test T105 T103
goif L9_end test
assignw T104 T105
assignw S10[0] 4
mult T107 4 T104
add T107 T107 4
assignw T108 1
assignw T110 T108
assignw T111 4
mult T111 T111 T110
add T111 T111 4
malloc T109 T111
assignw T109[0] T110
assignw T112 T33[T107]
assignw T109[4] T112
param T113 0
assignw T113[0] S10
assignb A0[0] 0
assignw T115 T109[0]
assignw T116 4
mult T116 T116 T115
add T116 T116 4
malloc T114 T116
memcpy T114 T109 T116
param T117 8
assignw T117[0] T114
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T118 PRINT 6
add T105 T105 1
goto L9
@label L9_end
assignw S11[0] 5
assignw T120 1
sub T121 T30 T120
mult T122 4 T121
add T122 T122 4
assignw T123 1
assignw T125 T123
assignw T126 4
mult T126 T126 T125
add T126 T126 4
malloc T124 T126
assignw T124[0] T125
assignw T127 T33[T122]
assignw T124[4] T127
assignb T128 10
assignw T129 1
assignw T131 T129
assignw T132 1
mult T132 T132 T131
add T132 T132 4
malloc T130 T132
assignw T130[0] T131
assignb T130[4] T128
param T133 0
assignw T133[0] S11
assignw T135 T130[0]
assignw T136 1
mult T136 T136 T135
add T136 T136 4
malloc T134 T136
memcpy T134 T130 T136
param T137 4
assignw T137[0] T134
assignb A0[0] 1
assignw T139 T124[0]
assignw T140 4
mult T140 T140 T139
add T140 T140 4
malloc T138 T140
memcpy T138 T124 T140
param T141 8
assignw T141[0] T138
assignb A0[1] 1
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T142 PRINT 6
goto L6
@label B369
@label L10
assignw T143 2
eq test T29 T143
goif B374 test
goto B516
@label B374
assignw T144 0
assignw T146 T144
@label L11
geq test T146 T30
goif L11_end test
assignw T145 T146
mult T147 4 T145
add T147 T147 4
call f4 READF 0
assignw T37[T147] f4
add T146 T146 1
goto L11
@label L11_end
assignw T148 0
assignw T150 T37[0]
assignw T151 4
mult T151 T151 T150
add T151 T151 4
malloc T149 T151
memcpy T149 T37 T151
param T152 0
assignw T152[0] T149
param T153 4
assignw T153[0] T148
param T154 8
assignw T154[0] T30
call T155 Function3  3
assignw S12[0] 41
assignb T157 10
assignb T158 91
assignw T159 2
assignw T161 T159
assignw T162 1
mult T162 T162 T161
add T162 T162 4
malloc T160 T162
assignw T160[0] T161
assignb T160[5] T158
assignb T160[4] T157
param T163 0
assignw T163[0] S12
assignw T165 T160[0]
assignw T166 1
mult T166 T166 T165
add T166 T166 4
malloc T164 T166
memcpy T164 T160 T166
param T167 4
assignw T167[0] T164
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T168 PRINT 6
assignw T169 0
assignw T170 1
sub T171 T30 T170
assignw T173 T169
@label L12
geq test T173 T171
goif L12_end test
assignw T172 T173
assignw S13[0] 4
mult T175 4 T172
add T175 T175 4
assignw T176 1
assignw T178 T176
assignw T179 4
mult T179 T179 T178
add T179 T179 4
malloc T177 T179
assignw T177[0] T178
assignw f5 T37[T175]
assignw T177[4] f5
param T180 0
assignw T180[0] S13
assignb A0[0] 0
assignb A0[1] 0
assignw T182 T177[0]
assignw T183 4
mult T183 T183 T182
add T183 T183 4
malloc T181 T183
memcpy T181 T177 T183
param T184 12
assignw T184[0] T181
assignb A0[2] 1
assignb A0[3] 0
assignb A0[4] 0
call T185 PRINT 6
add T173 T173 1
goto L12
@label L12_end
assignw S14[0] 5
assignw T187 1
sub T188 T30 T187
mult T189 4 T188
add T189 T189 4
assignw T190 1
assignw T192 T190
assignw T193 4
mult T193 T193 T192
add T193 T193 4
malloc T191 T193
assignw T191[0] T192
assignw f6 T37[T189]
assignw T191[4] f6
assignb T194 10
assignw T195 1
assignw T197 T195
assignw T198 1
mult T198 T198 T197
add T198 T198 4
malloc T196 T198
assignw T196[0] T197
assignb T196[4] T194
param T199 0
assignw T199[0] S14
assignw T201 T196[0]
assignw T202 1
mult T202 T202 T201
add T202 T202 4
malloc T200 T202
memcpy T200 T196 T202
param T203 4
assignw T203[0] T200
assignb A0[0] 1
assignb A0[1] 0
assignw T205 T191[0]
assignw T206 4
mult T206 T206 T205
add T206 T206 4
malloc T204 T206
memcpy T204 T191 T206
param T207 12
assignw T207[0] T204
assignb A0[2] 1
assignb A0[3] 0
assignb A0[4] 0
call T208 PRINT 6
goto L6
@label B516
@label L13
assignw T209 2
eq test T29 T209
goif B521 test
goto L6
@label B521
assignw T210 0
assignw T212 T210
@label L14
geq test T212 T30
goif L14_end test
assignw T211 T212
mult T213 1 T211
add T213 T213 4
call T214 READC 0
assignb T41[T213] T214
add T212 T212 1
goto L14
@label L14_end
assignw T215 0
assignw T217 T41[0]
assignw T218 1
mult T218 T218 T217
add T218 T218 4
malloc T216 T218
memcpy T216 T41 T218
param T219 0
assignw T219[0] T216
param T220 4
assignw T220[0] T215
param T221 8
assignw T221[0] T30
call T222 Function5  3
assignw S15[0] 42
assignb T224 10
assignb T225 91
assignw T226 2
assignw T228 T226
assignw T229 1
mult T229 T229 T228
add T229 T229 4
malloc T227 T229
assignw T227[0] T228
assignb T227[5] T225
assignb T227[4] T224
param T230 0
assignw T230[0] S15
assignw T232 T227[0]
assignw T233 1
mult T233 T233 T232
add T233 T233 4
malloc T231 T233
memcpy T231 T227 T233
param T234 4
assignw T234[0] T231
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T235 PRINT 6
assignw T236 0
assignw T237 1
sub T238 T30 T237
assignw T240 T236
@label L15
geq test T240 T238
goif L15_end test
assignw T239 T240
assignw S16[0] 4
mult T242 1 T239
add T242 T242 4
assignw T243 1
assignw T245 T243
assignw T246 1
mult T246 T246 T245
add T246 T246 4
malloc T244 T246
assignw T244[0] T245
assignb T247 T41[T242]
assignb T244[4] T247
param T248 0
assignw T248[0] S16
assignw T250 T244[0]
assignw T251 1
mult T251 T251 T250
add T251 T251 4
malloc T249 T251
memcpy T249 T244 T251
param T252 4
assignw T252[0] T249
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T253 PRINT 6
add T240 T240 1
goto L15
@label L15_end
assignw S17[0] 5
assignw T255 1
sub T256 T30 T255
mult T257 1 T256
add T257 T257 4
assignb T258 10
assignw T259 2
assignw T261 T259
assignw T262 1
mult T262 T262 T261
add T262 T262 4
malloc T260 T262
assignw T260[0] T261
assignb T260[5] T258
assignb T263 T41[T257]
assignb T260[4] T263
param T264 0
assignw T264[0] S17
assignw T266 T260[0]
assignw T267 1
mult T267 T267 T266
add T267 T267 4
malloc T265 T267
memcpy T265 T260 T267
param T268 4
assignw T268[0] T265
assignb A0[0] 1
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T269 PRINT 6
goto L6
goto L6
@label B649
@label L16
assignw T270 4
eq test T29 T270
goif B654 test
goto B665
@label B654
assignw S18[0] 12
param T272 0
assignw T272[0] S18
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignb A0[4] 0
call T273 PRINT 6
goto B694
goto L6
@label B665
assignw S19[0] 16
assignb T275 10
assignb T276 10
assignw T277 2
assignw T279 T277
assignw T280 1
mult T280 T280 T279
add T280 T280 4
malloc T278 T280
assignw T278[0] T279
assignb T278[5] T276
assignb T278[4] T275
param T281 0
assignw T281[0] S19
assignb A0[0] 0
assignb A0[1] 0
assignb A0[2] 0
assignb A0[3] 0
assignw T283 T278[0]
assignw T284 1
mult T284 T284 T283
add T284 T284 4
malloc T282 T284
memcpy T282 T278 T284
param T285 20
assignw T285[0] T282
assignb A0[4] 1
call T286 PRINT 6
goto L6
@label B694
@function Function0 12
assignw T287 BASE[0]
assignw BASE[8] T287
assignw T288 BASE[4]
assignw BASE[0] T288
assignw T289 BASE[8]
assignw BASE[4] T289
@label Function0_end
assignw lastbase BASE
return 0
@endfunction 12
@function Function1 28
assignw T291 BASE[8]
assignw T292 BASE[4]
leq test T291 T292
goif B711 test
goto B714
@label B711
assignw lastbase BASE
return 0
goto B714
@label B714
assignw T293 BASE[4]
assignw BASE[12] T293
assignw T294 1
assignw T296 BASE[8]
sub T295 T296 T294
assignw BASE[16] T295
assignw T297 BASE[0]
assignw T298 BASE[8]
mult T299 4 T298
add T299 T299 4
assignw T300 T297[T299]
assignw BASE[20] T300
@label L17
goto B728
@label B728
@label L18
assignw T301 BASE[0]
assignw T302 BASE[12]
mult T303 4 T302
add T303 T303 4
assignw T304 T301[T303]
assignw T305 BASE[20]
lt test T304 T305
goif B738 test
goto B743
@label B738
assignw T306 1
assignw T308 BASE[12]
add T307 T308 T306
assignw BASE[12] T307
goto L18
@label B743
@label L19
assignw T309 BASE[0]
assignw T310 BASE[16]
mult T311 4 T310
add T311 T311 4
assignw T312 T309[T311]
assignw T313 BASE[20]
gt test T312 T313
goif B753 test
goto B758
@label B753
assignw T314 1
assignw T316 BASE[16]
sub T315 T316 T314
assignw BASE[16] T315
goto L19
@label B758
assignw T317 BASE[12]
assignw T318 BASE[16]
geq test T317 T318
goif B763 test
goto B765
@label B763
goto B785
goto B765
@label B765
assignw T319 BASE[0]
assignw T320 BASE[12]
mult T321 4 T320
add T321 T321 4
assignw T322 BASE[0]
assignw T323 BASE[16]
mult T324 4 T323
add T324 T324 4
assignw T325 T319[T321]
param T326 0
assignw T326[0] T325
assignw T327 T322[T324]
param T328 4
assignw T328[0] T327
call T329 Function0 2
assignw T330 lastbase[0]
assignw T319[T321] T330
assignw T331 lastbase[4]
assignw T322[T324] T331
goto L17
@label B785
assignw T332 BASE[0]
assignw T333 BASE[12]
mult T334 4 T333
add T334 T334 4
assignw T335 BASE[0]
assignw T336 BASE[8]
mult T337 4 T336
add T337 T337 4
assignw T338 T332[T334]
param T339 0
assignw T339[0] T338
assignw T340 T335[T337]
param T341 4
assignw T341[0] T340
call T342 Function0 2
assignw T343 lastbase[0]
assignw T332[T334] T343
assignw T344 lastbase[4]
assignw T335[T337] T344
assignw T346 BASE[0]
assignw T347 T346[0]
assignw T348 4
mult T348 T348 T347
add T348 T348 4
malloc T345 T348
memcpy T345 T346 T348
param T349 0
assignw T349[0] T345
assignw T350 BASE[4]
param T351 4
assignw T351[0] T350
assignw T352 BASE[16]
param T353 8
assignw T353[0] T352
call T354 Function1 3
assignw T355 1
assignw T357 BASE[12]
add T356 T357 T355
assignw T359 BASE[0]
assignw T360 T359[0]
assignw T361 4
mult T361 T361 T360
add T361 T361 4
malloc T358 T361
memcpy T358 T359 T361
param T362 0
assignw T362[0] T358
param T363 4
assignw T363[0] T356
assignw T364 BASE[8]
param T365 8
assignw T365[0] T364
call T366 Function1 3
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
assignw T368 BASE[8]
assignw T369 BASE[4]
leq test T368 T369
goif B859 test
goto B862
@label B859
assignw lastbase BASE
return 0
goto B862
@label B862
assignw T370 BASE[4]
assignw BASE[12] T370
assignw T371 1
assignw T373 BASE[8]
sub T372 T373 T371
assignw BASE[16] T372
assignw T374 BASE[0]
assignw T375 BASE[8]
mult T376 4 T375
add T376 T376 4
assignw f10 T374[T376]
assignw BASE[20] f10
@label L20
goto B876
@label B876
@label L21
assignw T377 BASE[0]
assignw T378 BASE[12]
mult T379 4 T378
add T379 T379 4
assignw f11 T377[T379]
assignw f12 BASE[20]
lt test f11 f12
goif B886 test
goto B891
@label B886
assignw T380 1
assignw T382 BASE[12]
add T381 T382 T380
assignw BASE[12] T381
goto L21
@label B891
@label L22
assignw T383 BASE[0]
assignw T384 BASE[16]
mult T385 4 T384
add T385 T385 4
assignw f13 T383[T385]
assignw f14 BASE[20]
gt test f13 f14
goif B901 test
goto B906
@label B901
assignw T386 1
assignw T388 BASE[16]
sub T387 T388 T386
assignw BASE[16] T387
goto L22
@label B906
assignw T389 BASE[12]
assignw T390 BASE[16]
geq test T389 T390
goif B911 test
goto B913
@label B911
goto B933
goto B913
@label B913
assignw T391 BASE[0]
assignw T392 BASE[12]
mult T393 4 T392
add T393 T393 4
assignw T394 BASE[0]
assignw T395 BASE[16]
mult T396 4 T395
add T396 T396 4
assignw f15 T391[T393]
param T397 0
assignw T397[0] f15
assignw f16 T394[T396]
param T398 4
assignw T398[0] f16
call T399 Function2 2
assignw f17 lastbase[0]
assignw T391[T393] f17
assignw f18 lastbase[4]
assignw T394[T396] f18
goto L20
@label B933
assignw T400 BASE[0]
assignw T401 BASE[12]
mult T402 4 T401
add T402 T402 4
assignw T403 BASE[0]
assignw T404 BASE[8]
mult T405 4 T404
add T405 T405 4
assignw f19 T400[T402]
param T406 0
assignw T406[0] f19
assignw f20 T403[T405]
param T407 4
assignw T407[0] f20
call T408 Function2 2
assignw f21 lastbase[0]
assignw T400[T402] f21
assignw f22 lastbase[4]
assignw T403[T405] f22
assignw T410 BASE[0]
assignw T411 T410[0]
assignw T412 4
mult T412 T412 T411
add T412 T412 4
malloc T409 T412
memcpy T409 T410 T412
param T413 0
assignw T413[0] T409
assignw T414 BASE[4]
param T415 4
assignw T415[0] T414
assignw T416 BASE[16]
param T417 8
assignw T417[0] T416
call T418 Function3 3
assignw T419 1
assignw T421 BASE[12]
add T420 T421 T419
assignw T423 BASE[0]
assignw T424 T423[0]
assignw T425 4
mult T425 T425 T424
add T425 T425 4
malloc T422 T425
memcpy T422 T423 T425
param T426 0
assignw T426[0] T422
param T427 4
assignw T427[0] T420
assignw T428 BASE[8]
param T429 8
assignw T429[0] T428
call T430 Function3 3
@label Function3_end
assignw lastbase BASE
return 0
@endfunction 28
@function Function4 3
assignb T431 BASE[0]
assignb BASE[2] T431
assignb T432 BASE[1]
assignb BASE[0] T432
assignb T433 BASE[2]
assignb BASE[1] T433
@label Function4_end
assignw lastbase BASE
return 0
@endfunction 3
@function Function5 22
assignw T435 BASE[8]
assignw T436 BASE[4]
leq test T435 T436
goif B1007 test
goto B1010
@label B1007
assignw lastbase BASE
return 0
goto B1010
@label B1010
assignw T437 BASE[4]
assignw BASE[12] T437
assignw T438 1
assignw T440 BASE[8]
sub T439 T440 T438
assignw BASE[16] T439
assignw T441 BASE[0]
assignw T442 BASE[8]
mult T443 1 T442
add T443 T443 4
assignb T444 T441[T443]
assignb BASE[20] T444
@label L23
goto B1024
@label B1024
@label L24
assignw T445 BASE[0]
assignw T446 BASE[12]
mult T447 1 T446
add T447 T447 4
assignw T448 T445[T447]
assignw T449 BASE[20]
lt test T448 T449
goif B1034 test
goto B1039
@label B1034
assignw T450 1
assignw T452 BASE[12]
add T451 T452 T450
assignw BASE[12] T451
goto L24
@label B1039
@label L25
assignw T453 BASE[0]
assignw T454 BASE[16]
mult T455 1 T454
add T455 T455 4
assignw T456 T453[T455]
assignw T457 BASE[20]
gt test T456 T457
goif B1049 test
goto B1054
@label B1049
assignw T458 1
assignw T460 BASE[16]
sub T459 T460 T458
assignw BASE[16] T459
goto L25
@label B1054
assignw T461 BASE[12]
assignw T462 BASE[16]
geq test T461 T462
goif B1059 test
goto B1061
@label B1059
goto B1081
goto B1061
@label B1061
assignw T463 BASE[0]
assignw T464 BASE[12]
mult T465 1 T464
add T465 T465 4
assignw T466 BASE[0]
assignw T467 BASE[16]
mult T468 1 T467
add T468 T468 4
assignb T469 T463[T465]
param T470 0
assignb T470[0] T469
assignb T471 T466[T468]
param T472 1
assignb T472[0] T471
call T473 Function4 2
assignb T474 lastbase[0]
assignb T463[T465] T474
assignb T475 lastbase[1]
assignb T466[T468] T475
goto L23
@label B1081
assignw T476 BASE[0]
assignw T477 BASE[12]
mult T478 1 T477
add T478 T478 4
assignw T479 BASE[0]
assignw T480 BASE[8]
mult T481 1 T480
add T481 T481 4
assignb T482 T476[T478]
param T483 0
assignb T483[0] T482
assignb T484 T479[T481]
param T485 1
assignb T485[0] T484
call T486 Function4 2
assignb T487 lastbase[0]
assignb T476[T478] T487
assignb T488 lastbase[1]
assignb T479[T481] T488
assignw T490 BASE[0]
assignw T491 T490[0]
assignw T492 1
mult T492 T492 T491
add T492 T492 4
malloc T489 T492
memcpy T489 T490 T492
param T493 0
assignw T493[0] T489
assignw T494 BASE[4]
param T495 4
assignw T495[0] T494
assignw T496 BASE[16]
param T497 8
assignw T497[0] T496
call T498 Function5 3
assignw T499 1
assignw T501 BASE[12]
add T500 T501 T499
assignw T503 BASE[0]
assignw T504 T503[0]
assignw T505 1
mult T505 T505 T504
add T505 T505 4
malloc T502 T505
memcpy T502 T503 T505
param T506 0
assignw T506[0] T502
param T507 4
assignw T507[0] T500
assignw T508 BASE[8]
param T509 8
assignw T509[0] T508
call T510 Function5 3
@label Function5_end
assignw lastbase BASE
return 0
@endfunction 22
