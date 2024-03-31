
from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    def build(self):
        self.title = "Squaring App"
        return Builder.load_file('squaring.kv')

    def handle_calculate(self, value):
        try:
            squared_value = float(value) ** 2
            self.root.ids.output_label.text = str(squared_value)
        except ValueError:
            self.root.ids.output_label.text = 'Invalid input'


if __name__ == '__main__':
    SquaringApp().run()
