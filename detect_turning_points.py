import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    signal = np.array(signal, dtype=float)
    n = len(signal)

    if n < 3:
        ##not enough points to have a turning point
        turning_indices = np.array([], dtype=int)
    else:
        diffs = np.zeros(n - 1)
        for i in range(n - 1):
            diffs[i] = signal[i + 1] - signal[i]

        turning = []
        for i in range(1, len(diffs)):
            if (diffs[i] > 0 and diffs[i - 1] < 0) or \
               (diffs[i] < 0 and diffs[i - 1] > 0):
                turning.append(i)

        turning_indices = np.array(turning, dtype=int)

    plt.figure()
    plt.plot(signal, label="Signal")

    for idx in turning_indices:
        plt.plot(idx, signal[idx], "ro")

    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Turning Points of the Signal")
    plt.legend()

    plt.savefig(filename)
    plt.close()

    return turning_indices
