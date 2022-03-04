import sys
import pennylane as qml
from pennylane import numpy as np


def second_renyi_entropy(rho):
    """Computes the second Renyi entropy of a given density matrix."""
    # DO NOT MODIFY anything in this code block
    rho_diag_2 = np.diagonal(rho) ** 2.0
    return -np.real(np.log(np.sum(rho_diag_2)))


def compute_entanglement(theta):
    """Computes the second Renyi entropy of circuits with and without a tardigrade present.

    Args:
        - theta (float): the angle that defines the state psi_ABT

    Returns:
        - (float): The entanglement entropy of qubit B with no tardigrade
        initially present
        - (float): The entanglement entropy of qubit B where the tardigrade
        was initially present
    """

    dev = qml.device("default.qubit", wires=3)

    # QHACK #
    norm = 1 / (2 ** 0.5)
    AB = norm*np.array([0,1,1,0])
    ABT = norm * np.array([0, np.sin(theta / 2), np.cos(theta / 2), 0, 1, 0, 0, 0])

    @qml.qnode(dev)
    def circuitAB():
        qml.MottonenStatePreparation(AB, wires=[0,1])
        return qml.density_matrix(wires=1)

    @qml.qnode(dev)
    def circuitABT():
        qml.MottonenStatePreparation(ABT, wires=[0, 1, 2])
        return qml.density_matrix(wires=1)

    ABentropy = second_renyi_entropy(circuitAB())
    ABTentropy = second_renyi_entropy(circuitABT())
    return ABentropy,ABTentropy

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    theta = np.array(sys.stdin.read(), dtype=float)

    S2_without_tardigrade, S2_with_tardigrade = compute_entanglement(theta)
    print(*[S2_without_tardigrade, S2_with_tardigrade], sep=",")
