from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from search_by_date_widget import Ui_Form
class Dialog(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)

