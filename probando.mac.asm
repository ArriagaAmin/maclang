.text
li  $sp, 0x7fc00000
B0: 
# assignw S1[0] 16 
li  $s7, 16
la  $s6, S1
sw  $s7, 0($s6)
# malloc T23 6 
move  $a0, $s5
li  $v0, 9 
syscall
move  $s4, $v0
# assignw T23[0] 2 
li  $s5, 2
lw  $s4, T23
sw  $s5, 0($s4)
# assignb T23[5] 10 
li  $s3, 10
sb  $s3, 5($s4)
# assignb T23[4] 10 
sb  $s3, 4($s4)
# param T26 0 
# ===== Parameter =====
la  $v1, T26
la  $t9, 12($sp)
sw  $t9, 0($v1)
# =====================
# assignw T26[0] S1 
lw  $t9, T26
sw  $s6, 0($t9)
# assignw T28 T23[0] 
lw  $v1, 0($s4)
# mult T29 1 T28
li  $t5, 1
mul  $s1, $t5, $v1
# add T29 T29 4
li  $a0, 4
add  $s1, $s1, $a0
# malloc T27 T29 
sw  $a0, 4
move  $a0, $s1
li  $v0, 9 
syscall
move  $s0, $v0
# memcpy T27 T23 T29
sw  $v1, T28
lw  $s0, T27
lw  $s4, T23
lw  $s1, T29
MC0: 
beqz  $s1, MC0_END
addi  $s1, $s1, -1
add  $v0, $s4, $s1
lb  $v0, 0($v0)
add  $v1, $s0, $s1
sb  $v0, 0($v1)
j  MC0
MC0_END: 
# param T30 4 
# ===== Parameter =====
la  $s0, T30
la  $a0, 16($sp)
sw  $a0, 0($s0)
# =====================
# assignw T30[0] T27 
lw  $s0, T27
lw  $a1, T30
sw  $s0, 0($a1)
# assignb A0[0] 1 
la  $a2, A0
sb  $t5, 0($a2)
# assignb A0[1] 0 
li  $t4, 0
sb  $t4, 1($a2)
# assignb A0[2] 0 
sb  $t4, 2($a2)
# assignb A0[3] 0 
sb  $t4, 3($a2)
# assignb A0[4] 0 
sb  $t4, 4($a2)
# call T31 F9_B10 6
jal  F9_B10
lw  $v0, 4($sp)
# ===== Updating temporals =====
sw  $s1, T29
sw  $t9, T26
sw  $s4, T23
sw  $s6, S1
sw  $a1, T30
sw  $a2, A0
sw  $v0, T31
# ==============================
B1: 
# exit 0 
li  $a0, 0
li  $v0, 17 
syscall

# *===== Functions Section =====*

F9_B10: 
# ===== Foreword =====
addi  $sp, $sp, 4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, 8
sw  $ra, 4($fp)
addi  $sp, $sp, 8
addi  $a0, $fp, 8
sw  $a0, BASE
sw  $sp, STACK
# ====================
# assignb test A0[4] 
la  $s7, A0
lb  $s6, 4($s7)
# goif B12 test 
# ===== Updating temporals =====
sb  $s6, test
bnez  $s6, B12
# ==============================
B11: 
# assignw BASE[20] S0 
la  $s7, S0
lw  $s6, BASE
sw  $s7, 20($s6)
# ===== Updating temporals =====
sw  $s6, BASE
# ==============================
B12: 
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
sw  $s7, T8
sw  $s7, T9
sw  $s7, T11
sw  $s7, T10
# ==============================
B13: 
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
# goif B25 test 
# ===== Updating temporals =====
sb  $s6, T14
sw  $s3, T8
sb  $v1, test
bnez  $v1, B25
# ==============================
B14: 
# eq test T14 37
lw  $s7, T14
li  $s6, 37
seq  $s5, $s7, $s6
# goif B16 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B16
# ==============================
B15: 
# printc T14 
lw  $a0, T14
li  $v0, 11 
syscall
# goto B13 
j  B13
B25: 
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
B16: 
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
# goif B21 test 
# ===== Updating temporals =====
sb  $s6, T14
sw  $s3, T8
sb  $v1, test
bnez  $v1, B21
# ==============================
B17: 
# eq test T14 105
lw  $s7, T14
li  $s6, 105
seq  $s5, $s7, $s6
# goif B22 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B22
# ==============================
B18: 
# eq test T14 102
lw  $s7, T14
li  $s6, 102
seq  $s5, $s7, $s6
# goif B23 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B23
# ==============================
B19: 
# eq test T14 115
lw  $s7, T14
li  $s6, 115
seq  $s5, $s7, $s6
# goif B24 test 
# ===== Updating temporals =====
sb  $s5, test
bnez  $s5, B24
# ==============================
B20: 
# goto B13 
j  B13
B21: 
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
# goto B13 
# ===== Updating temporals =====
sw  $s6, T15
sb  $s5, T16
sw  $t9, T9
j  B13
# ==============================
B22: 
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
# goto B13 
# ===== Updating temporals =====
sw  $s6, T15
sw  $t9, T10
sw  $s5, T17
j  B13
# ==============================
B23: 
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
# goto B13 
# ===== Updating temporals =====
s.s  $f30, f3
sw  $s6, T15
sw  $s3, T11
j  B13
# ==============================
B24: 
# assignw T15 BASE[16] 
lw  $s7, BASE
lw  $s6, 16($s7)
# assignw T18 T15[T12] 
lw  $s5, T12
add  $s5, $s5, $s6
lw  $s5, 0($s5)
# print T18 
move  $a0, $s5
li  $v0, 4 
syscall
# add T12 T12 4
lw  $s4, T12
li  $s3, 4
add  $t9, $s4, $s3
# goto B13 
# ===== Updating temporals =====
sw  $s5, T18
sw  $s6, T15
sw  $t9, T12
j  B13
# ==============================

.data
BASE: .word  1
STACK: .word  1
A0: .word  5
.align 2
S0: .asciiz  "0000\n"
.align 2
S1: .asciiz  "0000Hello %c%cworld!"
T23: .word  1
T26: .word  1
T28: .word  1
T29: .word  1
T27: .word  1
T30: .word  1
T31: .word  1
test: .byte  1
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
