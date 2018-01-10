#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from forms import Frame

# класс приложения
class App(wx.App):
    # инициализация приложения
    def OnInit(self):
        # создание окна
        self.frame = Frame(None,-1,"Sensor DynPick")
        # отображение окна
        self.frame.Show(True)
        # указываем, что только что созданное окно - главное
        self.SetTopWindow(self.frame)
        return True # ну не False же возвращать, правда?:)

    # завершение приложения
    def shutdown(self):
        # закрываем приложение
        self.frame.Close()


# главная функция
if __name__=='__main__':
    # объект класса приложение
    app = App()
    # запускаем главный цикл приложения
    app.MainLoop()


