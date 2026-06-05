import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
    )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
font1=QFont("Calibri", 20,)

import random

app=QApplication([])

window=QWidget()
window.setWindowTitle("Random son")
window.setGeometry(1300, 190, 350, 600)
window.setStyleSheet("background-color: #7C89AC")

label1=QLabel(window)
label1.setText("Random number")
label1.setAlignment(Qt.AlignCenter)
label1.move(60, 70)
label1.setFont(font1)

label2=QLabel(window)
label2.setText("0")
label2.move(140, 150)
label2.setFixedWidth(200)
label2.setStyleSheet("font-size:68px; color:white;")

def func1():
    son=random.randint(1,100)
    label2.setText(str(son))


btn=QPushButton(window)
btn.setText('CLICK')
btn.setFixedSize(150, 100)
btn.move(100, 250)
btn.setStyleSheet("background-color: #102F85; font-size:28px; font-weight:bold; border-radius:20px; border: 2px solid black;")
btn.clicked.connect(func1)

layout=QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(btn)
layout.setAlignment(btn, Qt.AlignCenter)
window.show()
app.exec_()
