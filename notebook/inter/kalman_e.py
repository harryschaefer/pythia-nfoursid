import numpy as np
from matplotlib import figure as matplotlib_figure
from matplotlib import pyplot as plt

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
from src.nfoursid.kalman import Kalman
from src.nfoursid.state_space import StateSpace


class Kalman_e(Kalman):
    
    def __init__(
            self,
            state_space: StateSpace,
            noise_covariance: np.ndarray
    ):
        super().__init__(state_space, noise_covariance)

    def plot_filtered(self, fig: matplotlib_figure.Figure):  # pragma: no cover
        """
        The top graph plots the filtered output states of the Kalman filter and compares with the measured values.
        The error bars correspond to the expected standard deviations.
        The bottom graph zooms in on the errors between the filtered states and the measured values, compared with
        the expected standard deviations.
        """
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2, sharex=ax1)

        df = self.to_dataframe()

        top_legends, bottom_legends = [], []
        for output_name in self.state_space.y_column_names:
            actual_outputs = df[(output_name, self.actual_label, self.output_label)]
            predicted_outputs = df[(output_name, self.filtered_label, self.output_label)]
            std = df[(output_name, self.filtered_label, self.standard_deviation_label)]

            markers, = ax1.plot(
                list(range(len(actual_outputs))),
                actual_outputs,
                'x'
            )
            line, = ax1.plot(
                list(range(len(actual_outputs))),
                actual_outputs,
                '-',
                color=markers.get_color(),
                alpha=.15
            )
            top_legends.append(((markers, line), output_name))

            prediction_errorbar = ax1.errorbar(
                list(range(len(predicted_outputs))),
                predicted_outputs,
                yerr=std,
                marker='_',
                alpha=.5,
                color=markers.get_color(),
                markersize=10,
                linestyle='',
                capsize=3
            )
            top_legends.append((prediction_errorbar, f'Filtered {output_name}'))

            errors = actual_outputs - predicted_outputs
            markers_bottom, = ax2.plot(
                list(range(len(errors))),
                errors,
                'x'
            )
            lines_bottom, = ax2.plot(
                list(range(len(errors))),
                errors,
                '-',
                color=markers_bottom.get_color(),
                alpha=.15
            )
            bottom_legends.append(((markers_bottom, lines_bottom), f'Error {output_name}'))
            prediction_errorbar_bottom, = ax2.plot(
                list(range(len(predicted_outputs))),
                std,
                '--',
                alpha=.5,
                color=markers.get_color(),
            )
            ax2.plot(
                list(range(len(predicted_outputs))),
                -std,
                '--',
                alpha=.5,
                color=markers.get_color(),
            )
            bottom_legends.append((prediction_errorbar_bottom, rf'Filtered $\sigma(${output_name}$)$'))

        lines, names = zip(*top_legends)
        ax1.legend(lines, names, loc='upper left')
        ax1.set_ylabel('Output $y$ (a.u.)')
        ax1.grid()

        lines, names = zip(*bottom_legends)
        ax2.legend(lines, names, loc='upper left')
        ax2.set_xlabel('Index')
        ax2.set_ylabel(r'Filtering error $y-y_{\mathrm{filtered}}$ (a.u.)')
        ax2.grid()
        ax1.set_title('Kalman filter, filtered state')
        plt.setp(ax1.get_xticklabels(), visible=False)

    def plot_predicted(
            self,
            fig: matplotlib_figure.Figure,
            steps_to_extrapolate: int = 1
    ):  # pragma: no cover
        """
        The top graph plots the predicted output states of the Kalman filter and compares with the measured values.
        The error bars correspond to the expected standard deviations.

        The stars on the top right represent the ``steps_to_extrapolate``-steps ahead extrapolation under no further
        inputs. The bottom graph zooms in on the errors between the predicted states and the measured values, compared
        with the expected standard deviations.
        """
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2, sharex=ax1)

        df = self.to_dataframe()

        extrapolation = self.extrapolate(steps_to_extrapolate)

        top_legends, bottom_legends = [], []
        for output_name in self.state_space.y_column_names:
            actual_outputs = df[(output_name, self.actual_label, self.output_label)]
            predicted_outputs = df[(output_name, self.next_predicted_corrected_label, self.output_label)]
            std = df[(output_name, self.next_predicted_label, self.standard_deviation_label)]
            last_predicted_std = std.iloc[-1]

            markers, = ax1.plot(
                list(range(len(actual_outputs))),
                actual_outputs,
                'x'
            )
            line, = ax1.plot(
                list(range(len(actual_outputs))),
                actual_outputs,
                '-',
                color=markers.get_color(),
                alpha=.15
            )
            top_legends.append(((markers, line), output_name))

            prediction_errorbar = ax1.errorbar(
                list(range(1, len(predicted_outputs)+1)),
                predicted_outputs,
                yerr=std,
                marker='_',
                alpha=.5,
                color=markers.get_color(),
                markersize=10,
                linestyle='',
                capsize=3
            )
            top_legends.append((prediction_errorbar, f'Predicted {output_name}'))
            extrapolation_errorbar = ax1.errorbar(
                list(range(len(self.ys), len(self.ys) + steps_to_extrapolate)),
                extrapolation[output_name].to_numpy(),
                yerr=last_predicted_std,
                marker='*',
                markersize=9,
                alpha=.8,
                color=markers.get_color(),
                linestyle='',
                capsize=3
            )
            top_legends.append((extrapolation_errorbar, f'Extrapolation {output_name} (no input)'))

            errors = actual_outputs.to_numpy()[1:] - predicted_outputs.to_numpy()[:-1]
            markers_bottom, = ax2.plot(
                list(range(1, len(errors)+1)),
                errors,
                'x'
            )
            lines_bottom, = ax2.plot(
                list(range(1, len(errors)+1)),
                errors,
                '-',
                color=markers_bottom.get_color(),
                alpha=.15
            )
            bottom_legends.append(((markers_bottom, lines_bottom), f'Error {output_name}'))
            prediction_errorbar_bottom, = ax2.plot(
                list(range(1, len(predicted_outputs))),
                std[:-1],
                '--',
                alpha=.5,
                color=markers.get_color(),
            )
            ax2.plot(
                list(range(1, len(predicted_outputs))),
                -std[:-1],
                '--',
                alpha=.5,
                color=markers.get_color(),
            )
            bottom_legends.append((prediction_errorbar_bottom, rf'Predicted $\sigma(${output_name}$)$'))

        lines, names = zip(*top_legends)
        ax1.legend(lines, names, loc='upper left')
        ax1.set_ylabel('Output $y$ (a.u.)')
        ax1.grid()

        lines, names = zip(*bottom_legends)
        ax2.legend(lines, names, loc='upper left')
        ax2.set_xlabel('Index')
        ax2.set_ylabel(r'Prediction error $y-y_{\mathrm{predicted}}$ (a.u.)')
        ax2.grid()
        ax1.set_title('Kalman filter, predicted state')
        plt.setp(ax1.get_xticklabels(), visible=False)
