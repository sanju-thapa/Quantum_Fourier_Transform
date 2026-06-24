import numpy as np
from qiskit import QuantumCircuit

def qft(n):
    circuit = QuantumCircuit(n)
    for i in range(n):
        circuit.h(i)
        
        for j in range (i+1, n):
            circuit.cp(np.pi/2**(j-i), j, i)    
    
    for i in range(n//2):
         circuit.swap(i, n-i-1)

    return circuit