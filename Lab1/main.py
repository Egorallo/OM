import numpy as np
if __name__ == "__main__":
    # get user's input for matrix A with given size of n
    n = int(input("Enter the size of the matrix: "))
    # Now accept user's input for the matrix A
    def inputMatrix(n):
        A = []
        for i in range(n):
            row = list(map(int, input().split()))
            A.append(row)
        return A
    A = inputMatrix(n)
    # Now accept vector x with height n
    x = list(map(int, input().split()))
    # Multiply two matrices
    