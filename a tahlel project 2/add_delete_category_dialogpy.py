from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
R_Class,_=loadUiType('add_delete_category_dialog.ui')
class Dialog(QDialog,R_Class):
    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)