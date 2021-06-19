from PyQt5.QtWidgets import *
from add_buys_completepy2 import Ui_Dialog as main

class Dialog(QWidget,main):
    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)