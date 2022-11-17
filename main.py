import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(600, 600)
        self.flag = False
        self.pushButton = QPushButton('Нарисовать окружность', self)
        self.pushButton.setGeometry(200, 10, 200, 50)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def run(self):
        self.flag = True
        self.repaint()

    def draw_circles(self, qp):
        x = random.randint(10, 290)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(200, 200, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())