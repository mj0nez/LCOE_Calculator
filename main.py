# This is a sample Python script.
import calculate
import sensitivity as sst
import visualize as vs
from PyQt5.QtWidgets import *
from gui import MainWindow
import sys


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
    if True:
        calc_inputs, sens_inputs = get_inputs()
        variation_parameters, lcoe = sst.calculate_lcoes(calc_inputs,
                                                         sens_inputs[0],
                                                         sens_inputs[1])
        vs.plot(variation_parameters, lcoe, calculate.LCOE_ARGUMENTS)
    else:
        app = QApplication(sys.argv)
        ui = MainWindow()
        # exit programm if app window is closed
        sys.exit(app.exec_())

        # input('Press any key to exit program.')
