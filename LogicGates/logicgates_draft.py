def AND(A, B):
    if A and B > 0:
        return True
    else:
        return False

def NOT(A):
    if A > 0:
        return False
    else:
        return True

def OR(A, B):
    if (A or B) == 1:
        return True
    else:
        return False

def XOR(A, B):
    if A != B:
        return True
    else:
        return False

def NAND(A, B):
    if not (A and B) > 0:
        return True
    else:
        return False
    # TODO.... NOT(AND(A, B))

"""
// False
print(AND(1, 0))

// False
print(AND(0, 0))

// True
print(AND(1, 1))
"""

# print(NAND(1,1))
# print(NOT(1))
# print(OR(0, 0))
print(XOR(1, 1))

