from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
from src.nfoursid.nfoursid import NFourSID


class NFourSID_e(NFourSID):
    
    def __init__(
            self,
            dataframe: pd.DataFrame,
            output_columns: List[str],
            input_columns: List[str] = None,
            num_block_rows: int = 2
    ):
        super().__init__(dataframe, output_columns, input_columns, num_block_rows)
    
    def plot_eigenvalues(self, ax: plt.axes):  # pragma: no cover
        """
        Plot the eigenvalues of the :math:`R_{32}` matrix, so that the order of the state-space model can be determined.
        Since the :math:`R_{32}` matrix should have been calculated, this function can only be used after
        performing ``self.subspace_identification``.
        """
        if self.R32_decomposition is None:
            raise Exception('Perform subspace identification first.')

        ax.semilogy(np.diagonal(self.R32_decomposition.eigenvalues), 'x')
        ax.set_title('Estimated observability matrix decomposition')
        ax.set_xlabel('Index')
        ax.set_ylabel('Eigenvalue')
        ax.grid()
