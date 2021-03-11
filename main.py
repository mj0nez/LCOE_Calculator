# This is a sample Python script.
import calculate
import sensitivity as sst
import visualize as vs
from PyQt5.QtWidgets import *
from gui import MainWindow
import matplotlib.pyplot as plt
import sys
from app import LcoeCalculator


def get_inputs():
    # sample inputs
    capex = 1.5 * 10.0 ** 6.0   # €
    interest = 1.5  # % p.a.
    years = 15
    opex = 1.5 * 10 ** 4    # €
    annual_energy_yield = 500000  # kWh

    calculation_inputs = [capex,
                          interest,
                          years,
                          opex,
                          annual_energy_yield]
    delta = 20
    interval = 2

    sensitivity_inputs = [delta, interval]

    return [calculation_inputs, sensitivity_inputs]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # use test inputs and plot
    if False:
    # if True:
        calc_inputs, sens_inputs = get_inputs()
        variation_parameters, lcoe = sst.calculate_lcoes(calc_inputs,
                                                         sens_inputs[0],
                                                         sens_inputs[1])
        vs.plot(variation_parameters, lcoe, calculate.LCOE_ARGUMENTS)
    # use gui app and exits program after event loop
    # elif False:
    elif True:
        app = QApplication(sys.argv)
        ui = MainWindow()

        # exit program when app window is closed, earliest
        sys.exit(app.exec_())
    # creates instance of calculator app and runs on init
    else:
        # TODO
        #   change event loop to exit plots on app exit
        LcoeCalculator(sys.argv)



