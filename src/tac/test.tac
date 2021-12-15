@string S "hola"
@string S0 "0000\n"
@label Adios
assignb T7 True
assignw T0 0
assignw T1 1
assignw T2 T1
assignw T3 2
add T4 T2 T3
assignw T5 T4
param T27 20
assignw T27[0] S0
goifnot Adios T5
