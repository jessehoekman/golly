import pyqtgraph as pg
from PyQt5 import QtWidgets
import numpy as np
import time
from gol import Rules

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Needs a layout scheme
        # Buttons for initializing the grid and stepping through the iterations.
        # A text box for the user to input the amount of iterations.
        # A plot to display the grid.

        self.setWindowTitle('Game of Life')
        self.layout = QtWidgets.QGridLayout(self)

        # Create button objects
        self.initBtn = QtWidgets.QPushButton('Initialize Random Grid')
        self.startBtn = QtWidgets.QPushButton('Start Iterations',self)

        # Input
        self.size = QtWidgets.QLineEdit('Size')
        self.iterationsInput = QtWidgets.QLineEdit('Amount of iterations',self)

        # Widget
        self.plotWidget = pg.PlotWidget()

        # Add buttons in layout
        self.layout.addWidget(self.initBtn, 0, 0)
        self.layout.addWidget(self.startBtn, 0, 11)
        self.layout.addWidget(self.size, 1, 0)      
        self.layout.addWidget(self.iterationsInput, 1, 2)
        self.layout.addWidget(self.plotWidget, 3, 0, 3, 3)

        # Click events
        self.startBtn.clicked.connect(self.start_iterations)
        self.initBtn.clicked.connect(self.initialize_grid)

    def initialize_grid(self):
        self.rows = int(self.size.text())
        self.cols = int(self.size.text())
        self.rules = Rules(self.rows, self.cols)
        self.update_plot()

    def update_plot(self):
        self.plotWidget.clear()
        alive_cells = np.argwhere(self.rules.current_state == 1)
        if len(alive_cells) > 0:
            x, y = alive_cells.T
            self.plotWidget.plot(x, y, pen=None, symbol='x', symbolBrush='w')  # 'w' for white; change as needed

    def start_iterations(self):
        self.rules = Rules(self.cols, self. rows )
        try:
            num_iterations = int(self.iterationsInput.text())
            self.performIterations(num_iterations)
        except ValueError:
            print("Please enter a valid number of iterations.")

    def performIterations(self, num_iterations):
        for _ in range(num_iterations):
            self.rules.game_step()
            self.update_plot()
            QtWidgets.qApp.processEvents()

    def perform_game_step(self):
        self.rules.game_step()
        self.update_plot()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([sys.argv])
    ex = App()
    ex.show()
    sys.exit(app.exec_())