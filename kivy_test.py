from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        # label = Label(text='Hello World!',
        # size_hint=(.5, .5),
        # pos_hint={'center_x': .5, 'center_y': .5})
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # image
        self.window.add_widget(Image(source='Roll-Safe-Think-About-It.jpg'))

        # label
        self.label = Label(
                        text="What's your name?",
                        font_size = 18,
                        color = 'orange')
        self.window.add_widget(self.label)

        # user input
        self.user = TextInput(
                    multiline=False,
                    padding_y = (20, 20),
                    size_hint = (1, .5))
        self.window.add_widget(self.user)

        # button
        self.button = Button(text='GREET',
                             size_hint = (1, .5),
                             bold = True,
                             background_color = 'orange',
                             background_normal = '')
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"
        # print("Button pressed")

if __name__ == '__main__':
    app = MainApp()
    app.run()