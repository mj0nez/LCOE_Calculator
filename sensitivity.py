import numpy as np
import calculate


def get_variation_array(delta, interval):
    """
    Creates array of multipliers to change values from -x to +x with a given
    step length s.
    :param delta:       interval markers, [x,x]
    :param interval:    step length s, between multipliers
    :return:            float array, of size (2*x)/s +1
    """
    # function arange accepts float and integers
    variation = np.arange(-delta, delta + interval, interval)
    variation_count = len(variation)

    # convert variation from percentage to absolute value
    variation_absolute = np.zeros(variation_count, dtype='float')
    for v in range(0, variation_count):
        variation_absolute[v] = (100 + variation[v]) / 100
    return variation_absolute


def calculate_lcoes(input_values, delta, interval):
    """

    :param input_values:    base case inputs of LCOE
    :param delta:           interval markers, [x,x] for sensitivity study
    :param interval:        step length s, between calculation of LCOE
    :return:
    """
    # parameters sensitivity
    variation_absolute = get_variation_array(delta, interval)
    variation_count = len(variation_absolute)

    # parameters LCOE calculation
    args_count = len(calculate.LCOE_ARGUMENTS)

    # pre init return array
    sensitivity_of_lcoe = np.zeros((args_count, variation_count), dtype='float')

    for i in range(args_count):
        # iterate over LCOE arguments
        for j, var in enumerate(variation_absolute):
            # iterate over variation array
            input_values_iteration = input_values[:]  # reset inputs
            # change input argument by percentage of variation
            input_values_iteration[i] = input_values_iteration[i] * var

            # calculate and save LCOE for variation
            sensitivity_of_lcoe[i, j] = \
                calculate.levelized_cost_electricity(input_values_iteration)

    return [variation_absolute, sensitivity_of_lcoe]
