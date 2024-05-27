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

    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
