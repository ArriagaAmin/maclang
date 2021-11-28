@staticv A0 1
@staticv A1 400
@staticv A2 400
@staticv A3 100
@staticv A4 2
@staticv A5 2
@staticv A6 2
@staticv A7 2
@staticv A8 2
@staticv A9 1
@staticv A10 1
@staticv A11 2
@string S0 "Menu principal. Escoja una de las siguientes opciones: "
@string S1 "1. Ordenar numeros enteros. "
@string S2 "2. Ordenar numeros en punto flotante. "
@string S3 "3. Ordenar caracteres. "
@string S4 "4. Salir. "
@string S5 "Indique el numero de elementos a ordenar. Recuerde que debe estar entre 1 y 100: "
@string S6 "Numero de elementos invalido."
@string S7 "Indique los elementos: "
@string S8 "El arreglo ordenado de enteros es:"
@string S9 ", "
@string S10 "]"
@string S11 "El arreglo ordenado de flotantes es:"
@string S12 ", "
@string S13 "]"
@string S14 "El arreglo ordenado de caracteres es:"
@string S15 ", "
@string S16 "]"
@string S17 "Hasta luego!"
@string S18 "Opcion invalida."
assign T0 10
assign A0[0] T0
assign T1 A0
assign T2 512
assign T3 T2
assign T5 1
mult T5 T5 T3
malloc T4 T5
assign T9 100
assign T10 100
assign T11 100
@label L0
goto B13
@label B13
param S0
call T12 PRINT 1
param T1
call T13 PRINT 1
param S1
call T14 PRINT 1
param T1
call T15 PRINT 1
param S2
call T16 PRINT 1
param T1
call T17 PRINT 1
param S3
call T18 PRINT 1
param T1
call T19 PRINT 1
param S4
call T20 PRINT 1
param T1
call T21 PRINT 1
param T4
call T22 READ 1
param T4
call T23 STOI 1
assign T6 T23
assign T24 0
lt test T24 T6
goif B42 test
goto B275
@label B42
assign T25 4
lt test T6 T25
goif B46 test
goto B275
@label B46
param S5
call T26 PRINT 1
param T4
call T27 READ 1
param T4
call T28 STOI 1
assign T7 T28
assign T29 1
lt test T7 T29
goif B61 test
goto B57
@label B57
assign T30 100
gt test T7 T30
goif B61 test
goto B67
@label B61
param S6
call T31 PRINT 1
param T1
call T32 PRINT 1
goto L0
goto B67
@label B67
assign T33 0
assign T8 T33
param S7
call T34 PRINT 1
@label L1
assign T35 1
eq test T6 T35
goif B76 test
goto B140
@label B76
@label L2
lt test T8 T7
goif B80 test
goto B90
@label B80
param T4
call T36 READ 1
mult T38 T8 4
param T4
call T39 STOI 1
assign A1[T38] T39
assign T40 1
add T41 T8 T40
assign T8 T41
goto L2
@label B90
assign T42 0
param A1
param T42
param T7
call T43 F1 3
param T1
call T44 PRINT 1
param S8
call T45 PRINT 1
assign T46 10
assign T47 91
assign A4[1] T47
assign A4[0] T46
param A4
call T48 PRINT 1
assign T49 0
assign T8 T49
@label L3
assign T50 1
sub T51 T7 T50
lt test T8 T51
goif B113 test
goto B125
@label B113
mult T53 T8 4
param T4
param A1[T53]
call T54 ITOS 2
param T4
call T55 PRINT 1
param S9
call T56 PRINT 1
assign T57 1
add T58 T8 T57
assign T8 T58
goto L3
@label B125
mult T60 T8 4
param T4
param A1[T60]
call T61 ITOS 2
param T4
call T62 PRINT 1
param S10
call T63 PRINT 1
assign T64 10
assign T65 10
assign A5[1] T65
assign A5[0] T64
param A5
call T66 PRINT 1
goto L0
@label B140
@label L4
assign T67 2
eq test T6 T67
goif B145 test
goto B209
@label B145
@label L5
lt test T8 T7
goif B149 test
goto B159
@label B149
param T4
call T68 READ 1
mult T70 T8 4
param T4
call T71 STOF 1
assign A2[T70] T71
assign T72 1
add T73 T8 T72
assign T8 T73
goto L5
@label B159
assign T74 0
param A2
param T74
param T7
call T75 F3 3
param T1
call T76 PRINT 1
param S11
call T77 PRINT 1
assign T78 10
assign T79 91
assign A6[1] T79
assign A6[0] T78
param A6
call T80 PRINT 1
assign T81 0
assign T8 T81
@label L6
assign T82 1
sub T83 T7 T82
lt test T8 T83
goif B182 test
goto B194
@label B182
mult T85 T8 4
param T4
param A2[T85]
call T86 FTOS 2
param T4
call T87 PRINT 1
param S12
call T88 PRINT 1
assign T89 1
add T90 T8 T89
assign T8 T90
goto L6
@label B194
mult T92 T8 4
param T4
param A2[T92]
call T93 FTOS 2
param T4
call T94 PRINT 1
param S13
call T95 PRINT 1
assign T96 10
assign T97 10
assign A7[1] T97
assign A7[0] T96
param A7
call T98 PRINT 1
goto L0
@label B209
@label L7
assign T99 2
eq test T6 T99
goif B214 test
goto L0
@label B214
@label L8
lt test T8 T7
goif B218 test
goto B228
@label B218
param T4
call T100 READ 1
mult T102 T8 1
assign T103 0
mult T105 T103 1
assign A3[T102] T4[T105]
assign T106 1
add T107 T8 T106
assign T8 T107
goto L8
@label B228
assign T108 0
param A3
param T108
param T7
call T109 F5 3
param T1
call T110 PRINT 1
param S14
call T111 PRINT 1
assign T112 10
assign T113 91
assign A8[1] T113
assign A8[0] T112
param A8
call T114 PRINT 1
assign T115 0
assign T8 T115
@label L9
assign T116 1
sub T117 T7 T116
lt test T8 T117
goif B251 test
goto B261
@label B251
mult T119 T8 1
assign A9[0] A3[T119]
param A9
call T120 PRINT 1
param S15
call T121 PRINT 1
assign T122 1
add T123 T8 T122
assign T8 T123
goto L9
@label B261
mult T125 T8 1
assign A10[0] A3[T125]
param A10
call T126 PRINT 1
param S16
call T127 PRINT 1
assign T128 10
assign T129 10
assign A11[1] T129
assign A11[0] T128
param A11
call T130 PRINT 1
goto L0
goto L0
@label B275
@label L10
assign T131 4
eq test T6 T131
goif B280 test
goto B286
@label B280
param S17
call T132 PRINT 1
param T1
call T133 PRINT 1
goto B293
goto L0
@label B286
param S18
call T134 PRINT 1
param T1
call T135 PRINT 1
param T1
call T136 PRINT 1
goto L0
@label B293
goto F0_out
@function F0 12
assign base[8] base[0]
assign base[0] base[4]
assign base[4] base[8]
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 28
leq test base[8] base[4]
goif B307 test
goto B309
@label B307
return 0
goto B309
@label B309
assign base[12] base[4]
assign T137 1
sub T138 base[8] T137
assign base[16] T138
mult T140 base[8] 4
assign base[20] base[0][T140]
@label L11
goto B317
@label B317
@label L12
mult T142 base[12] 4
lt test base[0][T142] base[20]
goif B322 test
goto B326
@label B322
assign T143 1
add T144 base[12] T143
assign base[12] T144
goto L12
@label B326
@label L13
mult T146 base[16] 4
gt test base[0][T146] base[20]
goif B331 test
goto B335
@label B331
assign T147 1
sub T148 base[16] T147
assign base[16] T148
goto L13
@label B335
geq test base[12] base[16]
goif B338 test
goto B340
@label B338
goto B348
goto B340
@label B340
mult T150 base[12] 4
mult T152 base[16] 4
param base[0][T150]
param base[0][T152]
call T153 F0 2
assign base[0][T150] lastbase[0]
assign base[0][T152] lastbase[4]
goto L11
@label B348
mult T155 base[12] 4
mult T157 base[8] 4
param base[0][T155]
param base[0][T157]
call T158 F0 2
assign base[0][T155] lastbase[0]
assign base[0][T157] lastbase[4]
param base[0]
param base[4]
param base[16]
call T159 F1 3
assign T160 1
add T161 base[12] T160
param base[0]
param T161
param base[8]
call T162 F1 3
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 12
assign base[8] base[0]
assign base[0] base[4]
assign base[4] base[8]
@label F2_end
assign lastbase base
@endfunction
@label F2_out
goto F3_out
@function F3 28
leq test base[8] base[4]
goif B383 test
goto B385
@label B383
return 0
goto B385
@label B385
assign base[12] base[4]
assign T163 1
sub T164 base[8] T163
assign base[16] T164
mult T166 base[8] 4
assign base[20] base[0][T166]
@label L14
goto B393
@label B393
@label L15
mult T168 base[12] 4
lt test base[0][T168] base[20]
goif B398 test
goto B402
@label B398
assign T169 1
add T170 base[12] T169
assign base[12] T170
goto L15
@label B402
@label L16
mult T172 base[16] 4
gt test base[0][T172] base[20]
goif B407 test
goto B411
@label B407
assign T173 1
sub T174 base[16] T173
assign base[16] T174
goto L16
@label B411
geq test base[12] base[16]
goif B414 test
goto B416
@label B414
goto B424
goto B416
@label B416
mult T176 base[12] 4
mult T178 base[16] 4
param base[0][T176]
param base[0][T178]
call T179 F2 2
assign base[0][T176] lastbase[0]
assign base[0][T178] lastbase[4]
goto L14
@label B424
mult T181 base[12] 4
mult T183 base[8] 4
param base[0][T181]
param base[0][T183]
call T184 F2 2
assign base[0][T181] lastbase[0]
assign base[0][T183] lastbase[4]
param base[0]
param base[4]
param base[16]
call T185 F3 3
assign T186 1
add T187 base[12] T186
param base[0]
param T187
param base[8]
call T188 F3 3
@label F3_end
assign lastbase base
@endfunction
@label F3_out
goto F4_out
@function F4 3
assign base[2] base[0]
assign base[0] base[1]
assign base[1] base[2]
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 22
leq test base[8] base[4]
goif B459 test
goto B461
@label B459
return 0
goto B461
@label B461
assign base[12] base[4]
assign T189 1
sub T190 base[8] T189
assign base[16] T190
mult T192 base[8] 1
assign base[20] base[0][T192]
@label L17
goto B469
@label B469
@label L18
mult T194 base[12] 1
lt test base[0][T194] base[20]
goif B474 test
goto B478
@label B474
assign T195 1
add T196 base[12] T195
assign base[12] T196
goto L18
@label B478
@label L19
mult T198 base[16] 1
gt test base[0][T198] base[20]
goif B483 test
goto B487
@label B483
assign T199 1
sub T200 base[16] T199
assign base[16] T200
goto L19
@label B487
geq test base[12] base[16]
goif B490 test
goto B492
@label B490
goto B500
goto B492
@label B492
mult T202 base[12] 1
mult T204 base[16] 1
param base[0][T202]
param base[0][T204]
call T205 F4 2
assign base[0][T202] lastbase[0]
assign base[0][T204] lastbase[1]
goto L17
@label B500
mult T207 base[12] 1
mult T209 base[8] 1
param base[0][T207]
param base[0][T209]
call T210 F4 2
assign base[0][T207] lastbase[0]
assign base[0][T209] lastbase[1]
param base[0]
param base[4]
param base[16]
call T211 F5 3
assign T212 1
add T213 base[12] T212
param base[0]
param T213
param base[8]
call T214 F5 3
@label F5_end
assign lastbase base
@endfunction
@label F5_out
free T4
