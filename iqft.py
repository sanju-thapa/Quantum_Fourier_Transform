from qft import qft
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def test_roundtrip(n, input_state):
    qc = QuantumCircuit(n)

    for i in range(n):
        if (input_state >> i) & 1:
            qc.x(i)
    qc.append(qft(n), range(n))
    qc.append(qft(n).inverse(), range(n))
    sv = Statevector(qc)
    print(sv)
    return sv
test_roundtrip(3, 5)

