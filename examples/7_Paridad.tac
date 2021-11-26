@string S0 "Desea determinar la paridad de un numero? [Y/n] "
@string S1 "n"
@string S2 "N"
@string S3 "Gracias por usar nuestros utiles servicios de calidad!"
@string S4 "Indique el numero: "
@string S5 "El numero es par! Quien lo diria?"
@string S6 "Wow! El numero es impar, no me lo esperaba."
assign T0 0
assign T1 1
assign T3 1
mult T3 T3 T1
malloc T2 T3
assign T2[0] T0
assign T4 T2
assign T5 10
assign T6 1
assign T8 1
mult T8 T8 T6
malloc T7 T8
assign T7[0] T5
assign T9 T7
assign T10 0
goto F0_out
@function F0 12
assign T11 0
assign base[8] T11
@label L0
mult T13 base[8] 1
@label L1
neq test base[0][T13] base[4]
goif B25 test
goto B29
@label B25
assign T14 1
add T15 base[8] T14
assign base[8] T15
goto L0
@label B29
return base[8]
@label F0_end
assign lastbase base
@endfunction
@label F0_out
goto F1_out
@function F1 12
assign T16 0
assign base[8] T16
@label L2
mult T18 base[8] 1
@label L3
assign T19 0
neq test base[0][T18] T19
goif B45 test
goto B55
@label B45
mult T21 base[8] 1
@label L4
mult T23 base[8] 1
eq test base[0][T21] base[4][T23]
goif B51 test
goto B55
@label B51
assign T24 1
add T25 base[8] T24
assign base[8] T25
goto L2
@label B55
mult T27 base[8] 1
mult T29 base[8] 1
gt test base[0][T27] base[4][T29]
goif B60 test
goto B63
@label B60
assign T30 1
return T30
goto F1_end
@label B63
mult T32 base[8] 1
mult T34 base[8] 1
gt test base[4][T32] base[0][T34]
goif B68 test
goto B72
@label B68
assign T35 1
minus T36 T35
return T36
goto F1_end
@label B72
assign T37 0
return T37
@label F1_end
assign lastbase base
@endfunction
@label F1_out
goto F2_out
@function F2 16
param T38
param T10
call T39 F0 2
assign T40 1
add T41 T39 T40
assign base[8] T41
assign T42 0
assign base[12] T42
@label L5
lt test base[12] base[8]
goif B92 test
goto F2_end
@label B92
mult T44 base[12] 1
mult T46 base[12] 1
assign base[0][T44] base[4][T46]
assign T47 1
add T48 base[12] T47
assign base[12] T48
goto L5
@label F2_end
assign lastbase base
@endfunction
@label F2_out
goto F3_out
@function F3 28
assign T49 0
assign T50 0
assign base[12] T49
assign base[16] T50
@label L6
lt test base[12] base[4]
goif B113 test
goto B139
@label B113
mult T52 base[12] 4
param T53
param T10
call T54 F0 2
assign base[24] T54
assign T55 0
assign base[20] T55
@label L7
lt test base[20] base[24]
goif B124 test
goto B135
@label B124
mult T57 base[16] 1
mult T59 base[12] 4
mult T61 base[20] 1
assign base[8][T57] base[0][T59][T61]
assign T62 1
add T63 base[20] T62
assign base[20] T63
assign T64 1
add T65 base[16] T64
assign base[16] T65
goto L7
@label B135
assign T66 1
add T67 base[12] T66
assign base[12] T67
goto L6
@label B139
mult T69 base[16] 1
assign T70 0
assign base[8][T69] T70
@label F3_end
assign lastbase base
@endfunction
@label F3_out
goto F4_out
@function F4 29
assign T71 0
assign T72 0
assign T73 0
param T74
param T10
call T75 F0 2
assign base[12] T71
assign base[16] T72
assign base[20] T73
assign base[24] T75
goto B159
@label B159
assign base[28] True
goto Bool162
assign base[28] False
@label Bool162
@label L8
mult T77 base[12] 1
@label L9
assign T78 0
neq test base[0][T77] T78
goif B170 test
goto B218
@label B170
mult T80 base[12] 1
@label L10
eq test base[0][T80] base[8]
goif B175 test
goto B194
@label B175
goif B194 base[28]
goto B177
@label B177


goto B180
@label B180
assign base[28] True
goto Bool183
assign base[28] False
@label Bool183
mult T82 base[20] 4
mult T84 base[16] 1
assign T85 0
assign base[4][T82][T84] T85
assign T86 1
add T87 base[20] T86
assign base[20] T87
assign T88 0
assign base[16] T88
goto B214
@label B194
mult T90 base[12] 1
@label L11
neq test base[0][T90] base[8]
goif B199 test
goto B214
@label B199


goto B204
assign base[28] True
goto Bool205
@label B204
assign base[28] False
@label Bool205
mult T92 base[20] 4
mult T94 base[16] 1
mult T96 base[12] 1
assign base[4][T92][T94] base[0][T96]
assign T97 1
add T98 base[16] T97
assign base[16] T98
goto B214
@label B214
assign T99 1
add T100 base[12] T99
assign base[12] T100
goto L8
@label B218
goif B228 base[28]
goto B220
@label B220
mult T102 base[20] 4
mult T104 base[16] 1
assign T105 0
assign base[4][T102][T104] T105
assign T106 1
add T107 base[20] T106
assign base[20] T107
goto B228
@label B228
return base[20]
@label F4_end
assign lastbase base
@endfunction
@label F4_out
goto F5_out
@function F5 16
goto B239
goto B243
assign base[4] True
goto Bool240
@label B239
assign base[4] False
@label Bool240
assign base[5] True
goto Bool244
@label B243
assign base[5] False
@label Bool244
param T108
param T10
call T109 F0 2
assign T110 0
assign base[8] T109
assign base[12] T110
@label L12
lt test base[12] base[8]
goif B255 test
goto B317
@label B255
mult T112 base[12] 1
@label L13
assign T113 46
eq test base[0][T112] T113
goif B261 test
goto B271
@label B261
goif B271 base[4]
goto B263
@label B263


goto B266
@label B266
assign base[4] True
goto Bool269
assign base[4] False
@label Bool269
goto B313
@label B271
mult T115 base[12] 1
@label L14
assign T116 46
eq test base[0][T115] T116
goif B277 test
goto B284
@label B277
goto B280
assign T117 True
goto Bool281
@label B280
assign T117 False
@label Bool281
return T117
goto B313
@label B284
mult T119 base[12] 1
assign T120 48
lt test base[0][T119] T120
goif B294 test
goto B289
@label B289
mult T122 base[12] 1
assign T123 57
gt test base[0][T122] T123
goif B294 test
goto B301
@label B294
goto B297
assign T124 True
goto Bool298
@label B297
assign T124 False
@label Bool298
return T124
goto B313
@label B301
goif B303 base[4]
goto B313
@label B303
goif B313 base[5]
goto B305
@label B305


goto B308
@label B308
assign base[5] True
goto Bool311
assign base[5] False
@label Bool311
goto B313
@label B313
assign T125 1
add T126 base[12] T125
assign base[12] T126
goto L12
@label B317
goif B319 base[4]
goto B323
@label B319
goif B321 base[5]
goto B323
@label B321
assign T127 True
goto Bool324
@label B323
assign T127 False
@label Bool324
return T127
@label F5_end
assign lastbase base
@endfunction
@label F5_out
assign T128 1024
assign T129 T128
assign T131 1
mult T131 T131 T129
malloc T130 T131
@label L15
goto B337
@label B337
param T133
call T134 PRINT 1
assign T136 1
mult T136 T136 T129
malloc T135 T136
memcpy T135 T130
param T135
call T137 READ 1
assign T139 1
mult T139 T139 T129
malloc T138 T139
memcpy T138 T130
param T138
param T140
call T141 F1 2
@label L16
assign T142 0
eq test T141 T142
goif B369 test
goto B357
@label B357
assign T144 1
mult T144 T144 T129
malloc T143 T144
memcpy T143 T130
param T143
param T145
call T146 F1 2
@label L17
assign T147 0
eq test T146 T147
goif B369 test
goto B372
@label B369
param T148
call T149 PRINT 1
goto B372
@label B372
param T150
call T151 PRINT 1
assign T153 1
mult T153 T153 T129
malloc T152 T153
memcpy T152 T130
param T152
call T154 READ 1
assign T156 1
mult T156 T156 T129
malloc T155 T156
memcpy T155 T130
param T155
call T157 STOI 1
param T157
call T158 F6 1
assign T132 T158
param T132
call T159 F7 1
goif B393 T159
goto B398
@label B393
param T160
call T161 PRINT 1
param T162
call T163 PRINT 1
goto L15
@label B398
param T164
call T165 PRINT 1
param T166
call T167 PRINT 1
goto L15
goto F6_out
@function F6 4
assign T168 0
lt test base[0] T168
goif B409 test
goto B412
@label B409
minus T169 base[0]
return T169
goto F6_end
@label B412
return base[0]
@label F6_end
assign lastbase base
@endfunction
@label F6_out
goto F7_out
@function F7 4
@label L18
assign T170 0
eq test base[0] T170
goif B424 test
goto B431
@label B424
goto B425
@label B425
assign T171 True
goto Bool428
assign T171 False
@label Bool428
return T171
goto F7_end
@label B431
@label L19
assign T172 1
eq test base[0] T172
goif B436 test
goto B443
@label B436
goto B439
assign T173 True
goto Bool440
@label B439
assign T173 False
@label Bool440
return T173
goto F7_end
@label B443
assign T174 1
sub T175 base[0] T174
param T175
call T176 F8 1
goif B449 T176
goto B451
@label B449
assign T177 True
goto Bool452
@label B451
assign T177 False
@label Bool452
return T177
@label F7_end
assign lastbase base
@endfunction
@label F7_out
goto F8_out
@function F8 4
@label L20
assign T178 0
eq test base[0] T178
goif B465 test
goto B472
@label B465
goto B468
assign T179 True
goto Bool469
@label B468
assign T179 False
@label Bool469
return T179
goto F8_end
@label B472
@label L21
assign T180 1
eq test base[0] T180
goif B477 test
goto B484
@label B477
goto B478
@label B478
assign T181 True
goto Bool481
assign T181 False
@label Bool481
return T181
goto F8_end
@label B484
assign T182 1
sub T183 base[0] T182
param T183
call T184 F7 1
goif B490 T184
goto B492
@label B490
assign T185 True
goto Bool493
@label B492
assign T185 False
@label Bool493
return T185
@label F8_end
assign lastbase base
@endfunction
@label F8_out
