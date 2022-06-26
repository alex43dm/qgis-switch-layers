#-----------------------------------------------------------
# Copyright (C) 2022 Oleksandr Dmytrenko
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------

from PyQt5.QtWidgets import QAction, QMessageBox
from qgis.core import QgsProject

def classFactory(iface):
    return SwitchLayer(iface)

class SwitchLayer:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action1 = QAction('L1', self.iface.mainWindow())
        self.action1.triggered.connect(self.run1)
        self.action1.setShortcut('Alt+1')
        self.iface.addToolBarIcon(self.action1)
        self.action2 = QAction('L2', self.iface.mainWindow())
        self.action2.triggered.connect(self.run2)
        self.action2.setShortcut('Alt+2')
        self.iface.addToolBarIcon(self.action2)
        self.action3 = QAction('L3', self.iface.mainWindow())
        self.action3.triggered.connect(self.run3)
        self.action3.setShortcut('Alt+3')
        self.iface.addToolBarIcon(self.action3)
        self.action4 = QAction('L4', self.iface.mainWindow())
        self.action4.triggered.connect(self.run4)
        self.action4.setShortcut('Alt+4')
        self.iface.addToolBarIcon(self.action4)
        self.action5 = QAction('L5', self.iface.mainWindow())
        self.action5.triggered.connect(self.run5)
        self.action5.setShortcut('Alt+5')
        self.iface.addToolBarIcon(self.action5)
        self.action6 = QAction('L6', self.iface.mainWindow())
        self.action6.triggered.connect(self.run6)
        self.action6.setShortcut('Alt+6')
        self.iface.addToolBarIcon(self.action6)

    def unload(self):
        self.iface.removeToolBarIcon(self.action1)
        del self.action1
        self.iface.removeToolBarIcon(self.action2)
        del self.action2
        self.iface.removeToolBarIcon(self.action3)
        del self.action3
        self.iface.removeToolBarIcon(self.action4)
        del self.action4
        self.iface.removeToolBarIcon(self.action5)
        del self.action5
        self.iface.removeToolBarIcon(self.action6)
        del self.action6

    def run(self,n):
        i = 0
        root = QgsProject.instance().layerTreeRoot()
        for layer in root.layerOrder():
            if i != 0 and i != n:
                visible = False
            else:
                visible = True
            root.findLayer(layer.id()).setItemVisibilityChecked(visible)
            i += 1

    def run1(self):
        root = QgsProject.instance().layerTreeRoot()
        l = root.findLayer(root.layerOrder()[0].id())
        l.setItemVisibilityChecked(not l.isVisible())

    def run2(self):
        self.run(1)

    def run3(self):
        self.run(2)

    def run4(self):
        self.run(3)

    def run5(self):
        self.run(4)

    def run6(self):
        self.run(5)

