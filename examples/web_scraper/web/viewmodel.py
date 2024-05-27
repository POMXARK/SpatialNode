from PySide6.QtCore import QObject


class WebViewModel(QObject):

    def __init__(self, model):
        super().__init__()
        self.model = model  # Reference to the model
