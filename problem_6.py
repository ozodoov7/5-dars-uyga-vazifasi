from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

app=QApplication([])
window=QWidget()

window.setGeometry(400, 300, 250, 200)
window.setWindowTitle("Hisoblagich")

layout=QVBoxLayout(window)

label=QLabel()
label.setText("0")
label.setAlignment(Qt.AlignCenter)
label.setFont(QFont("Calibri", 24))
layout.addWidget(label)


def func1():
    a=int(label.text())
    a+=1
    label.setText(str(a))

def func2():
    a=int(label.text())
    a-=1
    label.setText(str(a))


btn1=QPushButton("+1")
btn1.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn1.clicked.connect(func1)
layout.addWidget(btn1)

btn2=QPushButton("-1")
btn2.setStyleSheet("background-color: #102F85; color: white; font-size: 14px;")
btn2.clicked.connect(func2)
layout.addWidget(btn2)

window.show()
app.exec_()