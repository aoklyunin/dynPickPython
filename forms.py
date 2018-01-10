#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from DynPicker import DynPicker


class Frame(wx.Frame):
    # закрытие формы
    def onClose(self, event):
        # останавливаем таймер
        self.timer.Stop()
        self.Close()

    # события по таймеру
    def OnTimer(self, event):
        forces = self.dp.readForces(True)
        for i in range(6):
            self.textes[i].Clear()
            self.textes[i].AppendText("%.2f"%forces[0])

    # конструктор
    def __init__(self, parent=None, id=-1, title='', pos=(0, 0), size=(480,70)):
        # создаём фрейм
        wx.Frame.__init__(self, parent, id, title, pos, size)
        # добавляем на фрейм панель
        self.panel = wx.Panel(self)
        # инициализируем элементы управления
        self.initControlItems()
        self.dp = DynPicker()
        # запускаем таймер
        self.timer = wx.Timer(self, -1)
        # раз в 0.2 секунды
        self.timer.Start(200)
        # указываем функцию, которая будет вызываться по таймеру
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

    # инициализируем элементы управления
    def initControlItems(self):
        # создаём поля ввода для координат тележки
        self.textes = [ wx.TextCtrl(self.panel, -1, '0', pos=(10+i*80, 30), size=(60, 30)) for i in range(10)]
        captions = ["Fx", "Fy", "Fz", "Mx", "My", "Mz"]
        for i in range(6):
            self.textes[i].SetBackgroundColour('#DDFFEE')
            self.textes[i].SetWindowStyle(wx.TE_RIGHT)
            wx.StaticText(self.panel,-1, captions[i], pos=(i*80+30, 10), size=(40, 30))




