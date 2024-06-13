import numpy as np

INPUT_DIM = 3
OUTPUT_DIM = 2
INTERNAL_STATE_DIM = 4

A = np.array([
    [1,  .01,    0,   0],
    [0,    1,  .01,   0],
    [0,    0,    1, .02],
    [0, -.01,    0,   1],
]) / 1.01
B = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 1],
]) / 3
C = np.array([
    [1, 0, 1,  1],
    [0, 0, 1, -1],
])
D = np.array([
    [1, 0, 1],
    [0, 1, 0]
]) / 10

import sympy as sp

sp_A = sp.Matrix([
    [100,    1,    0,    0],
    [0,    100,    1,    0],
    [0,      0,  100,    2],
    [0,     -1,    0,  100]
]) / sp.Rational(101)

sp_B = sp.Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 1]
]) / sp.Rational(3)

sp_C = sp.Matrix([
    [1, 0, 1,  1],
    [0, 0, 1, -1]
]) / sp.Rational(1)

sp_D = sp.Matrix([
    [1, 0, 1],
    [0, 1, 0]
]) / sp.Rational(10)
