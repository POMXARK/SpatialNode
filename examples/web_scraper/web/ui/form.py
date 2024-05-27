from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 407)
        Form.setBaseSize(QtCore.QSize(300, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)

        self.splitter = QtWidgets.QSplitter(parent=Form)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)

        self.frame = QtWidgets.QFrame(parent=self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)

        self.webEngineView = QtWebEngineWidgets.QWebEngineView(parent=self.frame)
        self.webEngineView.setUrl(QtCore.QUrl(Form.viewModel.model.web1))

        self.verticalLayout_2.addWidget(self.webEngineView)

        self.frame_2 = QtWidgets.QFrame(parent=self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.splitter)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)

        self.webEngineView2 = QtWebEngineWidgets.QWebEngineView(parent=self.frame_2)
        self.webEngineView2.setUrl(QtCore.QUrl(Form.viewModel.model.web2))

        self.verticalLayout_3.addWidget(self.webEngineView2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
