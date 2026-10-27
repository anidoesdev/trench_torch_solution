import numpy as np


def trace(A):
    """
    A: a square (n, n) NumPy array

    Returns:
        The sum of A's diagonal entries.
    """
    # TODO: Implement tr(A) = Sum_i A[i, i] from Theory.
    tr_A = 0
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            if i == j:
                tr_A += A[i][j]
    return tr_A


def trace_of_product(A, B):
    """
    A: shape (m, n)
    B: shape (n, m), so A @ B is a valid square (m, m) matrix

    Returns:
        trace(A @ B), computed WITHOUT forming the full product A @ B --
        use the cyclic-property shortcut from Theory instead.
    """
    # TODO: Implement using the sum(A * B.T) identity from Theory.
    return float(np.sum(A*B.T))
