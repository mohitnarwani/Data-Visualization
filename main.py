# config
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')
import io
import requests
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.app import App
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
c=" "
with open("wx2.txt","w") as f:
    f.write(f"{c}")
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from kivymd.app import MDApp
import numpy as np
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from kivy.uix.screenmanager import *
from kivy.properties import StringProperty,NumericProperty
from plyer import filechooser
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.core.window import Window
## Here for providing colour to the background  
from kivy.core.window import Window 
## Setting the window size 
Window.clearcolor = (1, 1, 1, 1) # White background
Window.size = (960, 540) 
from graph.backend_kivyagg import FigureCanvasKivyAgg



kv = """
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<Manager>:
    transition: SlideTransition()
    Intro:
        name: 'Intro'

    Start:
        name: 'Start'

    Ts:
        name:'Ts'
    Mar:
        name:'Mar'
    Tl:
        name:'Tl'
    Td:
        name:'Td'
    W3d:
        name: 'W3d'

    Rag:
        name: 'Rag'
    Settin:
        name: 'Settin'

    Settin3:
        name: 'Settin3'
    StartPage:
        name: 'StartPage'
    Disx:
        name: 'Disx'
    Disxx:
        name: 'Disxx'
    Dp:
        name: 'Dp'




    Stockvis:
        name: 'Stockvis'
    St1:
        name: 'St1'
    Dpxn:
        name: 'Dpxn'
    DC:
        name: 'DC'
    SecondPage:
        name: 'SecondPage'
    My:
        name: 'My'

    My1:
        name: 'My1'
    Triset:
        name:'Triset'
    set:
        name:'set'
    SwitchX:
        name: "SwitchX"
    Jointx:
        name: 'Jointx'
    Jointxx:
        name: 'Jointxx'
    Histx:
        name: 'Histx'
    Histxx:
        name: 'Histxx'
    Scatterx:
        name: 'Scatterx'
    Scatterxx:
        name: 'Scatterxx'
    LineX:
        name: 'LineX'
    LineXX:
        name: 'LineXX'
    StripX:
        name: 'StripX'
    StripXX:
        name: 'StripXX'
    Violinx:
        name: 'Violinx'
    Violinxx:
        name: 'Violinxx'
    Swarmx:
        name: 'Swarmx'
    Swarmxx:
        name: 'Swarmxx'
    Barx:
        name: 'Barx'
    Barxx:
        name: 'Barxx'
    Pairx:
        name: 'Pairx'
    Pairxx:
        name: 'Pairxx'
    tri:
        name: 'tri'
    bi:
        name: 'bi'
    bic:
        name: 'bic'
    Bibar:
        name:'Bibar'
    Bibarx:
        name:'Bibarx'
    Piex:
        name:'Piex'
    Piexx:
        name:'Piexx'
    Hebx:
        name:'Hebx'
    Hebxx:
        name:'Hebxx'
    UR:
        name:'UR'
    Cou:
        name:'Cou'
    Cor:
        name:'Cor'


    Cor3:
        name:'Cor3'
    T1:
        name:'T1'
    T2:
        name:'T2'
    T3:
        name:'T3'

<Intro>:
    canvas.before:
        Color:
            rgba: 1,250,250, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text:"Data Modeling & Visualization tool in python"
        size_hint:.6,1
        pos_hint:{"x":.2,"center_y":.7}
        theme_text_color: "Custom"
        text_color:'#4502EB'
        font_size: "100sp"
    MDIconButton:
        icon:"arrow-up"
        size_hint:.1,.1
        pos_hint:{"x":.45,"center_y":.1}
        theme_text_color: "Custom"
        text_color:1,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="up" 
            root.manager.current="Start"
        md_bg_color:'#4502EB'




<Jointxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Jointx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<Mar>:

    MDFloatLayout:
        canvas : 
            Color:
                rgb:1,1,1, 1
            Rectangle:
                source:'ss.png'
                size:self.size
                pos:self.pos
        MDLabel:
            text: ""

            theme_text_color: "Custom"
            text_color:1,0,0,1
  
        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.07,"center_y":.92}
            theme_text_color: "Custom"
            text_color:0,1,1,1
            font_size: 40
            on_release:root.manager.currrent="Settin3" 

    ScrollView:
        size_hint_y:.8
        size_hint_x:.8
    
        pos_hint:{"x":.3,"y":.1}
        do_scroll_y:True
        do_scroll_x:False
        bar_width:0   
  
        BoxLayout:
            orientation:'vertical'
            width:self.minimum_width
            height:self.minimum_height
          
            size_hint_x: .5
            size_hint_y: None 
            pos_hint:{"x":.6,"y":.1} 

            cols:1
            spacing:20
            canvas :
                Color:
                    rgb:1,1,1,1
                Rectangle:
                    source:'bgw.png'
                    size:self.size
                    pos:self.pos
     
            MDFlatButton:
            
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Point"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.po()

            MDFlatButton:
        
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Pixel"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.pi()
            MDFlatButton:
            
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Square"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.sq()


            MDFlatButton:
            
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Circle"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.ci()

            MDFlatButton:
        
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Triangle Up"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.tiu()


            MDFlatButton:
        
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Triangle Down"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.tid()


            MDFlatButton:
        
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Hexagon"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.he()




            MDFlatButton:
        
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Diamond"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.di()

            MDFlatButton:
        
                pos_hint:{"x":0}
                size_hint:1, None
         
                font_size:"50"
                text:"Star"
           
                theme_text_color: "Custom"
                text_color:0,1,1,1
      
                on_release: root.star()


<Ts>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.manager.current="W3d"

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Jointxx" 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }



<Td>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.manager.current="W3d"

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Jointxx" 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }


<Tl>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.manager.current="W3d"

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Jointxx" 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }







<Jointx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.Update()

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Jointxx"


 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<Cor>:
    colorpicker: colorpicker
    sd:sd

    canvas.before:
        Color:
            rgba: 0,0,0, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Settin" 

    MDFlatButton:
        text:"SAVE"
        size_hint:None,None
        pos_hint:{"x":.23,"center_y":.05}
        theme_text_color: "Custom"
        text_color:0,0,0, 1
        icon_size: "30sp"
        on_release:
            root.ls(colorpicker)

        canvas.before:
            Color:
                rgb:0,1,1,1

            RoundedRectangle:
          
                size:self.width,self.height
                pos:self.pos
                radius:[90,90,90,90]
    MDLabel:
        id:sd
        text:
        size_hint:.2,.06
        pos_hint:{"x":.73,"center_y":.05}
        theme_text_color: "Custom"
        text_color:0,1,0, 1
        font_size: "30sp"
            

    BoxLayout:
        id: box
        size_hint: 1,1
        pos_hint:{'x': 0.05,'y': 0.1 }
        ColorPicker:
            id: colorpicker
            size_hint: 1, 0.8


<Cor3>:
    colorpicker: colorpicker
    sd:sd

    canvas.before:
        Color:
            rgba: 0,0,0, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Settin3" 

    MDFlatButton:
        text:"SAVE"
        size_hint:None,None
        pos_hint:{"x":.23,"center_y":.05}
        theme_text_color: "Custom"
        text_color:0,0,0, 1
        icon_size: "30sp"
        on_release:
            root.ls(colorpicker)

        canvas.before:
            Color:
                rgb:0,1,1,1

            RoundedRectangle:
          
                size:self.width,self.height
                pos:self.pos
                radius:[90,90,90,90]
    MDLabel:
        id:sd
        text:
        size_hint:.2,.06
        pos_hint:{"x":.73,"center_y":.05}
        theme_text_color: "Custom"
        text_color:0,1,0, 1
        font_size: "30sp"
            

    BoxLayout:
        id: box
        pos_hint:{'x': 0.05,'y': 0.1 }
        ColorPicker:
            id: colorpicker
            size_hint: 1, 0.8


<Settin>:
 

    FloatLayout:
        canvas.before:
            Color:

            RoundedRectangle:
               
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]

        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_size: 40

            on_release:  root.manager.current="set"


        MDFlatButton:
          
            text:"Range"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release: root.manager.current="Rag"
            canvas.before:
                Color:
                    rgb:0,1,1,1
                RoundedRectangle:
                 
                    size:self.width,self.height
                    pos:self.pos
                    radius:[20,20,20,20]
        MDFlatButton:
            
            text: "Style"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="SwitchX" 

 
            canvas.before:
                Color:
                    rgb:1,0,1,1

                RoundedRectangle:
                
                    size:self.width,self.height
                    pos:self.pos
                    radius:[20,20,20,20]
        MDFlatButton:
          
            text:"Color"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Cor" 

 
            canvas.before:
                Color:
                    rgb:1,1,0,1

                RoundedRectangle:
            
                    size:self.width,self.height
                    pos:self.pos
                    radius:[20,20,20,20]

<Settin3>:
 

    FloatLayout:
        canvas.before:
            Color:

            RoundedRectangle:
               
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]

        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_size: 40

            on_release:  root.manager.current="W3d"


        MDFlatButton:
            
            text: "Style"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Mar" 

 
            canvas.before:
                Color:
                    rgb:1,0,1,1

                RoundedRectangle:
                
                    size:self.width,self.height
                    pos:self.pos
                    radius:[20,20,20,20]
        MDFlatButton:
          
            text:"Color"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Cor3" 

 
            canvas.before:
                Color:
                    rgb:1,1,0,1

                RoundedRectangle:
            
                    size:self.width,self.height
                    pos:self.pos
                    radius:[20,20,20,20]
<Hebxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Hebx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}


<Hebx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.manager.current="DC"
    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Hebxx" 

    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }





<Piexx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Piex"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }


    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<Piex>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.manager.current="bic"
    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa() 

    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Piexx" 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<Pairxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Pairx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}
<Pairx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.manager.current="tri"
    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()

    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Pairxx" 
    BoxLayout:
        id: box
        size_hint: .85, .98
        pos_hint:{'x': .08, 'y': .01 }


<Histxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Histx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}



<Histx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size



    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC"

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Histxx"  
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }
<Scatterxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Scatterx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<Scatterx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC" 
    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()

    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Scatterxx" 

    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<LineXX>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="LineX"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}
<LineX>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size



    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC" 

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()

    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="LineXX" 

    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }
<Dp>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size



    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="bic" 

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Dpxn" 

    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<Dpxn>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Dp"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }



    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<Barxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"x":.71,"y":.725}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"x":.851,"y":.725}

    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Barx"

    BoxLayout:
        id: box
        size_hint: .67, .8
        pos_hint:{'x': .005, 'y': .01 }


    MDLabel:
        id:xi
        text: 
        size_hint:.2,.2
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.2
        pos_hint:{"center_x":.92,"center_y":.905}


<Barx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size



    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC" 

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Barxx" 

    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<StripXX>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="StripX"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<StripX>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC"

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()

    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="StripXX" 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<Disxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Disx"
    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<Disx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="bic" 
    MDIconButton:
        icon:"restart"
        size_hint:None,None
        pos_hint:{"x":.08,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.rot()
           
    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Disxx"
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<Bibar>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="bic" 

    MDIconButton:
        icon:"restart"
        size_hint:None,None
        pos_hint:{"x":.08,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.rot()

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Bibarx"
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<Bibarx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Bibar"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }


    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}

<Violinx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Violinxx" 

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()

    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC" 


    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }



<Violinxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Violinx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}


<Swarmxx>:
    box: box
    xi:xi
    yi:yi
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Swarmx"

    BoxLayout:
        id: box
        size_hint: .67,.8
        pos_hint:{'x': .005, 'y': .01  }

    MDLabel:
       
        text:"X-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text:"Y-axis" 
        size_hint:.05,.15
        pos_hint:{"center_x":.92,"center_y":.905}

    MDLabel:
        id:xi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.78,"center_y":.905}

    MDLabel:
        id:yi
        text: 
        size_hint:.2,.3
        pos_hint:{"center_x":.92,"center_y":.905}


<StockVis>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:           
            root.manager.current="St1"
 
    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }


<Swarmx>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="DC" 

    MDIconButton:
        icon:"save.png"
        size_hint:None,None
        pos_hint:{"x":.5,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:root.sa()
    MDIconButton:
        icon:"google-analytics"
        size_hint:None,None
        pos_hint:{"x":.93,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="Swarmxx"

    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }

<SwitchX>:
    default: default 
    classic:classic  
    solarize:solarize
    hacked:hacked
    dark:dark
    gray:gray
    color:color
    poster:poster
    box:box
    bo:bo
    MDFloatLayout:
        canvas :
            Color:
                rgb:1,1,1, 1
            Rectangle:
               
                size:self.size
                pos:self.pos
        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.03,"center_y":.96}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                root.manager.transition.direction="left" 
                root.manager.current="Settin" 

        MDLabel:
            id:l
            text:"Default" 
            size_hint:.2,.41
            pos_hint:{"center_x":.85,"center_y":.1}
            theme_text_color: "Custom"
            text_color:1,0,1,1
            font_name: "B.otf"
            font_size: "40sp"

        Switch:
            id:default 
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.9,"center_y":.1}
            switch_size:"20sp"
            on_active: root.defaultz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)


        MDLabel:
         
            text:"Classic" 
            size_hint:.2,.41
            pos_hint:{"center_x":.85,"center_y":.25}
            theme_text_color: "Custom"
            text_color:1,0,1,1
            font_name: "B.otf"
            font_size: "40sp"
        Switch:
            id:classic
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.9,"center_y":.25}
            switch_size:"20sp"
            on_active:root.classicz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)

        MDLabel:
         
            text:"Solarize" 
            size_hint:.2,.41
            pos_hint:{"center_x":.6,"center_y":.25}
            theme_text_color: "Custom"
            text_color:0,1,1,1
            font_name: "B.otf"
            font_size: "40sp"

        Switch:
            id:solarize
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.65,"center_y":.25}
            switch_size:"20sp"
            on_active: root.solarizez(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)
        MDLabel:
         
            text:"Hacked" 
            size_hint:.2,.41
            pos_hint:{"center_x":.6,"center_y":.1}
            theme_text_color: "Custom"
            text_color:0,1,1,1
            font_name: "B.otf"
            font_size: "40sp"
        Switch:
            id:hacked
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.65,"center_y":.1}
            switch_size:"20sp"
            on_active: root.hackedz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)
        MDLabel:
         
            text:"Dark Light" 
            size_hint:.2,.41
            pos_hint:{"center_x":.35,"center_y":.1}
            theme_text_color: "Custom"
            text_color:0,0,0,1
            font_name: "B.otf"
            font_size: "40sp"

        Switch:
            id:dark
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.41,"center_y":.1}
            switch_size:"20sp"
            on_active: root.darkz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)

        MDLabel:
         
            text:"Gray scale" 
            size_hint:.2,.41
            pos_hint:{"center_x":.35,"center_y":.25}
            theme_text_color: "Custom"
            text_color:0,0,0,1
            font_name: "B.otf"
            font_size: "40sp"
        Switch:
            id:gray
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.41,"center_y":.25}
            switch_size:"20sp"
            on_active: root.grayz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)

        MDLabel:
         
            text:"Color blind" 
            size_hint:.2,.41
            pos_hint:{"center_x":.12,"center_y":.25}
            theme_text_color: "Custom"
            text_color:1,1,0,1
            font_name: "B.otf"
            font_size: "40sp"
        Switch:
            id:color
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.16,"center_y":.25}
            switch_size:"20sp"
            on_active: root.colorz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)

        MDLabel:
         
            text:"Poster" 
            size_hint:.2,.41
            pos_hint:{"center_x":.12,"center_y":.1}
            theme_text_color: "Custom"
            text_color:1,1,0,1
            font_name: "B.otf"
            font_size: "40sp"
        Switch:
            id:poster
            active: False
            text:"true"
            disabled: False
       
            size_hint:.05,.1
            pos_hint:{"center_x":.16,"center_y":.1}
            switch_size:"20sp"
            on_active: root.posterz(self, self.active)
            canvas:

                Color:
                    rgb: 0,1,1,1
                Rectangle:

                    size: sp(41.5), sp(20)
                    pos: self.center_x - sp(40.0), self.center_y - sp(10)
               
                Color:
                    rgb: 1, 0, 1, 1
                Rectangle:
                    source:'l1.png'
                    size: sp(41.0), sp(20)
                    pos: self.center_x, self.center_y - sp(10)


        Video:
            id:box
            source:root.dx()     
            allow_stretch: True
            size_hint: 0.8, 0.4
            pos_hint:{'x': .1, 'y': 0.4}
            keep_ratio: False    

        BoxLayout:
            id: bo
            size_hint: .2, .2
            pos_hint:{'x':.35, 'y': 0.8}  



<Start>:
    t:t
    FloatLayout:
        canvas.before:
            Color:

            RoundedRectangle:
                source:'1bg.png'
           
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]

        MDFlatButton:
          
            text:"Upload File"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release: 
                root.manager.current="StartPage"
                root.manager.transition.direction="left"
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'bgw.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"x":.2,"center_y":.7}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:1,0,1,1
         
            on_release:app.upinfo()



        MDFlatButton:
          
            text:"Enter URL"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:
                root.manager.current="UR"
                root.manager.transition.direction="left" 

 
            canvas.before:
                Color:
                    
                RoundedRectangle:
                    source:'bgw.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"x":.2,"center_y":.3}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:1,0,1,1
         
            on_release:app.urinfo()

        MDLabel:
            id:t
            text:
            font_size:'40sp' 
            size_hint:1,.1
            pos_hint:{"x":.1,"y":.45}


<set>:
 
    b1:b1
    FloatLayout:
        canvas.before:
            Color:
                rgb:0,1,1,1
            RoundedRectangle:
                source:'bgmm.png'
               
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]

        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_size: 40

            on_release:  root.manager.current="StartPage"


        MDIconButton:
            icon:"microphone-outline" 
            size_hint:None,None
            pos_hint:{"center_x":.5,"center_y":.9}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_size: 40

            on_release:app.st()

        MDIconButton:
            icon:"view-dashboard-edit-outline" 
            size_hint:None,None
            pos_hint:{"center_x":.9,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_size: 40

            on_release:  root.manager.current="Settin"

        MDFlatButton:
          
            text:"Single Variable"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release: app.bx()
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'sc1.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.2,"center_y":.7}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.sininfo()


        MDFlatButton:
            
            text: "Double Variable"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="My" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'double.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.2,"center_y":.5}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.sininfo()

        MDFlatButton:
          
            text:"Multiple Variable"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="tri" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'mc.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.2,"center_y":.3}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.sininfo()

        MDFlatButton:
            id:b1
            text: "Stock"
            size_hint:.2,.1
            pos_hint:{"center_x":.5,"center_y":.1}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_size:"60sp"
            on_release:root.manager.current="St1" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                   
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.41,"center_y":.1}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:1,1,0,1
         
            on_release:app.sininfo()









<St1>:
 
    FloatLayout:
        canvas.before:
            Color:
                rgb:0,1,1,1
            RoundedRectangle:
                source:'stobg.jfif'
               
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]
        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_size: 40

            on_release:  root.manager.current="set"



        MDFlatButton:
          
            text:"Visualize"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Stockvis" 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'stza.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDFlatButton:
            
            text: "Predict"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Stockvis" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                   
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDFlatButton:
          
            text:"Animate"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="tri" 

 
            canvas.before:
                Color:

                RoundedRectangle:
             
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]




<W3d>:
 

    FloatLayout:
        canvas.before:
            Color:
                rgb:1,1,1,1
            RoundedRectangle:
         
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]




        Video:
           
            source:'3db.jfif'   
            allow_stretch: True
            size_hint: 0.2, 0.2
            pos_hint:{'x': 0, 'y': 0}
            keep_ratio: False      


        Video:
           
            source:'3db1.jfif'   
            allow_stretch: True
            size_hint: 0.2, 0.2
            pos_hint:{'x': .8, 'y': 0}
            keep_ratio: False      


        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_size: 40

            on_release:  root.manager.current="tri"

        MDIconButton:
            icon:"view-dashboard-edit-outline" 
            size_hint:None,None
            pos_hint:{"center_x":.9,"center_y":.9}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_size: 40

            on_release:  root.manager.current="Settin3"

        MDFlatButton:
          
            text:"Line Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Tl"
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'3dlp.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDFlatButton:
            
            text: "Scatter Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Ts" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'3dsc.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDFlatButton:
          
            text:"Density Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Td" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'3dd.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

<DC>:
 
    t:t
    FloatLayout:
        canvas.before:
            Color:
                rgb:app.bg() 

            RoundedRectangle:
             
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]
                
        MDLabel:
            id:t
            text: 
            size_hint:.8,.25
            pos_hint: {"x":.1,"y":.8}
            theme_text_color: "Custom"

            font_size:"29sp"
            text_color:1,0,0,1
        MDIconButton:
            icon:"menu-left" 
            size_hint:None,None
            pos_hint:{"center_x":.07,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            icon_size: "40sp"

            on_release:  root.manager.current="set"

        MDFlatButton:
          
            text:"Joint Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.2,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release: root.manager.current="Jointx"
 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgjp.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.085,"center_y":.7}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.joinfo()

        MDFlatButton:
            
            text: "Hist Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.2,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="Histx" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fghist.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.085,"center_y":.5}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.hiinfo()

        MDFlatButton:
          
            text:"Scatter Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="Scatterx"  
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgsp.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.385,"center_y":.7}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.scinfo()

        MDFlatButton:
          
            text:"Line Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.8,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="LineX" 

            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fglp.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.685,"center_y":.7}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.liinfo2()

        MDFlatButton:
          
            text:"Bar Graph"
            size_hint:.2,.12
            pos_hint:{"center_x":.8,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="Barx"

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fbbar1.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.685,"center_y":.5}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.bainfo()


        MDFlatButton:
          
            text:"Strip Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="StripX"

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgs.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.385,"center_y":.5}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.stinfo()


        MDFlatButton:
          
            text:"Violin Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.2,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="Violinx"


 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgv.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.085,"center_y":.3}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.viinfo()


        MDFlatButton:
          
            text:"Swarm Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="Swarmx"

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgs1.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.385,"center_y":.3}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.swinfo()

        MDFlatButton:
          
            text:"Hexbin Plot"
            size_hint:.2,.12
            pos_hint:{"center_x":.8,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "C.ttf"
            font_size:"40sp"
            on_release:root.manager.current="Hebx"


 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgh.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"center_x":.685,"center_y":.3}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:0,0,0,1
         
            on_release:app.heinfo()




<StartPage>:
    ox:ox
    MDFloatLayout:
        canvas :
            Color:
                rgb:1,1,1,1
            Rectangle:
                source:'6.png'
                size:self.size
                pos:self.pos
        MDLabel:
            id:ox
            text: ""
            size_hint:.3,.11
            pos_hint: {"center_x":.586,"center_y":.35}
            theme_text_color: "Custom"
            text_color:1,0,0,1
        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.03,"center_y":.96}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                root.manager.transition.direction="left" 
                root.manager.current="Start"
        MDLabel:
            text: "UPLOAD FILE(.csv)"
            size_hint:.8,.2
            pos_hint: {"center_x":.725,"center_y":.75}
            theme_text_color: "Custom"
            font_name: "C.ttf"
            font_size:"60sp"
       
            text_color:0,1,1,1

        Video:
           
            source:'bgmap.jfif'   
            allow_stretch: True
            size_hint: 0.4, 0.3
            pos_hint:{'x': .6, 'y': 0.1}
            keep_ratio: False      

        MDFloatLayout:
    
            size_hint:.11,.11
            pos_hint: {"center_x":.5,"center_y":.5}
            canvas :
                Color:
            
                Rectangle:
                    source:'bgup.jfif'
                    size:self.size
                    pos:self.pos
    
            MDFlatButton:
                id:pc3
           
                size_hint:None,None
                pos_hint: {"center_x":.5,"center_y":.5}
                
               
                user_font_size:"40sp"
                theme_text_color:"Custom"
                text_color:0,10,1,1
            
                on_release:app.Update()




<UR>:
    t:t
    ox:ox
    MDFloatLayout:
        canvas :
            Color:
                rgb:1,1,1,1
            Rectangle:
                source:'6.png'
                size:self.size
                pos:self.pos

        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.03,"center_y":.96}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                root.manager.transition.direction="left" 
                root.manager.current="Start"
        MDLabel:
            id:ox
            text: ""
            size_hint:.6,.11
            pos_hint: {"x":.2,"center_y":.35}
            theme_text_color: "Custom"
            text_color:1,0,0,1
            font_size:"25sp"
        Video:
           
            source:'bgurl.jfif'     
            allow_stretch: True
            size_hint: 0.8, 0.2
            pos_hint:{'x': .1, 'y': 0.65}
            keep_ratio: False      

        MDTextField:
            id:t
            size_hint:.8,.12
            pos_hint: {"x":.03,"y":.5}
            theme_text_color: "Custom"
            font_name: "A.ttf"
            font_size:"20sp"
            text_color:1,0,1,1
            multiline:True

            theme_text_color: "Custom"
            text_color:1,0,1,1                
            color_mode: 'custom'
            line_color_focus:1,0,1,1
           
            text_color_focus: 1,0,1,1

            line_color_normal:1,0,1,1
            text_color_normal: 1,0,1,1
    
        MDIconButton:
            icon:"send"
            size_hint:None,None
            pos_hint:{"x":.9,"center_y":.56}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                app.ge()




<Cou>:
    t:t
    MDFloatLayout:
        canvas :
            Color:
                rgb:0,0,0,1
            Rectangle:
                source:'6.png'
                size:self.size
                pos:self.pos

        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.03,"center_y":.96}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                root.manager.transition.direction="left" 
                root.manager.current="Rag"

        MDLabel:
            id:t
            text:
            size_hint:1,1
            pos_hint:{"x":.4,"center_y":.7}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            font_size: "30sp"
          

<Rag>:
    t:t
    t1:t1
    er:er
    MDFloatLayout:
        canvas :
            Color:
                rgb:1,1,1,1
            Rectangle:
                source:'6.png'
                size:self.size
                pos:self.pos

        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.03,"center_y":.96}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                root.manager.transition.direction="left" 
                root.manager.current="Settin"
        MDLabel:
            id:ox
            text: ""
            size_hint:.6,.11
            pos_hint: {"x":.2,"center_y":.35}
            theme_text_color: "Custom"
            text_color:1,0,0,1
            font_size:"25sp"
        MDFlatButton:
            text: "Count"
            size_hint:None,None
            pos_hint: {"center_x":.537,"center_y":.85}
            theme_text_color: "Custom"
            font_size:"50sp"
            text_color:0,0,0,1
            on_release:app.teex()
            canvas.before:
                Color:

                RoundedRectangle:
                
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]
        MDLabel:
            text: "starting number"
            size_hint:.3,.2
            pos_hint: {"center_x":.52,"center_y":.6}
            theme_text_color: "Custom"
         
            font_size:"30sp"
            text_color:0,1,1,1
        MDLabel:
            text: "ending number"
            size_hint:.3,.2
            pos_hint: {"center_x":.52,"center_y":.5}
            theme_text_color: "Custom"
         
            font_size:"30sp"
            text_color:0,1,1,1

        MDLabel:
            id:er
            text: 
            size_hint:.3,.2
            pos_hint: {"center_x":.645,"center_y":.35}
            theme_text_color: "Custom"
         
            font_size:"30sp"
            text_color:1,0,0,1


        TextInput:
            id:t
            text:app.sav2()
            size_hint:.05,.04
            pos_hint: {"x":.6,"y":.48}
            theme_text_color: "Custom"
           
            font_size:"20sp"
            text_color:1,0,1,1
            multiline:True

            theme_text_color: "Custom"
            text_color:1,0,1,1                
            color_mode: 'custom'
            line_color_focus:1,0,1,1
           
            text_color_focus: 1,0,1,1

            line_color_normal:1,0,1,1
            text_color_normal: 1,0,1,1

        TextInput:
            id:t1
            text:app.sav1()
            size_hint:.05,.04
            pos_hint: {"x":.6,"y":.58}
            theme_text_color: "Custom"
         
            font_size:"20sp"
            text_color:1,0,1,1
            multiline:True

            theme_text_color: "Custom"
            text_color:1,0,1,1                
            color_mode: 'custom'
            line_color_focus:1,0,1,1
           
            text_color_focus: 1,0,1,1

            line_color_normal:1,0,1,1
            text_color_normal: 1,0,1,1
    
        MDFlatButton:
            text:"save"
            size_hint:None,None
            pos_hint:{"x":.5,"center_y":.2}
            theme_text_color: "Custom"
            text_color:0,0,0, 1
            font_size: "30sp"
            on_release:
                app.sav()
            canvas.before:
                Color:
                    rgb:0,1,1,1

                RoundedRectangle:
            
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDFlatButton:
            text:"reset"
            size_hint:None,None
            pos_hint:{"x":.85,"center_y":.96}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_size: "30sp"
            on_release:
                app.res()
            canvas.before:
                Color:
                    rgb:0,0,0,1
                RoundedRectangle:
        
                    size:self.width,self.height
                    pos:self.pos
                    radius:[50,50,50,50]



<My>:

    box: box
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
     
            pos: self.pos
            size: self.size

    Video:
          
        source:app.rd()   
        allow_stretch: True
        size_hint: 0.8, 0.4
        pos_hint:{'x': .1, 'y': 0.55}
        keep_ratio: False   

    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       
    MDLabel:
        text: "Choose your x-axis"
        size_hint:.8,.2
        pos_hint: {"center_x":.725,"center_y":.735}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:0,1,1,1


<T1>:

    box: box
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
     
            pos: self.pos
            size: self.size

    Video:
          
        source:app.rd()   
        allow_stretch: True
        size_hint: 0.8, 0.4
        pos_hint:{'x': .1, 'y': 0.55}
        keep_ratio: False   

    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       
    MDLabel:
        text: "Choose your x-axis"
        size_hint:.8,.2
        pos_hint: {"center_x":.725,"center_y":.735}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:0,1,1,1

<T2>:

    box: box
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
     
            pos: self.pos
            size: self.size

    Video:
          
        source:app.rd()   
        allow_stretch: True
        size_hint: 0.8, 0.4
        pos_hint:{'x': .1, 'y': 0.55}
        keep_ratio: False   

    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       
    MDLabel:
        text: "Choose your y-axis"
        size_hint:.8,.2
        pos_hint: {"center_x":.725,"center_y":.735}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:0,1,1,1


<T3>:

    box: box
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
     
            pos: self.pos
            size: self.size

    Video:
          
        source:app.rd()   
        allow_stretch: True
        size_hint: 0.8, 0.4
        pos_hint:{'x': .1, 'y': 0.55}
        keep_ratio: False   

    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       
    MDLabel:
        text: "Choose your z-axis"
        size_hint:.8,.2
        pos_hint: {"center_x":.725,"center_y":.735}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:0,1,1,1





<My1>:
    box: box
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Video:
          
        source:app.rd()    
        allow_stretch: True
        size_hint: 0.8, 0.4
        pos_hint:{'x': .1, 'y': 0.55}
        keep_ratio: False  

    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       
    MDLabel:
        text: "Choose your y-axis"
        size_hint:.8,.2
        pos_hint: {"center_x":.725,"center_y":.735}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:1,0,1,1



<Triset>:
    box: box
    sw:sw
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    MDIconButton:
        icon:"arrow-left"
        size_hint:None,None
        pos_hint:{"x":.03,"center_y":.96}
        theme_text_color: "Custom"
        text_color:0,1,1, 1
        icon_size: "30sp"
        on_release:
            root.manager.transition.direction="left" 
            root.manager.current="tri"

    MDLabel:
     
        text:"Default" 
        size_hint:.2,.1
        pos_hint:{"x":.4,"y":.81}
        theme_text_color: "Custom"
        text_color:0,1,1,1
        font_name: "B.otf"
        font_size: "40sp"
    Switch:
        id:sw
        active:True
        disabled: False
        size_hint:.05,.1
        pos_hint:{"x":.5,"y":.81}
        switch_size:"20sp"
        on_active: root.swi(self, self.active)
        canvas:

            Color:
                rgb: 0,1,1,1
            Rectangle:

                size: sp(41.5), sp(20)
                pos: self.center_x - sp(40.0), self.center_y - sp(10)
           
            Color:
                rgb: 1, 0, 1, 1
            Rectangle:
           
                size: sp(41.0), sp(20)
                pos: self.center_x, self.center_y - sp(10)


    MDLabel:
        text: "Which axis to compare?"
        size_hint:.8,.2
        pos_hint: {"center_x":.7,"center_y":.6}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:1,0,1,1


    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       




<bi>:
    box: box
    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Video:
          
        source:app.rd()    
        allow_stretch: True
        size_hint: 0.8, 0.4
        pos_hint:{'x': .1, 'y': 0.55}
        keep_ratio: False 

    BoxLayout:
        id: box
        size_hint:.5,.1
        pos_hint:{'x': .25, 'y': .25 }
       
    MDLabel:
        text: "Choose your axis"
        size_hint:.8,.2
        pos_hint: {"center_x":.725,"center_y":.735}
        theme_text_color: "Custom"

        font_size:"60sp"
        text_color:1,0,1,1

               

<SecondPage>:
    box: box

    canvas.before:
        Color:
            rgba: 1,1,1, 1
        Rectangle:
            pos: self.pos
            size: self.size


    BoxLayout:
        id: box
        size_hint: 1, .9
        pos_hint:{'x': -0.08, 'y': 0 }
  
        MDIconButton:
            icon:"arrow-left"
            size_hint:None,None
            pos_hint:{"x":.03,"center_y":.96}
            theme_text_color: "Custom"
            text_color:0,1,1, 1
            icon_size: "30sp"
            on_release:
                root.manager.transition.direction="left" 
                root.manager.current="DC" 

<tri>:
    FloatLayout:
        canvas.before:
            Color:
                rgb:app.bg() 
            RoundedRectangle:
               
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]

        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_size: 40

            on_release:  root.manager.current="set"
        MDIconButton:
            icon:"view-dashboard-edit-outline" 
            size_hint:None,None
            pos_hint:{"center_x":.9,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_size: 40

            on_release:  root.manager.current="Triset"




        MDFlatButton:
          
            text:"Pair Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release: root.manager.current="Pairx"
 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgpp.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]



        MDFlatButton:
          
            text:"3d Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.25}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release: root.manager.current="T1"
 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'3dbu.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

<bic>:
    t:t
    FloatLayout:
        canvas.before:
            Color:
                rgb:app.bg()
            RoundedRectangle:
                source:
                size:self.width,self.height
                pos:self.pos
                radius:[0,0,0,0]

        MDLabel:
            id:t
            text: 
            size_hint:.8,.25
            pos_hint: {"x":.2,"y":.8}
            theme_text_color: "Custom"

            font_size:"49sp"
            text_color:1,0,0,1


        MDIconButton:
            icon:"arrow-left" 
            size_hint:None,None
            pos_hint:{"center_x":.1,"center_y":.9}
            theme_text_color: "Custom"
            text_color:1,1,1, 1
            font_size: 40

            on_release:  root.manager.current="set"



        MDFlatButton:
          
            text:"Pie Chart"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.7}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release: root.manager.current="Piex"
 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgpie.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"x":.2,"center_y":.7}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:1,0,1,1
         
            on_release:app.piinfo()

        MDFlatButton:
            
            text: "Line Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.5}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Disx" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgline.png'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]


        MDIconButton:
       
            icon:"exclamation"
            pos_hint:{"x":.2,"center_y":.5}
                     
            icon_size:"28sp"
            theme_text_color: "Custom"
            text_color:1,0,1,1
         
            on_release:app.biinfo()

        MDFlatButton:
          
            text:"Bar Graph"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.3}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Bibar" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgbar.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]

        MDFlatButton:
          
            text:"Density Plot"
            size_hint:.6,.12
            pos_hint:{"center_x":.5,"center_y":.1}
            theme_text_color: "Custom"
            text_color:1,0,1, 1
            font_name: "A.ttf"
            font_size:"60sp"
            on_release:root.manager.current="Dp" 

 
            canvas.before:
                Color:

                RoundedRectangle:
                    source:'fgden.jfif'
                    size:self.width,self.height
                    pos:self.pos
                    radius:[0,0,0,0]




"""

Builder.load_string(kv)

# Start Page
class StartPage(Screen):      
    pass
class Cou(Screen):  
    pass 

class Intro(Screen):  
    pass  

class W3d(Screen):  
    pass  

class Start(Screen):      
    pass
class Rag(Screen):      
    pass


class St1(Screen):      
    pass

class Settin(Screen):      
    pass

class Settin3(Screen):      
    pass


class UR(Screen):      
    pass


class Mar(Screen):      
    def pi(self):
        d=','
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 
    def po(self):
        d='.'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 
    def ci(self):
        d='o'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 
    def sq(self):
        d='s'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 

    def tiu(self):
        d='^'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 

    def tid(self):
        d='v'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 

    def di(self):
        d='d'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 

    def star(self):
        d='*'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 

    def he(self):
        d='H'
        with open("mar.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="Settin3" 

class Cor(Screen):      
    def ls(self, colorpicker, *args):
        
        color = str(colorpicker.hex_color)[1:]
        screen_manager.get_screen('Cor').sd.text="SUCCESS"
        r="#"+color
        with open("col.txt","w") as f:
            f.write(f"{r}")

class Cor3(Screen):      
    def ls(self, colorpicker, *args):
        
        color = str(colorpicker.hex_color)[1:]
        screen_manager.get_screen('Cor3').sd.text="SUCCESS"
        r="#"+color
        with open("col3.txt","w") as f:
            f.write(f"{r}")
        
     
class set(Screen):      
    pass
class tri(Screen):      
    pass




class bic(Screen):      
    pass
class bi(Screen):      
    box = ObjectProperty(None)

    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
       

        for i in d: 
            self.box.add_widget(Button(text=str(i),color="white",background_color=(1,0,1,1), on_press=lambda x, y=i: self.uk(str(y))))         
   
    def uk(self,instance):
        d=str(instance)
        with open("bi.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="bic" 





class SwitchX(Screen):      
    def dx(self):
        with open("wx7.txt","r") as f:
            d = f.read()
        return d
    def defaultz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=True
            screen_manager.get_screen('SwitchX').box.source="id.png"   
            with open("wx7.txt", "w") as f:
                f.write(f"{'id.png'}")  
            y="default"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up() 
            
    def classicz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=True
            screen_manager.get_screen('SwitchX').default.active=False
            screen_manager.get_screen('SwitchX').box.source="ic.png"            
            with open("wx7.txt", "w") as f:
                f.write(f"{'ic.png'}")        
            y="classic"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up() 
       

    def solarizez(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=True
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=False
            self.Up() 
            screen_manager.get_screen('SwitchX').box.source="is.png"   
            with open("wx7.txt", "w") as f:
                f.write(f"{'is.png'}")        
            y="Solarize_Light2"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up() 
      
    def grayz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=True
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=False
            screen_manager.get_screen('SwitchX').box.source="ig.png"               
         
            with open("wx7.txt", "w") as f:
                f.write(f"{'ig.png'}")        
            y="grayscale"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")

            self.Up() 
    def colorz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=True
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=False
            screen_manager.get_screen('SwitchX').box.source="it.png"   
                   
            with open("wx7.txt", "w") as f:
                f.write(f"{'it.png'}")           
      
            y="tableau-colorblind10"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up() 

    def posterz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=True
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=False
 
            screen_manager.get_screen('SwitchX').box.source="ip.png"     
            with open("wx7.txt", "w") as f:
                f.write(f"{'ip.png'}")      
            y="seaborn-poster"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up() 

    def darkz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=False
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=True
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=False
                
            screen_manager.get_screen('SwitchX').box.source="idb.png"   

            with open("wx7.txt", "w") as f:
                f.write(f"{'idb.png'}")        
            y="dark_background"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up()       
           


    def hackedz(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('SwitchX').hacked.active=True
            screen_manager.get_screen('SwitchX').poster.active=False
            screen_manager.get_screen('SwitchX').gray.active=False
            screen_manager.get_screen('SwitchX').dark.active=False
            screen_manager.get_screen('SwitchX').color.active=False
            screen_manager.get_screen('SwitchX').solarize.active=False
            screen_manager.get_screen('SwitchX').classic.active=False
            screen_manager.get_screen('SwitchX').default.active=False
  
            screen_manager.get_screen('SwitchX').box.source="ih.png"        

            with open("wx7.txt", "w") as f:
                f.write(f"{'ih.png'}")      
      
            y="bmh"

            with open("wx6.txt", "w") as f:
                f.write(f"{y}")
            self.Up() 

    bo = ObjectProperty(None)



    def add_plot(self, N):
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        df = pd.read_csv("stock.csv")[x:y]  
   
        d="High"
        dz="Low"
        p = df[d].tolist()
        q = df[dz].tolist()  
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)   
 
 
        fig, ax = plt.subplots()
        with open("col.txt","r") as f:
            qq= f.read() 
     

        ax.hexbin(p,q, gridsize=20,color=qq)

        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.bo.clear_widgets()
        self.fig1 = SwitchX.add_plot(self,1000)
        self.bo.add_widget(FigureCanvasKivyAgg(self.fig1))
    def Up(self):
        plt.cla()
        self.bo.clear_widgets()
        self.fig1 = SwitchX.add_plot(self,1000)
        self.bo.add_widget(FigureCanvasKivyAgg(self.fig1))

class DC(Screen):      
    pass

class Swarmx(Screen):
    box = ObjectProperty(None)

    def sa(self):

        z="Swarm Plot.png"

        plt.savefig(z)


    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)   
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  
            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()  
     
        
            sns.swarmplot(y=dz, x=d,data=df)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)      

            plt.show()
            self.fig1 = plt.gcf()
            screen_manager.get_screen('DC').t.text =""
            screen_manager.current="DC" 


            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Swarmx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))

class Swarmxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)   
        with open("wx1.txt","r") as f:
            d = f.read()
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
 

        sns.swarmplot(y=dz, x=d,data=df)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)   
        plt.show()
   

        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        self.fig1 = Swarmxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()

        screen_manager.get_screen('Swarmxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Swarmxx').yi.text =str(df[dz].describe())
     

class Violinx(Screen):
    box = ObjectProperty(None)

    def sa(self):

        z="Violin Plot.png"
 
        plt.savefig(z)


    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  
            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()   
            with open("col.txt","r") as f:
                q= f.read()  
            sns.violinplot(y=dz, x=d,data=df,color=q)

            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da) 
            plt.show()
            self.fig1 = plt.gcf()
            screen_manager.get_screen('DC').t.text =""
            screen_manager.current="DC"
            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"  
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Violinx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))


class Violinxx(Screen):
    box = ObjectProperty(None)

    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)      
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()   
        with open("col.txt","r") as f:
            q= f.read() 
        sns.violinplot(y=dz, x=d,data=df,color=q)
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Violinxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        with open("wx1.txt","r") as f:
            d = f.read()
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]   
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()

        screen_manager.get_screen('Violinxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Violinxx').yi.text =str(df[dz].describe())





class StripX(Screen):
    box = ObjectProperty(None)

    def sa(self):

        z="Strip Plot.png"
  
        plt.savefig(z)



    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("wx1.txt","r") as f:
                d = f.read()

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            plt.title(d)
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  
            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()  
      
            sns.stripplot(y=dz, x=d,data=df)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)   
            plt.show()
            self.fig1 = plt.gcf()
            screen_manager.get_screen('DC').t.text =""
            screen_manager.current="DC"

            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"    

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = StripX.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
     

class StripXX(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  

        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  

        sns.stripplot(y=dz, x=d,data=df)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)   
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = StripXX.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('StripXX').xi.text =str(df[d].describe())
        screen_manager.get_screen('StripXX').yi.text =str(df[dz].describe())
class LineX(Screen):
    box = ObjectProperty(None)

    def sa(self):

        z="Line Plot.png"

        plt.savefig(z)

    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        plt.title(d)
        x=int(x)
        y=int(y)

        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
        with open("col.txt","r") as f:
            q= f.read()  
        sns.lineplot(y=dz, x=d,data=df,color=q)


        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)  
        plt.show()    

        self.fig1 = plt.gcf()
        screen_manager.current="DC"
        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = LineX.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
class LineXX(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
   
        with open("wx1.txt","r") as f:
            d = f.read()
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
 
        with open("col.txt","r") as f:
            q= f.read()   
        sns.lineplot(y=dz, x=d,data=df,color=q)

        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)      

        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = LineXX.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        with open("wx1.txt","r") as f:
            d = f.read()
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('LineXX').xi.text =str(df[d].describe())
        screen_manager.get_screen('LineXX').yi.text =str(df[dz].describe())



     

class Scatterxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
        with open("col.txt","r") as f:
            q= f.read() 

        sns.scatterplot(y=dz, x=d,data=df,color=q) 

        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da) 

        self.fig1 = plt.gcf() 

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Scatterxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Scatterxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Scatterxx').yi.text =str(df[dz].describe())

class Scatterx(Screen):
    box = ObjectProperty(None)
    def sa(self):
        z="Scatter Plot"+d+".png"
      
        plt.savefig(z)



    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("wx1.txt","r") as f:
                d = f.read()

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            plt.title(d)

            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  
        

            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()  
            with open("col.txt","r") as f:
                q= f.read()  
            sns.scatterplot(y=dz, x=d,data=df,color=q) 

            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)
            screen_manager.get_screen('DC').t.text =""
            plt.show()

            self.fig1 = plt.gcf() 
            screen_manager.current="DC"

            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Scatterx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
     

class Histxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  

        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
 
        with open("col.txt","r") as f:
            q= f.read() 
 
        sns.histplot(y=dz, x=d,data=df,color=q)
        with open("wx6.txt","r") as f:
            zza= f.read()  
        plt.style.use(zza)   
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Histxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)

        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Histxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Histxx').yi.text =str(df[dz].describe())

class Histx(Screen):
    box = ObjectProperty(None)

    def sa(self):
        z="Histogram.png"
     
        plt.savefig(z)


    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]     

            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()  
     
            with open("col.txt","r") as f:
                q= f.read() 
     
            sns.histplot(y=dz, x=d,data=df,color=q)
            with open("wx6.txt","r") as f:
                zza= f.read()  
            plt.style.use(zza)
            screen_manager.get_screen('DC').t.text =""
            self.fig1 = plt.gcf()
            plt.show()
            screen_manager.current="DC"

            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Histx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
  
class Jointxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  


        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
 
        with open("col.txt","r") as f:
            q= f.read() 
 
        sns.jointplot(y=dz, x=d,data=df,color=q)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)      
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Jointxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)

        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Jointxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Jointxx').yi.text =str(df[dz].describe())
     
    def Update(self):

        plt.cla()
        self.box.clear_widgets()
        screen_manager.current = 'DC'     
  
class Jointx(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("jointsave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Joint Plot"+d+".png"
        with open("jointsave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)
    
    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt

       
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  

            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()  
            with open("col.txt","r") as f:
                q= f.read() 
     
            sns.jointplot(y=dz, x=d,data=df,color=q)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)      
            self.fig1 = plt.gcf()
           
            screen_manager.get_screen('DC').t.text =""

            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Jointx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
     
    def Update(self):

        plt.cla()
        self.box.clear_widgets()
        screen_manager.current = 'DC'

class Disx(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("dissave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="1_Line Plot"+d+".png"
        with open("dissave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)

    def rot(self):
        with open("linst.txt","r") as f:
            d = f.read()
        if d=="0":
            d='1'
            with open("linst.txt", "w") as f:
                f.write(f"{d}")
        elif d=='1':
            d='0'
            with open("linst.txt", "w") as f:
                f.write(f"{d}")
     
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Disx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))



    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       

            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)


            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)

            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]   
            with open("bi.txt","r") as f:
                da = f.read() 
            with open("col.txt","r") as f:
                q= f.read() 
            with open("linst.txt","r") as f:
                o= f.read() 
            if o=='0':
                sns.displot(data=df,y=da,kind="kde", height=6,color=q)
            else:
                sns.displot(data=df,x=da,kind="kde", height=6,color=q)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)     
            screen_manager.get_screen('bic').t.text =""     
            self.fig1 = plt.gcf()
  

            return self.fig1
        except:
            screen_manager.get_screen('bic').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="bic"
            screen_manager.get_screen('bic').t.text_color =1,0,0,1             
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Disx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))

class Disxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   

        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("bi.txt","r") as f:
            da = f.read() 
        with open("col.txt","r") as f:
            q= f.read() 
        with open("linst.txt","r") as f:
            o= f.read() 
        if o=='0':
            sns.displot(data=df,y=da,kind="kde", height=6,color=q)
        else:
            sns.displot(data=df,x=da,kind="kde", height=6,color=q)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)     
 
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Disxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f: 
           d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)

        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]   
        with open("bi.txt","r") as f:
            dz= f.read()

        screen_manager.get_screen('Disxx').yi.text =str(df[dz].describe())

class Bibar(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("bibarsave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Bar Graph"+d+".png"
        with open("bibarsave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)

    def rot(self):

        with open("barsta.txt", "r") as f:
            d = f.read()
        if d=="0":
            d='1'
            with open("barsta.txt", "w") as f:
                f.write(f"{d}")
        elif d=='1':
            d='0'
            with open("barsta.txt", "w") as f:
                f.write(f"{d}")
    
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Bibar.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))


    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            with open("wx1.txt","r") as f:
                d = f.read()   
            plt.title(d)
   
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  

            with open("bi.txt","r") as f:
                da = f.read() 

            with open("col.txt","r") as f:
                q= f.read() 
            with open("barsta.txt","r") as f:
                o= f.read() 
            if o=='0':
                sns.displot(data=df,y=da,color=q)
            else:
                sns.displot(data=df,x=da,color=q)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)     
            self.fig1 = plt.gcf()              
      
         
            screen_manager.get_screen('bic').t.text =""

            return self.fig1
        except f:
            screen_manager.get_screen('bic').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="bic"
            screen_manager.get_screen('bic').t.text_color =1,0,0,1 

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Bibar.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))



class Bibarx(Screen):

    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)

        with open("wx1.txt","r") as f:
            d = f.read()
        plt.title(d)

        df = pd.read_csv(d)[x:y]  
        with open("bi.txt","r") as f:
            da = f.read() 
        with open("col.txt","r") as f:
            q= f.read() 
            with open("barsta.txt","r") as f:
                o= f.read() 
        if o=='0':
            sns.displot(data=df,y=da,color=q)
        else:
            sns.displot(data=df,x=da,color=q)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)     
 
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()       
        self.fig1 = Bibarx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]   
        with open("bi.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Bibarx').yi.text =str(df[dz].describe())


class Stockvis(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
   
        with open("wx1.txt","r") as f:
            d = f.read()        
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  

        x1=df['High'].values.tolist()
        y1=df['Low'].values.tolist()
        z1=df['Close'].values.tolist()
        q1=df['Open'].values.tolist()
        r=df['Date'].values.tolist()

        plt.plot(r, x1,color="green", label = "High")
        plt.plot(r, z1,color="magenta", label = "Close")
        plt.plot(r, y1,color="red", label = "Low")
        plt.plot(r, q1,color="cyan", label = "Open")
        plt.xlabel("Date")
        plt.ylabel("Amount") 
        plt.title(d)
        plt.legend()
        plt.show()


        self.fig1 = plt.gcf()
        screen_manager.current="St1" 

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 =Stockvis.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  


class Hebxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
   
        with open("wx1.txt","r") as f:
            d = f.read()        
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  

        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        p = df[d].tolist()
        q = df[dz].tolist()  
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)   
 
 
        fig, ax = plt.subplots()
        with open("col.txt","r") as f:
            q= f.read() 
        with open("col.txt","r") as f:
            qq= f.read() 
        ax.hexbin(p,q, gridsize=20,color=qq)

        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Hebxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Hebxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Hebxx').yi.text =str(df[dz].describe())

    def Update(self):
        #self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Hebx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))


class Hebx(Screen):
    box = ObjectProperty(None)
    def sa(self):
        with open("hebsave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Hexabin Plot"+d+".png"
        with open("hebsave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)


    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)


            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  

            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read()
            p = df[d].tolist()
            q = df[dz].tolist()  
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)   
     
      
            fig, ax = plt.subplots()
            with open("col.txt","r") as f:
                qq= f.read() 

            ax.hexbin(p,q, gridsize=20,color=qq)

            self.fig1 = plt.gcf()

            screen_manager.get_screen('DC').t.text =""

            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"         

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Hebx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
    def Update(self):
        #self.box.remove_widget(FigureCanvasKivyAgg(self.fig1))
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Hebx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))

class Piexx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   

        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("bi.txt","r") as f:
            da = f.read() 
        p = df[da].tolist()


        plt.pie(p)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)     
 
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Piexx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        
        with open("bi.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Piexx').yi.text =str(df[dz].describe())

class Piex(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("piesave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Pie Chart"+d+".png"
        with open("piesave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)



    def add_plot(self, N):
        try:
            import matplotlib.pyplot as plt
       

            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)


            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]   
            with open("bi.txt","r") as f:
                da = f.read() 
            p = df[da].tolist()


            plt.pie(p)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)
            plt.show()
            self.fig1 = plt.gcf()
            screen_manager.get_screen('bic').t.text =""
            screen_manager.current='bic'
            return self.fig1
        except:
            screen_manager.get_screen('bic').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="bic"
            screen_manager.get_screen('bic').t.text_color =1,0,0,1 
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Piex.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))

class Barxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]    
 

        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
        with open("col.txt","r") as f:
            q= f.read()
        sns.barplot(x=d,y=dz,data=df,color=q)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)     
 
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Barxx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()

        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]   
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Barxx').xi.text =str(df[d].describe())
        screen_manager.get_screen('Barxx').yi.text =str(df[dz].describe())

class Barx(Screen):
    box = ObjectProperty(None)
    def sa(self):
        with open("barsave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Bar Graph"+d+".png"
        with open("barsave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)



    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  
     

            with open("wx4.txt","r") as f:
                d = f.read()   
            with open("wx5.txt","r") as f:
                dz= f.read() 
            with open("col.txt","r") as f:
                q= f.read()  
            sns.barplot(x=d,y=dz,data=df,color=None)
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)     
            screen_manager.get_screen('DC').t.text =""
            self.fig1 = plt.gcf()

            return self.fig1
        except:
            screen_manager.get_screen('DC').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="DC"  
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Barx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))






class My(Screen):      
    box = ObjectProperty(None)

    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
       
        for i in d: 
            self.box.add_widget(Button(text=str(i),color="white",background_color=(1,0,1,1), on_press=lambda x, y=i: self.uk(str(y))))         
   
    def uk(self,instance):
        d=str(instance)
        with open("wx4.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="My1" 


class T1(Screen):      
    box = ObjectProperty(None)

    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
       
        for i in d: 
            self.box.add_widget(Button(text=str(i),color="white",background_color=(1,0,1,1), on_press=lambda x, y=i: self.uk(str(y))))         
   
    def uk(self,instance):
        d=str(instance)
        with open("Tx.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="T2" 



class T2(Screen):      
    box = ObjectProperty(None)

    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
       
        for i in d: 
            self.box.add_widget(Button(text=str(i),color="white",background_color=(1,0,1,1), on_press=lambda x, y=i: self.uk(str(y))))         
   
    def uk(self,instance):
        d=str(instance)
        with open("Ty.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="T3" 



class T3(Screen):      
    box = ObjectProperty(None)

    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
       
        for i in d: 
            self.box.add_widget(Button(text=str(i),color="white",background_color=(1,0,1,1), on_press=lambda x, y=i: self.uk(str(y))))         
   
    def uk(self,instance):
        d=str(instance)
        with open("Tz.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="W3d"


class Triset(Screen):
    box = ObjectProperty(None)

    def swi(self, switchObject, switchValue):
        if (switchValue):
            screen_manager.get_screen('Triset').sw.active=True
            x=""
            with open("tri.txt","w") as f:
                f.write(f"{x}")  
    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
        for i in d: 
            print(i)
            self.box.add_widget(Button(text=str(i),color="white",background_color=(1,0,0,1), on_press=lambda x, y=i: self.uk(str(y))))         
   
    def uk(self,instance):
        d=str(instance)
        with open("tri.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="tri"            
        screen_manager.get_screen('Triset').sw.active=False

class My1(Screen):      
    box = ObjectProperty(None)

    def on_box(self, *args):
        with open("wx3.txt","r") as f:
            d = f.read()
        d=d.strip().split(",")
        d=list(filter(None,d))
       
        for i in d: 
            self.box.add_widget(Button(text=str(i),color="white",background_color=(0,1,1,1), on_press=lambda x, y=i: self.uk(str(y))))        
  
    def uk(self,instance):
        d=str(instance)
        with open("wx5.txt","w") as f:
            f.write(f"{d}")  
        screen_manager.current="DC" 


#Second Page
class SecondPage(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
        plt.style.use('dark_background')  
 
        sns.lineplot(y=dz, x=d,data=df,color="cyan")
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        self.fig1 = SecondPage.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
     



class Manager(ScreenManager):
    pass


class Pairxx(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
 
 
        sns.pairplot(data=df)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)  
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Pairx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        with open("wx1.txt","r") as f:
            d = f.read()
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  


class Pairx(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("pairsave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Pair Plot"+d+".png"
        with open("pairsave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)



    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        plt.title(d)

        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]   
    

        with open("wx4.txt","r") as f:
            d = f.read()   
        with open("wx5.txt","r") as f:
            dz= f.read()  
        with open("tri.txt","r") as f:
            f = f.read()
        if len(f)==0:
            sns.pairplot(data=df, hue=None)
        else: 
            sns.pairplot(data=df, hue=f)
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)  
        self.fig1 = plt.gcf()

        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Pairx.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
     
  
class Dp(Screen):
    box = ObjectProperty(None)
    def sa(self):
        with open("dpsave.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="Density Plot"+d+".png"
        with open("dpsave.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)



    def add_plot(self, N):
        try:

            import matplotlib.pyplot as plt
       
            with open("wx1.txt","r") as f:
                d = f.read()
            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            plt.title(d)

            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]  
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)      
            with open("bi.txt","r") as f:
                dl= f.read()
            p = df[dl].tolist()
            with open("col.txt","r") as f:
                q= f.read()
            sns.distplot(p,color=q)
            screen_manager.get_screen('bic').t.text =""
            self.fig1 = plt.gcf()
            return self.fig1
        except:
            screen_manager.get_screen('bic').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="bic"
            screen_manager.get_screen('bic').t.text_color =1,0,0,1 
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Dp.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))

class Dpxn(Screen):
    box = ObjectProperty(None)


    def add_plot(self, N):

        import matplotlib.pyplot as plt
   
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
        with open("wx6.txt","r") as f:
            da= f.read()  
        plt.style.use(da)      
        with open("bi.txt","r") as f:
            dl= f.read()
        p = df[dl].tolist()
        with open("col.txt","r") as f:
            q= f.read()
        sns.distplot(p,color=q)

        self.fig1 = plt.gcf()
        return self.fig1

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Dpxn.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
        else:   
            df = pd.read_csv(d)[x:y]  
 
        with open("bi.txt","r") as f:
            dz= f.read()
        screen_manager.get_screen('Dpxn').yi.text =str(df[dz].describe())








class Tl(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("Tlsav.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="3D Line Plot"+d+".png"
        with open("Tlsav.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)
    def add_plot(self, N):
        try:
            import matplotlib.pyplot as plt
            with open("wx1.txt","r") as f:
                d = f.read()

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            plt.title(d)

            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]    
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)           
            axes = plt.axes(projection='3d')

            with open("Tz.txt","r") as f:
                z = f.read()
            with open("Tx.txt","r") as f:
                x = f.read()
            with open("Ty.txt","r") as f:
                y = f.read()
            x1=df[x].values.tolist()
            y1=df[y].values.tolist()
            z1=df[z].values.tolist()

            with open("col.txt","r") as f:
                q= f.read()
            axes.plot3D(x1, y1, z1,q)
            axes.set_xlabel(x, fontweight ='bold')
            axes.set_ylabel(y, fontweight ='bold')
            axes.set_zlabel(z, fontweight ='bold')

            self.fig1 = plt.gcf()

            return self.fig1
        except:
    
            screen_manager.current ="W3d"

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Tl.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))



class Td(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("Tdsav.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="3D Density Plot"+d+".png"
        with open("Tdsav.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)
    def add_plot(self, N):
        try:
            import matplotlib.pyplot as plt
            with open("wx1.txt","r") as f:
                d = f.read()
            plt.title(d)


            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]    
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)           
            axes = plt.axes(projection='3d')

            with open("Tz.txt","r") as f:
                z = f.read()
            with open("Tx.txt","r") as f:
                x = f.read()
            with open("Ty.txt","r") as f:
                y = f.read()
            x1=df[x].values.tolist()
            y1=df[y].values.tolist()
            z1=df[z].values.tolist()
            with open("col.txt","r") as f:
                q= f.read()
            with open("col3.txt","r") as f:
                r= f.read()
            with open("mar.txt","r") as f:
                m= f.read()
            axes.scatter3D(x1, y1, z1,color=r,marker =m,s=500)
            axes.plot3D(x1, y1, z1,q)
            axes.set_xlabel(x, fontweight ='bold')
            axes.set_ylabel(y, fontweight ='bold')
            axes.set_zlabel(z, fontweight ='bold')

            self.fig1 = plt.gcf()
            screen_manager.get_screen('bic').t.text =""
          
            return self.fig1
        except:
            screen_manager.get_screen('bic').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="W3d"

    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Td.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))


















class Ts(Screen):
    box = ObjectProperty(None)

    def sa(self):
        with open("Tssav.txt","r") as f:
            d = f.read()
        d=int(d)
        d=d+1
        d=str(d)
        z="3D Scatter Plot"+d+".png"
        with open("Tssav.txt", "w") as f:
            f.write(f"{d}")
        plt.savefig(z)



    def add_plot(self, N):
        try:
            import matplotlib.pyplot as plt
       

            with open("wx1.txt","r") as f:
                d = f.read()

            with open("s1.txt","r") as f:
                x = f.read()
            with open("s2.txt","r") as f:
                y = f.read()
            plt.title(d)

            x=int(x)
            y=int(y)
            if "https:" in d:          
                s = requests.get(d).content
                df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]        
            else:   
                df = pd.read_csv(d)[x:y]       
            with open("wx6.txt","r") as f:
                da= f.read()  
            plt.style.use(da)           
            axes = plt.axes(projection='3d')
            with open("Tz.txt","r") as f:
                z = f.read()
            with open("Tx.txt","r") as f:
                x = f.read()
            with open("Ty.txt","r") as f:
                y = f.read()
            x1=df[x].values.tolist()
            y1=df[y].values.tolist()
            z1=df[z].values.tolist()
            with open("mar.txt","r") as f:
                m= f.read()

            with open("col3.txt","r") as f:
                q= f.read()
            axes.scatter3D(x1, y1, z1,color=q,marker =m,s=500)
            axes.set_xlabel(x, fontweight ='bold')
            axes.set_ylabel(y, fontweight ='bold')
            axes.set_zlabel(z, fontweight ='bold')
            plt.show()
            self.fig1 = plt.gcf()
            screen_manager.get_screen('bic').t.text =""
            screen_manager.current ="W3d"
            return self.fig1
        except:
            screen_manager.get_screen('bic').t.text ="Sorry, The following graph is not supported"
            screen_manager.current ="W3d"
            screen_manager.get_screen('bic').t.text_color =1,0,0,1  
    def on_pre_enter(self, *args):
        plt.cla()
        self.box.clear_widgets()
        self.fig1 = Ts.add_plot(self,1000)
        self.box.add_widget(FigureCanvasKivyAgg(self.fig1))



class MyNewApp(MDApp):
    title = "Data Analyzer"
    def Update(self):
        filechooser.open_file(on_selection=self.handle_selection)

    def res(self):
         
        screen_manager.get_screen('Rag').t1.text="0"
        screen_manager.get_screen('Rag').t.text="99999"
        x=0
        x1=99999
        try:
            x=int(x)
            x1=int(x1)
            if x<x1:
         
                with open("s1.txt","w") as f:
                    f.write(f"{x}")
                with open("s2.txt","w") as f:
                    f.write(f"{x1}")
           
        except:
            screen_manager.get_screen('Rag').er.text="ERROR"
    def sav1(self):     
            with open("s1.txt","r") as f:
                d = f.read()  
                return d     

    def sav2(self):     
            with open("s2.txt","r") as f:
                d = f.read()  
                return d
    def bx(self):
        screen_manager.get_screen('bic').t.text =""
        screen_manager.current ="bi"

    def piinfo(self):
        screen_manager.get_screen('bic').t.text ="A Pie Chart is suitable to analyse small data. It is normally used to compare areas of growth"
        screen_manager.get_screen('bic').t.text_color =0,0,0,1
    def biinfo(self):
        screen_manager.get_screen('bic').t.text ="The following graphs are used to analyse frequency of variable. It is suitable for all kinds of data "
        screen_manager.get_screen('bic').t.text_color =0,0,0,1 

    def joinfo(self):
        screen_manager.get_screen('DC').t.text ="A Joint Plot is used to compare 2 variables/columns with each other and seprately at a same time. It is suitable for all kinds of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def hiinfo(self):
        screen_manager.get_screen('DC').t.text ="In this Plot, darker the color, more is the frequency. It is suitable for all kinds of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def scinfo(self):
        screen_manager.get_screen('DC').t.text ="It plots the dot, when two variables are in relationship with each other. It is suitable for all kinds of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def viinfo(self):
        screen_manager.get_screen('DC').t.text ="In this Plot, more the width, more is the frequency. It is suitable for all kinds of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def swinfo(self):
        screen_manager.get_screen('DC').t.text ="In this plot, the points are adjusted in such a way that it won’t get overlap. It is suitable for small to medium size of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def heinfo(self):
        screen_manager.get_screen('DC').t.text ="This Plot is the mixture of scatter and hist plot. It is suitable for all sizes of numeric data "  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def liinfo2(self):
        screen_manager.get_screen('DC').t.text ="In this plot, A line is plotted to show the relationship between 2 variables"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def stinfo(self):
        screen_manager.get_screen('DC').t.text ="It plots the dot, when two variables are in relationship with each other. It plots the dot individualy. It is suitable for small to medium size of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def bainfo(self):
        screen_manager.get_screen('DC').t.text ="This graph is mainly used in comparing one variable with many attributes. It is suitable for all kinds of data"  
        screen_manager.get_screen('DC').t.text_color =0,0,0,1 

    def upinfo(self):
        screen_manager.get_screen('Start').t.text ="Select this option, When you want to upload the file from storage"  

    def urinfo(self):
        screen_manager.get_screen('Start').t.text ="Select this option, When you want to upload the file from online csv file"  
   

    def sav(self):
         
        x=screen_manager.get_screen('Rag').t1.text 
        x1=screen_manager.get_screen('Rag').t.text
        try:
      
            x=int(x)
            x1=int(x1)
            if x<x1:
         
                with open("s1.txt","w") as f:
                    f.write(f"{x}")
                with open("s2.txt","w") as f:
                    f.write(f"{x1}")
        
            screen_manager.current="Settin" 
        except d:
            screen_manager.get_screen('Rag').er.text="ERROR"
     

    def handle_selection(self, selection):
        rv=selection
        rv = ' '.join([str(elem) for elem in rv])
        d=rv.replace("'","")
        d=d.replace("[","")
        rv=d.replace("]","")
        import pathlib
        file_extension = pathlib.Path(rv).suffix
     
    
        if file_extension==".csv":
            with open("wx1.txt","w") as f:
                f.write(f"{rv}")
       
            df = pd.read_csv(rv)
            for col in df.columns:
                col=col+","     
                with open("wx2.txt","a") as f:
                    f.write(f"{col}")
            with open("wx2.txt","r") as f:
                d = f.read()   
            with open("wx3.txt","w") as f:
                f.write(f"{d}")
 
            screen_manager.current="set"            
        else:
            screen_manager.get_screen('StartPage').ox.text="INVALID FILE FORMAT ("+file_extension+")"


    def ge(self):
        rv=screen_manager.get_screen('UR').t.text
    
        try:
            with open("wx1.txt","w") as f:
                f.write(f"{rv}")
         
            import io
            import requests

                     
            #s = requests.get(rv).content
            #try:
                #df = pd.read_csv(io.StringIO(s.decode('utf-8')), sep='delimiter', header=None,engine='python')
            #except:
                #df = pd.read_csv(s)
            try:
                url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
                c=pd.read_csv(rv)
                c.columns
                
                for col in c.columns:
                    col=str(col)
                    col=col+","   
                    print(col)
                    with open("wx2.txt","a") as f:
                        f.write(f"{col}")
                with open("wx2.txt","r") as f:
                    d = f.read()   
                with open("wx3.txt","w") as f:
                    f.write(f"{d}")
            except:
                print('dd')
  
            screen_manager.current="set"            
        except c:
            screen_manager.get_screen('UR').ox.text="If you don't know the meaning of csv file or URL. Kindly, don't use this application"

  
    def teex(self):
        with open("wx1.txt","r") as f:
            d = f.read()
        with open("s1.txt","r") as f:
            x = f.read()
        with open("s2.txt","r") as f:
            y = f.read()
        x=int(x)
        y=int(y)   
        if "https:" in d:          
            s = requests.get(d).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))[x:y]      
        else:   
            with open("wx1.txt","r") as f:
                d = f.read()
            df = pd.read_csv(d)[x:y] 
        screen_manager.get_screen('Cou').t.text =str(df.count())
        screen_manager.current="Cou" 
  
    def bg(self): 
        import random
        l1=0,1,1,1
        l2=1,0,1,1
        l4=0,1,0,1

        l5=1,1,0,1

        l6=0,0,1,22

     
        x=[l1,l2,l4,l5,l6][random.randrange(4)]
        return x


    def rd(self): 
        import random
        x=["deco1.jpg","deco2.jfif","deco3.jfif","deco4.jfif","deco5.jfif","deco6.jpg"][random.randrange(5)]
        return x





    def st(self):
        with sr.Microphone() as source:
            print("yes sir!! What can i do for you?")
            voice = listener.listen(source)
            ut = listener.recognize_google(voice)
            if ut=="select single variable":
                screen_manager.current="bi"
                engine_talk("As you say King")
            
            elif ut=="select double variable":
                screen_manager.current="My"
                engine_talk("As you say King")  
                        
            elif ut=="select multiple variable":
                screen_manager.current="tri"
                engine_talk("As you say King")        
            print(ut)



    def nxc1(self,dt):
        with open("nxc.txt","r") as f:
            asz = f.read()
     
        if asz=="0":
            asz="1"
            screen_manager.get_screen('set').b1.text_color=1,0,1,1
            with open("nxc.txt", "w") as f:
                f.write(f"{asz}")
        elif asz=="1":
            asz="2"  
            screen_manager.get_screen('set').b1.text_color=0,1,1, 1
            with open("nxc.txt", "w") as f:
                f.write(f"{asz}")
        elif asz=="2":
            asz="3"  
            screen_manager.get_screen('set').b1.text_color=1,1,0, 1
            with open("nxc.txt", "w") as f:
                f.write(f"{asz}")
        elif asz=="3":
            asz="4"  
            screen_manager.get_screen('set').b1.text_color=1,0,1, 1
            with open("nxc.txt", "w") as f:
                f.write(f"{asz}")
        elif asz=="4":
            asz="5"  
            screen_manager.get_screen('set').b1.text_color=0,1,1, 1
            with open("nxc.txt", "w") as f:
                f.write(f"{asz}")
        elif asz=="5":
            asz="0"  
            screen_manager.get_screen('set').b1.text_color=1,1,0, 1
            with open("nxc.txt", "w") as f:
                f.write(f"{asz}")
  

    def build(self):
        global screen_manager
        screen_manager = Manager() 
        Clock.schedule_interval(self.nxc1, 1 / 20.)
        return screen_manager    





MyNewApp().run()
