def merge(A, B):

    """This function sorts and merges two lists of numbers"""

    C = [0]*(len(A+B))
    i = j = k = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = B[j]
            j += 1
            k += 1
        while i < len(A):
            C[k] = A[i]
            k += 1
            i += 1
        while j < len(B):
            C[k] = B[j]
            k += 1
            j += 1
    return(C)


def merg_sort(mass):

    """This function splits list of numbers for 'merge function'"""

    if len(mass) <= 1:
        return
    middle = len(mass)//2
    L = [mass[i] for i in range(middle)]
    R = [mass[i] for i in range(middle, len(mass))]
    merg_sort(L)
    merg_sort(R)
    C = merge(L, R)
    for i in range(len(C)):
        mass[i] = C[i]