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
from ct_analysing_library.graphing import plot_difference_of_means
from ct_analysing_library.statistical_tests import perform_t_test, baysian_hypothesis_test
import numpy as np

# This is for testing
import seaborn as sns


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, window=None, df=None,
                 column=None, width=5, height=4,
                 dpi=100, plot_type=None, group_by=None, ttest=False):

        if group_by == 'None':
            self.group_by = None
        else:
            self.group_by = group_by
        self.ttest = ttest
        self.window = window
        self.plot_type = plot_type
        self.column = column

        if plot_type == 'histogram' and self.group_by is not None:
            self.fig = self.facet_hist(df, column, group_by)
            FigureCanvas.__init__(self, self.fig)
        else:
            self.fig = Figure(figsize=(width, height), dpi=dpi)
            self.axes = self.fig.add_subplot(111)
            FigureCanvas.__init__(self, self.fig)
            self.compute_initial_figure(self.axes, df)

        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def facet_hist(self, df, column, group_by):

        col_wrap = len(df[group_by].unique()) // 2
        if col_wrap < 4:
            col_wrap = None
        g = sns.FacetGrid(df, hue=group_by, col=group_by,
                          col_wrap=col_wrap)
        g = g.map(sns.distplot, column, kde=False,
                  hist_kws=dict(edgecolor="k", linewidth=2))
        g.fig.tight_layout()
        return g.fig

    def compute_initial_figure(self, axes, df):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Basic plotting functionality"""

    def compute_initial_figure(self, axes, df):
        try:
            if self.plot_type == 'histogram':
                sns.distplot(df[self.column], ax=self.axes,
                             kde=False, hist_kws=dict(edgecolor="k", linewidth=2))

            elif self.plot_type == 'boxplot':
                sns.boxplot(data=df, x=self.column,
                            y=self.group_by, ax=self.axes)
                if self.ttest:
                    u = list(df[self.group_by].unique())
                    s1 = df[df[self.group_by] == u[0]][self.column]
                    try:
                        s2 = df[df[self.group_by] == u[1]][self.column]
                    except IndexError:
                        s2 = s1
                    p = perform_t_test(s1, s2)
                    self.fig.suptitle('P-value of {0}'.format(p))

            elif self.plot_type == 'bayes':
                u = list(df[self.group_by].unique())
                s1 = np.array(df[df[self.group_by] == u[0]][self.column])
                try:
                    s2 = np.array(df[df[self.group_by] == u[1]][self.column])
                    trace, x = baysian_hypothesis_test(s1, s2, u[0], u[1])
                    plot_difference_of_means(trace, ax=self.axes)
                except IndexError:
                    trace, x = baysian_hypothesis_test(
                        s1, s1, u[0], "Duplicate")
                    plot_difference_of_means(trace, ax=self.axes)
                except ValueError:
                    trace, x = baysian_hypothesis_test(
                        s1, s1, u[0], "Duplicate")
                    plot_difference_of_means(trace, ax=self.axes)
            else:
                t = arange(0.0, 3.0, 0.01)
                s = sin(2 * pi * t)
                self.axes.plot(t, s)
            self.fig.tight_layout()
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
