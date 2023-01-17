"""CP1404 Practical 8 - Dynamic Labels"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabelsApp(App):
    """Kivy app for dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Meddie Fercury", "Jilly Boel", "Ciley Myrus"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create GUI widgets from list."""
        for name in self.names:
            name_label = Label(text=name)
            name_label.color = (1, 1, 0, 1)
            self.root.ids.main.add_widget(name_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
