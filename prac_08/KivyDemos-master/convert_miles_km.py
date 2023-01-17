"""CP1404 Practical 8 - Miles to Kilometres Converter"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output = StringProperty()

    def build(self):
        """Build app from file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.root.ids.output_label.text = "0.00km"
        return self.root

    def handle_convert(self):
        """Handle when convert button pressed."""
        miles = self.get_valid_miles()
        kilometers = MILES_TO_KM * miles
        self.output = f"{kilometers:.2f}km"

    def handle_increment(self, change):
        """Handle when up or down button is pressed."""
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_valid_miles(self):
        """Return valid miles or return 0."""
        try:
            miles = float(self.root.ids.input_miles.text)
            if miles < 0:
                miles = 0
            return miles
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesConverterApp().run()
