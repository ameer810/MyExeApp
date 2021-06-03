from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

FORM_CLASS, _ = loadUiType("simple loading screen.ui")

class LoadingDialog(QDialog,FORM_CLASS):
    def __init__(self,parent=None):
        super(LoadingDialog, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
