.text
B0: 
lw  $s7, 7
la  $s6, S1
sw  $s7, 0($s6)
lw  $s5, T31
la  $s6, T31
sw  $s7, 0($s6)
lw  $s6, 0
la  $s5, A0
sw  $s6, 0($s5)
sw  $s6, 1($s6)
sw  $s6, 2($s6)
sw  $s6, 3($s6)
sw  $s6, 4($s6)
addi  $sp, $sp, -4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, -8
sw  $ra, -8($fp)
addi  $sp, $sp, -24
sw  $s5, -12($fp)
addi  $a0, $fp, 4
sw  $a0, BASE
sw  $sp, STACK
jal  F9_B18
lw  $v0, -4($sp)
# Updating the temporals
sw  $s7, T31
sw  $s7, S1
sw  $s6, A0
sw  $v0, T32
B1: 
addi  $sp, $sp, -4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, -8
sw  $ra, -8($fp)
addi  $sp, $sp, -0
addi  $a0, $fp, 4
sw  $a0, BASE
sw  $sp, STACK
jal  F3_B12
lw  $v0, -4($sp)
sw  $v0, T33
B2: 
lw  $s7, T33
lw  $s6, 0
slt  $s5, $s7, $s6
# Updating the temporals
sw  $s5, test
bnez  $s5, B4
B3: 
j  B7
B4: 
lw  $s7, 12
la  $s6, S2
sw  $s7, 0($s6)
lw  $s5, T36
la  $s6, T36
sw  $s7, 0($s6)
lw  $s6, 0
la  $s5, A0
sw  $s6, 0($s5)
sw  $s6, 1($s6)
sw  $s6, 2($s6)
sw  $s6, 3($s6)
sw  $s6, 4($s6)
addi  $sp, $sp, -4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, -8
sw  $ra, -8($fp)
addi  $sp, $sp, -24
sw  $s5, -12($fp)
addi  $a0, $fp, 4
sw  $a0, BASE
sw  $sp, STACK
jal  F9_B18
lw  $v0, -4($sp)
# Updating the temporals
sw  $s7, T36
sw  $s7, S2
sw  $s6, A0
sw  $v0, T37
B5: 
lw  $s7, 0
lw  $a0, T38
li  $v0, 17 
syscall
# Updating the temporals
sw  $s7, T38
B7: 
lw  $s7, 20
la  $s6, S3
sw  $s7, 0($s6)
lw  $s5, T40
la  $s6, T40
sw  $s7, 0($s6)
lw  $s6, 0
la  $s5, A0
sw  $s6, 0($s5)
sw  $s6, 1($s6)
sw  $s6, 2($s6)
sw  $s6, 3($s6)
sw  $s6, 4($s6)
addi  $sp, $sp, -4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, -8
sw  $ra, -8($fp)
addi  $sp, $sp, -24
sw  $s5, -12($fp)
addi  $a0, $fp, 4
sw  $a0, BASE
sw  $sp, STACK
jal  F9_B18
lw  $v0, -4($sp)
# Updating the temporals
sw  $s7, T40
sw  $s6, A0
sw  $s7, S3
sw  $v0, T41
B8: 
lw  $s6, T42
lw  $s7, T33
la  $s6, T42
sw  $s7, 0($s6)
addi  $sp, $sp, -4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, -8
sw  $ra, -8($fp)
addi  $sp, $sp, -4
sw  $s6, -12($fp)
addi  $a0, $fp, 4
sw  $a0, BASE
sw  $sp, STACK
jal  F10_B32
lw  $v0, -4($sp)
# Updating the temporals
sw  $s7, T42
sw  $v0, T43
B9: 
lw  $a0, T43
li  $v0, 17 
syscall
lw  $a0, 0
li  $v0, 17 
syscall
F3_B12: 
li  $v0, 5 
syscall
sw  $v0, T3
lw  $v0, T3
sw  $v0, -4($fp)
lw  $ra, -8($fp)
lw  $fp, 0($fp)
addi  $sp, $sp, 12
jr  $ra
F9_B18: 
lw  $s7, 4
lw  $s6, BASE
lw  $s6, 0($s6)
# Updating the temporals
sw  $s7, T12
sw  $s6, T13
sw  $s7, T9
sw  $s7, T11
sw  $s7, T10
sw  $s7, T8
B19: 
lw  $s7, T13
lw  $s7, T8($s7)
lw  $s6, T8
lw  $s5, 1
add  $s4, $s6, $s5
lw  $s3, 0
seq  $t9, $s7, $s3
# Updating the temporals
sw  $s7, T14
sw  $t9, test
sw  $s4, T8
bnez  $t9, B31
B20: 
lw  $s7, T14
lw  $s6, 37
seq  $s5, $s7, $s6
# Updating the temporals
sw  $s5, test
bnez  $s5, B22
B21: 
lw  $a0, T14
li  $v0, 11 
syscall
j  B19
B31: 
lw  $s7, BASE
lw  $s7, 20($s7)
lw  $a0, T15
li  $v0, 4 
syscall
lw  $v0, 0
sw  $v0, -4($fp)
lw  $ra, -8($fp)
lw  $fp, 0($fp)
addi  $sp, $sp, 12
# Updating the temporals
sw  $s7, T15
jr  $ra
B22: 
lw  $s7, T13
lw  $s7, T8($s7)
lw  $s6, T8
lw  $s5, 1
add  $s4, $s6, $s5
lw  $s3, 99
seq  $t9, $s7, $s3
# Updating the temporals
sw  $s7, T14
sw  $t9, test
sw  $s4, T8
bnez  $t9, B27
B23: 
lw  $s7, T14
lw  $s6, 105
seq  $s5, $s7, $s6
# Updating the temporals
sw  $s5, test
bnez  $s5, B28
B24: 
lw  $s7, T14
lw  $s6, 102
seq  $s5, $s7, $s6
# Updating the temporals
sw  $s5, test
bnez  $s5, B29
B25: 
lw  $s7, T14
lw  $s6, 115
seq  $s5, $s7, $s6
# Updating the temporals
sw  $s5, test
bnez  $s5, B30
B26: 
j  B19
B27: 
lw  $s7, BASE
lw  $s7, 4($s7)
lw  $s7, T9($s7)
lw  $a0, T16
li  $v0, 11 
syscall
lw  $s6, T9
lw  $s5, 1
add  $s4, $s6, $s5
# Updating the temporals
sw  $s7, T15
sw  $s4, T9
sw  $s7, T16
j  B19
B28: 
lw  $s7, BASE
lw  $s7, 8($s7)
lw  $s7, T10($s7)
lw  $a0, T17
li  $v0, 1 
syscall
lw  $s6, T10
lw  $s5, 4
add  $s4, $s6, $s5
# Updating the temporals
sw  $s7, T15
sw  $s4, T10
sw  $s7, T17
j  B19
B29: 
lw  $s7, BASE
lw  $s7, 12($s7)
lw  $s7, T11($s7)
l.s  $f12, f3
li  $v0, 2 
syscall
lw  $s6, T11
lw  $s5, 4
add  $s4, $s6, $s5
# Updating the temporals
sw  $s7, f3
sw  $s4, T11
sw  $s7, T15
j  B19
B30: 
lw  $s7, BASE
lw  $s7, 16($s7)
lw  $s7, T12($s7)
lw  $a0, T18
li  $v0, 4 
syscall
lw  $s6, T12
lw  $s5, 4
add  $s4, $s6, $s5
# Updating the temporals
sw  $s7, T18
sw  $s4, T12
sw  $s7, T15
j  B19
F10_B32: 
lw  $s7, BASE
lw  $s7, 0($s7)
lw  $s6, 0
seq  $s5, $s7, $s6
# Updating the temporals
sw  $s7, T20
sw  $s5, test
bnez  $s5, B34
B33: 
j  B36
B34: 
lw  $s7, 1
lw  $v0, T21
sw  $v0, -4($fp)
lw  $ra, -8($fp)
lw  $fp, 0($fp)
addi  $sp, $sp, 12
# Updating the temporals
sw  $s7, T21
jr  $ra
B36: 
lw  $s7, BASE
lw  $s7, 0($s7)
lw  $s6, 1
sub  $s5, $s7, $s6
lw  $s3, T25
la  $s4, T25
sw  $s5, 0($s4)
addi  $sp, $sp, -4
sw  $fp, 0($sp)
move  $fp, $sp
addi  $sp, $sp, -8
sw  $ra, -8($fp)
addi  $sp, $sp, -4
sw  $s3, -12($fp)
addi  $a0, $fp, 4
sw  $a0, BASE
sw  $sp, STACK
jal  F10_B32
lw  $v0, -4($sp)
# Updating the temporals
sw  $s5, T25
sw  $s5, T23
sw  $s7, T24
sw  $v0, T26
B37: 
lw  $s7, BASE
lw  $s7, 0($s7)
lw  $s6, T26
mul  $s5, $s7, $s6
lw  $v0, T27
sw  $v0, -4($fp)
lw  $ra, -8($fp)
lw  $fp, 0($fp)
addi  $sp, $sp, 12
# Updating the temporals
sw  $s5, T27
sw  $s7, T28
jr  $ra

.data
BASE: .word  1
STACK: .word  1
A0: .word  5
S0: .asciiz  "0000\n"
S1: .asciiz  "0000Input: "
S2: .asciiz  "0000Hasta luego!"
S3: .asciiz  "0000Resultado calculado!"
T31: .word  1
T32: .word  1
T33: .word  1
test: .byte  1
T36: .word  1
T37: .word  1
T38: .word  1
T40: .word  1
T41: .word  1
T42: .word  1
T43: .word  1
T3: .word  1
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
T20: .word  1
T21: .word  1
T24: .word  1
T23: .word  1
T25: .word  1
T26: .word  1
T28: .word  1
T27: .word  1
