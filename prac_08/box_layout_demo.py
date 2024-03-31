from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("Greet")
        root = self.root
        root.ids.output_label.text = f"Hello {root.ids.input_name.text}"

    def handle_clear(self):
        print("Clear")
        root = self.root
        root.ids.input_name.text = ''
        root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
