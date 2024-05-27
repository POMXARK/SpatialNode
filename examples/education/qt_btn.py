#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import sys

from PySide6 import QtWidgets


def application():
    app = QtWidgets.QApplication()
    widget = QtWidgets.QWidget()

    widget.setWindowTitle("Простая программа")
    widget.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(widget)
    main_text.setText("Это базовая надпись")
    main_text.move(100, 100)
    main_text.adjustSize()

    btn = QtWidgets.QPushButton(widget)
    btn.move(70, 150)
    btn.setText("Нажми меня")
    btn.setFixedWidth(200)

    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
