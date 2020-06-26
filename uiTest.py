A = [1,2,3,4]
def prog(a):
    return(a, 6,7)
B = [prog(i) for i in A]
print(B)