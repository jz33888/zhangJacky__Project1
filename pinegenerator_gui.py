from PySide6 import QtWidgets, QtCore, QtGui
from shiboken6 import wrapInstance

import pinetreegenerator

#maya window
def get_maya_main_win():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)

#gui class
class PineTreeGeneratorWin(QtWidgets.QDialog):

    def __init__(self):
        
