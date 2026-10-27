import numpy as np


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """
    Mirrors np.dot(a, b) / torch.dot(a, b) for two 1D vectors:

        a . b = sum_i(a_i * b_i)

    A single scalar, the sum of the elementwise product.
    """
    prod = 0.0
    for i in range(len(a)):
        prod += a[i] * b[i]
    return prod


def l1_norm(x: np.ndarray) -> float:
    """
    The L1 ("Manhattan") norm: sum of absolute values.

        ||x||_1 = sum_i(|x_i|)
    """
    x_l1 = 0
    for i in range(len(x)):
        x_l1 += abs(x[i])
    return x_l1


def l2_norm(x: np.ndarray) -> float:
    """
    The L2 ("Euclidean") norm: the vector's straight-line length.

        ||x||_2 = sqrt(sum_i(x_i^2)) = sqrt(x . x)
    """
    x_l2 = 0
    for i in range(len(x)):
        x_l2 += (x[i] * x[i])
    return np.sqrt(x_l2)


def linf_norm(x: np.ndarray) -> float:
    """
    The L-infinity ("max") norm: the single largest magnitude entry.

        ||x||_inf = max_i(|x_i|)
    """
    x_inf = x[0]
    for i in range(len(x)):
        x_inf = max(abs(x[i]),x_inf)
    return x_inf
