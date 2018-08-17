# -*- coding: utf-8 -*-

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder 
from kivy.properties import StringProperty 

Builder.load_string(''' 
#: import MDFlatButton kivymd.button.MDFlatButton 

# Данные инструкции в Kivy-Language аналогичны импорту в python сценариях: 
# from kivymd.button import MDFlatButton 
# 
# В kv-файле вы можете включать другие файлы разметки, 
# если интерфейс, например, слишком сложный: #: include your_kv_file.kv 
#
# Стандартные виджеты и контроллы, предоставляемые Kivy из коробки,
# не нужно импортировать в Activity — просто используйте их.

# Все элементы данного Activity будут располагаться в BoxLayout - 
# виджете, от которого унаследован базовый класс. 
<StartScreen> 
    orientation: 'vertical'
    Label:
        color: [0,0,0,1]
        text_size: root.width, None
        halign: 'left'
        size_hint_y: None
        height: '30dp'
        text: 'Считайте штрих-код:' 
    
    TextInput:
        size_hint_y: None
        height: '40dp'

    MDFlatButton: 
        id: button 
        text: 'Press Me' 
        size_hint_x: 1  # относительная ширина контролла - от 0 до 1 
        pos_hint: {'y': .5}  # положение контролла относительно вертикали 'y' корневого виджета 

        # Событие контролла. 
        on_release: 
            # Ключевое слово 'root' - это инстанс базового класса разметки, 
            # через который вы можете получить доступ ко всем его методам и атрибутам. 
            root.set_text_on_button() 

    Widget:
''') 
# Или Builder.load_file('path/to/kv-file'), 
# если разметка Activity находится в файле. 

class StartScreen(BoxLayout): 
    '''Базовый класс.''' 

    new_text_for_button = StringProperty() 
    # В Kivy вы должны явно указывать тип атрибутов: 
    # 
    # StringProperty; 
    # NumericProperty; 
    # BoundedNumericProperty; 
    # ObjectProperty; 
    # DictProperty; 
    # ListProperty; 
    # OptionProperty; 
    # AliasProperty; 
    # BooleanProperty; 
    # ReferenceListProperty; 
    # 
    # в противном случае вы получите ошибку 
    # при установке значений этих атрибутов. 
    # 
    # Например, если не указывать тип: 
    # 
    # new_text_for_button = '' 
    # 
    # будет возбуждено исключение - 
    # TypeError: object.__init__() takes no parameters. 

    def set_text_on_button(self): 
        self.ids.button.text = self.new_text_for_button 
        # ids - это словарь всех объектов Activity 
        # которым назначен идентификатор. 
        # 
        # Так, обратившись через идентификатор 'button' - self.ids.button - 
        # к объекту кнопки, мы получаем доступ 
        # ко всем его методам и атрибутам. 

    # Любой атрибут, инициализировванный как Properties, 
    # автоматически получает метод в базовом классе с префиксом 'on_', 
    # который будет вызван как только данный атрибут получит новое значение. 
    def on_new_text_for_button(self, instance, value): 
        print(instance, value) 

class Program(App): 
    def build(self): 
        '''Метод, вызываемый при старте программы. 
        Должен возвращать объект создаваемого Activity.''' 

        return StartScreen(new_text_for_button='This new text') 

if __name__ in ('__main__', '__android__'): 
    Program().run()  # запуск приложения