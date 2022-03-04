#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    source = cnot.wires[0]
    dest = cnot.wires[1]
    # infinity constant:
    infinity = np.inf
    # agenda[0]  is length, while agenda[1] is parent node. source has no parent so stays -1
    agenda = [[infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
    closed = [0,0,0,0,0,0,0,0,0] # 0 means open, 1 means closed
    closed[source] = 1
    agenda[0][source] = 0

    # This method returns the index of the shortest path so far.
    # simplified brute force version of a priority queue!
    def shortest(agenda):
        min = infinity
        minIndex = infinity
        for i in range(9):
            #print("i is ", i)
            if agenda[0][i] < min:
                if closed[i] == 0:
                    min = agenda[0][i]
                    minIndex = i
        return minIndex

    # performing a messy version of dijkstra's algorithm here.
    def dfs(u):
        while closed[dest] == 0:
            for v in graph[u]:
                #print("v is ", v)
                newWeight = agenda[0][u] + 1
                #print("newWeight = ", newWeight)
                if newWeight <= agenda[0][v]:
                    #print("YES")
                    agenda[0][v] = newWeight
                    agenda[1][v] = u
            u = shortest(agenda)
            #print("Shortest u is ", u)
            if u == infinity:
                return
            closed[u] = 1

    # call dfs to get the shortest path to all nodes in graph
    dfs(source)
    # print("result is ", agenda[0][dest]+1)

    # number of cnot gates is equal to 2 * ((path to destination) - 1)
    return 2*(agenda[0][dest]-1)
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
