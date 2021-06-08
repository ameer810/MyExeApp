from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUiType
R_Class,_=loadUiType('mandobui.ui')
class Dialog(QWidget,R_Class):
    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)