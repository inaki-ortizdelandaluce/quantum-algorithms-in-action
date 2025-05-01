from enum import Enum
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


class OracleType(Enum):
    CONSTANT = 0,
    BALANCED = 1


def oracle(n, oracle_type: OracleType, bitstring=None):
    """
    Create a Deutsch-Jozsa oracle circuit for n qubits.

    Parameters:
    - n: number of input qubits (int)
    - oracle_type: 'constant' or 'balanced'
    - bitstring: for balanced oracle, a string like '1010' to define f(x) = a·x

    Returns:
    - QuantumCircuit: oracle circuit with (n+1) qubits
    """
    qc = QuantumCircuit(n + 1)

    match oracle_type:
        case OracleType.CONSTANT:
            if bitstring == '1':
                qc.x(n)  # flip the output qubit
        case OracleType.BALANCED:
            if bitstring is None:
                raise ValueError("You must provide a bitstring for balanced oracle.")
            if len(bitstring) != n:
                raise ValueError("Bitstring length must match number of input qubits.")
            for i, bit in enumerate(bitstring):
                if bit == '1':
                    qc.cx(i, n)
    return qc


def circuit(n, oracle_type: OracleType, bitstring):

    # create n+1-qubit circuit
    qc = QuantumCircuit(n + 1, n)

    # initialize answer qubit to one state
    qc.x(n)

    # apply hadamard to input qubits and answer qubit
    qc.h(range(n + 1))

    # apply oracle
    qc.compose(oracle(n, oracle_type, bitstring), inplace=True)

    # apply hadamard to input qubits
    qc.h(range(n))

    # measure input qubits
    qc.measure(range(n), range(n))

    return qc


def simulate(qc: QuantumCircuit, shots=1024):
    # run circuit in Aer simulator
    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)

    # return results
    return job.result()


if __name__ == "__main__":
    shots = 1024
    qc = circuit(n=3, oracle_type=OracleType.CONSTANT, bitstring='1')

    from matplotlib import pyplot as plt
    qc.draw('mpl')
    plt.show()

    result = simulate(qc, shots)

    plot_histogram(result.get_counts())
    plt.show()
