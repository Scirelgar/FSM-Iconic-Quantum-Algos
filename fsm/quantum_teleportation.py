from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
import numpy as np


secret = QuantumRegister(1, "Q")
Alice = QuantumRegister(1, "A")
Bob = QuantumRegister(1, "B") 
# No CFP

cr = ClassicalRegister(3, "c") 
# No CFP

qc = QuantumCircuit(secret, Alice, Bob, cr) 

qc.h(Alice) # 1 Entry for functional process H, + 1 Exit
qc.cx(Alice, Bob) # 2 Entries for functional process CNOT, + 1 Exit for Bob

qc.barrier() # no CFP

np.random.seed(42)
theta = np.random.uniform(0.0, 1.0) * np.pi
varphi = np.random.uniform(0.0, 2.0) * np.pi # no CFP


qc.u(theta, varphi, 0.0, secret) # 1 Entry for the functional process U on entry `secret`, + 1 Exit for secret
qc.barrier()


qc.cx(secret, Alice) # 2 Entries for func proc CNOT, + 1 Exit for Alice
qc.h(secret) # 1 Entry for func proc H, 1 Exit for secret
qc.barrier()


qc.measure(Alice, cr[1]) # 1 Entry Alice + 1 Write for func proc measure
qc.measure(secret, cr[0]) # 1 Write for measurement


with qc.if_test((cr[0], 1)): # 1 Read, `if_test` is a func proc, + 1 Entry for the trigger "System", + 1 Exit 
    qc.z(Bob) # 1 Entry for func proc Z, triggered by if_test
with qc.if_test((cr[1], 1)): # 1 Read, `if_test` is a func proc, + 1 Entry for the trigger "System", + 1 Exit 
    qc.x(Bob) # 1 Entry for func proc X, triggered by if_test

qc.measure(Bob, cr[2]) # We removed the u.inverse, because we mean to measure the Encoded message (state) # +1 Entry (Bob) 1 Write for measurement, then 1 Read

qc.draw(output="mpl") 