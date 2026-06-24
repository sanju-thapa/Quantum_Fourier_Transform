from qft import qft
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def run_qft(n, input_state):
    qc = QuantumCircuit(n)
    for i in range(n):
        if (input_state >> i) & 1:
            qc.x(i)

