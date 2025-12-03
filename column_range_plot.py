import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    A = np.array(A, dtype=float)
    rows, cols = A.shape

    ranges = np.zeros(cols)

    for j in range(cols):           
        col_min = A[0, j]
        col_max = A[0, j]
        for i in range(rows):        
            if A[i, j] < col_min:
                col_min = A[i, j]
            if A[i, j] > col_max:
                col_max = A[i, j]
        ranges[j] = col_max - col_min

    ##my plot
    plt.figure()
    plt.bar(range(cols), ranges)
    plt.xlabel("Column index")
    plt.ylabel("Range (max - min)")
    plt.title("Column Ranges")
    plt.savefig(filename)
    plt.close()

    return ranges

