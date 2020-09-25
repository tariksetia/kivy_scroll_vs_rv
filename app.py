from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from widgets.heartbeat_list import HeartbeatList


class MainApp(App):
    def build(self):
        return HeartbeatList()

if __name__ ==  '__main__':
    Window.size = (1200,700)
    Window.clearcolor = (1,1,1,1)
    MainApp().run()