.data
A0: .word  5
.align 2
S0: .asciiz  "0000\n"
.align 2
S1: .asciiz  "0000fact(%i)"
.align 2
S2: .asciiz  "0000Resultado: %i"
.align 2
S3: .asciiz  "0000Input: "
.align 2
S4: .asciiz  "0000Hasta luego!"
.align 2
S5: .asciiz  "0000Calculando factorial de %i"
.align 2
S6: .asciiz  "0000Resultado calculado: %i"
.align 2
S7: .asciiz  "0000Caracteres: %c %c %c%cNumeros: %i %i%cTextos: %s %s%c"
.align 2
S8: .asciiz  "0000Hello"
.align 2
S9: .asciiz  "0000 world!"
.align 2
S10: .asciiz  "0000Final"
BASE: .word  1
STACK: .word  1
T106: .byte  1
T109: .word  1
T114: .word  1
T117: .word  1
T121: .word  1
T123: .word  1
T124: .word  1
T126: .word  1
T127: .word  1
T128: .word  1
T129: .word  1
T130: .word  1
T131: .word  1
T132: .word  1
T133: .word  1
T134: .word  1
T135: .word  1
T136: .word  1
T137: .word  1
T138: .word  1
T139: .word  1
T140: .word  1
T141: .word  1
T142: .word  1
T143: .word  1
T144: .word  1
T145: .word  1
T146: .word  1
T147: .word  1
T148: .word  1
T149: .word  1
T62: .word  1
T63: .word  1
T64: .word  1
T67: .word  1
T68: .word  1
T69: .word  1
T72: .word  1
T75: .word  1
T76: .word  1
T77: .word  1
T78: .word  1
T79: .word  1
T80: .word  1
T81: .word  1
T82: .word  1
T84: .word  1
T85: .word  1
T87: .word  1
T90: .word  1
T91: .word  1
T92: .word  1
T93: .word  1
T94: .word  1
T95: .word  1
T96: .word  1
T97: .word  1
test: .byte  1

.text
li  $sp, 0x7fc00000
li  $fp, 0x7fc00000
B0: 
# assignw S3[0] 7 
li  $s7, 7
la  $s6, S3
sw  $s7, 0($s6)
# param T62 0 
# ===== Parameter =====
la  $s4, 12($sp)
# =====================
# assignw T62[0] S3 
sw  $s6, 0($s4)
# assignb A0[0] 0 
li  $s5, 0
la  $s3, A0
sb  $s5, 0($s3)
# assignb A0[1] 0 
sb  $s5, 1($s3)
# assignb A0[2] 0 
sb  $s5, 2($s3)
# assignb A0[3] 0 
sb  $s5, 3($s3)
# assignb A0[4] 0 
sb  $s5, 4($s3)
# call T63 F9_B26 
sw  $s4, T62
jal  F9_B26
lw  $t9, 4($sp)
sw  $t9, T63
B1: 
# call T64 F3_B20 
jal  F3_B20
lw  $s7, 4($sp)
sw  $s7, T64
B2: 
# lt test T64 0
lw  $s7, T64
li  $s6, 0
slt  $s5, $s7, $s6
# goif B4 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B4
B3: 
# goto B7 
j  B7
B4: 
# assignw S4[0] 12 
li  $s7, 12
la  $s6, S4
sw  $s7, 0($s6)
# param T67 0 
# ===== Parameter =====
la  $s4, 12($sp)
# =====================
# assignw T67[0] S4 
sw  $s6, 0($s4)
# assignb A0[0] 0 
li  $s5, 0
la  $s3, A0
sb  $s5, 0($s3)
# assignb A0[1] 0 
sb  $s5, 1($s3)
# assignb A0[2] 0 
sb  $s5, 2($s3)
# assignb A0[3] 0 
sb  $s5, 3($s3)
# assignb A0[4] 0 
sb  $s5, 4($s3)
# call T68 F9_B26 
sw  $s4, T67
jal  F9_B26
lw  $t9, 4($sp)
sw  $t9, T68
B5: 
# assignw T69 0 
li  $s7, 0
# exit T69 
lw  $a0, T69
li  $v0, 17 
syscall
# ===== Updating temporals =====
sw  $s7, T69
# ==============================
B7: 
# assignw S5[0] 26 
li  $s7, 26
la  $s6, S5
sw  $s7, 0($s6)
# malloc T75 8 
li  $s5, 8
move  $a0, $s5
li  $v0, 9 
syscall
move  $s4, $v0
# assignw T75[0] 1 
li  $s3, 1
sw  $s3, 0($s4)
# assignw T72 T75 
# assignw T72[4] T64 
lw  $t9, T64
sw  $t9, 4($s4)
# param T76 0 
# ===== Parameter =====
la  $t5, 12($sp)
# =====================
# assignw T76[0] S5 
sw  $s6, 0($t5)
# assignb A0[0] 0 
li  $v1, 0
la  $s1, A0
sb  $v1, 0($s1)
# assignw T78 T75[0] 
lw  $a0, 0($s4)
# mult T79 4 T78
li  $s0, 4
mul  $a1, $s0, $a0
# add T79 T79 4
add  $a1, $a1, $s0
# malloc T80 T79 
sw  $a0, T78
move  $a0, $a1
li  $v0, 9 
syscall
move  $a2, $v0
# assignw T77 T80 
# memcpy T77 T75 T79
MC0: 
beqz  $a1, MC0_END
addi  $a1, $a1, -1
add  $v0, $s4, $a1
lb  $v0, 0($v0)
add  $v1, $a2, $a1
sb  $v0, 0($v1)
j  MC0
MC0_END: 
# param T81 8 
# ===== Parameter =====
la  $v1, 20($sp)
# =====================
# assignw T81[0] T80 
sw  $a2, 0($v1)
# assignb A0[1] 1 
sb  $s3, 1($s1)
# assignb A0[2] 0 
li  $a0, 0
sb  $a0, 2($s1)
# assignb A0[3] 0 
sb  $a0, 3($s1)
# assignb A0[4] 0 
sb  $a0, 4($s1)
# call T82 F9_B26 
sw  $a1, T79
sw  $s4, T72
sw  $s4, T75
sw  $t5, T76
sw  $a2, T77
sw  $a2, T80
sw  $v1, T81
jal  F9_B26
lw  $t4, 4($sp)
sw  $t4, T82
B8: 
# assignw S6[0] 23 
li  $s7, 23
la  $s6, S6
sw  $s7, 0($s6)
# param T84 0 
# ===== Parameter =====
la  $s4, 12($sp)
# =====================
# assignw T84[0] T64 
lw  $s5, T64
sw  $s5, 0($s4)
# call T85 F10_B42 
sw  $s4, T84
jal  F10_B42
lw  $s3, 4($sp)
sw  $s3, T85
B9: 
# malloc T90 8 
li  $s7, 8
move  $a0, $s7
li  $v0, 9 
syscall
move  $s6, $v0
# assignw T90[0] 1 
li  $s5, 1
sw  $s5, 0($s6)
# assignw T87 T90 
# assignw T87[4] T85 
lw  $s4, T85
sw  $s4, 4($s6)
# param T91 0 
# ===== Parameter =====
la  $t9, 12($sp)
# =====================
# assignw T91[0] S6 
la  $s3, S6
sw  $s3, 0($t9)
# assignb A0[0] 0 
li  $v1, 0
la  $t5, A0
sb  $v1, 0($t5)
# assignw T93 T90[0] 
lw  $s1, 0($s6)
# mult T94 4 T93
li  $a0, 4
mul  $s0, $a0, $s1
# add T94 T94 4
add  $s0, $s0, $a0
# malloc T95 T94 
move  $a0, $s0
li  $v0, 9 
syscall
move  $a1, $v0
# assignw T92 T95 
# memcpy T92 T90 T94
MC1: 
beqz  $s0, MC1_END
addi  $s0, $s0, -1
add  $v0, $s6, $s0
lb  $v0, 0($v0)
add  $v1, $a1, $s0
sb  $v0, 0($v1)
j  MC1
MC1_END: 
# param T96 8 
# ===== Parameter =====
la  $v1, 20($sp)
# =====================
# assignw T96[0] T95 
sw  $a1, 0($v1)
# assignb A0[1] 1 
sb  $s5, 1($t5)
# assignb A0[2] 0 
li  $a0, 0
sb  $a0, 2($t5)
# assignb A0[3] 0 
sb  $a0, 3($t5)
# assignb A0[4] 0 
sb  $a0, 4($t5)
# call T97 F9_B26 
sw  $v1, T96
sw  $a1, T95
sw  $s0, T94
sw  $s1, T93
sw  $t9, T91
sw  $s6, T87
sw  $a1, T92
sw  $s6, T90
jal  F9_B26
lw  $a2, 4($sp)
sw  $a2, T97
B10: 
# assignw S7[0] 53 
li  $s7, 53
la  $s6, S7
sw  $s7, 0($s6)
# malloc T109 10 
li  $s5, 10
move  $a0, $s5
li  $v0, 9 
syscall
move  $s4, $v0
# assignw T109[0] 6 
li  $s3, 6
sw  $s3, 0($s4)
# assignw T106 T109 
# assignb T106[9] 10 
sb  $s5, 9($s4)
# assignb T106[8] 10 
sb  $s5, 8($s4)
# assignb T106[7] 10 
sb  $s5, 7($s4)
# assignb T106[6] 70 
li  $t9, 70
sb  $t9, 6($s4)
# assignb T106[5] 9 
li  $v1, 9
sb  $v1, 5($s4)
# assignb T106[4] 65 
li  $t5, 65
sb  $t5, 4($s4)
# malloc T117 12 
li  $s1, 12
move  $a0, $s1
li  $v0, 9 
syscall
move  $a0, $v0
# assignw T117[0] 2 
li  $s0, 2
sw  $s0, 0($a0)
# assignw T114 T117 
# assignw T114[8] -69 
li  $a1, -69
sw  $a1, 8($a0)
# assignw T114[4] 42 
li  $a2, 42
sw  $a2, 4($a0)
# assignw S8[0] 5 
li  $t4, 5
la  $t0, S8
sw  $t4, 0($t0)
# assignw S9[0] 7 
li  $t1, 7
la  $t8, S9
sw  $t1, 0($t8)
# assignw T123 12 
# malloc T124 12 
sw  $a0, T117
sw  $a0, T114
move  $a0, $s1
li  $v0, 9 
syscall
move  $t3, $v0
# assignw T124[0] 2 
sw  $s0, 0($t3)
# assignw T121 T124 
# ===== Updating temporals =====
sw  $t3, T121
sw  $t3, T124
sw  $s4, T109
sb  $s4, T106
sw  $s1, T123
# ==============================
B11: 
# sub T123 T123 4
lw  $s7, T123
li  $s6, 4
sub  $s5, $s7, $s6
# lt test T123 4
slt  $s7, $s5, $s6
# goif B13 test 
# ===== Updating temporals =====
sb  $s7, test
sw  $s5, T123
# ==============================
bnez  $s7, B13
B12: 
# goto B11 
j  B11
B13: 
# assignw T121[8] S9 
la  $s7, S9
lw  $s6, T121
sw  $s7, 8($s6)
# assignw T121[4] S8 
la  $s5, S8
sw  $s5, 4($s6)
# assignw S10[0] 5 
li  $s4, 5
la  $s3, S10
sw  $s4, 0($s3)
# param T126 0 
# ===== Parameter =====
la  $v1, 12($sp)
# =====================
# assignw T126[0] S7 
la  $t9, S7
sw  $t9, 0($v1)
# assignw T128 T109[0] 
lw  $t5, T109
lw  $s1, 0($t5)
# mult T129 1 T128
li  $a0, 1
mul  $s0, $a0, $s1
# add T129 T129 4
li  $a1, 4
add  $s0, $s0, $a1
# malloc T130 T129 
move  $a0, $s0
li  $v0, 9 
syscall
move  $a2, $v0
# assignw T127 T130 
# memcpy T127 T109 T129
sw  $v1, T126
MC2: 
beqz  $s0, MC2_END
addi  $s0, $s0, -1
add  $v0, $t5, $s0
lb  $v0, 0($v0)
add  $v1, $a2, $s0
sb  $v0, 0($v1)
j  MC2
MC2_END: 
# param T131 4 
# ===== Parameter =====
la  $v1, 16($sp)
# =====================
# assignw T131[0] T130 
sw  $a2, 0($v1)
# assignb A0[0] 1 
li  $a0, 1
la  $t4, A0
sb  $a0, 0($t4)
# assignw T133 T117[0] 
lw  $t0, T117
lw  $t1, 0($t0)
# mult T134 4 T133
mul  $t8, $a1, $t1
# add T134 T134 4
add  $t8, $t8, $a1
# malloc T135 T134 
move  $a0, $t8
li  $v0, 9 
syscall
move  $t3, $v0
# assignw T132 T135 
# memcpy T132 T117 T134
sw  $v1, T131
MC3: 
beqz  $t8, MC3_END
addi  $t8, $t8, -1
add  $v0, $t0, $t8
lb  $v0, 0($v0)
add  $v1, $t3, $t8
sb  $v0, 0($v1)
j  MC3
MC3_END: 
# param T136 8 
# ===== Parameter =====
la  $a0, 20($sp)
# =====================
# assignw T136[0] T135 
sw  $t3, 0($a0)
# assignb A0[1] 1 
li  $v1, 1
sb  $v1, 1($t4)
# assignb A0[2] 0 
li  $s2, 0
sb  $s2, 2($t4)
# assignw T138 T124[0] 
lw  $t2, T124
lw  $t6, 0($t2)
# mult T139 4 T138
mul  $t7, $a1, $t6
# add T139 T139 4
add  $t7, $t7, $a1
# malloc T140 T139 
sw  $a0, T136
move  $a0, $t7
li  $v0, 9 
syscall
move  $v1, $v0
# assignw T137 T140 
# assignw T141 T139 
# ===== Updating temporals =====
sw  $t1, T133
sw  $a2, T127
sw  $t3, T132
sw  $s0, T129
sw  $s6, T121
sw  $s1, T128
sw  $v1, T140
sw  $t7, T139
sw  $t3, T135
sw  $t8, T134
sw  $t7, T141
sw  $v1, T137
sw  $a2, T130
sw  $t6, T138
# ==============================
B14: 
# sub T141 T141 4
lw  $s7, T141
li  $s6, 4
sub  $s5, $s7, $s6
# lt test T141 4
slt  $s7, $s5, $s6
# goif B16 test 
# ===== Updating temporals =====
sb  $s7, test
sw  $s5, T141
# ==============================
bnez  $s7, B16
B15: 
# assignw T142 T124[T141] 
lw  $s7, T124
lw  $s6, T141
add  $s6, $s6, $s7
lw  $s6, 0($s6)
# assignw T143 T142[0] 
lw  $s5, 0($s6)
# mult T144 1 T143
li  $s4, 1
mul  $s3, $s4, $s5
# add T144 T144 4
li  $t9, 4
add  $s3, $s3, $t9
# malloc T145 T144 
move  $a0, $s3
li  $v0, 9 
syscall
move  $v1, $v0
# assignw T137[T141] T145 
lw  $t5, T137
lw  $v0, T141
add  $v0, $t5, $v0
sw  $v1, 0($v0)
# assignw T146 T140[T141] 
lw  $s1, T140
lw  $a0, T141
add  $a0, $a0, $s1
lw  $a0, 0($a0)
# memcpy T146 T142 T144
sw  $v1, T145
MC4: 
beqz  $s3, MC4_END
addi  $s3, $s3, -1
add  $v0, $s6, $s3
lb  $v0, 0($v0)
add  $v1, $a0, $s3
sb  $v0, 0($v1)
j  MC4
MC4_END: 
# goto B14 
# ===== Updating temporals =====
sw  $a0, T146
sw  $s5, T143
sw  $s3, T144
sw  $s6, T142
sw  $t5, T137
# ==============================
j  B14
B16: 
# param T147 16 
# ===== Parameter =====
la  $s6, 28($sp)
# =====================
# assignw T147[0] T140 
lw  $s7, T140
sw  $s7, 0($s6)
# assignb A0[3] 1 
li  $s5, 1
la  $s4, A0
sb  $s5, 3($s4)
# param T148 20 
# ===== Parameter =====
la  $t9, 32($sp)
# =====================
# assignw T148[0] S10 
la  $s3, S10
sw  $s3, 0($t9)
# assignb A0[4] 1 
sb  $s5, 4($s4)
# call T149 F9_B26 
sw  $s6, T147
sw  $t9, T148
jal  F9_B26
lw  $v1, 4($sp)
sw  $v1, T149
B17: 
# exit 0 
li  $a0, 0
li  $v0, 17 
syscall

# *===== Functions Section =====*

F3_B20: 
# ===== Foreword =====
sw  $fp, 0($sp)
sw  $ra, 8($sp)
move  $fp, $sp
addi  $sp, $sp, 16
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
# ====================
# readi T3 
li  $v0, 5 
syscall
move  $s7, $v0
lw  $v0, BASE
sw  $s7, 0($v0)
# return T3 
lw  $s7, BASE
lw  $s7, 0($s7)
# ===== Epilogue =====
move  $sp, $fp
lw  $ra, 8($fp)
sw  $s7, 4($fp)
lw  $fp, 0($fp)
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
jr  $ra
# ====================
F9_B26: 
# ===== Foreword =====
sw  $fp, 0($sp)
sw  $ra, 8($sp)
move  $fp, $sp
addi  $sp, $sp, 88
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
# ====================
# assignb test A0[4] 
la  $s7, A0
lb  $s6, 4($s7)
# goif B28 test 
# ===== Updating temporals =====
sb  $s6, test
# ==============================
bnez  $s6, B28
B27: 
# assignw BASE[20] S0 
la  $s7, S0
lw  $s6, BASE
sw  $s7, 20($s6)
# ===== Updating temporals =====
sw  $s6, BASE
# ==============================
B28: 
# assignw T8 4 
li  $s7, 4
# assignw T9 4 
# assignw T10 4 
# assignw T11 4 
# assignw T12 4 
# assignw T13 BASE[0] 
lw  $s6, BASE
lw  $s5, 0($s6)
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s7, 32($v0)
lw  $v0, BASE
sw  $s7, 28($v0)
lw  $v0, BASE
sw  $s7, 24($v0)
lw  $v0, BASE
sw  $s7, 64($v0)
lw  $v0, BASE
sw  $s7, 60($v0)
lw  $v0, BASE
sw  $s5, 36($v0)
# ==============================
B29: 
# assignb T14 T13[T8] 
lw  $s7, BASE
lw  $s7, 36($s7)
lw  $s6, BASE
lw  $s6, 60($s6)
add  $s6, $s6, $s7
lb  $s6, 0($s6)
# add T8 T8 1
lw  $s5, BASE
lw  $s5, 60($s5)
li  $s4, 1
add  $s3, $s5, $s4
# eq test T14 0
li  $s5, 0
seq  $t9, $s6, $s5
# goif B41 test 
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s3, 60($v0)
sb  $t9, test
lw  $v0, BASE
sb  $s6, 40($v0)
# ==============================
bnez  $t9, B41
B30: 
# eq test T14 37
lw  $s7, BASE
lb  $s7, 40($s7)
li  $s6, 37
seq  $s5, $s7, $s6
# goif B32 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B32
B31: 
# printc T14 
lw  $a0, BASE
lb  $a0, 40($a0)
li  $v0, 11 
syscall
# goto B29 
j  B29
B32: 
# assignb T14 T13[T8] 
lw  $s7, BASE
lw  $s7, 36($s7)
lw  $s6, BASE
lw  $s6, 60($s6)
add  $s6, $s6, $s7
lb  $s6, 0($s6)
# add T8 T8 1
lw  $s5, BASE
lw  $s5, 60($s5)
li  $s4, 1
add  $s3, $s5, $s4
# eq test T14 99
li  $s5, 99
seq  $t9, $s6, $s5
# goif B37 test 
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s3, 60($v0)
sb  $t9, test
lw  $v0, BASE
sb  $s6, 40($v0)
# ==============================
bnez  $t9, B37
B33: 
# eq test T14 105
lw  $s7, BASE
lb  $s7, 40($s7)
li  $s6, 105
seq  $s5, $s7, $s6
# goif B38 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B38
B34: 
# eq test T14 102
lw  $s7, BASE
lb  $s7, 40($s7)
li  $s6, 102
seq  $s5, $s7, $s6
# goif B39 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B39
B35: 
# eq test T14 115
lw  $s7, BASE
lb  $s7, 40($s7)
li  $s6, 115
seq  $s5, $s7, $s6
# goif B40 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B40
B36: 
# goto B29 
j  B29
B37: 
# assignw T15 BASE[4] 
lw  $s7, BASE
lw  $s6, 4($s7)
# assignb T16 T15[T9] 
lw  $s5, BASE
lw  $s5, 64($s5)
add  $s5, $s5, $s6
lb  $s5, 0($s5)
# printc T16 
move  $a0, $s5
li  $v0, 11 
syscall
# add T9 T9 1
lw  $s4, BASE
lw  $s4, 64($s4)
li  $s3, 1
add  $t9, $s4, $s3
# goto B29 
# ===== Updating temporals =====
lw  $v0, BASE
sw  $t9, 64($v0)
lw  $v0, BASE
sw  $s6, 44($v0)
lw  $v0, BASE
sw  $s5, 48($v0)
# ==============================
j  B29
B38: 
# assignw T15 BASE[8] 
lw  $s7, BASE
lw  $s6, 8($s7)
# assignw T17 T15[T10] 
lw  $s5, BASE
lw  $s5, 24($s5)
add  $s5, $s5, $s6
lw  $s5, 0($s5)
# printi T17 
move  $a0, $s5
li  $v0, 1 
syscall
# add T10 T10 4
lw  $s4, BASE
lw  $s4, 24($s4)
li  $s3, 4
add  $t9, $s4, $s3
# goto B29 
# ===== Updating temporals =====
lw  $v0, BASE
sw  $t9, 24($v0)
lw  $v0, BASE
sw  $s6, 44($v0)
lw  $v0, BASE
sw  $s5, 52($v0)
# ==============================
j  B29
B39: 
# assignw T15 BASE[12] 
lw  $s7, BASE
lw  $s6, 12($s7)
# assignw f3 T15[T11] 
lw  $v0, BASE
lw  $v0, 28($v0)
add  $v0, $s6, $v0
l.s  $f30, ($v0)
# printf f3 
lw  $v0, BASE
l.s  $f12, 68($v0)
li  $v0, 2 
syscall
# add T11 T11 4
lw  $s5, BASE
lw  $s5, 28($s5)
li  $s4, 4
add  $s3, $s5, $s4
# goto B29 
# ===== Updating temporals =====
lw  $v0, BASE
s.s  $f30, 68($v0)
lw  $v0, BASE
sw  $s3, 28($v0)
lw  $v0, BASE
sw  $s6, 44($v0)
# ==============================
j  B29
B40: 
# assignw T15 BASE[16] 
lw  $s7, BASE
lw  $s6, 16($s7)
# assignw T18 T15[T12] 
lw  $s5, BASE
lw  $s5, 32($s5)
add  $s5, $s5, $s6
lw  $s5, 0($s5)
# add T18 T18 4
li  $s4, 4
add  $s5, $s5, $s4
# print T18 
move  $a0, $s5
li  $v0, 4 
syscall
# add T12 T12 4
lw  $s3, BASE
lw  $s3, 32($s3)
add  $t9, $s3, $s4
# goto B29 
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s5, 56($v0)
lw  $v0, BASE
sw  $t9, 32($v0)
lw  $v0, BASE
sw  $s6, 44($v0)
# ==============================
j  B29
B41: 
# assignw T15 BASE[20] 
lw  $s7, BASE
lw  $s6, 20($s7)
# add T15 T15 4
li  $s5, 4
add  $s6, $s6, $s5
# print T15 
move  $a0, $s6
li  $v0, 4 
syscall
# return 0 
li  $s4, 0
# ===== Epilogue =====
move  $sp, $fp
lw  $ra, 8($fp)
sw  $s4, 4($fp)
lw  $fp, 0($fp)
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
jr  $ra
# ====================
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s6, 44($v0)
# ==============================
F10_B42: 
# ===== Foreword =====
sw  $fp, 0($sp)
sw  $ra, 8($sp)
move  $fp, $sp
addi  $sp, $sp, 156
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
# ====================
# assignw S1[0] 8 
li  $s7, 8
la  $s6, S1
sw  $s7, 0($s6)
# malloc T23 8 
move  $a0, $s7
li  $v0, 9 
syscall
move  $s5, $v0
# assignw T23[0] 1 
li  $s4, 1
sw  $s4, 0($s5)
# assignw BASE[4] T23 
lw  $s3, BASE
sw  $s5, 4($s3)
# assignw T24 BASE[4] 
lw  $t9, 4($s3)
# assignw T25 BASE[0] 
lw  $v1, 0($s3)
# assignw T24[4] T25 
sw  $v1, 4($t9)
# param T26 0 
# ===== Parameter =====
la  $s1, 12($sp)
# =====================
# assignw T26[0] S1 
sw  $s6, 0($s1)
# assignb A0[0] 0 
li  $t5, 0
la  $a0, A0
sb  $t5, 0($a0)
# assignw T28 BASE[4] 
lw  $s0, 4($s3)
# assignw T29 T28[0] 
lw  $a1, 0($s0)
# mult T30 4 T29
li  $a2, 4
mul  $t4, $a2, $a1
# add T30 T30 4
add  $t4, $t4, $a2
# malloc T31 T30 
move  $a0, $t4
li  $v0, 9 
syscall
move  $t0, $v0
# assignw T27 T31 
# memcpy T27 T28 T30
lw  $v0, BASE
sw  $v1, 24($v0)
MC5: 
beqz  $t4, MC5_END
addi  $t4, $t4, -1
add  $v0, $s0, $t4
lb  $v0, 0($v0)
add  $v1, $t0, $t4
sb  $v0, 0($v1)
j  MC5
MC5_END: 
# param T32 8 
# ===== Parameter =====
la  $v1, 20($sp)
# =====================
# assignw T32[0] T31 
sw  $t0, 0($v1)
# assignb A0[1] 1 
la  $a0, A0
sb  $s4, 1($a0)
# assignb A0[2] 0 
sb  $t5, 2($a0)
# assignb A0[3] 0 
sb  $t5, 3($a0)
# assignb A0[4] 0 
sb  $t5, 4($a0)
# call T33 F9_B26 
lw  $v0, BASE
sw  $v1, 52($v0)
lw  $v0, BASE
sw  $t0, 32($v0)
lw  $v0, BASE
sw  $t4, 44($v0)
lw  $v0, BASE
sw  $s1, 28($v0)
lw  $v0, BASE
sw  $t9, 20($v0)
lw  $v0, BASE
sw  $s5, 16($v0)
lw  $v0, BASE
sw  $s0, 36($v0)
sw  $s3, BASE
lw  $v0, BASE
sw  $t0, 48($v0)
lw  $v0, BASE
sw  $a1, 40($v0)
jal  F9_B26
lw  $t1, 4($sp)
lw  $v0, BASE
sw  $t1, 56($v0)
B43: 
# assignw T35 BASE[0] 
lw  $s7, BASE
lw  $s6, 0($s7)
# eq test T35 0
li  $s5, 0
seq  $s4, $s6, $s5
# goif B45 test 
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s6, 60($v0)
sb  $s4, test
# ==============================
bnez  $s4, B45
B44: 
# goto B47 
j  B47
B45: 
# assignw T36 1 
li  $s7, 1
# return T36 
# ===== Epilogue =====
move  $sp, $fp
lw  $ra, 8($fp)
sw  $s7, 4($fp)
lw  $fp, 0($fp)
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
jr  $ra
# ====================
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s7, 64($v0)
# ==============================
B47: 
# assignw T39 BASE[0] 
lw  $s7, BASE
lw  $s6, 0($s7)
# sub T38 T39 1
li  $s5, 1
sub  $s4, $s6, $s5
# param T40 0 
# ===== Parameter =====
la  $t9, 12($sp)
# =====================
# assignw T40[0] T38 
sw  $s4, 0($t9)
# call T41 F10_B42 
lw  $v0, BASE
sw  $t9, 76($v0)
lw  $v0, BASE
sw  $s4, 68($v0)
lw  $v0, BASE
sw  $s6, 72($v0)
jal  F10_B42
lw  $s3, 4($sp)
lw  $v0, BASE
sw  $s3, 80($v0)
B48: 
# assignw BASE[8] T41 
lw  $s7, BASE
lw  $s7, 80($s7)
lw  $s6, BASE
sw  $s7, 8($s6)
# assignw S2[0] 13 
li  $s5, 13
la  $s4, S2
sw  $s5, 0($s4)
# malloc T46 8 
li  $s3, 8
move  $a0, $s3
li  $v0, 9 
syscall
move  $t9, $v0
# assignw T46[0] 1 
li  $v1, 1
sw  $v1, 0($t9)
# assignw BASE[12] T46 
sw  $t9, 12($s6)
# assignw T47 BASE[12] 
lw  $t5, 12($s6)
# assignw T48 BASE[8] 
lw  $s1, 8($s6)
# assignw T47[4] T48 
sw  $s1, 4($t5)
# param T49 0 
# ===== Parameter =====
la  $s0, 12($sp)
# =====================
# assignw T49[0] S2 
sw  $s4, 0($s0)
# assignb A0[0] 0 
li  $a0, 0
la  $a1, A0
sb  $a0, 0($a1)
# assignw T51 BASE[12] 
lw  $a2, 12($s6)
# assignw T52 T51[0] 
lw  $t4, 0($a2)
# mult T53 4 T52
li  $t0, 4
mul  $t1, $t0, $t4
# add T53 T53 4
add  $t1, $t1, $t0
# malloc T54 T53 
move  $a0, $t1
li  $v0, 9 
syscall
move  $t8, $v0
# assignw T50 T54 
# memcpy T50 T51 T53
MC6: 
beqz  $t1, MC6_END
addi  $t1, $t1, -1
add  $v0, $a2, $t1
lb  $v0, 0($v0)
add  $v1, $t8, $t1
sb  $v0, 0($v1)
j  MC6
MC6_END: 
# param T55 8 
# ===== Parameter =====
la  $v1, 20($sp)
# =====================
# assignw T55[0] T54 
sw  $t8, 0($v1)
# assignb A0[1] 1 
li  $a0, 1
sb  $a0, 1($a1)
# assignb A0[2] 0 
li  $t3, 0
sb  $t3, 2($a1)
# assignb A0[3] 0 
sb  $t3, 3($a1)
# assignb A0[4] 0 
sb  $t3, 4($a1)
# call T56 F9_B26 
lw  $v0, BASE
sw  $v1, 120($v0)
lw  $v0, BASE
sw  $t4, 108($v0)
lw  $v0, BASE
sw  $s1, 92($v0)
lw  $v0, BASE
sw  $t9, 84($v0)
lw  $v0, BASE
sw  $s0, 96($v0)
lw  $v0, BASE
sw  $t8, 116($v0)
lw  $v0, BASE
sw  $t8, 100($v0)
lw  $v0, BASE
sw  $t5, 88($v0)
lw  $v0, BASE
sw  $a2, 104($v0)
sw  $s6, BASE
lw  $v0, BASE
sw  $t1, 112($v0)
jal  F9_B26
lw  $s2, 4($sp)
lw  $v0, BASE
sw  $s2, 124($v0)
B49: 
# assignw T58 BASE[0] 
lw  $s7, BASE
lw  $s6, 0($s7)
# assignw T59 BASE[8] 
lw  $s5, 8($s7)
# mult T57 T58 T59
mul  $s4, $s6, $s5
# return T57 
# ===== Epilogue =====
move  $sp, $fp
lw  $ra, 8($fp)
sw  $s4, 4($fp)
lw  $fp, 0($fp)
addi  $a0, $fp, 12
sw  $a0, BASE
sw  $sp, STACK
jr  $ra
# ====================
# ===== Updating temporals =====
lw  $v0, BASE
sw  $s5, 136($v0)
lw  $v0, BASE
sw  $s6, 132($v0)
lw  $v0, BASE
sw  $s4, 128($v0)
# ==============================
