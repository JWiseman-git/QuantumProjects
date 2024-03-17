import cirq

q = cirq.LineQubit(1)

# I = cirq.unitary(cirq.X)
#
# o = cirq.H(cirq.LineQubit(1))
#
# circuit = cirq.Circuit()
# qubits = cirq.LineQubit.range(3)
# circuit.append(cirq.H(qubits[0]))
# circuit.append(cirq.H(qubits[1]))
# circuit.append(cirq.H(qubits[2]))
# print(circuit)
#
# print(cirq.Circuit(cirq.SWAP(q, q + 1) for q in cirq.LineQubit.range(3)))

import cirq

def less_than_circuit(numbers, input_value):
    num_qubits = len(numbers)
    input_qubits = [cirq.GridQubit(i, 0) for i in range(num_qubits)]
    output_qubits = [cirq.GridQubit(i, 1) for i in range(num_qubits)]

    circuit = cirq.Circuit()

    # Apply X gate to input qubits based on input value
    for i, qubit in enumerate(input_qubits):
        if (input_value >> i) & 1:
            circuit.append(cirq.X(qubit))

    # Apply comparison gates
    for input_qubit, output_qubit in zip(input_qubits, output_qubits):
        circuit.append(cirq.CX(input_qubit, output_qubit))

    return circuit

# Example usage
numbers = [3, 5, 2, 7]  # List of numbers
input_value = 4         # Input value to compare against

circuit = less_than_circuit(numbers, input_value)