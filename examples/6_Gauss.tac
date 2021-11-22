@staticv A0 1       # Arreglo ['\0']
@staticv A1 1       # Arreglo ['\n']
@staticv A2 110     # M
@string S0 "Desea resolver un sistema de ecuaciones? [Y/n] "
@string S1 "n"
@string S2 "N"
@string S3 "Hasta luego!"
@string S4 "Indique el numero de ecuaciones. Debe ser entre 1 y 10: "
@string S5 "Indique los "
@string S6 " coeficientes flotantes de la "
@string S7 "-esima ecuacion: "
@string S8 "El valor de las variables es: "
@string S9 "X"
@string S10 " = "
@string S11 "El sistema de ecuaciones no tiene solucion."
# Asignacion de STRNUL
assign T0 0
assign A0[0] T0
#declared T1 STRNUL
assign T1 A0
# Asignacion de nl
assign T2 10
assign A1[0] T2
#declared T3 nl
assign T3 A1
assign T4 0
# Declaracion funcion strlen
goto F0_out
@function F0 3
# Asignacion i = 0
assign T5 0
#declared base[2] i
assign base[2] T5
@label L0
mult T7 base[2] 1
@label L1
neq test base[0][T7] base[1]
goif B20 test
goto B24
@label B20
assign T8 1
add T9 base[2] T8
assign base[2] T9
goto L0
@label B24
return base[2]
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 3
assign T10 0
#declared base[2] i
assign base[2] T10
@label L2
mult T12 base[2] 1
@label L3
assign T13 0
neq test base[0][T12] T13
goif B41 test
goto B51
@label B41
mult T15 base[2] 1
@label L4
mult T17 base[2] 1
eq test base[0][T15] base[1][T17]
goif B47 test
goto B51
@label B47
assign T18 1
add T19 base[2] T18
assign base[2] T19
goto L2
@label B51
mult T21 base[2] 1
mult T23 base[2] 1
gt test base[0][T21] base[1][T23]
goif B56 test
goto B59
@label B56
assign T24 1
return T24
goto F1_end
@label B59
mult T26 base[2] 1
mult T28 base[2] 1
gt test base[1][T26] base[0][T28]
goif B64 test
goto B68
@label B64
assign T29 1
minus T30 T29
return T30
goto F1_end
@label B68
assign T31 0
return T31
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 4
param base[1]
param T4
call T32 F0 2
assign T33 1
add T34 T32 T33
#declared base[2] n
assign base[2] T34
assign T35 0
#declared base[3] i
assign base[3] T35
@label L5
lt test base[3] base[2]
goif B90 test
goto F2_end
@label B90
mult T37 base[3] 1
mult T39 base[3] 1
assign base[0][T37] base[1][T39]
assign T40 1
add T41 base[3] T40
assign base[3] T41
goto L5
@label F2_end
assign lastbase base
@endfunction
@label F2_out
assign T42 1
goto F3_out
@function F3 7
assign T43 0
assign T44 0
#declared base[3] i
assign base[3] T43
#declared base[4] j
assign base[4] T44
#declared base[5] k
#declared base[6] n
@label L6
lt test base[3] base[1]
goif B116 test
goto B142
@label B116
mult T46 base[3] 1
param base[0][T46]
param T4
call T47 F0 2
assign base[6] T47
assign T48 0
assign base[5] T48
@label L7
lt test base[5] base[6]
goif B127 test
goto B138
@label B127
mult T50 base[4] 1
mult T52 base[3] 1
mult T54 base[5] 1
assign base[2][T50] base[0][T52][T54]
assign T55 1
add T56 base[5] T55
assign base[5] T56
assign T57 1
add T58 base[4] T57
assign base[4] T58
goto L7
@label B138
assign T59 1
add T60 base[3] T59
assign base[3] T60
goto L6
@label B142
mult T62 base[4] 1
assign T63 0
assign base[2][T62] T63
@label F3_end
assign lastbase base
@endfunction
@label F3_out
assign T64 1
goto F4_out
@function F4 8
assign T65 0
assign T66 0
assign T67 0
param base[0]
param T4
call T68 F0 2
#declared base[3] i
assign base[3] T65
#declared base[4] j
assign base[4] T66
#declared base[5] t
assign base[5] T67
#declared base[6] N
assign base[6] T68
goto B168
#declared base[7] sep
@label B168
assign base[7] True
goto Bool171
assign base[7] False
@label Bool171
@label L8
mult T70 base[3] 1
@label L9
assign T71 0
neq test base[0][T70] T71
goif B179 test
goto B227
@label B179
mult T73 base[3] 1
@label L10
eq test base[0][T73] base[2]
goif B184 test
goto B203
@label B184
goif B203 base[7]
goto B186
@label B186


goto B189
@label B189
assign base[7] True
goto Bool192
assign base[7] False
@label Bool192
mult T75 base[5] 1
mult T77 base[4] 1
assign T78 0
assign base[1][T75][T77] T78
assign T79 1
add T80 base[5] T79
assign base[5] T80
assign T81 0
assign base[4] T81
goto B223
@label B203
mult T83 base[3] 1
@label L11
neq test base[0][T83] base[2]
goif B208 test
goto B223
@label B208


goto B213
assign base[7] True
goto Bool214
@label B213
assign base[7] False
@label Bool214
mult T85 base[5] 1
mult T87 base[4] 1
mult T89 base[3] 1
assign base[1][T85][T87] base[0][T89]
assign T90 1
add T91 base[4] T90
assign base[4] T91
goto B223
@label B223
assign T92 1
add T93 base[3] T92
assign base[3] T93
goto L8
@label B227
goif B237 base[7]
goto B229
@label B229
mult T95 base[5] 1
mult T97 base[4] 1
assign T98 0
assign base[1][T95][T97] T98
assign T99 1
add T100 base[5] T99
assign base[5] T100
goto B237
@label B237
return base[5]
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 5
goto B249
goto B254
#declared base[1] dot
assign base[1] True
goto Bool250
@label B249
assign base[1] False
@label Bool250
#declared base[2] decimal
assign base[2] True
goto Bool255
@label B254
assign base[2] False
@label Bool255
param base[0]
param T4
call T101 F0 2
assign T102 0
#declared base[3] N
assign base[3] T101
#declared base[4] i
assign base[4] T102
@label L12
lt test base[4] base[3]
goif B268 test
goto B330
@label B268
mult T104 base[4] 1
@label L13
assign T105 46
eq test base[0][T104] T105
goif B274 test
goto B284
@label B274
goif B284 base[1]
goto B276
@label B276


goto B279
@label B279
assign base[1] True
goto Bool282
assign base[1] False
@label Bool282
goto B326
@label B284
mult T107 base[4] 1
@label L14
assign T108 46
eq test base[0][T107] T108
goif B290 test
goto B297
@label B290
goto B293
assign T109 True
goto Bool294
@label B293
assign T109 False
@label Bool294
return T109
goto B326
@label B297
mult T111 base[4] 1
assign T112 48
lt test base[0][T111] T112
goif B307 test
goto B302
@label B302
mult T114 base[4] 1
assign T115 57
gt test base[0][T114] T115
goif B307 test
goto B314
@label B307
goto B310
assign T116 True
goto Bool311
@label B310
assign T116 False
@label Bool311
return T116
goto B326
@label B314
goif B316 base[1]
goto B326
@label B316
goif B326 base[2]
goto B318
@label B318


goto B321
@label B321
assign base[2] True
goto Bool324
assign base[2] False
@label Bool324
goto B326
@label B326
assign T117 1
add T118 base[4] T117
assign base[4] T118
goto L12
@label B330
goif B332 base[1]
goto B336
@label B332
goif B334 base[2]
goto B336
@label B334
assign T119 True
goto Bool337
@label B336
assign T119 False
@label Bool337
return T119
@label F5_end
assign lastbase base
@endfunction
@label F5_out

# Inicio del Gauss
assign T120 1
assign T121 1
assign T122 1024
#declared T123 LINE_SIZE
assign T123 T122
assign T124 10
assign T125 11
#declared A2 M
#declared T126 N
#declared T127 i
#declared T128 j
assign T130 1
mult T130 T130 T123
malloc T129 T130
#declared T129 buffer
@label L15
goto B360
@label B360
param S0
call T131 PRINT 1
param T129
call T132 READ 1
param T129
param S1
call T133 F1 2
@label L16
assign T134 0
eq test T133 T134
goif B380 test
goto B372
@label B372
param T129
param S2
call T135 F1 2
@label L17
assign T136 0
eq test T135 T136
goif B380 test
goto B383
@label B380
param S3
call T137 PRINT 1
goto B383
@label B383
param S4
call T138 PRINT 1
param T129
call T139 READ 1
param T129
call T140 STOI 1
assign T126 T140
assign T141 0
assign T127 T141
@label L18
lt test T127 T126
goif B396 test
goto B440
@label B396
param S5
call T142 PRINT 1
assign T143 1
add T144 T126 T143
param T129
param T144
call T145 ITOS 2
param T129
call T146 PRINT 1
param S6
call T147 PRINT 1
param T129
param T127
call T148 ITOS 2
param T129
call T149 PRINT 1
param S7
call T150 PRINT 1
param T3
call T151 PRINT 1
assign T152 0
assign T128 T152
@label L19
assign T153 1
add T154 T126 T153
lt test T128 T154
goif B424 test
goto B436
@label B424
param T129
call T155 READ 1
mult T156 T127 10
add T157 A2 T156
mult T159 T128 1
param T129
call T160 STOF 1
assign T157[T159] T160
assign T161 1
add T162 T128 T161
assign T128 T162
goto L19
@label B436
assign T163 1
add T164 T127 T163
assign T127 T164
goto L18
@label B440
param A2
param T126
call T165 F9 2
goif B445 T165
goto B478
@label B445
param S8
call T166 PRINT 1
param T3
call T167 PRINT 1
assign T168 0
assign T127 T168
@label L20
lt test T127 T126
goif B455 test
goto B475
@label B455
param S9
call T169 PRINT 1
param T129
param T127
call T170 ITOS 2
param T129
call T171 PRINT 1
param S10
call T172 PRINT 1
mult T173 T127 10
add T174 A2 T173
mult T176 T126 1
param T129
param T174[T176]
call T177 FTOS 2
param T129
call T178 PRINT 1
param T3
call T179 PRINT 1
goto L20
@label B475
param T3
call T180 PRINT 1
goto L15
@label B478
param S11
call T181 PRINT 1
param T3
call T182 PRINT 1
goto L15
goto F6_out
@function F6 1
assign T183 0
lt test base[0] T183
goif B489 test
goto B492
@label B489
minus T184 base[0]
return T184
goto F6_end
@label B492
return base[0]
@label F6_end
assign lastbase base
@endfunction
@label F6_out
assign T185 1
assign T186 1
goto F7_out
@function F7 6
assign T187 0
mult T188 T187 1
add T189 base[0] T188
mult T191 base[2] 1
param T189[T191]
call T192 F6 1
#declared base[3] max
assign base[3] T192
assign T193 1
assign T194 0
#declared base[4] i
assign base[4] T193
#declared base[5] i_max
assign base[5] T194
@label L21
lt test base[4] base[1]
goif B519 test
goto B536
@label B519
mult T195 base[4] 1
add T196 base[0] T195
mult T198 base[2] 1
param T196[T198]
call T199 F6 1
gt test T199 base[3]
goif B527 test
goto L21
@label B527
mult T200 base[4] 1
add T201 base[0] T200
mult T203 base[2] 1
param T201[T203]
call T204 F6 1
assign base[3] T204
assign base[5] base[4]
goto L21
goto L21
@label B536
return base[5]
@label F7_end
assign lastbase base
@endfunction
@label F7_out
assign T205 1
assign T206 1
goto F8_out
@function F8 6
#declared base[4] aux
assign T207 0
#declared base[5] i
assign base[5] T207
@label L22
lt test base[5] base[1]
goif B553 test
goto F8_end
@label B553
mult T208 base[2] 1
add T209 base[0] T208
mult T211 base[5] 1
assign base[4] T209[T211]
mult T212 base[2] 1
add T213 base[0] T212
mult T215 base[5] 1
mult T216 base[3] 1
add T217 base[0] T216
mult T219 base[5] 1
assign T213[T215] T217[T219]
mult T220 base[3] 1
add T221 base[0] T220
mult T223 base[5] 1
assign T221[T223] base[4]
goto L22
@label F8_end
assign lastbase base
@endfunction
@label F8_out
assign T224 1
assign T225 1
goto F9_out
@function F9 7
assign T226 0
#declared base[2] h
assign base[2] T226
#declared base[3] i_max
#declared base[4] i
#declared base[5] j
#declared base[6] f
@label L23
lt test base[2] base[1]
goif B588 test
goto B663
@label B588
param base[0]
param base[1]
param base[2]
call T227 F7 3
assign base[3] T227
mult T228 base[3] 1
add T229 base[0] T228
mult T231 base[2] 1
@label L24
assign T232 0
eq test T229[T231] T232
goif B601 test
goto B608
@label B601
goto B604
assign T233 True
goto Bool605
@label B604
assign T233 False
@label Bool605
return T233
goto B608
@label B608
assign T234 1
add T235 base[1] T234
param base[0]
param T235
param base[2]
param base[3]
call T236 F8 4
assign T237 1
add T238 base[2] T237
assign base[4] T238
@label L25
lt test base[4] base[1]
goif B622 test
goto B659
@label B622
mult T239 base[4] 1
add T240 base[0] T239
mult T242 base[2] 1
mult T243 base[2] 1
add T244 base[0] T243
mult T246 base[2] 1
div T247 T240[T242] T244[T246]
assign base[6] T247
assign T248 1
add T249 base[2] T248
assign base[5] T249
@label L26
assign T250 1
add T251 base[1] T250
lt test base[5] T251
goif B639 test
goto B655
@label B639
mult T252 base[4] 1
add T253 base[0] T252
mult T255 base[5] 1
mult T256 base[4] 1
add T257 base[0] T256
mult T259 base[5] 1
mult T260 base[2] 1
add T261 base[0] T260
mult T263 base[5] 1
mult T264 T261[T263] base[6]
sub T265 T257[T259] T264
assign T253[T255] T265
assign T266 1
add T267 base[5] T266
assign base[5] T267
goto L26
@label B655
assign T268 1
add T269 base[4] T268
assign base[4] T269
goto L25
@label B659
assign T270 1
add T271 base[2] T270
assign base[2] T271
goto L23
@label B663
assign T272 1
sub T273 base[1] T272
assign base[2] T273
@label L27
assign T274 0
geq test base[2] T274
goif B671 test
goto F9_end
@label B671
assign T275 0
assign base[4] T275
@label L28
lt test base[4] base[2]
goif B677 test
goto B700
@label B677
mult T276 base[4] 1
add T277 base[0] T276
mult T279 base[1] 1
mult T280 base[4] 1
add T281 base[0] T280
mult T283 base[1] 1
mult T284 base[2] 1
add T285 base[0] T284
mult T287 base[1] 1
mult T288 base[4] 1
add T289 base[0] T288
mult T291 base[2] 1
mult T292 T285[T287] T289[T291]
mult T293 base[2] 1
add T294 base[0] T293
mult T296 base[2] 1
div T297 T292 T294[T296]
sub T298 T281[T283] T297
assign T277[T279] T298
assign T299 1
add T300 base[4] T299
assign base[4] T300
goto L28
@label B700
mult T301 base[2] 1
add T302 base[0] T301
mult T304 base[1] 1
mult T305 base[2] 1
add T306 base[0] T305
mult T308 base[1] 1
mult T309 base[2] 1
add T310 base[0] T309
mult T312 base[2] 1
div T313 T306[T308] T310[T312]
assign T302[T304] T313
assign T314 1
sub T315 base[2] T314
assign base[2] T315
goto L27
@label F9_end
assign lastbase base
@endfunction
@label F9_out
free T129
