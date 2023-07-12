from kivy.config import Config

#Kivy Screen Config 
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '1400')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)
#Config.set('graphics', 'borderless', True)
#Config.set('kivy', 'exit_on_escape', False)

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from defs import ceaser, defs

class LockFilesApp(App):
    def build(self):
        screen = FloatLayout()
        #Plano de fundo
        background_image = Image(source="background_image_lock_files.png", allow_stretch=True)
        screen.add_widget(background_image)
        
        #TextInputs
        self.encrypt_text_input = TextInput(size_hint = (0.3, 0.1), pos_hint = {"x": 0.025, "y": 0.72}, font_size = 30, hint_text = "Text", halign = "center", multiline = False)
        self.encrypt_text_input.input_filter = defs.filter_char
        screen.add_widget(self.encrypt_text_input)

        self.encrypt_key_input = TextInput(size_hint = (0.2, 0.1), pos_hint = {"x": 0.075, "y": 0.57}, font_size = 45, hint_text = "Key", halign = "center", multiline = False)
        self.encrypt_key_input.input_filter = defs.filter_numbers
        screen.add_widget(self.encrypt_key_input)

        self.decrypt_text_input = TextInput(size_hint = (0.3, 0.1), pos_hint = {"x": 0.025, "y": 0.275}, font_size = 30, hint_text = "Text", halign = "center", multiline = False)
        self.decrypt_text_input.input_filter = defs.filter_char
        screen.add_widget(self.decrypt_text_input)

        self.decrypt_key_input = TextInput(size_hint = (0.2, 0.1), pos_hint = {"x": 0.075, "y": 0.125}, font_size = 45, hint_text = "Key", halign = "center", multiline = False)
        self.decrypt_key_input.input_filter = defs.filter_numbers
        screen.add_widget(self.decrypt_key_input)

        self.decrypt_nokey_input = TextInput(size_hint = (0.3, 0.1), pos_hint = {"x": 0.64, "y": 0.65}, font_size = 30, hint_text = "Text", halign = "center", multiline = False)
        self.decrypt_nokey_input.input_filter = defs.filter_char
        screen.add_widget(self.decrypt_nokey_input)

        #Botões
        self.encrypt_button = Button(text = "Encrypt", size_hint = (0.2, 0.1),pos_hint = {"x": 0.34, "y": 0.72}, background_color = (0.05, 1, 0, 1))
        self.encrypt_button.bind(on_release = self.encriptar)
        screen.add_widget(self.encrypt_button)

        self.decrypt_button = Button(text = "Decrypt", size_hint = (0.2, 0.1),pos_hint = {"x": 0.34, "y": 0.275}, background_color = (0.05, 1, 0, 1))
        self.decrypt_button.bind(on_release = self.decriptar)
        screen.add_widget(self.decrypt_button)

        self.decrypt_nokey_button = Button(text = "Decrypt", size_hint = (0.2, 0.1),pos_hint = {"x": 0.695, "y": 0.525}, background_color = (0.05, 1, 0, 1)) 
        self.decrypt_nokey_button.bind(on_release = self.decriptar_nokey)
        screen.add_widget(self.decrypt_nokey_button)

        #Labels
        #São botões mas funcionam como labels!
        self.encrypt_label = Button(text="", size_hint = (0.3,0.3), text_size = (300,None), pos_hint = {"x": 0.29, "y": 0.4}, background_color = (0,0,0,0))
        self.encrypt_label.bind(on_press= self.copy_text)
        screen.add_widget(self.encrypt_label)

        self.decrypt_label = Button(text= "", size_hint = (0.3,0.3), text_size = (300,None), pos_hint = {"x": 0.29, "y": -0.05}, background_color = (0,0,0,0))
        self.decrypt_label.bind(on_press= self.copy_text)
        screen.add_widget(self.decrypt_label)

        self.scrollview = ScrollView(size_hint = (0.45,0.4), pos_hint = {"x": 0.5, "y": 0.1})
        screen.add_widget(self.scrollview)
        return screen

    def copy_text(self, button):
        text = button.text
        Clipboard.copy(text)

    def encriptar(self, kw):
        #try:
        text = self.encrypt_text_input.text
        key = self.encrypt_key_input.text
        #Verificação de string
        if key != "" and text != "":
            for char in text:
                    if not char.isalpha() and char != ' ':
                        return
            if key.isdigit() == False:
                return
        else:
            return   
        encrypted = ceaser.Ceaser_encrypt(text, int(key))
        self.encrypt_label.text = encrypted.center(65)
        #except:
           # None
        
    def decriptar(self, kw):
        try:
            text = self.decrypt_text_input.text
            key = self.decrypt_key_input.text
            #Verificação de string
            if key != "" and text != "":
                for char in text:
                    if not char.isalpha() and char != ' ':
                        return
                if key.isdigit() == False:
                    return
            else:
                return   
            decrypted = ceaser.Ceaser_decrypt_with_key(text, int(key))
            self.decrypt_label.text = decrypted.center(65)
        except:
            None

    def decriptar_nokey(self, kw):
        try:
            self.scrollview.clear_widgets()
            text = self.decrypt_nokey_input.text
            #Verificação de string
            if text != "":
                for char in text:
                    if not char.isalpha() and char != ' ':
                        return
            else:
                return
            
            scroll_layout = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
            scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
            
            decrypteds = ceaser.Ceaser_decrypt_withot_key(text)
            counter = 0
            for decrypt in decrypteds:
                label_text = (f" {counter} - {decrypt} ")
                label = Label(text=label_text, height = 35, font_size = 25, size_hint = (1, None))
                scroll_layout.add_widget(label)
                counter += 1

            self.scrollview.add_widget(scroll_layout)

        except:
            None

if __name__ == "__main__":
    LockFilesApp().run()

