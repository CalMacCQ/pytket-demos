from pytket import Circuit, OpType


def qft_layer(n_qubits: int, target=0):
    """
    Creates one layer of the Quantum Fourier Transform (QFT)
    """
    circ = Circuit(n_qubits)
    # circ.add_barrier([x for x in range(n_qubits)]) #add barrier to preserve pattern - looks better
    circ.H(target)
    if n_qubits - target == 1:
        return circ

    control = target + 1
    for j in range(1, n_qubits):
        circ.add_gate(OpType.CU1, 0.5 ** j, [control, target])
        control += 1

        if control >= n_qubits:
            return circ


def swap_circ(n_qubits: int):
    """
    Creates a swap circuit to append to the QFT circuit.
    """
    scirc = Circuit(n_qubits)

    for i in range(0, n_qubits // 2):
        scirc.add_gate(OpType.SWAP, [i, n_qubits - i - 1])

    return scirc


def build_qft(n_qubits: int):
    """
    Builds the circuit for the Quantum Fourier Transform 
    """
    qft_circ = Circuit()
    for target in range(0, n_qubits):
        qft_circ.append(qft_layer(n_qubits, target))

    qft_circ.append(swap_circ(n_qubits))
    return qft_circ


def build_inverse_qft(n_qubits: int):
    """
    Creates the circuit for the inverse QFT.
    """
    return build_qft(n_qubits).dagger()
