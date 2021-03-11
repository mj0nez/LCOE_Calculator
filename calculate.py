LCOE_ARGUMENTS = ['CAPEX', 'Interest', 'Duration Repayment',
                  'OPEX', 'Annual Energy Yield']


def lcoe_from_annuity(annual_cost, opex, annual_energy_yield):
    levelized_cost = (annual_cost + opex) / annual_energy_yield
    return levelized_cost


def get_annuity(capex, interest, years):
    interest = interest / 100  # conversion from %
    an = capex \
         * (interest * (1 + interest) ** years) \
         / ((1 + interest) ** years - 1)
    return an


def levelized_cost_electricity(*args):

    if len(args) == 1:
        args = args[0]

    if len(args) != 3 and len(args) != 5:
        # check for right number of inputs
        raise ValueError('Not enough input arguments for calculation!')
    elif len(args) > 3:
        # calculate annuity and LCOE
        capex = args[0]
        interest = args[1]
        years = args[2]
        opex = args[3]
        annual_energy_yield = args[4]

        levelized_cost = lcoe_from_annuity(get_annuity(capex, interest, years),
                                           opex, annual_energy_yield)
    else:
        # use given annuity and calculate LCOE
        annuity_arg = args[0]
        opex = args[1]
        annual_energy_yield = args[2]

        levelized_cost = lcoe_from_annuity(annuity_arg, opex,
                                           annual_energy_yield)

    return levelized_cost
