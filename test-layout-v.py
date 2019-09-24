#! /d/Python/Python37/python

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Me'))
layout.addWidget(QPushButton('Piasa'))
window.setLayout(layout)
app.setStyle('Fusion')
window.show()
app.exec_()