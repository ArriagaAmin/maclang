@staticv A0 1
@staticv A1 1
@staticv A2 1
@staticv A3 1
@staticv A4 1
@string S0 "Menu principal. Escoja una de las siguientes opciones: "
@string S1 "1. Insertar un valor en el arbol. "
@string S2 "2. Eliminar un valor del arbol. "
@string S3 "3. Buscar un valor en el arbol. "
@string S4 "4. Mostrar arbol. "
@string S5 "5. Salir. "
@string S6 "Indique el caracter a insertar: "
@string S7 "Indique el caracter a borrar: "
@string S8 "El caracter "
@string S9 " no se encuentra en el arbol."
@string S10 "Indique el caracter a buscar: "
@string S11 "El caracter "
@string S12 " no se encuentra en el arbol."
@string S13 "El caracter "
@string S14 " se encuentra "
@string S15 " veces en el arbol."
@string S16 "Hasta pronto!"
@string S17 "Opcion invalida"
@string S18 "    "
@string S19 "-"
assign T0 0
assign A0[0] T0
assign T1 A0
assign T2 10
assign A1[0] T2
assign T3 A1
assign T4 0
goto F0_out
@function F0 12
assign T5 0
assign base[8] T5
@label L0
mult T7 base[8] 1
@label L1
neq test base[0][T7] base[4]
goif B17 test
goto B21
@label B17
assign T8 1
add T9 base[8] T8
assign base[8] T9
goto L0
@label B21
return base[8]
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 12
assign T10 0
assign base[8] T10
@label L2
mult T12 base[8] 1
@label L3
assign T13 0
neq test base[0][T12] T13
goif B37 test
goto B47
@label B37
mult T15 base[8] 1
@label L4
mult T17 base[8] 1
eq test base[0][T15] base[4][T17]
goif B43 test
goto B47
@label B43
assign T18 1
add T19 base[8] T18
assign base[8] T19
goto L2
@label B47
mult T21 base[8] 1
mult T23 base[8] 1
gt test base[0][T21] base[4][T23]
goif B52 test
goto B55
@label B52
assign T24 1
return T24
goto F1_end
@label B55
mult T26 base[8] 1
mult T28 base[8] 1
gt test base[4][T26] base[0][T28]
goif B60 test
goto B64
@label B60
assign T29 1
minus T30 T29
return T30
goto F1_end
@label B64
assign T31 0
return T31
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 16
param base[4]
param T4
call T32 F0 2
assign T33 1
add T34 T32 T33
assign base[8] T34
assign T35 0
assign base[12] T35
@label L5
lt test base[12] base[8]
goif B84 test
goto F2_end
@label B84
mult T37 base[12] 1
mult T39 base[12] 1
assign base[0][T37] base[4][T39]
assign T40 1
add T41 base[12] T40
assign base[12] T41
goto L5
@label F2_end
assign lastbase base
@endfunction
@label F2_out
goto F3_out
@function F3 28
assign T42 0
assign T43 0
assign base[12] T42
assign base[16] T43
@label L6
lt test base[12] base[4]
goif B105 test
goto B131
@label B105
mult T45 base[12] 4
param base[0][T45]
param T4
call T46 F0 2
assign base[24] T46
assign T47 0
assign base[20] T47
@label L7
lt test base[20] base[24]
goif B116 test
goto B127
@label B116
mult T49 base[16] 1
mult T51 base[12] 4
mult T53 base[20] 1
assign base[8][T49] base[0][T51][T53]
assign T54 1
add T55 base[20] T54
assign base[20] T55
assign T56 1
add T57 base[16] T56
assign base[16] T57
goto L7
@label B127
assign T58 1
add T59 base[12] T58
assign base[12] T59
goto L6
@label B131
mult T61 base[16] 1
assign T62 0
assign base[8][T61] T62
@label F3_end
assign lastbase base
@endfunction
@label F3_out
goto F4_out
@function F4 29
assign T63 0
assign T64 0
assign T65 0
param base[0]
param T4
call T66 F0 2
assign base[12] T63
assign base[16] T64
assign base[20] T65
assign base[24] T66
goto B151
@label B151
assign base[28] True
goto Bool154
assign base[28] False
@label Bool154
@label L8
mult T68 base[12] 1
@label L9
assign T69 0
neq test base[0][T68] T69
goif B162 test
goto B210
@label B162
mult T71 base[12] 1
@label L10
eq test base[0][T71] base[8]
goif B167 test
goto B186
@label B167
goif B186 base[28]
goto B169
@label B169


goto B172
@label B172
assign base[28] True
goto Bool175
assign base[28] False
@label Bool175
mult T73 base[20] 4
mult T75 base[16] 1
assign T76 0
assign base[4][T73][T75] T76
assign T77 1
add T78 base[20] T77
assign base[20] T78
assign T79 0
assign base[16] T79
goto B206
@label B186
mult T81 base[12] 1
@label L11
neq test base[0][T81] base[8]
goif B191 test
goto B206
@label B191


goto B196
assign base[28] True
goto Bool197
@label B196
assign base[28] False
@label Bool197
mult T83 base[20] 4
mult T85 base[16] 1
mult T87 base[12] 1
assign base[4][T83][T85] base[0][T87]
assign T88 1
add T89 base[16] T88
assign base[16] T89
goto B206
@label B206
assign T90 1
add T91 base[12] T90
assign base[12] T91
goto L8
@label B210
goif B220 base[28]
goto B212
@label B212
mult T93 base[20] 4
mult T95 base[16] 1
assign T96 0
assign base[4][T93][T95] T96
assign T97 1
add T98 base[20] T97
assign base[20] T98
goto B220
@label B220
return base[20]
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 22
goto B231
goto B235
assign base[4] True
goto Bool232
@label B231
assign base[4] False
@label Bool232
assign base[5] True
goto Bool236
@label B235
assign base[5] False
@label Bool236
param base[0]
param T4
call T99 F0 2
assign T100 0
assign base[10] T99
assign base[18] T100
@label L12
lt test base[18] base[10]
goif B247 test
goto B309
@label B247
mult T102 base[18] 1
@label L13
assign T103 46
eq test base[0][T102] T103
goif B253 test
goto B263
@label B253
goif B263 base[4]
goto B255
@label B255


goto B258
@label B258
assign base[4] True
goto Bool261
assign base[4] False
@label Bool261
goto B305
@label B263
mult T105 base[18] 1
@label L14
assign T106 46
eq test base[0][T105] T106
goif B269 test
goto B276
@label B269
goto B272
assign T107 True
goto Bool273
@label B272
assign T107 False
@label Bool273
return T107
goto B305
@label B276
mult T109 base[18] 1
assign T110 48
lt test base[0][T109] T110
goif B286 test
goto B281
@label B281
mult T112 base[18] 1
assign T113 57
gt test base[0][T112] T113
goif B286 test
goto B293
@label B286
goto B289
assign T114 True
goto Bool290
@label B289
assign T114 False
@label Bool290
return T114
goto B305
@label B293
goif B295 base[4]
goto B305
@label B295
goif B305 base[5]
goto B297
@label B297


goto B300
@label B300
assign base[5] True
goto Bool303
assign base[5] False
@label Bool303
goto B305
@label B305
assign T115 1
add T116 base[18] T115
assign base[18] T116
goto L12
@label B309
goif B311 base[4]
goto B315
@label B311
goif B313 base[5]
goto B315
@label B313
assign T117 True
goto Bool316
@label B315
assign T117 False
@label Bool316
return T117
@label F5_end
assign lastbase base
@endfunction
@label F5_out
assign T118 2
assign T119 0
malloc T120 30
assign T121 T120
assign T122 0
assign T121[0][0] T122
assign T123 512
assign T124 T123
assign T126 1
mult T126 T126 T124
malloc T125 T126
call T128 F13 0
assign T129 T128
@label L15
goto B337
@label B337
param S0
call T131 PRINT 1
param T3
call T132 PRINT 1
param S1
call T133 PRINT 1
param T3
call T134 PRINT 1
param S2
call T135 PRINT 1
param T3
call T136 PRINT 1
param S3
call T137 PRINT 1
param T3
call T138 PRINT 1
param S4
call T139 PRINT 1
param T3
call T140 PRINT 1
param S5
call T141 PRINT 1
param T3
call T142 PRINT 1
param T125
call T143 READ 1
param T125
call T144 STOI 1
assign T127 T144
@label L16
assign T145 1
eq test T127 T145
goif B371 test
goto B381
@label B371
param S6
call T146 PRINT 1
param T125
call T147 READ 1
assign T148 0
mult T150 T148 1
param T129
param T125[T150]
call T151 F21 2
goto L15
@label B381
@label L17
assign T152 2
eq test T127 T152
goif B386 test
goto B410
@label B386
param S7
call T153 PRINT 1
param T125
call T154 READ 1
assign T155 0
mult T157 T155 1
param T129
param T125[T157]
call T158 F22 2
goif L15 T158
goto B397
@label B397
param S8
call T159 PRINT 1
assign T160 0
mult T162 T160 1
assign A2[0] T125[T162]
param A2
call T163 PRINT 1
param S9
call T164 PRINT 1
param T3
call T165 PRINT 1
goto L15
goto L15
@label B410
@label L18
assign T166 3
eq test T127 T166
goif B415 test
goto B461
@label B415
param S10
call T167 PRINT 1
param T125
call T168 READ 1
assign T169 0
mult T171 T169 1
param T129
param T125[T171]
call T172 F20 2
assign T130 T172
param T130
param T121
call T173 F8 2
goif B430 T173
goto B442
@label B430
param S11
call T174 PRINT 1
assign T175 0
mult T177 T175 1
assign A3[0] T125[T177]
param A3
call T178 PRINT 1
param S12
call T179 PRINT 1
param T3
call T180 PRINT 1
goto L15
@label B442
param S13
call T181 PRINT 1
assign T182 0
mult T184 T182 1
assign A4[0] T125[T184]
param A4
call T185 PRINT 1
param S14
call T186 PRINT 1
param T125
param T130[0][26]
call T187 ITOS 2
param T125
call T188 PRINT 1
param S15
call T189 PRINT 1
param T3
call T190 PRINT 1
goto L15
@label B461
@label L19
assign T191 4
eq test T127 T191
goif B466 test
goto B469
@label B466
param T129
call T192 F23 1
goto L15
@label B469
@label L20
assign T193 5
eq test T127 T193
goif B474 test
goto B482
@label B474
param S16
call T194 PRINT 1
param T3
call T195 PRINT 1
param T129
call T196 F14 1
goto B487
goto L15
@label B482
param S17
call T197 PRINT 1
param T3
call T198 PRINT 1
goto L15
@label B487
goto F6_out
@function F6 12
malloc T199 30
assign base[8] T199
assign base[8][0][18] base[0]
assign base[8][0][0] base[4]
assign T200 1
assign base[8][0][26] T200
assign T201 0
mult T203 T201 4
assign base[8][0][6][T203] base[56]
assign T204 1
mult T206 T204 4
assign base[8][0][6][T206] base[56]


goto B504
@label B504
assign base[8][0][1] True
goto Bool507
assign base[8][0][1] False
@label Bool507
return base[8]
@label F6_end
assign lastbase base
@endfunction
@label F6_out
goto F7_out
@function F7 4
free base[0]
@label F7_end
assign lastbase base
@endfunction
@label F7_out
goto F8_out
@function F8 8
@label L21
eq test base[0][0][0] base[4][0][0]
goif B526 test
goto B528
@label B526
assign T207 True
goto Bool529
@label B528
assign T207 False
@label Bool529
return T207
@label F8_end
assign lastbase base
@endfunction
@label F8_out
goto F9_out
@function F9 4
param base[0]
param base[56]
call T208 F8 2
goif B542 T208
goto B544
@label B542
return 0
goto B544
@label B544
assign T209 0
mult T211 T209 4
param base[0][0][6][T211]
param base[56]
call T212 F8 2
goif B556 T212
goto B551
@label B551
assign T213 0
mult T215 T213 4
param base[0][0][6][T215]
call T216 F9 1
goto B556
@label B556
assign T217 1
mult T219 T217 4
param base[0][0][6][T219]
param base[56]
call T220 F8 2
goif B568 T220
goto B563
@label B563
assign T221 1
mult T223 T221 4
param base[0][0][6][T223]
call T224 F9 1
goto B568
@label B568
free base[0]
@label F9_end
assign lastbase base
@endfunction
@label F9_out
goto F10_out
@function F10 4
assign T225 0
mult T227 T225 4
param base[0][0][6][T227]
param base[56]
call T228 F8 2
goif B582 T228
goto B584
@label B582
return base[0]
goto B584
@label B584
assign T229 0
mult T231 T229 4
param base[0][0][6][T231]
call T232 F10 1
return T232
@label F10_end
assign lastbase base
@endfunction
@label F10_out
goto F11_out
@function F11 8
assign T233 0
mult T235 T233 4
param base[0][0][6][T235]
param base[56]
call T236 F8 2
goif B602 T236
goto B610
@label B602
assign T237 1
mult T239 T237 4
assign base[4] base[0][0][6][T239]
assign T240 1
mult T242 T240 4
assign base[0][0][6][T242] base[56]
return base[4]
goto B610
@label B610
assign T243 0
mult T245 T243 4
assign T246 0
mult T248 T246 4
param base[0][0][6][T248]
call T249 F11 1
assign base[0][0][6][T245] T249
return base[0]
@label F11_end
assign lastbase base
@endfunction
@label F11_out
goto F12_out
@function F12 52
assign T250 0
assign base[8] T250
assign T251 32
assign T252 1
mult T252 T252 T251
malloc base[12] T252
@label L22
lt test base[8] base[4]
goif B634 test
goto B637
@label B634
param S18
call T253 PRINT 1
goto L22
@label B637
param base[0]
param base[56]
call T254 F8 2
goif B642 T254
goto B647
@label B642
param S19
call T255 PRINT 1
param base[12]
call T256 PRINT 1
goto F12_end
@label B647
assign T257 40
assign T258 44
assign T259 32
assign T260 1
mult T260 T260 
malloc base[44] T260
assign base[44][3] T259
assign base[44][2] T258
assign base[44][1] base[0][0][0]
assign base[44][0] T257
param base[44]
call T261 PRINT 1
param base[12]
call T262 STOI 1
param base[12]
call T263 PRINT 1
assign T264 41
assign T265 10
assign T266 1
mult T266 T266 
malloc base[48] T266
assign base[48][1] T265
assign base[48][0] T264
param base[48]
call T267 PRINT 1
assign T268 0
mult T270 T268 4
assign T271 1
add T272 base[4] T271
param base[0][0][6][T270]
param T272
call T273 F12 2
assign T274 1
mult T276 T274 4
assign T277 1
add T278 base[4] T277
param base[0][0][6][T276]
param T278
call T279 F12 2
@label F12_end
assign lastbase base
@endfunction
@label F12_out
goto F13_out
@function F13 4
malloc T280 4
assign base[0] T280
assign base[0][0][0] base[56]
return base[0]
@label F13_end
assign lastbase base
@endfunction
@label F13_out
goto F14_out
@function F14 4
param base[0][0][0]
call T281 F9 1
free base[0]
@label F14_end
assign lastbase base
@endfunction
@label F14_out
goto F15_out
@function F15 24
assign T282 1
sub T283 T282 base[8]
mult T285 T283 4
assign base[12] base[4][0][18]
assign base[16] base[4][0][6][T285]
mult T287 base[8] 4
assign base[20] base[16][0][6][T287]
assign T288 1
sub T289 T288 base[8]
mult T291 T289 4
assign base[4][0][6][T291] base[20]
param base[20]
param base[56]
call T292 F8 2
goif B729 T292
goto B727
@label B727
assign base[20][0][18] base[4]
goto B729
@label B729
mult T294 base[8] 4
assign base[16][0][6][T294] base[4]
assign base[4][0][18] base[16]
assign base[16][0][18] base[12]
param base[12]
param base[56]
call T295 F8 2
goif B753 T295
goto B738
@label B738
assign T296 1
mult T298 T296 4
param base[4]
param base[12][0][6][T298]
call T299 F8 2
goif B745 T299
goto B749
@label B745
assign T300 1
mult T302 T300 4
assign base[12][0][6][T302] base[16]
goto B754
@label B749
assign T303 0
mult T305 T303 4
assign base[12][0][6][T305] base[16]
goto B754
@label B753
assign base[0][0][0] base[16]
@label B754
return base[16]
@label F15_end
assign lastbase base
@endfunction
@label F15_out
goto F16_out
@function F16 8
assign T306 0
param base[0]
param base[4]
param T306
call T307 F15 3
return T307
@label F16_end
assign lastbase base
@endfunction
@label F16_out
goto F17_out
@function F17 8
assign T308 1
param base[0]
param base[4]
param T308
call T309 F15 3
return T309
@label F17_end
assign lastbase base
@endfunction
@label F17_out
goto F18_out
@function F18 13
param base[0][0][0]
param base[56]
call T310 F8 2
goif B790 T310
goto B796
@label B790
param base[56]
param base[4]
call T311 F6 2
assign base[0][0][0] T311
return base[0][0][0]
goto B796
@label B796
assign base[8] base[0][0][0]
goto B798
@label B798
assign base[12] True
goto Bool801
assign base[12] False
@label Bool801
@label L23
@label L24
neq test base[8][0][0] base[4]
goif B807 test
goto B853
@label B807
lt test base[8][0][0] base[4]
goif B810 test
goto B821
@label B810
assign T312 1
mult T314 T312 4
param base[8][0][6][T314]
param base[56]
call T315 F8 2
goif B821 T315
goto B817
@label B817
assign T316 1
mult T318 T316 4
assign base[8] base[8][0][6][T318]
goto L23
@label B821
lt test base[8][0][0] base[4]
goif B824 test
goto B833
@label B824


goto B829
assign base[12] True
goto Bool830
@label B829
assign base[12] False
@label Bool830
goto B853
goto L23
@label B833
assign T319 0
mult T321 T319 4
param base[8][0][6][T321]
param base[56]
call T322 F8 2
goif B844 T322
goto B840
@label B840
assign T323 0
mult T325 T323 4
assign base[8] base[8][0][6][T325]
goto L23
@label B844


goto B849
assign base[12] True
goto Bool850
@label B849
assign base[12] False
@label Bool850
goto B853
goto L23
@label B853
goif B855 base[12]
goto B860
@label B855
assign T326 1
add T327 base[8][0][26] T326
assign base[8][0][26] T327
return base[8]
goto F18_end
@label B860
lt test base[8][0][0] base[4]
goif B863 test
goto B873
@label B863
assign T328 1
mult T330 T328 4
param base[8]
param base[4]
call T331 F6 2
assign base[8][0][6][T330] T331
assign T332 1
mult T334 T332 4
return base[8][0][6][T334]
goto F18_end
@label B873
assign T335 0
mult T337 T335 4
param base[8]
param base[4]
call T338 F6 2
assign base[8][0][6][T337] T338
assign T339 0
mult T341 T339 4
return base[8][0][6][T341]
@label F18_end
assign lastbase base
@endfunction
@label F18_out
goto F19_out
@function F19 12
param base[0]
param base[56]
call T342 F8 2
goif B893 T342
goto B895
@label B893
return base[56]
goto B895
@label B895
lt test base[4] base[0][0][0]
goif B898 test
goto B908
@label B898
assign T343 0
mult T345 T343 4
assign T346 0
mult T348 T346 4
param base[0][0][6][T348]
param base[4]
call T349 F19 2
assign base[0][0][6][T345] T349
return base[0]
goto F19_end
@label B908
gt test base[4] base[0][0][0]
goif B911 test
goto B921
@label B911
assign T350 1
mult T352 T350 4
assign T353 1
mult T355 T353 4
param base[0][0][6][T355]
param base[4]
call T356 F19 2
assign base[0][0][6][T352] T356
return base[0]
goto F19_end
@label B921
assign T357 0
mult T359 T357 4
param base[0][0][6][T359]
param base[56]
call T360 F8 2
goif B928 T360
goto B938
@label B928
assign T361 1
mult T363 T361 4
assign base[8] base[0][0][6][T363]
assign T364 1
mult T366 T364 4
assign base[0][0][6][T366] base[56]
param base[0]
call T367 F7 1
return base[8]
goto B938
@label B938
assign T368 1
mult T370 T368 4
param base[0][0][6][T370]
param base[56]
call T371 F8 2
goif B945 T371
goto B955
@label B945
assign T372 0
mult T374 T372 4
assign base[8] base[0][0][6][T374]
assign T375 0
mult T377 T375 4
assign base[0][0][6][T377] base[56]
param base[0]
call T378 F7 1
return base[8]
goto B955
@label B955
assign T379 1
mult T381 T379 4
param base[0][0][6][T381]
call T382 F10 1
assign base[8] T382
assign T383 1
mult T385 T383 4
assign T386 1
mult T388 T386 4
param base[0][0][6][T388]
call T389 F11 1
assign base[8][0][6][T385] T389
assign T390 0
mult T392 T390 4
assign T393 0
mult T395 T393 4
assign base[8][0][6][T392] base[0][0][6][T395]
param base[0]
call T396 F7 1
return base[8]
@label F19_end
assign lastbase base
@endfunction
@label F19_out
goto F20_out
@function F20 12
param base[0][0][0]
param base[56]
call T397 F8 2
goif B986 T397
goto B988
@label B986
return base[56]
goto B988
@label B988
assign base[8] base[0][0][0]
@label L25
@label L26
neq test base[8][0][0] base[4]
goif B994 test
goto B1010
@label B994
param base[8]
param base[56]
call T398 F8 2
goif B1010 T398
goto B999
@label B999
lt test base[8][0][0] base[4]
goif B1002 test
goto B1006
@label B1002
assign T399 1
mult T401 T399 4
assign base[8] base[8][0][6][T401]
goto L25
@label B1006
assign T402 0
mult T404 T402 4
assign base[8] base[8][0][6][T404]
goto L25
@label B1010
return base[8]
@label F20_end
assign lastbase base
@endfunction
@label F20_out
goto F21_out
@function F21 16
param base[0]
param base[4]
call T405 F18 2
assign base[8] T405
@label L27
assign T406 1
eq test base[8][0][26] T406
goif B1026 test
goto B1028
@label B1026
return 0
goto B1028
@label B1028
@label L28
param base[8]
param base[0][0][0]
call T407 F8 2
goif B1159 T407
goto B1034
@label B1034
goif B1036 base[8][0][18][0][1]
goto B1159
@label B1036
assign T408 0
mult T410 T408 4
param base[8][0][18]
param base[8][0][18][0][18][0][6][T410]
call T411 F8 2
goif B1043 T411
goto B1101
@label B1043
assign T412 1
mult T414 T412 4
assign base[12] base[8][0][18][0][18][0][6][T414]
goif B1048 base[12][0][1]
goto B1071
@label B1048


goto B1053
assign base[8][0][18][0][1] True
goto Bool1054
@label B1053
assign base[8][0][18][0][1] False
@label Bool1054


goto B1060
assign base[12][0][1] True
goto Bool1061
@label B1060
assign base[12][0][1] False
@label Bool1061


goto B1065
@label B1065
assign base[8][0][18][0][18][0][1] True
goto Bool1068
assign base[8][0][18][0][18][0][1] False
@label Bool1068
assign base[8] base[8][0][18][0][18]
goto L28
@label B1071
assign T415 1
mult T417 T415 4
param base[8]
param base[8][0][18][0][6][T417]
call T418 F8 2
goif B1078 T418
goto B1083
@label B1078
assign base[8] base[8][0][18]
param base[0]
param base[8]
call T419 F16 2
goto B1083
@label B1083


goto B1088
assign base[8][0][18][0][1] True
goto Bool1089
@label B1088
assign base[8][0][18][0][1] False
@label Bool1089


goto B1093
@label B1093
assign base[8][0][18][0][18][0][1] True
goto Bool1096
assign base[8][0][18][0][18][0][1] False
@label Bool1096
param base[0]
param base[8][0][18][0][18]
call T420 F17 2
goto L28
@label B1101
assign T421 0
mult T423 T421 4
assign base[12] base[8][0][18][0][18][0][6][T423]
goif B1106 base[12][0][1]
goto B1129
@label B1106


goto B1111
assign base[8][0][18][0][1] True
goto Bool1112
@label B1111
assign base[8][0][18][0][1] False
@label Bool1112


goto B1118
assign base[12][0][1] True
goto Bool1119
@label B1118
assign base[12][0][1] False
@label Bool1119


goto B1123
@label B1123
assign base[8][0][18][0][18][0][1] True
goto Bool1126
assign base[8][0][18][0][18][0][1] False
@label Bool1126
assign base[8] base[8][0][18][0][18]
goto L28
@label B1129
assign T424 0
mult T426 T424 4
param base[8]
param base[8][0][18][0][6][T426]
call T427 F8 2
goif B1136 T427
goto B1141
@label B1136
assign base[8] base[8][0][18]
param base[0]
param base[8]
call T428 F17 2
goto B1141
@label B1141


goto B1146
assign base[8][0][18][0][1] True
goto Bool1147
@label B1146
assign base[8][0][18][0][1] False
@label Bool1147


goto B1151
@label B1151
assign base[8][0][18][0][18][0][1] True
goto Bool1154
assign base[8][0][18][0][18][0][1] False
@label Bool1154
param base[0]
param base[8][0][18][0][18]
call T429 F16 2
goto L28
@label B1159


goto B1164
assign base[0][0][0][0][1] True
goto Bool1165
@label B1164
assign base[0][0][0][0][1] False
@label Bool1165
@label F21_end
assign lastbase base
@endfunction
@label F21_out
goto F22_out
@function F22 12
param base[0]
param base[4]
call T430 F20 2
assign base[8] T430
param base[8]
param base[56]
call T431 F8 2
goif B1181 T431
goto B1188
@label B1181
goto B1184
assign T432 True
goto Bool1185
@label B1184
assign T432 False
@label Bool1185
return T432
goto B1188
@label B1188
assign T433 1
gt test base[8][0][26] T433
goif B1192 test
goto B1202
@label B1192
assign T434 1
sub T435 base[8][0][26] T434
assign base[8][0][26] T435
goto B1196
@label B1196
assign T436 True
goto Bool1199
assign T436 False
@label Bool1199
return T436
goto B1202
@label B1202
param base[0][0][0]
param base[4]
call T437 F19 2
assign base[0][0][0] T437
@label F22_end
assign lastbase base
@endfunction
@label F22_out
goto F23_out
@function F23 4
assign T438 0
param base[0][0][0]
param T438
call T439 F12 2
@label F23_end
assign lastbase base
@endfunction
@label F23_out
free T125
