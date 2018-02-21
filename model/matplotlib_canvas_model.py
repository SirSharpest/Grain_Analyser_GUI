import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ct_analysing_library.graphing import plot_histogram as hist_func

# This is for testing
import seaborn as sns


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, df=None,
                 column=None, width=5, height=4,
                 dpi=100, plot_type=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.plot_type = plot_type
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
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self, axes, df):
        if self.plot_type == 'histogram':
            sns.distplot(df[self.column], ax=self.axes)
            #= hist_func(df, self.column)
        else:
            t = arange(0.0, 3.0, 0.01)
            s = sin(2 * pi * t)
            self.axes.plot(t, s)
