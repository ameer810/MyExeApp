from PyQt5.QtWidgets import QDialog
from add_delete_category_dialogpy2 import Ui_Dialog as main
class Dialog(QDialog,main):
    def __init__(self,parent=None):
        super(Dialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)