
import sys
import pennylane as qml
from pennylane import numpy as np

## I.10.1
## measure pauli Y

dev = qml.device('default.qubit', wires=1)
pi = 3.14159265359


@qml.qnode(dev)
def circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE AND MEASURE PAULI Y
    qml.RX(pi / 4, wires=0)
    qml.Hadamard(0)
    qml.PauliZ(0)

    # this measures pauli y:
    return qml.expval(qml.PauliY(0))


print(circuit())

