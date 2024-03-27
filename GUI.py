from PyQt5 import QtWidgets  # Should work with PyQt5 / PySide2 / PySide6 as well
import pyqtgraph as pg
import numpy as np

## Always start by initializing Qt (only once per application)
app = QtWidgets.QApplication([])

## Define a top-level widget to hold everything
w = QtWidgets.QWidget()
w.setWindowTitle('Game of Life')

## Create some widgets to be placed inside
btn = QtWidgets.QPushButton('Initialize Grid')
text = QtWidgets.QLineEdit('Amount of iterations')
listw = QtWidgets.QListWidget()
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
plot = pg.plot(x, y, pen=None, symbol='o')

## Create a grid layout to manage the widgets size and position
layout = QtWidgets.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)  # button goes in upper-left
layout.addWidget(text, 1, 0)  # text edit goes in middle-left
layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows
## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec()