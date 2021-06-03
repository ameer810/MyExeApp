from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from multy import Ui_Dialog as dialog

class MultyDialog(QDialog,dialog):
    def __init__(self,parent=None):
        super(MultyDialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)