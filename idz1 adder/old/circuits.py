from gates import *
def half_adder(A, B) -> ["carry", "sum"]:
    return [aand(A, B), xor(A, B)]

def full_adder(A, B, Cin) -> ["carry", "sum"]:
    half1 = half_adder(A, B)
    half2 = half_adder(half1[1], Cin)
    return [orr(half1[0], half2[0]), half2[1]]

def full_8_bit_adder(A: "list", B: "list", Cin: "bool"):
    result = [False, False, False, False, False, False, False, False]
    carry_out = Cin
    for i in range(8):
        res = full_adder(A[7-i], B[7-i], carry_out)
        carry_out = res[0]
        result[7-i] = res[1]

    return [carry_out, result]
num1 = [1,0,0,0,0,0,1,1]
num2 = [1,0,0,0,0,0,1,1]
print(full_8_bit_adder(num1, num2, 0))
