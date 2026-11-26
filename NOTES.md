# Quantum Computing Notes

These are notes for the IMAPP Quantum Computing sessions.

## Sessions

- **Session 1**: Introduction to qubits and quantum states
- **Session 2**: Quantum gates and circuits

## Key Concepts

### Qubit
A qubit is the basic unit of quantum information. Unlike a classical bit, which is 0 or 1, a qubit can be in a **superposition** of both:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1$$

### Common Gates

| Gate     | Effect                                   |
|----------|------------------------------------------|
| X        | Bit flip: swaps \|0⟩ and \|1⟩              |
| H        | Hadamard: creates an equal superposition |
| Z        | Phase flip: \|1⟩ → −\|1⟩                   |
| CNOT     | Flips the target if the control is \|1⟩   |

### Entanglement
Two qubits are entangled when their joint state can't be written as a product of single-qubit states. An example is the Bell state:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}\left(|00\rangle + |11\rangle\right)$$

## To Do

- [ ] Finish the Session 2 notebook
- [ ] Try building a Bell state circuit
