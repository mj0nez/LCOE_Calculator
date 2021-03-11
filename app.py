from PyQt5.QtWidgets import QApplication
import sys
from gui import MainWindow


class LcoeCalculator(QApplication):

    def __init__(self, system):
        app = QApplication(system)
        self.ui = MainWindow()

        app.exec_()
        self.ui.close_all()
        sys.exit()
        QApplication.processEvents()

    # def exit(self, ex=None):
    #
    #     # exit program when app window is closed, earliest
    #
    #
    #     # # exit program

