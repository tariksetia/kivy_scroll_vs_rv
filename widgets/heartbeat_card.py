import os, time
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from .label import BorderLabel, BackgroundLabel

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)


Builder.load_file('heartbeat_card.kv')  

class HeartbeatCard(GridLayout):
    alert = ObjectProperty()

    def __init__(self,**kwargs):
        Clock.schedule_once(self.update_card_date,0)
        super().__init__(**kwargs)

    def update_card_date(self, dt):
        self.ids.sent_time.text = self.alert.sent
        self.ids.expiry_time.text = self.alert.expires
        self.ids.sender.text = self.alert.sender
        self.ids.alert_id.text = self.alert.alert_id

