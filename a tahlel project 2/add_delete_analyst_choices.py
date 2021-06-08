from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
main,_ = loadUiType('add_delete_analyst_choices.ui')
class Dialog(QWidget,main):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)