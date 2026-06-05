import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

app=QApplication([])
window=QWidget()
window.setGeometry(500, 300, 400, 100)
layout=QVBoxLayout(window)

input1=QLineEdit()
input1.setAlignment(Qt.AlignCenter)
input1.setFont(QFont('Calibri', 20))
input1.setPlaceholderText("Parol!")
layout.addWidget(input1)

label=QLabel()
label.setAlignment(Qt.AlignCenter)
label.setText("-----")
label.setFont(QFont("Calibri", 26))
layout.addWidget(label)


def func():
    a=input1.text()
    if a == '12345':
        label.setText("Parol to'g'ri!")
    else:
        label.setText("Noto'g'ri parol!")

btn=QPushButton("Check")
btn.setStyleSheet("background-color: #4A77FF; color: #E9E8F6; font-size: 16px;")
btn.clicked.connect(func)
layout.addWidget(btn)


window.show()
app.exec_()
