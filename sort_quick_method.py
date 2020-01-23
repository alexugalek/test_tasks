def quick_sort(mass):

    """Quick sort with barrier method
      This function sorts list with numbers"""

    if len(mass) <= 1:
        return
    A = []
    B = []
    M = []
    N = len(mass)
    barrier = mass[0]
    for x in range(N):
        if barrier > mass[x]:
            A.append(mass[x])
        elif barrier == mass[x]:
            M.append(mass[x])
        else:
            B.append(mass[x])
    quick_sort(A)
    quick_sort(B)
    N = 0
    for x in (A+M+B):
        mass[N] = x
        N += 1