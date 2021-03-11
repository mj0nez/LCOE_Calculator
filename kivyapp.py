from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1

        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100)
        # set columns
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="Hello Dude"))
        # add input Box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        #2
        # add widgets
        self.top_grid.add_widget(Label(text="Fav pizza"))
        # add input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # add topgrid to our app
        self.add_widget(self.top_grid)

        # create a submit button
        self.submit = Button(text='Submit',
                             font_size=32,
                             size_hint_y=None,
                             height=50)
        # bind the button to an action
        self.submit.bind(on_press=self.press)

        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        txt = f'Hello {name}, it appears {pizza} is your fav slice'

        # add text to layout
        self.top_grid.add_widget(Label(text=txt))

        # clear the input boxes
        self.name.text = ''
        self.pizza.text = ''

class TutorialApp(App):
    def build(self):
        # f = FloatLayout()
        # s = Scatter()
        # l = Label(text="Hello!", font_size=150)
        #
        # f.add_widget(s)
        # f.add_widget(l)

        return MyGridLayout()

        # return Button(text="Hello!",
        #               background_color=(0, 0, 1, 1),
        #               font_size=150)


if __name__ == "__main__":
    TutorialApp().run()
