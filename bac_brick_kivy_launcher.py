from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class BASBrickLauncher(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text='BAS-Brick Tools', font_size=32))
        self.add_widget(Button(text='Run Network Scan', on_press=self.run_scan))
        self.add_widget(Button(text='Set IP Address', on_press=self.set_ip))
        self.add_widget(Button(text='Set Scan Range', on_press=self.set_scan_range))
        self.add_widget(Button(text='Exit', on_press=self.exit_app))

    def run_scan(self, instance):
        print("Running network scan...")

    def set_ip(self, instance):
        print("IP configuration screen")

    def set_scan_range(self, instance):
        print("Scan range configuration")

    def exit_app(self, instance):
        App.get_running_app().stop()

class BASBrickApp(App):
    def build(self):
        return BASBrickLauncher()

if __name__ == '__main__':
    BASBrickApp().run()