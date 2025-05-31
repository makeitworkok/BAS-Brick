from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label

# Configure for 480x320 screen
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')
Config.set('graphics', 'fullscreen', '0')

class BASBrickLauncher(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.add_widget(Label(text='BAS-Brick Tools', font_size=24, size_hint=(1, 0.2)))

        btn_style = {'size_hint': (1, 0.2), 'font_size': 20}
        self.add_widget(Button(text='Run Network Scan', on_press=self.run_scan, **btn_style))
        self.add_widget(Button(text='Set Static IP', on_press=self.set_ip, **btn_style))
        self.add_widget(Button(text='Set Scan Range', on_press=self.set_scan_range, **btn_style))
        self.add_widget(Button(text='Exit', on_press=self.exit_app, **btn_style))

    def run_scan(self, instance):
        print(">> Placeholder: running network scan")

    def set_ip(self, instance):
        print(">> Placeholder: launching IP configuration")

    def set_scan_range(self, instance):
        print(">> Placeholder: launching scan range configuration")

    def exit_app(self, instance):
        App.get_running_app().stop()

class BASBrickApp(App):
    def build(self):
        return BASBrickLauncher()

if __name__ == '__main__':
    BASBrickApp().run()