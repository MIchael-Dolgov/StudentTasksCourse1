def aand(A, B):
    return A and B
def orr(A, B):
    return A or B
def nott(A):
    return not(A)
def xor(A, B):
    return orr(aand(A, nott(B)), aand(nott(A), B))
