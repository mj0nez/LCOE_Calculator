import calculate
import main


# values = main.get_inputs()
#
# # calculate.Levelized_Cost_Electricity(values)
# print(calculate.levelized_cost_electricity(values[0], values[1], values[2],
#                                            values[3], values[4]))
# print(calculate.levelized_cost_electricity(112416.53348360844, values[3],
#                                            values[4]))
# print('hello world')

class Dummy:
    def __init__(self):
        self.hello = 'hello'
        self.dude = 'dude'
        self.what = 'what'


if __name__ == '__main__':
    d = Dummy()
    string = ['hello', 'dude', 'what']
    for i in range(3):
        print(d.exec(string[i]))


