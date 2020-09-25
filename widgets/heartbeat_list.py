import os
from os.path import join, dirname
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from dataclasses import dataclass
from .heartbeat_card import HeartbeatCard

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)
Builder.load_file('heartbeat_list.kv')  

@dataclass
class Data:
    sent: str
    sender: str
    expires: str
    alert_id: str

    @property
    def to_dict(self):
        return self.__dict__


class HeartbeatList(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_data_grid,0)
        Clock.schedule_once(self.load_data_rv,0)

    def load_data_grid(self, dt):
        al = {
            'sent': '03/24/2020 11:54:48',
            'expires': '04/01/2020 01:34:02',
            'sender': 'Pikachu',
            'alert_id': 'GK47HJ-CSF8VDG8-3KKWJH'
        }
        hbeat_grid = self.ids.hbeat_grid_list
        for i in range(100):
            hbeat_grid.add_widget(HeartbeatCard(alert=Data(**al)))

    def load_data_rv(self, dt):
        al = {
                'sent': '03/24/2020 11:54:48',
                'expires': '04/01/2020 01:34:02',
                'sender': 'Pikachu',
                'alert_id': 'GK47HJ-CSF8VDG8-3KKWJH'
            }
        heat_rv = self.ids.hbeat_rv_list
        heat_rv.data = [ {'alert': Data(**al)} for i in range(100) ]

