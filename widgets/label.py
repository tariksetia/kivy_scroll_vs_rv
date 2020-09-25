import os
from os.path import join, dirname
from kivy.app import App
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty, StringProperty


KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)
Builder.load_file('label.kv')  

class FieldName(Label):
    pass

class FieldValue(Label):
    pass

class FieldValueWrappable(Label):
    pass

class BorderLabel(Label):
    pass

class BackgroundLabel(Label):
    background_color = StringProperty("#fc960c")
    

