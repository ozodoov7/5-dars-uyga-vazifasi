import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

import random

colors=['red', 'blue', 'green', 'yellow']

app=QApplication([])
window=QWidget()

window.setWindowTitle("Color changer")
window.setGeometry(1500, 800, 250,150)

layout=QVBoxLayout(window)

label=QLabel("Colour")
label.setAlignment(Qt.AlignCenter)
label.setFont(QFont("Calibri", 25))
layout.addWidget(label)

def func():
    color=random.choice(colors)
    label.setStyleSheet(f"color: {color}")

btn=QPushButton("Press")
btn.setStyleSheet("background-color: #4A77FF; color: #E9E8F6; font-size: 16px;")
btn.clicked.connect(func)
layout.addWidget(btn)

layout.addSpacing(10)
window.show()
app.exec_()