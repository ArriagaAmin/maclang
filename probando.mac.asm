.text
li  $sp, 0x7fc00000
B0: 
# assignw S1[0] 51 
li  $s7, 51
la  $s6, S1
sw  $s7, 0($s6)
# malloc T27 10 
move  $a0, $s5
li  $v0, 9 
syscall
move  $s4, $v0
# assignw T27[0] 6 
li  $s5, 6
sw  $s5, 0($s4)
# assignb T27[9] 10 
li  $s3, 10
sb  $s3, 9($s4)
# assignb T27[8] 10 
sb  $s3, 8($s4)
# assignb T27[7] 10 
sb  $s3, 7($s4)
# assignb T27[6] 110 
li  $t9, 110
sb  $t9, 6($s4)
# assignb T27[5] 9 
li  $v1, 9
sb  $v1, 5($s4)
# assignb T27[4] 65 
li  $t5, 65
sb  $t5, 4($s4)
# malloc T34 12 
move  $a0, $s1
li  $v0, 9 
syscall
move  $a0, $v0
# assignw T34[0] 2 
li  $s1, 2
sw  $s1, 0($a0)
# assignw T34[8] -69 
lw  $s0, -69
sw  $s0, 8($a0)
# assignw T34[4] 42 
li  $a1, 42
sw  $a1, 4($a0)
# assignw S2[0] 5 
li  $a2, 5
la  $t4, S2
sw  $a2, 0($t4)
# assignw S3[0] 7 
li  $t0, 7
la  $t1, S3
sw  $t0, 0($t1)
# assignw T42 12 
li  $t8, 12
# malloc T40 12 
sw  $a0, T34
move  $a0, $t8
li  $v0, 9 
syscall
move  $t3, $v0
# assignw T40[0] 2 
sw  $s1, 0($t3)
# ===== Updating temporals =====
sw  $t3, T40
sw  $t8, T42
sw  $t4, S2
sw  $s4, T27
sw  $s6, S1
sw  $t1, S3
# ==============================
B32: 
# lt test T42 0
lw  $s7, T42
li  $s6, 0
slt  $s5, $s7, $s6
# ===== Updating temporals =====
sb  $s5, test
# ==============================
B1: 
# sub T42 T42 4
lw  $s7, T42
li  $s6, 4
sub  $s5, $s7, $s6
# goif B3 test 
# ===== Updating temporals =====
sw  $s5, T42
bnez  $s4, B3
# ==============================
B2: 
# goto B1 
j  B1
B3: 
# assignw T40[8] S3 
la  $s7, S3
lw  $s6, T40
sw  $s7, 8($s6)
# assignw T40[4] S2 
la  $s5, S2
sw  $s5, 4($s6)
# assignw S4[0] 5 
li  $s4, 5
la  $s3, S4
sw  $s4, 0($s3)
# param T44 0 
# ===== Parameter =====
la  $v1, T44
la  $t9, 12($sp)
sw  $t9, 0($v1)
# =====================
# assignw T44[0] S1 
la  $t9, S1
lw  $v1, T44
sw  $t9, 0($v1)
# assignw T46 T27[0] 
lw  $t5, T27
lw  $s1, 0($t5)
# mult T47 1 T46
li  $a0, 1
mul  $s0, $a0, $s1
# add T47 T47 4
li  $a1, 4
add  $s0, $s0, $a1
# malloc T45 T47 
move  $a0, $s0
li  $v0, 9 
syscall
move  $a2, $v0
# memcpy T45 T27 T47
sw  $v1, T44
MC0: 
beqz  $s0, MC0_END
addi  $s0, $s0, -1
add  $v0, $t5, $s0
lb  $v0, 0($v0)
add  $v1, $a2, $s0
sb  $v0, 0($v1)
j  MC0
MC0_END: 
# param T48 4 
# ===== Parameter =====
la  $t4, T48
la  $a1, 16($sp)
sw  $a1, 0($t4)
# =====================
# assignw T48[0] T45 
lw  $t4, T48
sw  $a2, 0($t4)
# assignb A0[0] 1 
la  $t0, A0
sb  $a0, 0($t0)
# assignw T50 T34[0] 
lw  $t1, T34
lw  $t8, 0($t1)
# mult T51 4 T50
mul  $t3, $a1, $t8
# add T51 T51 4
add  $t3, $t3, $a1
# malloc T49 T51 
move  $a0, $t3
li  $v0, 9 
syscall
move  $s2, $v0
# memcpy T49 T34 T51
sw  $v1, T44
MC1: 
beqz  $t3, MC1_END
addi  $t3, $t3, -1
add  $v0, $t1, $t3
lb  $v0, 0($v0)
add  $v1, $s2, $t3
sb  $v0, 0($v1)
j  MC1
MC1_END: 
# param T52 8 
# ===== Parameter =====
la  $t6, T52
la  $t2, 20($sp)
sw  $t2, 0($t6)
# =====================
# assignw T52[0] T49 
lw  $t2, T52
sw  $s2, 0($t2)
# assignb A0[1] 1 
sb  $a0, 1($t0)
# assignb A0[2] 0 
li  $t6, 0
sb  $t6, 2($t0)
# assignw T54 T40[0] 
lw  $t7, 0($s6)
# mult T55 4 T54
sw  $s6, T40
sw  $s4, 5
sw  $s3, S4
sw  $s1, T46
sw  $a0, 1
sw  $s0, T47
sw  $a1, 4
sw  $a2, T45
sw  $t4, T48
sw  $t0, A0
sw  $t8, T50
sw  $t3, T51
sw  $s2, T49
sw  $t2, T52
sw  $t6, 0
sw  $t7, T54
mul  $v1, $a1, $t7
# add T55 T55 4
add  $v1, $v1, $a1
# malloc T53 T55 
sw  $s4, 5
sw  $v1, T55
sw  $a0, 1
sw  $t6, 0
move  $a0, $v1
li  $v0, 9 
syscall
move  $v1, $v0
# assignw T56 T55 
# ===== Updating temporals =====
sw  $v1, T56
sw  $v1, T53
# ==============================
B4: 
# sub T56 T56 4
lw  $s7, T56
li  $s6, 4
sub  $s5, $s7, $s6
# lt test T56 0
li  $s4, 0
slt  $s3, $s7, $s4
# goif B6 test 
# ===== Updating temporals =====
sb  $s3, test
sw  $s5, T56
bnez  $s3, B6
# ==============================
B5: 
# assignw T57 T40[T56] 
lw  $s7, T40
lw  $s6, T56
add  $s6, $s6, $s7
lw  $s6, 0($s6)
# assignw T59 T57[0] 
lw  $s5, 0($s6)
# mult T60 1 T59
li  $s4, 1
mul  $s3, $s4, $s5
# add T60 T60 4
li  $t9, 4
add  $s3, $s3, $t9
# malloc T58 T60 
move  $a0, $s3
li  $v0, 9 
syscall
move  $v1, $v0
# assignw T58[0] T58 
sw  $v1, 0($v1)
# memcpy T58 T57 T60
sw  $v1, T58
MC2: 
beqz  $s3, MC2_END
addi  $s3, $s3, -1
add  $v0, $s6, $s3
lb  $v0, 0($v0)
add  $v1, $v1, $s3
sb  $v0, 0($v1)
j  MC2
MC2_END: 
# goto B4 
# ===== Updating temporals =====
sw  $s3, T60
sw  $s5, T59
sw  $s6, T57
j  B4
# ==============================
B6: 
# param T61 16 
# ===== Parameter =====
la  $s6, T61
la  $s7, 28($sp)
sw  $s7, 0($s6)
# =====================
# assignw T61[0] T53 
lw  $s7, T53
lw  $s6, T61
sw  $s7, 0($s6)
# assignb A0[3] 1 
li  $s5, 1
la  $s4, A0
sb  $s5, 3($s4)
# param T62 20 
# ===== Parameter =====
la  $t9, T62
la  $s3, 32($sp)
sw  $s3, 0($t9)
# =====================
# assignw T62[0] S4 
la  $s3, S4
lw  $t9, T62
sw  $s3, 0($t9)
# assignb A0[4] 1 
sb  $s5, 4($s4)
# call T63 F9_B16 6
jal  F9_B16
lw  $v0, 4($sp)
# ===== Updating temporals =====
sw  $t9, T62
sw  $s6, T61
sw  $s4, A0
sw  $v0, T63
# ==============================
B7: 
# exit 0 
li  $a0, 0
li  $v0, 17 
syscall

# *===== Functions Section =====*

F9_B16: 
# ===== Foreword =====
addi  $sp, $sp, 4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, 8
sw  $ra, 4($fp)
addi  $sp, $sp, 20
addi  $a0, $fp, 8
sw  $a0, BASE
sw  $sp, STACK
# ====================
# assignb test A0[4] 
la  $s7, A0
lb  $s6, 4($s7)
# goif B18 test 
# ===== Updating temporals =====
sb  $s6, test
bnez  $s6, B18
# ==============================
B17: 
# assignw BASE[20] S0 
la  $s7, S0
lw  $s6, BASE
sw  $s7, 20($s6)
# ===== Updating temporals =====
sw  $s6, BASE
# ==============================
B18: 
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
sw  $s7, T12
sw  $s7, T11
sw  $s7, T10
sw  $s7, T8
sw  $s5, T13
sw  $s7, T9
# ==============================
B19: 
# assignb T14 T13[T8] 
lw  $s7, T13
lw  $s6, T8
add  $s6, $s6, $s7
lb  $s6, 0($s6)
# add T8 T8 1
lw  $s5, T8
li  $s4, 1
add  $s3, $s5, $s4
# eq test T14 0
li  $t9, 0
seq  $v1, $s6, $t9
# goif B31 test 
# ===== Updating temporals =====
sb  $s6, T14
sw  $s3, T8
sb  $v1, test
bnez  $v1, B31
# ==============================
B20: 
# eq test T14 37
lw  $s7, T14
li  $s6, 37
seq  $s5, $s7, $s6
# goif B22 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B22
# ==============================
B21: 
# printc T14 
lw  $a0, T14
li  $v0, 11 
syscall
# goto B19 
j  B19
B31: 
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
# ===== Epilogue =====
li  $v0, 0
sw  $v0, 0($fp)
lw  $ra, 4($fp)
lw  $fp, -4($fp)
addi  $sp, $sp, -12
jr  $ra
# ====================
# ===== Updating temporals =====
sw  $s6, T15
# ==============================
B22: 
# assignb T14 T13[T8] 
lw  $s7, T13
lw  $s6, T8
add  $s6, $s6, $s7
lb  $s6, 0($s6)
# add T8 T8 1
lw  $s5, T8
li  $s4, 1
add  $s3, $s5, $s4
# eq test T14 99
li  $t9, 99
seq  $v1, $s6, $t9
# goif B27 test 
# ===== Updating temporals =====
sb  $s6, T14
sw  $s3, T8
sb  $v1, test
bnez  $v1, B27
# ==============================
B23: 
# eq test T14 105
lw  $s7, T14
li  $s6, 105
seq  $s5, $s7, $s6
# goif B28 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B28
# ==============================
B24: 
# eq test T14 102
lw  $s7, T14
li  $s6, 102
seq  $s5, $s7, $s6
# goif B29 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B29
# ==============================
B25: 
# eq test T14 115
lw  $s7, T14
li  $s6, 115
seq  $s5, $s7, $s6
# goif B30 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B30
# ==============================
B26: 
# goto B19 
j  B19
B27: 
# assignw T15 BASE[4] 
lw  $s7, BASE
lw  $s6, 4($s7)
# assignb T16 T15[T9] 
lw  $s5, T9
add  $s5, $s5, $s6
lb  $s5, 0($s5)
# printc T16 
move  $a0, $s5
li  $v0, 11 
syscall
# add T9 T9 1
lw  $s4, T9
li  $s3, 1
add  $t9, $s4, $s3
# goto B19 
# ===== Updating temporals =====
sb  $s5, T16
sw  $t9, T9
sw  $s6, T15
j  B19
# ==============================
B28: 
# assignw T15 BASE[8] 
lw  $s7, BASE
lw  $s6, 8($s7)
# assignw T17 T15[T10] 
lw  $s5, T10
add  $s5, $s5, $s6
lw  $s5, 0($s5)
# printi T17 
move  $a0, $s5
li  $v0, 1 
syscall
# add T10 T10 4
lw  $s4, T10
li  $s3, 4
add  $t9, $s4, $s3
# goto B19 
# ===== Updating temporals =====
sw  $t9, T10
sw  $s5, T17
sw  $s6, T15
j  B19
# ==============================
B29: 
# assignw T15 BASE[12] 
lw  $s7, BASE
lw  $s6, 12($s7)
# assignw f3 T15[T11] 
lw  $v0, T11
add  $v0, $s6, $v0
l.s  $f30, ($v0)
# printf f3 
l.s  $f12, f3
li  $v0, 2 
syscall
# add T11 T11 4
lw  $s5, T11
li  $s4, 4
add  $s3, $s5, $s4
# goto B19 
# ===== Updating temporals =====
s.s  $f30, f3
sw  $s3, T11
sw  $s6, T15
j  B19
# ==============================
B30: 
# assignw T15 BASE[16] 
lw  $s7, BASE
lw  $s6, 16($s7)
# assignw T18 T15[T12] 
lw  $s5, T12
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
lw  $s3, T12
add  $t9, $s3, $s4
# goto B19 
# ===== Updating temporals =====
sw  $s5, T18
sw  $t9, T12
sw  $s6, T15
j  B19
# ==============================

.data
BASE: .word  1
STACK: .word  1
A0: .word  5
.align 2
S0: .asciiz  "0000\n"
.align 2
S1: .asciiz  "0000Caracteres: %c %c%cNumeros: %i %i%c%cTextos %s %s%c"
.align 2
S2: .asciiz  "0000Hello"
.align 2
S3: .asciiz  "0000 world!"
.align 2
S4: .asciiz  "0000Final"
T27: .word  1
T34: .word  1
T42: .word  1
T40: .word  1
test: .byte  1
T44: .word  1
T46: .word  1
T47: .word  1
T45: .word  1
T48: .word  1
T50: .word  1
T51: .word  1
T49: .word  1
T52: .word  1
T54: .word  1
T55: .word  1
T53: .word  1
T56: .word  1
T57: .word  1
T59: .word  1
T60: .word  1
T58: .word  1
T61: .word  1
T62: .word  1
T63: .word  1
T8: .word  1
T9: .word  1
T10: .word  1
T11: .word  1
T12: .word  1
T13: .word  1
T14: .byte  1
T15: .word  1
T16: .byte  1
T17: .word  1
f3: .float  1
T18: .word  1
