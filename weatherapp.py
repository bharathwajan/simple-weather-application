import kivy
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import requests
import json
from kivy.core.window import Window

Window.size = (310,500)

username_helper="""
MDTextField :
        pos_hint :{'center_x':0.5,'center_y':0.5}
        hint_text:"Enter city name"
        icon_right:"apple-icloud"
        icon_right_color: app.theme_cls.primary_color
        size_hint_x:0.7

"""

class bharathwajan(MDApp): 
        def show_data(self,obj):
                
                a=self.username.text
                if a=="":
                        b='please enter city name'
                else:
                        b=a   #there are two b's and b selected in dialog box is based on if condition 
                close_button=MDFlatButton(text='close',on_release=self.close_dialog)
                more_button=MDFlatButton(text='more')
                url='http://api.openweathermap.org/data/2.5/weather?q='+a+'&appid=298ab7b018fb976afc348901a83a9ec8'
                result=requests.get(url).json()
                c=result['weather']#list
                d=c[0]#dict
                e=result['main']
                weather='Now the weather is : '+str(d['description'])+'\n The current temperature is : '+str(e['temp'])+'farenheit'+'\n The minimum temperture will be : '+str(e['temp_min'])+'The maximum temperature will be :'+str(e['temp_max'])
                
                temp='the current temperature is : '+str(e['temp'])+'farenheit'
                min_temp='the minimum temperture will be : '+str(e['temp_min'])
                max_temp='the maximum temperature will be :'+str(e['temp_max'])
                self.dialog=MDDialog(text=weather,title='Weather in :'+ a,size_hint=(0.7,0),buttons=(close_button,more_button))#size hint 1 refers to the responsize size acc to screen
                self.dialog.open()#open keyword shold come after defining the dialog box 

        def close_dialog(self,obj):
                self.dialog.dismiss()
                
        def build(self):
                self.theme_cls.theme_style = "Dark"
                self.theme_cls.primary_palette="Yellow" 
                screen=Screen() #always 1 
                self.username=Builder.load_string(username_helper)# attribute used here is for geting input builder.load_string is used to give decorations as string
                button=MDRectangleFlatButton(text='Get weather',pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)#used to add button
                screen.add_widget(self.username)
                screen.add_widget(button)
                return screen # always last 
        
bharathwajan().run()
