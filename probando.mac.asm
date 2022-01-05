.text
li  $sp, 0x7fc00000
B0: 
# assignw S1[0] 50 
li  $s7, 50
la  $s6, S1
sw  $s7, 0($s6)
# malloc T29 9 
li  $s5, 9
move  $a0, $s5
li  $v0, 9 
syscall
move  $s4, $v0
# assignw T29[0] 5 
li  $s5, 5
sw  $s5, 0($s4)
# assignw T26 T29 
# assignb T26[8] 10 
li  $s3, 10
sb  $s3, 8($s4)
# assignb T26[7] 10 
sb  $s3, 7($s4)
# assignb T26[6] 10 
sb  $s3, 6($s4)
# assignb T26[5] 9 
li  $t9, 9
sb  $t9, 5($s4)
# assignb T26[4] 65 
li  $v1, 65
sb  $v1, 4($s4)
# malloc T37 12 
li  $t5, 12
move  $a0, $t5
li  $v0, 9 
syscall
move  $s1, $v0
# assignw T37[0] 2 
li  $t5, 2
sw  $t5, 0($s1)
# assignw T34 T37 
# assignw T34[8] -69 
li  $a0, -69
sw  $a0, 8($s1)
# assignw T34[4] 42 
li  $s0, 42
sw  $s0, 4($s1)
# assignw S2[0] 5 
la  $a1, S2
sw  $s5, 0($a1)
# assignw S3[0] 7 
li  $a2, 7
la  $t4, S3
sw  $a2, 0($t4)
# assignw T43 12 
li  $t0, 12
# malloc T44 12 
move  $a0, $t0
li  $v0, 9 
syscall
move  $t1, $v0
# assignw T44[0] 2 
sw  $t5, 0($t1)
# assignw T41 T44 
# ===== Updating temporals =====
sw  $t1, T41
sw  $t1, T44
sw  $t0, T43
sw  $s4, T29
sw  $s4, T26
sw  $s1, T37
sw  $s1, T34
# ==============================
B1: 
# sub T43 T43 4
lw  $s7, T43
li  $s6, 4
sub  $s5, $s7, $s6
# lt test T43 4
slt  $s7, $s5, $s6
# goif B3 test 
# ===== Updating temporals =====
sb  $s7, test
sw  $s5, T43
# ==============================
bnez  $s7, B3
B2: 
# goto B1 
j  B1
B3: 
# assignw T41[8] S3 
la  $s7, S3
lw  $s6, T41
sw  $s7, 8($s6)
# assignw T41[4] S2 
la  $s5, S2
sw  $s5, 4($s6)
# assignw S4[0] 5 
li  $s4, 5
la  $s3, S4
sw  $s4, 0($s3)
# param T46 0 
# ===== Parameter =====
la  $v1, T46
la  $v0, 12($sp)
sw  $v0, 0($v1)
# =====================
# assignw T46[0] S1 
la  $t9, S1
lw  $v1, T46
sw  $t9, 0($v1)
# assignw T48 T29[0] 
lw  $t5, T29
lw  $s1, 0($t5)
# mult T49 1 T48
li  $a0, 1
mul  $s0, $a0, $s1
# add T49 T49 4
li  $a1, 4
add  $s0, $s0, $a1
# malloc T50 T49 
move  $a0, $s0
li  $v0, 9 
syscall
move  $a2, $v0
# assignw T47 T50 
# memcpy T47 T29 T49
sw  $v1, T46
MC0: 
beqz  $s0, MC0_END
addi  $s0, $s0, -1
add  $v0, $t5, $s0
lb  $v0, 0($v0)
add  $v1, $a2, $s0
sb  $v0, 0($v1)
j  MC0
MC0_END: 
# param T51 4 
# ===== Parameter =====
la  $t4, T51
la  $v0, 16($sp)
sw  $v0, 0($t4)
# =====================
# assignw T51[0] T50 
lw  $t4, T51
sw  $a2, 0($t4)
# assignb A0[0] 1 
la  $t0, A0
sb  $a0, 0($t0)
# assignw T53 T37[0] 
lw  $t1, T37
lw  $t8, 0($t1)
# mult T54 4 T53
mul  $t3, $a1, $t8
# add T54 T54 4
add  $t3, $t3, $a1
# malloc T55 T54 
move  $a0, $t3
li  $v0, 9 
syscall
move  $s2, $v0
# assignw T52 T55 
# memcpy T52 T37 T54
sw  $v1, T46
MC1: 
beqz  $t3, MC1_END
addi  $t3, $t3, -1
add  $v0, $t1, $t3
lb  $v0, 0($v0)
add  $v1, $s2, $t3
sb  $v0, 0($v1)
j  MC1
MC1_END: 
# param T56 8 
# ===== Parameter =====
la  $t6, T56
la  $v0, 20($sp)
sw  $v0, 0($t6)
# =====================
# assignw T56[0] T55 
lw  $t2, T56
sw  $s2, 0($t2)
# assignb A0[1] 1 
sb  $a0, 1($t0)
# assignb A0[2] 0 
li  $t6, 0
sb  $t6, 2($t0)
# assignw T58 T44[0] 
sw  $v1, T46
lw  $t7, T44
lw  $v1, 0($t7)
# mult T59 4 T58
mul  $t9, $a1, $v1
# add T59 T59 4
add  $t9, $t9, $a1
# malloc T60 T59 
sw  $v1, T46
sw  $v1, T58
move  $a0, $t9
li  $v0, 9 
syscall
move  $v1, $v0
# assignw T57 T60 
# assignw T61 T59 
# ===== Updating temporals =====
sw  $v1, T60
sw  $v1, T57
sw  $t9, T61
sw  $a2, T47
sw  $s0, T49
sw  $s6, T41
sw  $a2, T50
sw  $t8, T53
sw  $t2, T56
sw  $s1, T48
sw  $t4, T51
sw  $t3, T54
sw  $s2, T55
sw  $s2, T52
sw  $t9, T59
# ==============================
B4: 
# sub T61 T61 4
lw  $s7, T61
li  $s6, 4
sub  $s5, $s7, $s6
# lt test T61 4
slt  $s7, $s5, $s6
# goif B6 test 
# ===== Updating temporals =====
sw  $s5, T61
sb  $s7, test
# ==============================
bnez  $s7, B6
B5: 
# assignw T62 T44[T61] 
lw  $s7, T44
lw  $s6, T61
add  $s6, $s6, $s7
lw  $s6, 0($s6)
# assignw T63 T62[0] 
lw  $s5, 0($s6)
# mult T64 1 T63
li  $s4, 1
mul  $s3, $s4, $s5
# add T64 T64 4
li  $t9, 4
add  $s3, $s3, $t9
# malloc T65 T64 
move  $a0, $s3
li  $v0, 9 
syscall
move  $v1, $v0
# assignw T57[T61] T65 
lw  $t5, T57
sw  $v1, T61($t5)
# assignw T66 T60[T61] 
lw  $s1, T60
lw  $a0, T61
add  $a0, $a0, $s1
lw  $a0, 0($a0)
# memcpy T66 T62 T64
sw  $v1, T65
MC2: 
beqz  $s3, MC2_END
addi  $s3, $s3, -1
add  $v0, $s6, $s3
lb  $v0, 0($v0)
add  $v1, $a0, $s3
sb  $v0, 0($v1)
j  MC2
MC2_END: 
# goto B4 
# ===== Updating temporals =====
sw  $a0, T66
sw  $s5, T63
sw  $t5, T57
sw  $s3, T64
sw  $s6, T62
# ==============================
j  B4
B6: 
# param T67 16 
# ===== Parameter =====
la  $s6, T67
la  $v0, 28($sp)
sw  $v0, 0($s6)
# =====================
# assignw T67[0] T60 
lw  $s7, T60
lw  $s6, T67
sw  $s7, 0($s6)
# assignb A0[3] 1 
li  $s5, 1
la  $s4, A0
sb  $s5, 3($s4)
# param T68 20 
# ===== Parameter =====
la  $t9, T68
la  $v0, 32($sp)
sw  $v0, 0($t9)
# =====================
# assignw T68[0] S4 
la  $s3, S4
lw  $t9, T68
sw  $s3, 0($t9)
# assignb A0[4] 1 
sb  $s5, 4($s4)
# call T69 F9_B16 6
jal  F9_B16
lw  $v0, 4($sp)
# ===== Updating temporals =====
sw  $t9, T68
sw  $s6, T67
# ==============================
sw  $v0, T69
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
# ==============================
bnez  $s6, B18
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
sw  $s5, T13
sw  $s7, T12
sw  $s7, T11
sw  $s7, T8
sw  $s7, T10
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
li  $s5, 0
seq  $t9, $s6, $s5
# goif B31 test 
# ===== Updating temporals =====
sb  $s6, T14
sw  $s3, T8
sb  $t9, test
# ==============================
bnez  $t9, B31
B20: 
# eq test T14 37
lw  $s7, T14
li  $s6, 37
seq  $s5, $s7, $s6
# goif B22 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B22
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
li  $s5, 99
seq  $t9, $s6, $s5
# goif B27 test 
# ===== Updating temporals =====
sb  $s6, T14
sw  $s3, T8
sb  $t9, test
# ==============================
bnez  $t9, B27
B23: 
# eq test T14 105
lw  $s7, T14
li  $s6, 105
seq  $s5, $s7, $s6
# goif B28 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B28
B24: 
# eq test T14 102
lw  $s7, T14
li  $s6, 102
seq  $s5, $s7, $s6
# goif B29 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B29
B25: 
# eq test T14 115
lw  $s7, T14
li  $s6, 115
seq  $s5, $s7, $s6
# goif B30 test 
# ===== Updating temporals =====
sb  $s5, test
# ==============================
bnez  $s5, B30
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
# ==============================
j  B19
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
# ==============================
j  B19
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
# ==============================
j  B19
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
# ==============================
j  B19

.data
BASE: .word  1
STACK: .word  1
A0: .word  5
.align 2
S0: .asciiz  "0000\n"
.align 2
S1: .asciiz  "0000Caracteres: %c %c%cNumeros: %i %i%cTextos: %s %s%c"
.align 2
S2: .asciiz  "0000Hello"
.align 2
S3: .asciiz  "0000 world!"
.align 2
S4: .asciiz  "0000Final"
T29: .word  1
T26: .word  1
T37: .word  1
T34: .word  1
T43: .word  1
T44: .word  1
T41: .word  1
test: .byte  1
T46: .word  1
T48: .word  1
T49: .word  1
T50: .word  1
T47: .word  1
T51: .word  1
T53: .word  1
T54: .word  1
T55: .word  1
T52: .word  1
T56: .word  1
T58: .word  1
T59: .word  1
T60: .word  1
T57: .word  1
T61: .word  1
T62: .word  1
T63: .word  1
T64: .word  1
T65: .word  1
T66: .word  1
T67: .word  1
T68: .word  1
T69: .word  1
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
