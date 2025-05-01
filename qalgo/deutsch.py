from enum import Enum
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


class OracleType(Enum):
    CONSTANT_0 = 0,
    CONSTANT_1 = 1,
    BALANCED_X = 2,
    BALANCED_NOT_X = 3


def oracle(oracle_type: OracleType):

    qc = QuantumCircuit(2)

    match oracle_type:
        case OracleType.CONSTANT_0:
            pass
        case OracleType.CONSTANT_1:
            qc.x(1)
        case OracleType.BALANCED_X:
            qc.cx(0, 1)
        case OracleType.BALANCED_NOT_X:
            qc.x(0)
            qc.cx(0, 1)
            qc.x(0)

    return qc


def simulate(oracle_type: OracleType, shots=1024):

    # create two-qubit circuit
    qc = QuantumCircuit(2, 1)

    # initialize answer qubit to minus state
    qc.x(1)
    qc.h(1)

    # apply hadamard to input qubit
    qc.h(0)

    # apply oracle
    qc.compose(oracle(oracle_type), inplace=True)

    # apply hadamard to input qubit
    qc.h(0)

    # measure input qubit
    qc.measure(0, 0)

    # run circuit in Aer simulator
    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)

    # return results
    return job.result()


if __name__ == "__main__":
    shots = 1024
    result = simulate(OracleType.CONSTANT_0, shots=shots)
    print(f"Deutsch Algorithm with constant-0 oracle results into "
          f"{'constant' if result.get_counts()['0'] == shots else 'inconclusive'} function")
    result = simulate(OracleType.CONSTANT_1, shots=shots)
    print(f"Deutsch Algorithm with constant-1 oracle results into "
          f"{'constant' if result.get_counts()['0'] == shots else 'inconclusive'} function")
    result = simulate(OracleType.BALANCED_X, shots=shots)
    print(f"Deutsch Algorithm with balanced-x oracle results into "
          f"{'balanced' if result.get_counts()['1'] == shots else 'inconclusive'} function")
    result = simulate(OracleType.BALANCED_NOT_X, shots=shots)
    print(f"Deutsch Algorithm with balanced-not-x oracle results into "
          f"{'balanced' if result.get_counts()['1'] == shots else 'inconclusive'} function")
