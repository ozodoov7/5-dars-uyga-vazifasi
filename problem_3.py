import os
os.system('cls')
from PyQt5.QtWidgets import (
QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

app=QApplication([])

window=QWidget()
window.setGeometry(500, 200, 300, 200)
window.setWindowTitle("Calculator")

layout=QVBoxLayout(window)


input1=QLineEdit("")
input1.setAlignment(Qt.AlignCenter)
input1.setFont(QFont('Times New Roman', 20))
layout.addWidget(input1)

input2=QLineEdit("")
input2.setAlignment(Qt.AlignCenter)
input2.setFont(QFont('Times New Roman', 20))
layout.addWidget(input2)

layout.addSpacing(10)

label1=QLabel("=")
label1.setAlignment(Qt.AlignCenter)
label1.setFont(QFont('Times New Roman', 20))
layout.addWidget(label1)

button_layout=QVBoxLayout()
def f1():
    s1=int(input1.text())
    s2=int(input2.text())
    s3=s1+s2
    s3=str(s3)
    label1.setText(s3)

def f2():
    s1=int(input1.text())
    s2=int(input2.text())
    s3=s1-s2
    s3=str(s3)
    label1.setText(s3)

def f3():
    s1=int(input1.text())
    s2=int(input2.text())
    s3=s1*s2
    s3=str(s3)
    label1.setText(s3)

def f4():
    s1=int(input1.text())
    s2=int(input2.text())
    s3=s1/s2
    s3=str(s3)
    label1.setText(s3)


btn1=QPushButton("+")
btn1.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn1.clicked.connect(f1)
button_layout.addWidget(btn1)

btn2=QPushButton("-")
btn2.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn2.clicked.connect(f2)
button_layout.addWidget(btn2)

btn3=QPushButton("*")
btn3.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn3.clicked.connect(f3)
button_layout.addWidget(btn3)

btn4=QPushButton("/")
btn4.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn4.clicked.connect(f4)
button_layout.addWidget(btn4)

layout.addLayout(button_layout)

window.show()
app.exec_()