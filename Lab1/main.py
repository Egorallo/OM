import numpy as np

if __name__ == "__main__":
    n = int(input("Enter the size of the matrix: "))
    x = np.array(input("Enter the elements of vector x: ").split(), dtype=int)
    ith = int(input("Enter the i: "))

    print("Enter the elements of matrix A: ")
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        A.append(row)

    A = np.array(A)

    A_inv = np.linalg.inv(A)

    A_altered = A.copy()
    A_altered[:, ith - 1] = x  # ith-1 because the index starts from 0

    l = A_inv @ x
    # check if ith column of l is equal to zero
    if l[ith - 1] == 0:
        raise Exception("Matrix is not reversible")
    else:
        print("Matrix is reversible")
    pass

    # swap ith element of l to -1
    l_swapped = l.copy()
    l_swapped[ith - 1] = -1

    l_dot = -1 / l[ith - 1] * l_swapped

    Q = np.eye(n)

    Q[:, ith - 1] = l_dot

    A_altered_inv = Q @ A_inv

    print("Matrix A:\n", A)
    print("Reversed matrix A:\n", A_inv)
    print("Vector x:\n", x)
    print("Altered matrix A:\n", A_altered)
    print("Final altered inverted matrix A:\n", A_altered_inv)
