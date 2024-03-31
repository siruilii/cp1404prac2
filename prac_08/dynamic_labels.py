from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)
ALTERNATIVE_COLOUR = (1, 0, 1, 1)

class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            # set the button's background colour
            temp_button.background_color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handler for button press."""
        name = instance.text
        instance.background_color = ALTERNATIVE_COLOUR
        self.status_text = f"{name}'s number is {self.name_to_phone[name]}"

    def clear_all(self):
        """Clear all dynamically created widgets."""
        self.root.ids.entries_box.clear_widgets()

if __name__ == "__main__":
    DynamicWidgetsApp().run()
