# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyQt5_TestLayoutzcqxhy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sensitivity as sst
import visualize as vs
import calculate as cc

from PyQt5 import QtWidgets


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

        # sliders
        # self.slider_parameter = QSlider(self.centralwidget)
        # self.slider_interval = QSlider(self.centralwidget)

        # separation lines between input, output and sensitivity
        self.line_2 = QFrame(self.formLayoutWidget)
        self.line = QFrame(self.formLayoutWidget)

        # execution button
        self.pushButton = QPushButton(self.centralwidget)

        # plot figure
        self.fig

        # call of setup for ui objects, default text of lines and window call
        self.setup_ui()
        self.retranslate_ui()
        self.show()

    def setup_ui(self):
        # if not MainWindow.objectName():
        #     MainWindow.setObjectName(u"MainWindow")
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

        # self.slider_parameter.setObjectName(u"slider_parameter")
        # self.slider_parameter.setGeometry(QRect(390, 375, 121, 25))
        # sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # sizePolicy2.setHorizontalStretch(0)
        # sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(
        #     self.slider_parameter.sizePolicy().hasHeightForWidth())
        # self.slider_parameter.setSizePolicy(sizePolicy2)
        # self.slider_parameter.setAutoFillBackground(True)
        # self.slider_parameter.setMinimum(0)
        # self.slider_parameter.setMaximum(100)
        # self.slider_parameter.setPageStep(5)
        # self.slider_parameter.setSliderPosition(30)
        # self.slider_parameter.setTracking(True)
        # self.slider_parameter.setOrientation(Qt.Horizontal)
        # self.slider_parameter.setTickPosition(QSlider.NoTicks)
        #
        # self.slider_interval.setObjectName(u"slider_interval")
        # self.slider_interval.setGeometry(QRect(390, 405, 121, 25))
        # sizePolicy2.setHeightForWidth(
        #     self.slider_interval.sizePolicy().hasHeightForWidth())
        # self.slider_interval.setSizePolicy(sizePolicy2)
        # self.slider_interval.setAutoFillBackground(True)
        # self.slider_interval.setMinimum(0)
        # self.slider_interval.setMaximum(100)
        # self.slider_interval.setPageStep(5)
        # self.slider_interval.setValue(10)
        # self.slider_interval.setSliderPosition(10)
        # self.slider_interval.setTracking(True)
        # self.slider_interval.setOrientation(Qt.Horizontal)
        # self.slider_interval.setTickPosition(QSlider.NoTicks)
        self.setCentralWidget(self.centralwidget)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 21))
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # # connect sliders to text lines for output
        # self.slider_parameter.valueChanged.connect(self.variation_change)
        # self.slider_interval.valueChanged.connect(self.interval_change)

        # button layout
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 330, 81, 41))

        # button action
        self.pushButton.clicked.connect(self.button_execution)

        self.retranslate_ui()

        QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        # set text in ui, labels and text lines
        self.setWindowTitle("MainWindow")
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
        self.lineEdit_interval.setText("0.5")
        self.pushButton.setText("PushButton")

    def button_execution(self):
        print('Hello Dude')
        # if self.fig is not None:
        #     self.fig.close()

        calc_inputs, sens_inputs = self.get_field_inputs()
        variation_parameters, lcoe = sst.calculate_lcoes(calc_inputs,
                                                         sens_inputs[0],
                                                         sens_inputs[1])

        vs.plot(variation_parameters, lcoe, cc.LCOE_ARGUMENTS)

    # def variation_change(self):
    #     my_value = str(self.slider_parameter.value())
    #     self.lineEdit_variation.setText(my_value)
    #     # reset max value of interval size
    #     self.slider_interval.setMaximum(self.slider_parameter.value())
    #
    # def interval_change(self):
    #     my_value = str(self.slider_interval.value())
    #     self.lineEdit_interval.setText(my_value)

    def get_field_inputs(self):

        calculation_inputs = [float(self.lineEdit_capex.text()),
                              float(self.lineEdit_interest.text()),
                              float(self.lineEdit_repay.text()),
                              float(self.lineEdit_opex.text()),
                              float(self.lineEdit_energy.text())]

        sensitivity_inputs = [float(self.lineEdit_variation.text()),
                              float(self.lineEdit_interval.text())]

        return [calculation_inputs, sensitivity_inputs]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
