from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

app=QApplication([])

window=QWidget()
window.setWindowTitle("Ism-Familya")
window.setGeometry(500, 200, 300, 200)

layout=QVBoxLayout(window)
label=QLabel("Ism-Familya")
label.setAlignment(Qt.AlignCenter)
label.setFont(QFont("Calibri", 24))
layout.addWidget(label)

layout.addSpacing(20)

buttons_layout=QVBoxLayout()

def f1():
    label.setText("Javohir")

def f2():
    label.setText("Ozodov")

def f3():
    label.setText("07.12.2005")

btn1=QPushButton("Ismingiz")
btn1.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn1.clicked.connect(f1)
buttons_layout.addWidget(btn1)

btn2=QPushButton("Familyangiz")
btn2.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn2.clicked.connect(f2)
buttons_layout.addWidget(btn2)

btn3=QPushButton("Tug'ilgan kuningiz")
btn3.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn3.clicked.connect(f3)
buttons_layout.addWidget(btn3)

layout.addLayout(buttons_layout)

window.show()
app.exec_()