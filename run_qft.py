from qft import qft
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def run_qft(n, input_state):
    #1. Initialize the quantum circuit with 'n' qubits
    qc = QuantumCircuit(n)

    #2. State preparation: Encode the integer into binary qubits 
    # Loop through each qubit index
    for i in range(n):
        # Extract the i-th bit of the integer using right-shift and bitwise AND
        if (input_state >> i) & 1:
            qc.x(i) # Apply the X gate if the bit is 1

     # Append the QFT operation to the circuit
    qc.append(qft(n), range(n))
    sv = Statevector(qc)
    print(sv)
    return qc 

circuit = run_qft(3,5)
print(circuit.decompose().draw())