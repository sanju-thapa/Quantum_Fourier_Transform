# Quantum Fourier Transform — Qiskit Implementation

A clean, well-commented implementation of the **n-qubit Quantum Fourier Transform (QFT)** using Qiskit, with statevector simulation, numpy FFT verification, and inverse QFT round-trip testing.

## What is the QFT?

The QFT is the quantum analogue of the Discrete Fourier Transform (DFT). It acts on computational basis states as:

$$|j\rangle \mapsto \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i jk/N} |k\rangle$$

where $N = 2^n$.

Unlike the classical FFT (which runs in $O(N \log N)$), the QFT runs in $O(n^2)$ gate operations — exponentially faster in the number of bits.

The QFT is a core subroutine in:
- **Shor's algorithm** (integer factorization)
- **Quantum phase estimation**
- **Quantum signal processing**

## Circuit Structure

For $n$ qubits, the QFT decomposes as:

1. **Hadamard** on qubit $n-1$ (most significant)
2. **Controlled phase rotations** $CP(2\pi/2^k)$ from each lower qubit
3. **Recurse** on the remaining $n-1$ qubits
4. **SWAP network** to reverse bit ordering

Total gate count: $O(n^2)$, specifically $\frac{n(n+1)}{2}$ single-qubit gates + $\frac{n(n-1)}{2}$ CP gates + $\lfloor n/2 \rfloor$ SWAPs.

## Files

| File | Description |
|------|-------------|
| `qft.py` | Core QFT circuit builder (`qft(n)`, `inverse_qft(n)`) |
| `run_qft.py` | Demo: prepare `\|5⟩`, apply QFT, verify vs numpy FFT |
| `qft_output.png` | Output plot (amplitude magnitudes and phases) |

## Usage

```bash
pip install qiskit qiskit-aer matplotlib
python run_qft.py
```

### Build a QFT circuit

```python
from qft import qft, inverse_qft

# 4-qubit QFT
circ = qft(4)
print(circ.decompose().draw())

# Inverse QFT (e.g., for phase estimation)
icirc = inverse_qft(4)
```

### Compose with your own state preparation

```python
from qiskit import QuantumCircuit
from qft import qft

n = 3
qc = QuantumCircuit(n)
qc.h(0)          # Your state prep here
qc.cx(0, 1)

qft_circ = qft(n)
full = qc.compose(qft_circ)
```

## Verification

The demo (`run_qft.py`) performs two checks:

1. **Numpy FFT comparison** — amplitude magnitudes of the Qiskit statevector match the normalized DFT of a unit vector $e_x$, up to numerical precision ($\sim 10^{-16}$). Phase conventions differ because Qiskit uses little-endian qubit ordering vs numpy's big-endian.

2. **IQFT round-trip** — applying QFT then IQFT on $|5\rangle$ recovers $|5\rangle$ exactly.

## Notes on Qubit Ordering

Qiskit uses **little-endian** convention: qubit 0 is the least significant bit. This flips the bit ordering relative to the standard mathematical QFT definition. The SWAP network at the end of the circuit corrects for this so the output matches the standard Fourier basis.

## Author

Sanju — M.Sc. Physics, quantum computing research.  
Related project: [VQE for Transverse Field Ising Model](https://github.com/sanju/vqe-transverse-field-spin-model)

