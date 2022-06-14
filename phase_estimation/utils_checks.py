import numpy as np


# build matrix for QFT to compare with get_unitary() for circuit (Sanity check)
def qft_unitary(n_qubits):
    """
    Unitary matrix for the Quantum Fourier transform.
    """
    N = 2 ** n_qubits
    list_of_rows = []
    for u in range(N):
        row = [1 / np.sqrt(N) * np.exp(2 * np.pi * 1j * u * v / N) for v in range(N)]
        list_of_rows.append(row)
        qft_mat = np.matrix(list_of_rows)

    # return np.round(qft_mat,3)
    return qft_mat


def qft_unitary_dag(n_qubits):
    """
    Unitary matrix for the Inverse Quantum Fourier Transform.
    """
    return qft_unitary(n_qubits).conj().T
