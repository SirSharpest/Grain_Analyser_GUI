import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ct_analysing_library.graphing import plot_histogram as hist_func

# This is for testing
import seaborn as sns


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, window=None, df=None,
                 column=None, width=5, height=4,
                 dpi=100, plot_type=None, group_by=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.window = window
        self.axes = fig.add_subplot(111)
        self.plot_type = plot_type
        self.group_by = group_by
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.column = column
        self.compute_initial_figure(self.axes, df)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, axes, df):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Basic plotting functionality"""

    def compute_initial_figure(self, axes, df):
        try:
            print('Trying to make figure')
            if self.plot_type == 'histogram':
                sns.distplot(df[self.column], ax=self.axes, kde=False)
            elif self.plot_type == 'boxplot':
                sns.boxplot(data=df, x=self.column,
                            y=self.group_by, ax=self.axes)
            else:
                t = arange(0.0, 3.0, 0.01)
                s = sin(2 * pi * t)
                self.axes.plot(t, s)
        except ValueError:
            print('Column:\t{0} is giving problems'.format(self.column))
            print('\nHelp! NaN Imma just make a volume plot\n')
            QMessageBox.warning(self.window, "Error",
                                "Data looks bad, try cleaning first")
        except TypeError:
            print('\nBad comparison types in column:\t{0}'.format(self.column))
