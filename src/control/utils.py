
# A library for control systems, transfer functions, and state space models.

import numpy as np
import control as ct

from ..nfoursid.state_space import StateSpace

class Utils:

    def ss2tf(ssm: StateSpace, dt: float = None):

        a = ssm.a
        b = ssm.b
        c = ssm.c
        d = ssm.d

        tf = ct.ss2tf(a, b, c, d)

        return tf

    def tf2ss(tf: ct.TransferFunction):

        a, b, c, d = ct.tf2ss(tf)

        ssm = StateSpace(a, b, c, d)

        return ssm
