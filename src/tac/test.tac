@string S "hola"
@label Adios
assignb T7 True
assignw T0 0
assignw T1 1
assignw T2 T1
assignw T3 2
add T4 T2 T3
assignw T5 T4
assignb T4 T3[T2]
goifnot Adios T5
