import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class Repo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        x, y = 100, 100
        w = randint(10, 200)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(x, y, w, w)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Repo()
    ex.show()
    sys.exit(app.exec())
