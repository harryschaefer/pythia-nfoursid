import numpy as np

INPUT_DIM = 4
OUTPUT_DIM = 2
INTERNAL_STATE_DIM = 16

w1 = 2 * np.pi * 50

# Current controller
Kii = 60  # Integral gain of CC
Kpi = 9  # Proportional gain of CC
B = 0  # feedforward gain of inner CC
Td = 3e-4  # sampling period of digital com

# Line filter
Lf1 = 450e-6  # inductance of LCL line filter (H)
Rf1 = 3e-3  # internal resistance of first inductor in LCL filter (Ohm)
Lf2 = 450e-6  # inductance of LCL line filter (H)
Rf2 = 3e-3  # internal resistance of second inductor in LCL filter (Ohm)
Cf = 50e-6  # capacitance of LCL line filter (F)

# @ POC
V2d = 469  # d axis POC voltage (V)
I2d = 1000  # d axis POC current (A)
I2q = 500  # q axis POC current (A)

# PLL
Kipll = 200 / 575  # integral gain of PLL
Kppll = 20 / 575  # proportional gain of PLL

# CC-PLL-GFLI SSM from Appendix C
A = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [Kii, 0, -120 / (Td ** 3), -60 / (Td ** 2), -12 / Td, 0, 0, 0, 0, 0, -Kpi, -w1 * (Lf1 + Lf2), 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, Kii, 0, 0, 0, -120 / (Td ** 3), -60 / (Td ** 2), -12 / Td, 0, 0, w1 * (Lf1 + Lf2), -Kpi, 0, 0, -B * V2d, 0],
    [-Kii / Lf1, 0, 240 / (Lf1 * Td ** 3), 0, 24 / (Lf1 * Td), 0, 0, 0, -Rf1 / Lf1, w1, Kpi / Lf1, w1 * (Lf1 + Lf2) / Lf1, -1 / Lf1, 0, 0, 0],
    [0, -Kii / Lf1, 0, 0, 0, 240 / (Lf1 * Td ** 3), 0, 24 / (Lf1 * Td), -w1, -Rf1 / Lf1, -w1 * (Lf1 + Lf2) / Lf1, Kpi / Lf1, 0, -1 / Lf1, B * V2d / Lf1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -Rf2 / Lf2, w1, 1 / Lf2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -w1, -Rf2 / Lf2, 0, 1 / Lf2, V2d / Lf2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1 / Cf, 0, -1 / Cf, 0, 0, w1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1 / Cf, 0, -1 / Cf, -w1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -Kppll * V2d, Kipll],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -V2d, 0]
])

B = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [Kpi, 0, B, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, Kpi, 0, B],
    [-Kpi / Lf1, 0, -B / Lf1, 0],
    [0, -Kpi / Lf1, 0, -B / Lf1],
    [0, 0, -1 / Lf2, 0],
    [0, 0, 0, -1 / Lf2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, Kppll],
    [0, 0, 0, 1]
])

C = np.array([
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [1, 0],
    [0, 1],
    [0, 0],
    [0, 0],
    [-I2q, I2d],
    [0, 0]
]).transpose()

D = np.zeros((2, 4))
