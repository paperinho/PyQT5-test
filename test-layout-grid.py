#! /d/Python/Python37/python

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QComboBox, QMessageBox
from PyQt5 import QtGui 

# Application and windows design
app = QApplication([])
window = QWidget()
layout = QGridLayout()
labelsel = QLabel('Selezionare la porta seriale:')
combosel = QComboBox()
labelapp = QLabel('IC-7300 Time & Date Sync by IW2NOY')
buttonsync = QPushButton('Sync IC-7300 !')
buttonquit = QPushButton('Chiudi')
layout.addWidget(labelapp, 0,0,1,2)
labelapp.setFont(QtGui.QFont("Verdana", 12, QtGui.QFont.Bold)) # This use QtGui
layout.addWidget(labelsel, 1,0)
layout.addWidget(combosel, 1,1)
layout.addWidget(buttonquit, 2,0)
layout.addWidget(buttonsync, 2,1)
window.setLayout(layout)
app.setStyle('Fusion')

def on_buttonquit_clicked():
    app.quit()
buttonquit.clicked.connect(on_buttonquit_clicked)

def get_serial():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports(include_links=False)
    for port in ports :
        print(port.device)
        combosel.addItem(port.device)
get_serial()

def msg_alert():
    alert = QMessageBox()
    alert.setText(str(combosel.currentText()))
    alert.exec_()

buttonsync.clicked.connect(msg_alert)

window.show()
app.exec_()