import numpy as np


def gaussian_eliminate(A, b):
    """
    A: a square (n, n) NumPy array that does not require row swaps
    b: a length-n NumPy array

    Returns:
        (U, c): U is A row-reduced to upper-triangular form, c is b
        transformed by the same row operations, such that Ux = c has
        the same solution as Ax = b.
    """
    # TODO: Implement elimination on copies of A and b in lockstep,
    # from Theory.
    U = A.astype(float).copy()
    c = b.astype(float).copy()
    n = len(b)

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            U[j, i:] -= factor * U[i, i:]
            c[j] -= factor * c[i]

    return U, c
           

    
    


def back_substitute(U, c):
    """
    U: an upper-triangular (n, n) NumPy array
    c: a length-n NumPy array

    Returns:
        x, the solution to Ux = c, solved from the last row up.
    """
    # TODO: Implement back substitution from Theory's formula.
    n = len(c)
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x
