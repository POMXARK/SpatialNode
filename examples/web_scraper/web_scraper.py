import sys
from PySide6.QtWidgets import QApplication

from web.model import WebModel
from web.view import WebView
from web.viewmodel import WebViewModel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = WebModel()
    viewModel = WebViewModel(model)
    view = WebView(viewModel)
    view.show()
    sys.exit(app.exec())