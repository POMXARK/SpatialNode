from PySide6 import QtWidgets

from .ui.form import Ui_Form


class WebView(QtWidgets.QWidget):
    def __init__(self, viewModel):
        super().__init__()
        self.viewModel = viewModel  # The ViewModel instance
        self.ui = Ui_Form()
        self.ui.setupUi(self)


