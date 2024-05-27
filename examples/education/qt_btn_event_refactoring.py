#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import sys

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        print("add")


def application():
    app = QtWidgets.QApplication()
    widget = Window()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()