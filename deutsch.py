from qiskit import Aer, assemble
from qiskit.quantum_info.operators import Operator


def deutsch(function):
    """Implements Deutsch's algorithm.

    Args:
        function (QuantumCircuit): Deutsch function to solve.
            Must be a 2-qubit circuit, and either balanced,
            or constant.
    Returns:
        bool: True if the circuit is balanced, otherwise False.
    """

    qc = QuantumCircuit(2,1)
    qc.x(1)
    qc.h([0,1])
    qc.append(Operator(function),[0,1])
    qc.h(0)
    qc.measure(0,0)

    
    svsim = Aer.get_backend('aer_simulator')
    final_state = svsim.run(qc).result().get_counts()
    final_state = list(final_state.keys())[0]
    if final_state == '1':
      return 'True'
    if final_state == '0':
      return 'False'


f =deutsch_problem()
display(f.draw())
deutsch(f)
