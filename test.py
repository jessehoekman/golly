import pyqtgraph as pg
from PyQt5 import QtWidgets
import numpy as np
import time

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Temperature vs time plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)        
        self.plot_graph.plot(x, y, pen=None, symbol='o')

app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()