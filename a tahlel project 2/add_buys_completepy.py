from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
R_Class,_=loadUiType('add_buys_complete.ui')
class Dialog(QWidget,R_Class):
    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)