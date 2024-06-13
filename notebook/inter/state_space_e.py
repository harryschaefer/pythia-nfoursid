import numpy as np
from matplotlib import pyplot as plt
from matplotlib import figure as matplotlib_figure

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
from src.nfoursid.state_space import StateSpace


class StateSpace_e(StateSpace):

    def __init__(
            self,
            a: np.ndarray,
            b: np.ndarray,
            c: np.ndarray,
            d: np.ndarray,
    ):
        super().__init__(a, b, c, d)
    
    def plot_input_output(self, fig: matplotlib_figure.Figure):  # pragma: no cover
        """
        Given a matplotlib figure ``fig``, plot the inputs and outputs of the state-space model.
        """
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2, sharex=ax1)

        for output_name, outputs in zip(self.y_column_names, np.array(self.ys).squeeze(axis=2).T):
            ax1.plot(outputs, label=output_name, alpha=.6)
        ax1.legend(loc='upper right')
        ax1.set_ylabel('Output $y$ (a.u.)')
        ax1.grid()

        for input_name, inputs in zip(self.u_column_names, np.array(self.us).squeeze(axis=2).T):
            ax2.plot(inputs, label=input_name, alpha=.6)
        ax2.legend(loc='upper right')
        ax2.set_ylabel('Input $u$ (a.u.)')
        ax2.set_xlabel('Index')
        ax2.grid()

        ax1.set_title('Inputs and outputs of state-space model')
        plt.setp(ax1.get_xticklabels(), visible=False)
