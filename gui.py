"""  A gui to allow user dialog.

gui created with: Qt User Interface Compiler version 5.15.2
-*- coding: utf-8 -*-

Copyright (c) 2021 mj0nez
under MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sensitivity as sst
import visualize as vs
import calculate as cc

import sys
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        # constructor call of super class
        super().__init__()

        # creates ui elements
        self.centralwidget = QWidget(self)
        self.label_group = QGroupBox(self.centralwidget)
        self.formLayoutWidget = QWidget(self.label_group)
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.horizontalLayout = QHBoxLayout()

        # menu elements
        self.statusbar = QStatusBar(self)
        self.menubar = QMenuBar(self)

        # elements for input values:    label + text line
        self.label_capex = QLabel(self.formLayoutWidget)
        self.lineEdit_capex = QLineEdit(self.formLayoutWidget)
        self.label_interest = QLabel(self.formLayoutWidget)
        self.lineEdit_interest = QLineEdit(self.formLayoutWidget)
        self.label_repay = QLabel(self.formLayoutWidget)
        self.lineEdit_repay = QLineEdit(self.formLayoutWidget)
        self.label_opex = QLabel(self.formLayoutWidget)
        self.lineEdit_opex = QLineEdit(self.formLayoutWidget)
        self.label_energy = QLabel(self.formLayoutWidget)
        self.lineEdit_energy = QLineEdit(self.formLayoutWidget)

        # lcoe output
        self.label_lcoe = QLabel(self.formLayoutWidget)
        self.lineEdit_lcoe = QLineEdit(self.formLayoutWidget)

        # sensitivity study
        self.label_variation = QLabel(self.formLayoutWidget)
        self.lineEdit_variation = QLineEdit(self.formLayoutWidget)
        self.label_interval = QLabel(self.formLayoutWidget)
        self.lineEdit_interval = QLineEdit(self.formLayoutWidget)

        # separation lines between input, output and sensitivity
        self.line_2 = QFrame(self.formLayoutWidget)
        self.line = QFrame(self.formLayoutWidget)

        # execution button
        self.pushButton = QPushButton(self.centralwidget)
        self.exitButton = QPushButton(self.centralwidget)
        self.exitAllButton = QPushButton(self.centralwidget)

        # plot figure
        self.fig_active = None
        self.fig_handles = []

        # call of setup for ui objects, default text of lines and window call
        self.setup_ui()
        self.retranslate_ui()
        self.show()

    def set_fig(self, figure):
        self.fig_handles.append(figure)

    def setup_ui(self):
        self.resize(400, 400)
        self.centralwidget.setObjectName("centralwidget")

        self.label_group.setObjectName("label_group")
        self.label_group.setEnabled(True)
        self.label_group.setGeometry(QRect(10, 20, 381, 291))
        self.label_group.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 359, 267))

        self.formLayout.setObjectName("formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        self.label_capex.setObjectName("label_capex")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_capex)

        self.lineEdit_capex.setObjectName("lineEdit_capex")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_capex)

        self.label_interest.setObjectName("label_interest")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_interest)

        self.lineEdit_interest.setObjectName("lineEdit_interest")
        self.formLayout.setWidget(1, QFormLayout.FieldRole,
                                  self.lineEdit_interest)

        self.label_repay.setObjectName("label_repay")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_repay)

        self.lineEdit_repay.setObjectName("lineEdit_repay")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_repay)

        self.label_opex.setObjectName("label_opex")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_opex)

        self.lineEdit_opex.setObjectName("lineEdit_opex")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_opex)

        self.label_energy.setObjectName("label_energy")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_energy)

        self.lineEdit_energy.setObjectName("lineEdit_energy")
        self.formLayout.setWidget(4, QFormLayout.FieldRole,
                                  self.lineEdit_energy)

        self.label_lcoe.setObjectName("label_lcoe")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_lcoe)

        self.lineEdit_lcoe.setObjectName("lineEdit_lcoe")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_lcoe)

        self.label_variation.setObjectName("label_variation")
        self.formLayout.setWidget(8, QFormLayout.LabelRole,
                                  self.label_variation)

        self.lineEdit_variation.setObjectName("lineEdit_variation")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_variation.sizePolicy().hasHeightForWidth())
        self.lineEdit_variation.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(8, QFormLayout.FieldRole,
                                  self.lineEdit_variation)

        self.label_interval.setObjectName("label_interval")
        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_interval)

        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout.setLayout(10, QFormLayout.FieldRole,
                                  self.horizontalLayout)

        self.lineEdit_interval.setObjectName("lineEdit_interval")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.lineEdit_interval.sizePolicy().hasHeightForWidth())
        self.lineEdit_interval.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(9, QFormLayout.FieldRole,
                                  self.lineEdit_interval)

        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.line)

        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.line_2)

        self.setCentralWidget(self.centralwidget)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 21))
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # button layout
        self.pushButton.setObjectName("Generate Plot")
        self.pushButton.setGeometry(QRect(50, 330, 81, 41))

        self.exitButton.setObjectName("Close all Plots")
        self.exitButton.setGeometry(QRect(150, 330, 81, 41))

        self.exitAllButton.setObjectName("Close App")
        self.exitAllButton.setGeometry(QRect(250, 330, 81, 41))

        # button action
        self.pushButton.clicked.connect(self.button_plot)
        self.exitButton.clicked.connect(self.button_close)
        self.exitAllButton.clicked.connect(self.button_close_app)

        self.retranslate_ui()

        QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        # set text in ui, labels and text lines
        self.setWindowTitle("LCOE_sensitivities")
        self.label_group.setTitle("")
        self.label_capex.setText("CAPEX [€] :")
        self.lineEdit_capex.setText("1500000")
        self.label_interest.setText("Interest [% p.a.] :")
        self.lineEdit_interest.setText("2")
        self.label_repay.setText("Repay Duration [a] :")
        self.lineEdit_repay.setText("15")
        self.label_opex.setText("OPEX [€ p.a.] :")
        self.lineEdit_opex.setText("10000")
        self.label_energy.setText("Energy Yield [kWh p.a.] :")
        self.lineEdit_energy.setText("500000")
        self.label_lcoe.setText("LCOE [€ / kWh] :")
        self.label_variation.setText("Parameter Variation [%] :")
        self.lineEdit_variation.setText("30")
        self.label_interval.setText("Plot Interval :")
        self.lineEdit_interval.setText("2")     # also works with 0.5
        self.pushButton.setText("Plot")
        self.exitButton.setText("Close \nall Figures")
        self.exitAllButton.setText("Exit App")

    def button_plot(self):

        calc_inputs, sens_inputs = self.get_field_inputs()
        variation_parameters, lcoe = sst.calculate_lcoes(calc_inputs,
                                                         sens_inputs[0],
                                                         sens_inputs[1])

        fig_plot = vs.plot(variation_parameters, lcoe, cc.LCOE_ARGUMENTS)
        self.set_fig(fig_plot)

    def button_close(self):
        for fig in self.fig_handles:
            plt.close(fig)

    def button_close_app(self):
        self.button_close()
        sys.exit()

    def get_field_inputs(self):
        calculation_inputs = [float(self.lineEdit_capex.text()),
                              float(self.lineEdit_interest.text()),
                              float(self.lineEdit_repay.text()),
                              float(self.lineEdit_opex.text()),
                              float(self.lineEdit_energy.text())]

        sensitivity_inputs = [float(self.lineEdit_variation.text()),
                              float(self.lineEdit_interval.text())]

        return [calculation_inputs, sensitivity_inputs]


def start_app():
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_app()
