# -*- coding: utf-8 -*-
import time
from call import *
# Form implementation generated from reading ui file 'avtovaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this fi
#
#
# le unless you know what you are doing.
from io import StringIO
import faulthandler
from EDR_read import *
from PyQt5 import QtCore, QtGui, QtWidgets
import codecs
import re
import math
import STO_tests_V2_nanopb_pb2 as Messages
import serial
import threading
from states import *
from serial.tools import list_ports
from Reprogramm import *
import os
import subprocess
import sys
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
class Ui_MainWindow(object):
    def __init__(self):
        self.file = None
        self.tests_dict=dict()

    def setupUi(self, MainWindow):
        #buffer=[0x69,0x40,0x2C,0x40,0x64,0x40,0x69,0x40,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x2C,0x40,0xD0,0x07,0x00,0x28,0x28,0x28,0x28,0x28,0x28,0x28,0x28,0x28,0x28,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0x00,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x40,0x00,0x0C,0x00,0x01,0x00,0x1A,0x00,0x1A,0x00,0xFE,0xFE,0x01,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0x62,0x40,0x5F,0x40,0x60,0x60,0x40,0x60,0x40,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5F,0x40,0xD0,0x07,0xE8,0x03,0x00,0x00,0x4B,0x0C,0x4B,0x0E,0x4B,0x0E,0x4B,0x10,0x4B,0x10,0x4B,0x00,0x4B,0x00,0x4B,0x00,0x4B,0x00,0x4B,0x02,0xFE,0xFF,0xFE,0xFF,0xFE,0xFF,0xFE,0xFF,0x00,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x00,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x00,0x00,0x00,0x00,0x94,0xB6,0x94,0xB6,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x15,0x00,0x15,0x00,0xFE,0xFE,0xFE,0xFE,0x01,0x01,0x01,0xFE,0x0F,0x0F,0x0F,0x0F,0x0F,0x0F,0x0F,0x0F,0x0F,0x0F,0x0F,0x0A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0A,0x00,0x00,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x14,0x03,0x00,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE,0xFE]
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 960)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        os.chdir('pillows')
        os.chdir('..')
        self.COM_PORT=None
        self.UART=None
        self.progress_changed = QtCore.pyqtSignal(int)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        font=QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.init_tab = QtWidgets.QWidget()
        self.init_tab.setObjectName("init_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.init_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_13 = QtWidgets.QGroupBox(self.init_tab)

        font.setPointSize(16)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.VALIDAB_BRS = QtWidgets.QTextBrowser(self.groupBox_13)
        self.VALIDAB_BRS.setObjectName("VALIDAB_BRS")
        self.VALIDAB_BRS.setFont(font)
        self.gridLayout_2.addWidget(self.VALIDAB_BRS, 2, 0, 1, 2)
        self.STOP_BTN_8 = QtWidgets.QPushButton(self.groupBox_13)
        self.STOP_BTN_8.setMinimumSize(QtCore.QSize(0, 55))

        font.setPointSize(12)
        self.STOP_BTN_8.setFont(font)
        self.STOP_BTN_8.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_8.setObjectName("STOP_BTN_8")
        self.gridLayout_2.addWidget(self.STOP_BTN_8, 1, 1, 1, 1)
        self.START_VALID_AB_BTN = QtWidgets.QPushButton(self.groupBox_13)
        self.START_VALID_AB_BTN.setMinimumSize(QtCore.QSize(0, 55))

        font.setPointSize(12)
        self.START_VALID_AB_BTN.setFont(font)
        self.START_VALID_AB_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.START_VALID_AB_BTN.setObjectName("START_VALID_AB_BTN")
        self.gridLayout_2.addWidget(self.START_VALID_AB_BTN, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_13, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.init_tab)

        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.STOP_BTN_3 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STOP_BTN_3.sizePolicy().hasHeightForWidth())
        self.STOP_BTN_3.setSizePolicy(sizePolicy)
        self.STOP_BTN_3.setMinimumSize(QtCore.QSize(0, 55))

        font.setPointSize(12)
        self.STOP_BTN_3.setFont(font)
        self.STOP_BTN_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_3.setObjectName("STOP_BTN_3")
        self.gridLayout_3.addWidget(self.STOP_BTN_3, 1, 2, 1, 1)
        self.Inittime_lbl = QtWidgets.QLabel(self.groupBox_2)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.Inittime_lbl.setFont(font)
        self.Inittime_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.Inittime_lbl.setObjectName("Inittime_lbl")
        self.gridLayout_3.addWidget(self.Inittime_lbl, 2, 1, 1, 1)
        self.inittime_brs = QtWidgets.QTextBrowser(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inittime_brs.sizePolicy().hasHeightForWidth())
        self.inittime_brs.setSizePolicy(sizePolicy)
        self.inittime_brs.setMinimumSize(QtCore.QSize(0, 30))

        font.setPointSize(16)
        self.inittime_brs.setFont(font)
        self.inittime_brs.setObjectName("inittime_brs")
        self.gridLayout_3.addWidget(self.inittime_brs, 3, 1, 1, 1)
        self.can_msg_lbl = QtWidgets.QLabel(self.groupBox_2)

        font.setPointSize(16)
        self.can_msg_lbl.setFont(font)
        self.can_msg_lbl.setObjectName("can_msg_lbl")
        self.gridLayout_3.addWidget(self.can_msg_lbl, 6, 1, 1, 1)
        self.Initreuult_lbl = QtWidgets.QLabel(self.groupBox_2)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.Initreuult_lbl.setFont(font)
        self.Initreuult_lbl.setObjectName("Initreuult_lbl")
        self.gridLayout_3.addWidget(self.Initreuult_lbl, 2, 2, 1, 1)
        self.initresult_brs = QtWidgets.QTextBrowser(self.groupBox_2)

        font.setPointSize(16)
        self.initresult_brs.setFont(font)
        self.initresult_brs.setObjectName("initresult_brs")
        self.gridLayout_3.addWidget(self.initresult_brs, 3, 2, 1, 1)
        self.can_msg_brs = QtWidgets.QTextBrowser(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.can_msg_brs.sizePolicy().hasHeightForWidth())
        self.can_msg_brs.setSizePolicy(sizePolicy)
        self.can_msg_brs.setMinimumSize(QtCore.QSize(0, 100))

        font.setPointSize(14)
        self.can_msg_brs.setFont(font)
        self.can_msg_brs.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.can_msg_brs.setObjectName("can_msg_brs")
        self.gridLayout_3.addWidget(self.can_msg_brs, 7, 1, 1, 2)
        self.Run_Init_btn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Run_Init_btn.sizePolicy().hasHeightForWidth())
        self.Run_Init_btn.setSizePolicy(sizePolicy)
        self.Run_Init_btn.setMinimumSize(QtCore.QSize(50, 55))

        font.setPointSize(12)
        self.Run_Init_btn.setFont(font)
        self.Run_Init_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Run_Init_btn.setObjectName("Run_Init_btn")
        self.gridLayout_3.addWidget(self.Run_Init_btn, 0, 2, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.init_tab, "")
        self.can_tab = QtWidgets.QWidget()
        self.can_tab.setObjectName("can_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.can_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.can_tab)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)

        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 3, 1, 1, 1)
        self.accepted_trig_brs = QtWidgets.QTextBrowser(self.groupBox_4)

        font.setPointSize(14)
        self.accepted_trig_brs.setFont(font)
        self.accepted_trig_brs.setObjectName("accepted_trig_brs")
        self.gridLayout_5.addWidget(self.accepted_trig_brs, 3, 0, 2, 1)
        self.expected_trig_brs = (QtWidgets.QTextBrowser(self.groupBox_4))
        self.expected_trig_brs.setObjectName("expected_trig_brs")
        self.gridLayout_5.addWidget(self.expected_trig_brs, 3, 4, 1, 1)
        self.measured_trig_brs = QtWidgets.QTextBrowser(self.groupBox_4)

        font.setPointSize(14)
        self.expected_trig_brs.setFont(font)
        self.measured_trig_brs.setFont(font)
        self.measured_trig_brs.setObjectName("measured_trig_brs")
        self.gridLayout_5.addWidget(self.measured_trig_brs, 4, 4, 1, 1)
        self.result_trig_brs = QtWidgets.QTextBrowser(self.groupBox_4)

        font.setPointSize(14)
        self.result_trig_brs.setFont(font)
        self.result_trig_brs.setObjectName("result_trig_brs")
        self.gridLayout_5.addWidget(self.result_trig_brs, 8, 4, 1, 1)
        self.measured_trig_lbl = QtWidgets.QLabel(self.groupBox_4)

        font.setPointSize(14)
        self.measured_trig_lbl.setFont(font)
        self.measured_trig_lbl.setObjectName("measured_trig_lbl")
        self.gridLayout_5.addWidget(self.measured_trig_lbl, 4, 1, 1, 1)
        self.result_trig_lbl = QtWidgets.QLabel(self.groupBox_4)

        font.setPointSize(14)
        self.result_trig_lbl.setFont(font)
        self.result_trig_lbl.setObjectName("result_trig_lbl")
        self.gridLayout_5.addWidget(self.result_trig_lbl, 8, 1, 1, 1)
        self.start_trig_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.start_trig_btn.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.start_trig_btn.setFont(font)
        self.start_trig_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start_trig_btn.setObjectName("start_trig_btn")
        self.gridLayout_5.addWidget(self.start_trig_btn, 0, 4, 1, 1)
        self.STOP_BTN_2 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STOP_BTN_2.sizePolicy().hasHeightForWidth())
        self.STOP_BTN_2.setSizePolicy(sizePolicy)
        self.STOP_BTN_2.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.STOP_BTN_2.setFont(font)
        self.STOP_BTN_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_2.setObjectName("STOP_BTN_2")
        self.gridLayout_5.addWidget(self.STOP_BTN_2, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)

        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.accepted_trig_lbl = QtWidgets.QLabel(self.groupBox_4)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.accepted_trig_lbl.setFont(font)
        self.accepted_trig_lbl.setObjectName("accepted_trig_lbl")
        self.gridLayout_5.addWidget(self.accepted_trig_lbl, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.can_tab)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
        self.period_peciodic_title = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.period_peciodic_title.sizePolicy().hasHeightForWidth())
        self.period_peciodic_title.setSizePolicy(sizePolicy)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.period_peciodic_title.setFont(font)
        self.period_peciodic_title.setObjectName("period_peciodic_title")
        self.gridLayout_4.addWidget(self.period_peciodic_title, 0, 0, 1, 3)
        self.STOP_BTN_1 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STOP_BTN_1.sizePolicy().hasHeightForWidth())
        self.STOP_BTN_1.setSizePolicy(sizePolicy)
        self.STOP_BTN_1.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.STOP_BTN_1.setFont(font)
        self.STOP_BTN_1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_1.setObjectName("STOP_BTN_1")
        self.gridLayout_4.addWidget(self.STOP_BTN_1, 2, 5, 1, 1)
        self.perod_periodic_btn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perod_periodic_btn.sizePolicy().hasHeightForWidth())
        self.perod_periodic_btn.setSizePolicy(sizePolicy)
        self.perod_periodic_btn.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.perod_periodic_btn.setFont(font)
        self.perod_periodic_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.perod_periodic_btn.setObjectName("perod_periodic_btn")
        self.gridLayout_4.addWidget(self.perod_periodic_btn, 0, 5, 1, 1)
        self.result_periodic_brs = QtWidgets.QTextBrowser(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_periodic_brs.sizePolicy().hasHeightForWidth())
        self.result_periodic_brs.setSizePolicy(sizePolicy)
        self.result_periodic_brs.setMinimumSize(QtCore.QSize(371, 40))

        font.setPointSize(14)
        self.result_periodic_brs.setFont(font)
        self.result_periodic_brs.setObjectName("result_periodic_brs")
        self.gridLayout_4.addWidget(self.result_periodic_brs, 10, 5, 1, 1)
        self.measured_period_brs = QtWidgets.QTextBrowser(self.groupBox_3)

        font.setPointSize(14)
        self.measured_period_brs.setFont(font)
        self.measured_period_brs.setObjectName("measured_period_brs")
        self.gridLayout_4.addWidget(self.measured_period_brs, 7, 5, 1, 1)
        self.expected_period_brs = QtWidgets.QTextBrowser(self.groupBox_3)

        font.setPointSize(14)
        self.expected_period_brs.setFont(font)
        self.expected_period_brs.setObjectName("expected_period_brs")
        self.gridLayout_4.addWidget(self.expected_period_brs, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)

        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)

        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 7, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)

        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 10, 2, 1, 1)
        self.accepted_periodic_brs = QtWidgets.QTextBrowser(self.groupBox_3)

        font.setPointSize(14)
        self.accepted_periodic_brs.setFont(font)
        self.accepted_periodic_brs.setObjectName("accepted_periodic_brs")
        self.gridLayout_4.addWidget(self.accepted_periodic_brs, 3, 0, 5, 1)
        self.gridLayout_9.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.can_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.exp_res_acc_brs = QtWidgets.QTextBrowser(self.groupBox_5)

        font.setPointSize(12)
        self.exp_res_acc_brs.setFont(font)
        self.exp_res_acc_brs.setObjectName("exp_res_acc_brs")
        self.gridLayout_7.addWidget(self.exp_res_acc_brs, 1, 1, 1, 1)
        self.got_res_brs = QtWidgets.QTextBrowser(self.groupBox_5)

        font.setPointSize(12)
        self.got_res_brs.setFont(font)
        self.got_res_brs.setObjectName("got_res_brs")
        self.gridLayout_7.addWidget(self.got_res_brs, 3, 1, 1, 1)
        self.got_res_acc_lbl = QtWidgets.QLabel(self.groupBox_5)

        font.setPointSize(16)
        self.got_res_acc_lbl.setFont(font)
        self.got_res_acc_lbl.setObjectName("got_res_acc_lbl")
        self.gridLayout_7.addWidget(self.got_res_acc_lbl, 2, 1, 1, 1)
        self.expected_res_acc_lbl = QtWidgets.QLabel(self.groupBox_5)

        font.setPointSize(16)
        self.expected_res_acc_lbl.setFont(font)
        self.expected_res_acc_lbl.setObjectName("expected_res_acc_lbl")
        self.gridLayout_7.addWidget(self.expected_res_acc_lbl, 0, 1, 1, 1)
        self.gridLayout_25.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab_2)

        font.setPointSize(14)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.CRASHDETECTED_BRS = QtWidgets.QTextBrowser(self.groupBox_20)
        self.CRASHDETECTED_BRS.setObjectName("CRASHDETECTED_BRS")

        font.setPointSize(12)
        self.CRASHDETECTED_BRS.setFont(font)
        self.gridLayout_10.addWidget(self.CRASHDETECTED_BRS, 0, 0, 1, 1)
        self.gridLayout_25.addWidget(self.groupBox_20, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setFont(font)
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.start_acc_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_acc_btn.sizePolicy().hasHeightForWidth())
        self.start_acc_btn.setSizePolicy(sizePolicy)
        self.start_acc_btn.setMinimumSize(QtCore.QSize(100, 55))

        font.setPointSize(12)
        self.start_acc_btn.setFont(font)
        self.start_acc_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start_acc_btn.setObjectName("start_acc_btn")
        self.gridLayout_6.addWidget(self.start_acc_btn, 1, 0, 1, 1)
        self.acc_selector = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acc_selector.sizePolicy().hasHeightForWidth())
        self.acc_selector.setSizePolicy(sizePolicy)
        self.acc_selector.setMaximumSize(QtCore.QSize(16777215, 45))

        font.setPointSize(13)
        self.acc_selector.setFont(font)
        self.acc_selector.setObjectName("acc_selector")
        folder_path = 'pillows\\test_folder\\XGF'
        # Перебираем все файлы в указанной папке
        for filename in os.listdir(folder_path):
            if filename.startswith("~$"):
                continue
            if filename.endswith('.csv'):  # Проверяем, что файл имеет расширение .csv
                file_path = os.path.join(folder_path, filename)
                self.acc_selector.addItem(filename.replace(".csv",""))
        self.gridLayout_6.addWidget(self.acc_selector, 5, 0, 1, 1)
        #self.AIRBAG_OFF_btn = QtWidgets.QRadioButton(self.groupBox)

        font.setPointSize(12)
        #self.AIRBAG_OFF_btn.setFont(font)
        #self.AIRBAG_OFF_btn.setObjectName("AIRBAG_OFF_btn")
        #self.gridLayout_6.addWidget(self.AIRBAG_OFF_btn, 0, 0, 1, 1)
        self.acc_selector_lbl = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acc_selector_lbl.sizePolicy().hasHeightForWidth())
        self.acc_selector_lbl.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.acc_selector_lbl.setFont(font)
        self.acc_selector_lbl.setObjectName("acc_selector_lbl")
        self.acc_set_changed()
        self.gridLayout_6.addWidget(self.acc_selector_lbl, 4, 0, 1, 1)
        self.STOP_BTN_4 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STOP_BTN_4.sizePolicy().hasHeightForWidth())
        self.STOP_BTN_4.setSizePolicy(sizePolicy)
        self.STOP_BTN_4.setMinimumSize(QtCore.QSize(0, 55))

        font.setPointSize(12)
        self.STOP_BTN_4.setFont(font)
        self.STOP_BTN_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_4.setObjectName("STOP_BTN_4")
        self.gridLayout_6.addWidget(self.STOP_BTN_4, 3, 0, 1, 1)
        self.gridLayout_25.addWidget(self.groupBox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.exp_res_SBR_brs = QtWidgets.QTextBrowser(self.groupBox_6)

        font.setPointSize(14)
        self.exp_res_SBR_brs.setFont(font)
        self.exp_res_SBR_brs.setObjectName("exp_res_SBR_brs")
        self.gridLayout_11.addWidget(self.exp_res_SBR_brs, 6, 0, 1, 1)
        self.exp_res_SBR_lbl = QtWidgets.QLabel(self.groupBox_6)

        font.setPointSize(16)
        self.exp_res_SBR_lbl.setFont(font)
        self.exp_res_SBR_lbl.setObjectName("exp_res_SBR_lbl")
        self.gridLayout_11.addWidget(self.exp_res_SBR_lbl, 5, 0, 1, 1)
        self.got_res_SBR_brs = QtWidgets.QTextBrowser(self.groupBox_6)

        font.setPointSize(14)
        self.got_res_SBR_brs.setFont(font)
        self.got_res_SBR_brs.setObjectName("got_res_SBR_brs")
        self.gridLayout_11.addWidget(self.got_res_SBR_brs, 8, 0, 1, 1)
        self.got_res_SBR_lbl = QtWidgets.QLabel(self.groupBox_6)

        font.setPointSize(16)
        self.got_res_SBR_lbl.setFont(font)
        self.got_res_SBR_lbl.setObjectName("got_res_SBR_lbl")
        self.gridLayout_11.addWidget(self.got_res_SBR_lbl, 7, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)

        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.start_SBR_btn = QtWidgets.QPushButton(self.groupBox_7)
        self.start_SBR_btn.setMinimumSize(QtCore.QSize(0, 42))

        font.setPointSize(12)
        self.start_SBR_btn.setFont(font)
        self.start_SBR_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start_SBR_btn.setObjectName("start_SBR_btn")
        self.gridLayout_12.addWidget(self.start_SBR_btn, 2, 0, 1, 1)
        self.STOP_BTN_5 = QtWidgets.QPushButton(self.groupBox_7)
        self.STOP_BTN_5.setMinimumSize(QtCore.QSize(0, 42))

        font.setPointSize(12)
        self.STOP_BTN_5.setFont(font)
        self.STOP_BTN_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_5.setObjectName("STOP_BTN_5")
        self.gridLayout_12.addWidget(self.STOP_BTN_5, 2, 1, 1, 1)
        self.Seatbelt_selector = QtWidgets.QComboBox(self.groupBox_7)
        self.Seatbelt_selector.setMinimumSize(QtCore.QSize(0, 32))

        font.setPointSize(11)
        self.Seatbelt_selector.setFont(font)
        self.Seatbelt_selector.setObjectName("Seatbelt_selector")
        self.Seatbelt_selector.addItem("")
        self.Seatbelt_selector.addItem("")
        self.Seatbelt_selector.addItem("")
        self.Seatbelt_selector.addItem("")
        self.Seatbelt_selector.addItem("")
        self.gridLayout_12.addWidget(self.Seatbelt_selector, 1, 0, 1, 2)
        self.SBR_test_selector = QtWidgets.QComboBox(self.groupBox_7)
        self.SBR_test_selector.setMinimumSize(QtCore.QSize(0, 32))

        font.setPointSize(11)
        self.SBR_test_selector.setFont(font)
        self.SBR_test_selector.setObjectName("SBR_test_selector")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.SBR_test_selector.addItem("")
        self.gridLayout_12.addWidget(self.SBR_test_selector, 5, 0, 1, 2)
        self.sbr_test_sel_lbl = QtWidgets.QLabel(self.groupBox_7)

        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sbr_test_sel_lbl.setFont(font)
        self.sbr_test_sel_lbl.setObjectName("sbr_test_sel_lbl")
        self.gridLayout_12.addWidget(self.sbr_test_sel_lbl, 3, 0, 1, 1)
        self.SB_select_lbl = QtWidgets.QLabel(self.groupBox_7)

        font.setPointSize(14)
        self.SB_select_lbl.setFont(font)
        self.SB_select_lbl.setObjectName("SB_select_lbl")
        self.gridLayout_12.addWidget(self.SB_select_lbl, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_22.setTitle("")
        self.groupBox_22.setObjectName("groupBox_22")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_22)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.accepted_SBR_title = QtWidgets.QLabel(self.groupBox_22)

        font.setPointSize(16)
        self.accepted_SBR_title.setFont(font)
        self.accepted_SBR_title.setObjectName("accepted_SBR_title")
        self.verticalLayout_2.addWidget(self.accepted_SBR_title)
        self.acc_SBR_brs = QtWidgets.QTextBrowser(self.groupBox_22)

        font.setPointSize(14)
        self.acc_SBR_brs.setFont(font)
        self.acc_SBR_brs.setObjectName("acc_SBR_brs")
        self.verticalLayout_2.addWidget(self.acc_SBR_brs)
        self.horizontalLayout_3.addWidget(self.groupBox_22)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.UDS_TEST_LBL = QtWidgets.QLabel(self.groupBox_12)

        font.setPointSize(14)
        self.UDS_TEST_LBL.setFont(font)
        self.UDS_TEST_LBL.setObjectName("UDS_TEST_LBL")
        self.gridLayout_18.addWidget(self.UDS_TEST_LBL, 3, 0, 1, 1)
        self.UDS_RUN_BTN = QtWidgets.QPushButton(self.groupBox_12)
        self.UDS_RUN_BTN.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.UDS_RUN_BTN.setFont(font)
        self.UDS_RUN_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.UDS_RUN_BTN.setObjectName("UDS_RUN_BTN")
        self.gridLayout_18.addWidget(self.UDS_RUN_BTN, 0, 0, 1, 1)
        self.STOP_BTN_6 = QtWidgets.QPushButton(self.groupBox_12)
        self.STOP_BTN_6.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.STOP_BTN_6.setFont(font)
        self.STOP_BTN_6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.STOP_BTN_6.setObjectName("STOP_BTN_6")
        self.gridLayout_18.addWidget(self.STOP_BTN_6, 1, 0, 1, 1)
        self.UDS_TEST_SELECTOR = QtWidgets.QComboBox(self.groupBox_12)

        font.setPointSize(11)
        self.UDS_TEST_SELECTOR.setFont(font)
        self.UDS_TEST_SELECTOR.setObjectName("UDS_TEST_SELECTOR")
        self.UDS_TEST_SELECTOR.addItem("Проверка ECU reset 0x11")
        self.UDS_TEST_SELECTOR.addItem("Проверка InputOutputControlByIdentifier 0x2F")
        self.UDS_TEST_SELECTOR.addItem("Проверка Tester Present 0x3E")
        self.UDS_TEST_SELECTOR.addItem("Проверка CommunicationControl 0x28 disable tx")
        self.UDS_TEST_SELECTOR.addItem("Проверка CommunicationControl 0x28 disable tx,rx")
        self.UDS_TEST_SELECTOR.addItem("Проверка ClearDiagnosticInformation 0x14")
        self.UDS_TEST_SELECTOR.addItem("Проверка ReadDiagnosticInformation 0x19 - 0x0A ReportSupportedDTC")
        self.UDS_TEST_SELECTOR.addItem("Проверка ControlDTCSetting 0x85")
        self.UDS_TEST_SELECTOR.addItem("Проверка SecurityAccess 0x27")
        self.UDS_TEST_SELECTOR.addItem("Проверка записи DID ECU Operating States(Working mode)")
        self.UDS_TEST_SELECTOR.addItem("Проверка записи DID ECU Operating States(Plant mode)")
        self.UDS_TEST_SELECTOR.addItem("Проверка записи DID ACU configuration")
        self.UDS_TEST_SELECTOR.addItem("Проверка чтения DID")

        self.gridLayout_18.addWidget(self.UDS_TEST_SELECTOR, 4, 0, 1, 1)
        self.UDS_LED_SELECTOR = QtWidgets.QComboBox(self.groupBox_12)

        font.setPointSize(11)
        self.UDS_LED_SELECTOR.setFont(font)
        self.UDS_LED_SELECTOR.setObjectName("UDS_LED_SELECTOR")
        self.gridLayout_18.addWidget(self.UDS_LED_SELECTOR, 9, 0, 1, 1)
        self.UDS_NRC_SELECTOR=QtWidgets.QComboBox(self.groupBox_12)
        self.UDS_NRC_SELECTOR.setFont(font)
        self.UDS_NRC_SELECTOR.addItem("No NRC")
        self.UDS_NRC_SELECTOR.addItem("0x12-Subfunction not supported")
        self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
        #self.UDS_NRC_SELECTOR.addItem("NRC2")
        self.gridLayout_18.addWidget(self.UDS_NRC_SELECTOR, 6, 0, 1, 1)
        self.UDS_NRC_LBL=QtWidgets.QLabel(self.groupBox_12)
        font=QtGui.QFont()
        font.setPointSize(14)
        self.UDS_NRC_LBL.setFont(font)
        self.UDS_NRC_LBL.setText("NRC")
        self.gridLayout_18.addWidget(self.UDS_NRC_LBL, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_12)

        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_18.addWidget(self.label_4, 5, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_12, 0, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UDS_MSG_LBL = QtWidgets.QLabel(self.groupBox_11)

        font.setPointSize(16)
        self.UDS_MSG_LBL.setFont(font)
        self.UDS_MSG_LBL.setObjectName("UDS_MSG_LBL")
        self.verticalLayout.addWidget(self.UDS_MSG_LBL)
        self.UDS_MSG_BRS = QtWidgets.QTextBrowser(self.groupBox_11)

        font.setPointSize(14)
        self.UDS_MSG_BRS.setFont(font)
        self.UDS_MSG_BRS.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.UDS_MSG_BRS.setObjectName("UDS_MSG_BRS")
        self.verticalLayout.addWidget(self.UDS_MSG_BRS)
        self.gridLayout_20.addWidget(self.groupBox_11, 0, 1, 2, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_19.setTitle("")
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.EXP_UDS_BRS = QtWidgets.QTextBrowser(self.groupBox_19)

        font.setPointSize(14)
        self.EXP_UDS_BRS.setFont(font)
        self.EXP_UDS_BRS.setObjectName("EXP_UDS_BRS")
        self.gridLayout_19.addWidget(self.EXP_UDS_BRS, 1, 0, 1, 1)
        self.EXP_UDS_LBL = QtWidgets.QLabel(self.groupBox_19)

        font.setPointSize(16)
        self.EXP_UDS_LBL.setFont(font)
        self.EXP_UDS_LBL.setObjectName("EXP_UDS_LBL")
        self.gridLayout_19.addWidget(self.EXP_UDS_LBL, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_19, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.SNAPSHOT_TAB = QtWidgets.QWidget()
        self.SNAPSHOT_TAB.setObjectName("SNAPSHOT_TAB")
        self.gridLayout_243 = QtWidgets.QGridLayout(self.SNAPSHOT_TAB)
        self.gridLayout_243.setObjectName("gridLayout_243")
        self.groupBox11 = QtWidgets.QGroupBox(self.SNAPSHOT_TAB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox11.sizePolicy().hasHeightForWidth())
        self.groupBox11.setSizePolicy(sizePolicy)
        self.groupBox11.setMinimumSize(QtCore.QSize(55, 55))

        font.setPointSize(12)
        self.groupBox11.setFont(font)
        self.groupBox11.setObjectName("groupBox")
        self.gridLayout_511 = QtWidgets.QGridLayout(self.groupBox11)
        self.gridLayout_511.setObjectName("gridLayout_511")

        font.setPointSize(16)
        self.snap_brs = QtWidgets.QTextBrowser(self.groupBox11)
        self.snap_brs.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snap_brs.sizePolicy().hasHeightForWidth())
        self.snap_brs.setSizePolicy(sizePolicy)
        self.snap_brs.setObjectName("snap_brs")
        self.gridLayout_511.addWidget(self.snap_brs, 0, 0, 1, 1)
        self.gridLayout_243.addWidget(self.groupBox11, 2, 0, 1, 1)
        self.groupBox_243 = QtWidgets.QGroupBox(self.SNAPSHOT_TAB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_243.sizePolicy().hasHeightForWidth())
        self.groupBox_243.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.groupBox_243.setFont(font)
        self.groupBox_243.setObjectName("groupBox_243")
        self.gridLayout_412 = QtWidgets.QGridLayout(self.groupBox_243)
        self.gridLayout_412.setObjectName("gridLayout_412")
        self.lcdNumber_4 = QtWidgets.QTextBrowser(self.groupBox_243)
        #self.lcdNumber_4.setDigitCount(8)
        self.lcdNumber_4.setObjectName("lcdNumber_4")

        font.setPointSize(52)
        self.lcdNumber_4.setFont(font)
        self.gridLayout_412.addWidget(self.lcdNumber_4, 4, 1, 1, 3)
        self.stat_snap = QtWidgets.QLabel(self.groupBox_243)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stat_snap.sizePolicy().hasHeightForWidth())
        self.stat_snap.setSizePolicy(sizePolicy)

        font.setPointSize(20)
        self.stat_snap.setFont(font)
        self.stat_snap.setObjectName("stat_snap")
        self.gridLayout_412.addWidget(self.stat_snap, 2, 0, 1, 1)
        self.speed_snap = QtWidgets.QLabel(self.groupBox_243)

        font.setPointSize(20)
        self.speed_snap.setFont(font)
        self.speed_snap.setObjectName("speed_snap")
        self.gridLayout_412.addWidget(self.speed_snap, 3, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QTextBrowser(self.groupBox_243)
        self.lcdNumber_3.setObjectName("lcdNumber_3")

        font.setPointSize(52)
        self.lcdNumber_3.setFont(font)
        self.gridLayout_412.addWidget(self.lcdNumber_3, 5, 1, 1, 3)
        self.errctr_snpa = QtWidgets.QLabel(self.groupBox_243)

        font.setPointSize(20)
        self.errctr_snpa.setFont(font)
        self.errctr_snpa.setObjectName("errctr_snpa")
        self.gridLayout_412.addWidget(self.errctr_snpa, 6, 0, 1, 1)
        self.lifetime_snap = QtWidgets.QLabel(self.groupBox_243)

        font.setPointSize(20)
        self.lifetime_snap.setFont(font)
        self.lifetime_snap.setObjectName("lifetime_snap")
        self.gridLayout_412.addWidget(self.lifetime_snap, 4, 0, 1, 1)
        self.probeg_snap = QtWidgets.QLabel(self.groupBox_243)

        font.setPointSize(20)
        self.probeg_snap.setFont(font)
        self.probeg_snap.setObjectName("probeg_snap")
        self.gridLayout_412.addWidget(self.probeg_snap, 5, 0, 1, 1)
        self.status_brs = QtWidgets.QTextBrowser(self.groupBox_243)
        self.status_brs.setMaximumSize(1000,150)
        self.status_brs.setObjectName("lcdNumber")
        self.status_brs.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        font.setPointSize(52)
        self.status_brs.setFont(font)
        self.gridLayout_412.addWidget(self.status_brs, 2, 1, 1, 3)
        self.lcdNumber_2 = QtWidgets.QTextBrowser(self.groupBox_243)
#        self.lcdNumber_2.setDigitCount(8)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setFont(font)
        self.gridLayout_412.addWidget(self.lcdNumber_2, 3, 1, 1, 3)
        self.lcdNumber_5 = QtWidgets.QTextBrowser(self.groupBox_243)
#        self.lcdNumber_5.setDigitCount(8)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_5.setFont(font)
        self.gridLayout_412.addWidget(self.lcdNumber_5, 6, 1, 1, 3)
        self.gridLayout_243.addWidget(self.groupBox_243, 2, 1, 1, 1)
        self.SNAP_GROUP = QtWidgets.QGroupBox(self.SNAPSHOT_TAB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SNAP_GROUP.sizePolicy().hasHeightForWidth())
        self.SNAP_GROUP.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.SNAP_GROUP.setFont(font)
        self.SNAP_GROUP.setObjectName("SNAP_GROUP")
        self.gridLayout_311 = QtWidgets.QGridLayout(self.SNAP_GROUP)
        self.gridLayout_311.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem1, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem2, 0, 1, 1, 1)
        self.read_snap_btn = QtWidgets.QPushButton(self.SNAP_GROUP)
        self.read_snap_btn.setMinimumSize(QtCore.QSize(0, 60))

        font.setPointSize(12)
        self.read_snap_btn.setFont(font)
        self.read_snap_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.read_snap_btn.setObjectName("read_snap_btn")
        self.gridLayout_311.addWidget(self.read_snap_btn, 13, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem4, 8, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_311.addItem(spacerItem8, 5, 1, 1, 1)
        self.snap_sel_1_lbl = QtWidgets.QLabel(self.SNAP_GROUP)
        self.snap_sel_1_lbl.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snap_sel_1_lbl.sizePolicy().hasHeightForWidth())
        self.snap_sel_1_lbl.setSizePolicy(sizePolicy)
        self.snap_sel_1_lbl.setMinimumSize(QtCore.QSize(0, 10))
        self.snap_sel_1_lbl.setObjectName("snap_sel_1_lbl")
        self.gridLayout_311.addWidget(self.snap_sel_1_lbl, 1, 0, 1, 1)
        self.snap_sel_1 = QtWidgets.QComboBox(self.SNAP_GROUP)
        self.snap_sel_1.setFont(font)
        self.snap_sel_1.setMinimumSize(QtCore.QSize(0, 35))
        self.snap_sel_1.setObjectName("snap_sel_1")
        self.snap_sel_1.addItem("General errors")
        self.snap_sel_1.addItem("ACU crash")
        self.snap_sel_1.addItem("ECU supply voltage")
        self.snap_sel_1.addItem("Front Airbag Driver")
        self.snap_sel_1.addItem("Front Airbag Passenger")
        self.snap_sel_1.addItem("Pretensioner Driver")
        self.snap_sel_1.addItem("Pretensioner Passenger")
        self.snap_sel_1.addItem("Side Airbag Driver")
        self.snap_sel_1.addItem("Side Airbag Passenger")
        self.snap_sel_1.addItem("Curtain Airbag Driver")
        self.snap_sel_1.addItem("Curtain Airbag Passenger")
        self.snap_sel_1.addItem("Passenger Airbag Cutoff switch")
        self.snap_sel_1.addItem("Passenger Presence sensor")
        self.snap_sel_1.addItem("Lost CAN communication")







        self.gridLayout_311.addWidget(self.snap_sel_1, 2, 0, 1, 1)
        self.snap_sel_2_lbl = QtWidgets.QLabel(self.SNAP_GROUP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snap_sel_2_lbl.sizePolicy().hasHeightForWidth())
        self.snap_sel_2_lbl.setSizePolicy(sizePolicy)
        self.snap_sel_2_lbl.setObjectName("snap_sel_2_lbl")
        self.snap_sel_2_lbl.setFont(font)
        self.gridLayout_311.addWidget(self.snap_sel_2_lbl, 4, 0, 1, 1)
        self.snap_sel_2 = QtWidgets.QComboBox(self.SNAP_GROUP)
        self.snap_sel_2.setMinimumSize(QtCore.QSize(0, 35))
        self.snap_sel_2.setObjectName("snap_sel_2")
        self.snap_sel_2.setFont(font)
        self.snap_sel_2.addItem("Vehicle Option Fault")
        self.snap_sel_2.addItem("VIN absence")
        self.snap_sel_2.addItem("Internal Module Fault")
        self.snap_sel_2.addItem("WatchDog Continues Fault")
        self.gridLayout_311.addWidget(self.snap_sel_2, 5, 0, 1, 1)
        self.gridLayout_243.addWidget(self.SNAP_GROUP, 0, 0, 1, 2)
        self.tabWidget.addTab(self.SNAPSHOT_TAB, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.DIAG_VIN1_BTN = QtWidgets.QPushButton(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DIAG_VIN1_BTN.sizePolicy().hasHeightForWidth())
        self.DIAG_VIN1_BTN.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.DIAG_VIN1_BTN.setFont(font)
        self.DIAG_VIN1_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_VIN1_BTN.setObjectName("DIAG_VIN1_BTN")
        self.gridLayout_16.addWidget(self.DIAG_VIN1_BTN, 0, 0, 1, 1)
        self.DIAG_VIN0_BTN = QtWidgets.QPushButton(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DIAG_VIN0_BTN.sizePolicy().hasHeightForWidth())
        self.DIAG_VIN0_BTN.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.DIAG_VIN0_BTN.setFont(font)
        self.DIAG_VIN0_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_VIN0_BTN.setObjectName("DIAG_VIN0_BTN")
        self.gridLayout_16.addWidget(self.DIAG_VIN0_BTN, 1, 0, 1, 1)



        font.setPointSize(12)

        self.DIAG_RESET_BTN = QtWidgets.QPushButton(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DIAG_RESET_BTN.sizePolicy().hasHeightForWidth())
        self.DIAG_RESET_BTN.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.DIAG_RESET_BTN.setFont(font)
        self.DIAG_RESET_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_RESET_BTN.setObjectName("DIAG_RESET_BTN")
        self.gridLayout_16.addWidget(self.DIAG_RESET_BTN, 1, 1, 1, 1)
        self.CHECK_CRASH_DETECTION_BTN = QtWidgets.QPushButton(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHECK_CRASH_DETECTION_BTN.sizePolicy().hasHeightForWidth())
        self.CHECK_CRASH_DETECTION_BTN.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.CHECK_CRASH_DETECTION_BTN.setFont(font)
        self.CHECK_CRASH_DETECTION_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.CHECK_CRASH_DETECTION_BTN.setObjectName("CHECK_CRASH_DETECTION_BTN")
        self.gridLayout_16.addWidget(self.CHECK_CRASH_DETECTION_BTN, 0, 1, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_9, 0, 2, 2, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.DIAG_READ_0x09_BTN = QtWidgets.QPushButton(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DIAG_READ_0x09_BTN.sizePolicy().hasHeightForWidth())
        self.DIAG_READ_0x09_BTN.setSizePolicy(sizePolicy)
        self.DIAG_READ_0x09_BTN.setMaximumSize(QtCore.QSize(1000, 50))

        font.setPointSize(10)
        self.DIAG_READ_0x09_BTN.setFont(font)
        self.DIAG_READ_0x09_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_READ_0x09_BTN.setObjectName("DIAG_READ_0x09_BTN")
        self.gridLayout_15.addWidget(self.DIAG_READ_0x09_BTN, 0, 0, 1, 1)
        self.DIAG_READ_0x08_BTN = QtWidgets.QPushButton(self.groupBox_8)
        self.DIAG_READ_0x08_BTN.setMaximumSize(QtCore.QSize(16777215, 60))

        font.setPointSize(10)
        self.DIAG_READ_0x08_BTN.setFont(font)
        self.DIAG_READ_0x08_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_READ_0x08_BTN.setObjectName("DIAG_READ_0x08_BTN")
        self.gridLayout_15.addWidget(self.DIAG_READ_0x08_BTN, 0, 1, 1, 1)
        self.DIAG_CLEAR_DTC_BTN = QtWidgets.QPushButton(self.groupBox_8)
        self.DIAG_CLEAR_DTC_BTN.setMaximumSize(QtCore.QSize(16777215, 55))

        font.setPointSize(10)
        self.DIAG_CLEAR_DTC_BTN.setFont(font)
        self.DIAG_CLEAR_DTC_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_CLEAR_DTC_BTN.setObjectName("DIAG_CLEAR_DTC_BTN")
        self.gridLayout_15.addWidget(self.DIAG_CLEAR_DTC_BTN, 0, 2, 1, 1)
        self.DIAG_ERRORS_LBL = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DIAG_ERRORS_LBL.sizePolicy().hasHeightForWidth())
        self.DIAG_ERRORS_LBL.setSizePolicy(sizePolicy)

        font.setPointSize(16)
        self.DIAG_ERRORS_LBL.setFont(font)
        self.DIAG_ERRORS_LBL.setObjectName("DIAG_ERRORS_LBL")
        self.gridLayout_15.addWidget(self.DIAG_ERRORS_LBL, 1, 0, 1, 2)
        self.DIAG_ERRORS_BRS = QtWidgets.QTextBrowser(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DIAG_ERRORS_BRS.sizePolicy().hasHeightForWidth())
        self.DIAG_ERRORS_BRS.setSizePolicy(sizePolicy)

        font.setPointSize(14)
        self.DIAG_ERRORS_BRS.setFont(font)
        self.DIAG_ERRORS_BRS.setObjectName("DIAG_ERRORS_BRS")
        self.gridLayout_15.addWidget(self.DIAG_ERRORS_BRS, 2, 0, 1, 3)
        self.gridLayout_21.addWidget(self.groupBox_8, 2, 2, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy)
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_2 = QtWidgets.QLabel(self.groupBox_14)

        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_17.addWidget(self.label_2, 0, 0, 1, 1)
        self.DIAG_ACCEPTED_BRS = QtWidgets.QTextBrowser(self.groupBox_14)

        font.setPointSize(14)
        self.DIAG_ACCEPTED_BRS.setFont(font)
        self.DIAG_ACCEPTED_BRS.setObjectName("DIAG_ACCEPTED_BRS")
        self.gridLayout_17.addWidget(self.DIAG_ACCEPTED_BRS, 1, 0, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_14, 2, 0, 1, 2)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 500))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.DIAG_SPEED_SELECTOR = QtWidgets.QSlider(self.groupBox_10)
        self.DIAG_SPEED_SELECTOR.setOrientation(1)  # Установка ориентации (1 - вертикально, 0 - горизонтально)
        self.DIAG_SPEED_SELECTOR.setRange(0, 25500)  # Установка диапазона от 0 до 100
        self.DIAG_SPEED_SELECTOR.setValue(0)  # Установка начального значения
        self.DIAG_SPEED_SELECTOR.setTickInterval(1)

        font.setPointSize(14)
        self.DIAG_SPEED_SELECTOR.setFont(font)
        self.DIAG_SPEED_SELECTOR.setObjectName("DIAG_SPEED_SELECTOR")
        self.gridLayout_14.addWidget(self.DIAG_SPEED_SELECTOR, 11, 0, 1, 3)

        self.DIAG_MILEAGE_SELECTOR = QtWidgets.QSlider(self.groupBox_10)
        self.DIAG_MILEAGE_SELECTOR.setOrientation(1)  # Установка ориентации (1 - вертикально, 0 - горизонтально)
        self.DIAG_MILEAGE_SELECTOR.setRange(0, 50000000)  # Установка диапазона от 0 до 100
        self.DIAG_MILEAGE_SELECTOR.setValue(0)  # Установка начального значения
        self.DIAG_MILEAGE_SELECTOR.setTickInterval(1)
        self.DIAG_MILEAGE_SELECTOR.setFont(font)
        self.DIAG_MILEAGE_SELECTOR.setObjectName("DIAG_MILEAGE_SELECTOR")
        self.gridLayout_14.addWidget(self.DIAG_MILEAGE_SELECTOR, 13, 0, 1, 3)

        self.DIAG_MILEAGE_SELECTOR_2 = QtWidgets.QLabel(self.groupBox_10)
        self.DIAG_MILEAGE_SELECTOR_2.setFont(font)
        self.DIAG_MILEAGE_SELECTOR_2.setObjectName("DIAG_SPEED_SELECTOR_2")
        self.gridLayout_14.addWidget(self.DIAG_MILEAGE_SELECTOR_2, 12, 0, 1, 1)

        self.DIAG_MILEAGE_SELECTOR_2.setText('Отправляемый пробег:')

        self.DIAG_DIAGENABLE_SELECTOR_2 = QtWidgets.QLabel(self.groupBox_10)

        font.setPointSize(13)
        self.DIAG_DIAGENABLE_SELECTOR_2.setFont(font)
        self.DIAG_DIAGENABLE_SELECTOR_2.setObjectName("DIAG_DIAGENABLE_SELECTOR_2")
        self.gridLayout_14.addWidget(self.DIAG_DIAGENABLE_SELECTOR_2, 15, 0, 1, 1)
        self.DIAG_UPD_CAN_MSG_BTN = QtWidgets.QPushButton(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.DIAG_UPD_CAN_MSG_BTN.sizePolicy().hasHeightForWidth())
        self.DIAG_UPD_CAN_MSG_BTN.setSizePolicy(sizePolicy)
        self.DIAG_UPD_CAN_MSG_BTN.setMaximumSize(QtCore.QSize(474, 70))

        font.setPointSize(10)
        self.DIAG_UPD_CAN_MSG_BTN.setFont(font)
        self.DIAG_UPD_CAN_MSG_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_UPD_CAN_MSG_BTN.setObjectName("DIAG_UPD_CAN_MSG_BTN")

        self.DIAG_STOP_CAN_MSG_BTN = QtWidgets.QPushButton(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.DIAG_STOP_CAN_MSG_BTN.sizePolicy().hasHeightForWidth())
        self.DIAG_STOP_CAN_MSG_BTN.setSizePolicy(sizePolicy)
        self.DIAG_STOP_CAN_MSG_BTN.setMaximumSize(QtCore.QSize(474, 70))

        font.setPointSize(10)
        self.DIAG_STOP_CAN_MSG_BTN.setFont(font)
        self.DIAG_STOP_CAN_MSG_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DIAG_STOP_CAN_MSG_BTN.setObjectName("DIAG_UPD_CAN_MSG_BTN")
        self.gridLayout_14.addWidget(self.DIAG_STOP_CAN_MSG_BTN, 5, 0, 1, 1)

        self.gridLayout_14.addWidget(self.DIAG_UPD_CAN_MSG_BTN, 4, 0, 1, 1)
        self.DIAG_CAN_MSG_LBL = QtWidgets.QLabel(self.groupBox_10)

        font.setPointSize(14)
        self.DIAG_CAN_MSG_LBL.setFont(font)
        self.DIAG_CAN_MSG_LBL.setObjectName("DIAG_CAN_MSG_LBL")
        self.gridLayout_14.addWidget(self.DIAG_CAN_MSG_LBL, 3, 0, 1, 1)
        self.DIAG_DIAGENABLE_SELECTOR = QtWidgets.QComboBox(self.groupBox_10)

        font.setPointSize(13)
        self.DIAG_DIAGENABLE_SELECTOR.setFont(font)
        self.DIAG_DIAGENABLE_SELECTOR.setObjectName("DIAG_DIAGENABLE_SELECTOR")
        self.DIAG_DIAGENABLE_SELECTOR.addItem("")
        self.DIAG_DIAGENABLE_SELECTOR.addItem("")
        self.DIAG_DIAGENABLE_SELECTOR.addItem("")
        self.DIAG_DIAGENABLE_SELECTOR.addItem("")
        self.gridLayout_14.addWidget(self.DIAG_DIAGENABLE_SELECTOR, 17, 0, 1, 3)
        self.DIAG_SPEED_SELECTOR_2 = QtWidgets.QLabel(self.groupBox_10)

        font.setPointSize(14)
        self.DIAG_SPEED_SELECTOR_2.setFont(font)
        self.DIAG_SPEED_SELECTOR_2.setObjectName("DIAG_SPEED_SELECTOR_2")
        self.gridLayout_14.addWidget(self.DIAG_SPEED_SELECTOR_2, 10, 0, 1, 1)
        '''self.DIAG_RPM_SELECTOR = QtWidgets.QSlider(self.groupBox_10)
        self.DIAG_RPM_SELECTOR.setOrientation(1)  # Установка ориентации (1 - вертикально, 0 - горизонтально)
        self.DIAG_RPM_SELECTOR.setRange(0, 25500)  # Установка диапазона от 0 до 100
        self.DIAG_RPM_SELECTOR.setValue(0)  # Установка начального значения
        self.DIAG_RPM_SELECTOR.setTickInterval(1)
        
        font.setPointSize(11)
        self.DIAG_RPM_SELECTOR.setFont(font)
        self.DIAG_RPM_SELECTOR.setObjectName("DIAG_SPEED_SELECTOR")
        #self.gridLayout_14.addWidget(self.DIAG_RPM_SELECTOR, 20, 0, 1, 3)'''
        self.gridLayout_21.addWidget(self.groupBox_10, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.EDR_tab = QtWidgets.QWidget()
        self.EDR_tab.setObjectName("EDR_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.EDR_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_11223344 = QtWidgets.QGroupBox(self.EDR_tab)
        self.groupBox_11223344.setTitle("")
        self.groupBox_11223344.setObjectName("groupBox_11223344")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_11223344)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox789 = QtWidgets.QGroupBox(self.groupBox_11223344)
        self.groupBox789.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox789.setTitle("")
        self.groupBox789.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox789)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.EDR_STOP_BTN = QtWidgets.QPushButton(self.groupBox789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EDR_STOP_BTN.sizePolicy().hasHeightForWidth())
        self.EDR_STOP_BTN.setSizePolicy(sizePolicy)
        self.EDR_STOP_BTN.setMaximumSize(QtCore.QSize(16777215, 100))

        font.setPointSize(12)
        self.EDR_STOP_BTN.setFont(font)
        self.EDR_STOP_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.EDR_STOP_BTN.setObjectName("EDR_STOP_BTN")
        self.gridLayout_4.addWidget(self.EDR_STOP_BTN, 0, 3, 1, 1)
        self.EDR1_BTN = QtWidgets.QPushButton(self.groupBox789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EDR1_BTN.sizePolicy().hasHeightForWidth())
        self.EDR1_BTN.setSizePolicy(sizePolicy)
        self.EDR1_BTN.setMinimumSize(QtCore.QSize(0, 50))
        self.EDR1_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.EDR1_BTN.setMaximumSize(QtCore.QSize(16777215, 50))

        font.setPointSize(12)
        self.EDR1_BTN.setFont(font)
        self.EDR1_BTN.setObjectName("EDR1_BTN")
        self.gridLayout_4.addWidget(self.EDR1_BTN, 0, 2, 1, 1)
        self.EDR3_BTN = QtWidgets.QPushButton(self.groupBox789)
        self.EDR3_BTN.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.EDR3_BTN.setFont(font)
        self.EDR3_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.EDR3_BTN.setObjectName("EDR3_BTN")
        self.gridLayout_4.addWidget(self.EDR3_BTN, 2, 2, 1, 1)
        self.EDR2_BTN = QtWidgets.QPushButton(self.groupBox789)
        self.EDR2_BTN.setMinimumSize(QtCore.QSize(0, 50))
        self.EDR2_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        font.setPointSize(12)
        self.EDR2_BTN.setFont(font)
        self.EDR2_BTN.setObjectName("EDR2_BTN")
        self.gridLayout_4.addWidget(self.EDR2_BTN, 1, 2, 1, 1)
        self.READ_NUM_BTN = QtWidgets.QPushButton(self.groupBox789)
        self.READ_NUM_BTN.setMinimumSize(QtCore.QSize(0, 50))

        font.setPointSize(12)
        self.READ_NUM_BTN.setFont(font)
        self.READ_NUM_BTN.setObjectName("READ_NUM_BTN")
        self.READ_NUM_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.gridLayout_4.addWidget(self.READ_NUM_BTN, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox789, 0, 0, 1, 3)
        self.groupBox_17 = QtWidgets.QGroupBox(self.groupBox_11223344)
        self.groupBox_17.setMaximumSize(QtCore.QSize(16777215, 500))

        font.setPointSize(12)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setObjectName("groupBox_17")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Precrash_data_table = QtWidgets.QTableWidget(self.groupBox_17)
        self.Precrash_data_table.setMaximumSize(QtCore.QSize(6666, 6666))

        font.setPointSize(10)
        self.Precrash_data_table.setFont(font)
        self.Precrash_data_table.setShowGrid(True)
        self.Precrash_data_table.setGridStyle(QtCore.Qt.SolidLine)
        self.Precrash_data_table.setWordWrap(True)
        self.Precrash_data_table.setCornerButtonEnabled(True)
        self.Precrash_data_table.setObjectName("Precrash_data_table")
        self.Precrash_data_table.setColumnCount(12)
        self.Precrash_data_table.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Precrash_data_table.setHorizontalHeaderItem(11, item)
        self.horizontalLayout_2.addWidget(self.Precrash_data_table)
        self.gridLayout_3.addWidget(self.groupBox_17, 1, 1, 1, 2)
        self.groupBox_16 = QtWidgets.QGroupBox(self.groupBox_11223344)
        self.groupBox_16.setMinimumSize(QtCore.QSize(330, 0))
        self.groupBox_16.setMaximumSize(QtCore.QSize(66666, 16777215))

        font.setPointSize(12)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Crash_data_table = QtWidgets.QTableWidget(self.groupBox_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Crash_data_table.sizePolicy().hasHeightForWidth())
        self.Crash_data_table.setSizePolicy(sizePolicy)
        self.Crash_data_table.setMaximumSize(QtCore.QSize(6666, 66666))
        self.Crash_data_table.setStyleSheet("""
                    QTableWidget {
                        background-color: #f0f0f0; /* Цвет фона таблицы */
                        gridline-color: #aaaaaa; /* Цвет линий сетки */
                    }
                    QHeaderView::section {
                        background-color: #d0d0d0; /* Цвет фона заголовка столбца */
                        border: 1px solid #aaaaaa; /* Цвет границы заголовка */
                        padding: 4px; /* Отступы в заголовке */
                    }
                    QTableWidget::item {
                        padding: 10px; /* Отступы для элементов таблицы */
                    }
                    QTableWidget::item:selected {
                        background-color: #0078d7; /* Цвет выделенного элемента */
                        color: white; /* Цвет текста выделенного элемента */
                    }
                """)
        self.Precrash_data_table.setStyleSheet("""
                            QTableWidget {
                                background-color: #f0f0f0; /* Цвет фона таблицы */
                                gridline-color: #aaaaaa; /* Цвет линий сетки */
                            }
                            QHeaderView::section {
                                background-color: #d0d0d0; /* Цвет фона заголовка столбца */
                                border: 1px solid #aaaaaa; /* Цвет границы заголовка */
                                padding: 4px; /* Отступы в заголовке */
                            }
                            QTableWidget::item {
                                padding: 10px; /* Отступы для элементов таблицы */
                            }
                            QTableWidget::item:selected {
                                background-color: #0078d7; /* Цвет выделенного элемента */
                                color: white; /* Цвет текста выделенного элемента */
                            }
                        """)

        font.setPointSize(10)
        self.Crash_data_table.setFont(font)
        self.Crash_data_table.setObjectName("Crash_data_table")
        self.Crash_data_table.setColumnCount(3)
        self.Crash_data_table.setRowCount(25)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Crash_data_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.Crash_data_table)
        self.gridLayout_3.addWidget(self.groupBox_16, 1, 0, 3, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_11223344)
        self.groupBox_18.setMinimumSize(QtCore.QSize(0, 1))
        self.groupBox_18.setMaximumSize(QtCore.QSize(16777215, 600))

        font.setPointSize(12)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EDR_OTHER_DATA_BRS = QtWidgets.QListWidget(self.groupBox_18)
        self.EDR_OTHER_DATA_BRS.setMaximumSize(QtCore.QSize(16777215, 6666))
        self.EDR_OTHER_DATA_BRS.setObjectName("EDR_OTHER_DATA_BRS")
        self.EDR_OTHER_DATA_BRS.setFont(font)
        self.gridLayout_2.addWidget(self.EDR_OTHER_DATA_BRS, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_18, 2, 2, 2, 1)
        self.gridLayout_5.addWidget(self.groupBox_11223344, 0, 0, 1, 1)
        self.Crash_data_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.Crash_data_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.Precrash_data_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.Precrash_data_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabWidget.addTab(self.EDR_tab, "")
        self.params_tab = QtWidgets.QWidget()
        self.params_tab.setObjectName("params_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.params_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxA = QtWidgets.QGroupBox(self.params_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxA.sizePolicy().hasHeightForWidth())
        self.groupBoxA.setSizePolicy(sizePolicy)
        self.groupBoxA.setMinimumSize(QtCore.QSize(500, 0))

        font.setPointSize(13)
        self.groupBoxA.setFont(font)
        self.groupBoxA.setObjectName("groupBoxA")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxA)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.defined_params_selector = QtWidgets.QComboBox(self.groupBoxA)
        self.defined_params_selector.setObjectName("defined_params_selector")
        self.gridLayout_3.addWidget(self.defined_params_selector, 1, 0, 1, 1)
        self.defined_params_lbl = QtWidgets.QLabel(self.groupBoxA)
        self.defined_params_lbl.setObjectName("defined_params_lbl")
        self.gridLayout_3.addWidget(self.defined_params_lbl, 0, 0, 1, 1)
        self.Sresimpact_side_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.defined_params_selector.setFont(font)
        self.defined_params_lbl.setFont(font)
        self.Sresimpact_side_input.setFont(font)
        self.Sresimpact_side_input.setMinimumSize(QtCore.QSize(0, 26))
        self.Sresimpact_side_input.setMaximum(65535)
        self.Sresimpact_side_input.setObjectName("Sresimpact_side_input")
        self.gridLayout_3.addWidget(self.Sresimpact_side_input, 16, 1, 1, 1)
        self.LimitSxSyfront_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.LimitSxSyfront_input.setFont(font)
        self.LimitSxSyfront_input.setMinimumSize(QtCore.QSize(0, 26))
        self.LimitSxSyfront_input.setMaximum(65535)
        self.LimitSxSyfront_input.setObjectName("LimitSxSyfront_input")
        self.gridLayout_3.addWidget(self.LimitSxSyfront_input, 5, 1, 1, 1)
        self.Tcalc_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.Tcalc_input.setFont(font)
        self.Tcalc_input.setMaximum(255)
        self.Tcalc_input.setMinimumSize(QtCore.QSize(0, 26))
        self.Tcalc_input.setObjectName("Tcalc_input")
        self.gridLayout_3.addWidget(self.Tcalc_input, 11, 1, 1, 1)
        self.Sresimpactfront_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.Sresimpactfront_input.setFont(font)
        self.Sresimpactfront_input.setMinimumSize(QtCore.QSize(0, 26))
        self.Sresimpactfront_input.setMaximum(65535)
        self.Sresimpactfront_input.setObjectName("Sresimpactfront_input")
        self.gridLayout_3.addWidget(self.Sresimpactfront_input, 15, 1, 1, 1)
        self.LimitAresfront_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.LimitAresfront_input.setFont(font)
        self.LimitAresfront_input.setMinimumSize(QtCore.QSize(0, 26))
        self.LimitAresfront_input.setMaximum(65535)
        self.LimitAresfront_input.setObjectName("LimitAresfront_input")
        self.gridLayout_3.addWidget(self.LimitAresfront_input, 3, 1, 1, 1)
        self.LimitAresfront_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.LimitAresfront_lbl.setFont(font)
        self.LimitAresfront_lbl.setObjectName("LimitAresfront_lbl")
        self.gridLayout_3.addWidget(self.LimitAresfront_lbl, 3, 0, 1, 1)
        self.Tcalc_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.Tcalc_lbl.setFont(font)
        self.Tcalc_lbl.setObjectName("Tcalc_lbl")
        self.gridLayout_3.addWidget(self.Tcalc_lbl, 11, 0, 1, 1)
        self.LimitSresfront_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.LimitSresfront_input.setFont(font)
        self.LimitSresfront_input.setMaximum(65535)
        self.LimitSresfront_input.setMinimumSize(QtCore.QSize(0, 26))
        self.LimitSresfront_input.setObjectName("LimitSresfront_input")
        self.gridLayout_3.addWidget(self.LimitSresfront_input, 8, 1, 1, 1)
        self.Sresimpactfront_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.Sresimpactfront_lbl.setFont(font)
        self.Sresimpactfront_lbl.setObjectName("Sresimpactfront_lbl")
        self.gridLayout_3.addWidget(self.Sresimpactfront_lbl, 15, 0, 1, 1)
        self.Sresimpactside_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.Sresimpactside_lbl.setFont(font)
        self.Sresimpactside_lbl.setObjectName("Sresimpactside_lbl")
        self.gridLayout_3.addWidget(self.Sresimpactside_lbl, 16, 0, 1, 1)
        self.LimitSxSyfront_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.LimitSxSyfront_lbl.setFont(font)
        self.LimitSxSyfront_lbl.setObjectName("LimitSxSyfront_lbl")
        self.gridLayout_3.addWidget(self.LimitSxSyfront_lbl, 5, 0, 1, 1)
        self.LimitSxSyside_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.LimitSxSyside_lbl.setFont(font)
        self.LimitSxSyside_lbl.setObjectName("LimitSxSyside_lbl")
        self.gridLayout_3.addWidget(self.LimitSxSyside_lbl, 6, 0, 1, 1)
        self.Time_to_stop_calc_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.Time_to_stop_calc_lbl.setFont(font)
        self.Time_to_stop_calc_lbl.setObjectName("Time_to_stop_calc_lbl")
        self.gridLayout_3.addWidget(self.Time_to_stop_calc_lbl, 14, 0, 1, 1)
        self.LimitSresside_input = QtWidgets.QSpinBox(self.groupBoxA)
        self.LimitSresside_input.setMinimumSize(QtCore.QSize(0, 26))

        font.setPointSize(12)
        self.LimitSresside_input.setFont(font)
        self.LimitSresside_input.setMaximum(65535)
        self.LimitSresside_input.setObjectName("LimitSresside_input")
        self.gridLayout_3.addWidget(self.LimitSresside_input, 10, 1, 1, 1)
        self.LimitSxSyside_input = QtWidgets.QSpinBox(self.groupBoxA)
        self.LimitSxSyside_input.setMinimumSize(QtCore.QSize(0, 26))

        font.setPointSize(12)
        self.LimitSxSyside_input.setFont(font)
        self.LimitSxSyside_input.setMaximum(65535)
        self.LimitSxSyside_input.setObjectName("LimitSxSyside_input")
        self.gridLayout_3.addWidget(self.LimitSxSyside_input, 6, 1, 1, 1)
        self.LimitAresside_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.LimitAresside_input.setFont(font)
        self.LimitAresside_input.setMaximum(65535)
        self.LimitAresside_input.setMinimumSize(QtCore.QSize(0, 26))
        self.LimitAresside_input.setObjectName("LimitAresside_input")
        self.gridLayout_3.addWidget(self.LimitAresside_input, 4, 1, 1, 1)
        self.deltaAres_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.deltaAres_lbl.setFont(font)
        self.deltaAres_lbl.setObjectName("deltaAres_lbl")
        self.gridLayout_3.addWidget(self.deltaAres_lbl, 13, 0, 1, 1)
        self.Timetostopcalc_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.Timetostopcalc_input.setFont(font)
        self.Timetostopcalc_input.setMaximum(255)
        self.Timetostopcalc_input.setMinimumSize(QtCore.QSize(0, 26))
        self.Timetostopcalc_input.setObjectName("Timetostopcalc_input")
        self.gridLayout_3.addWidget(self.Timetostopcalc_input, 14, 1, 1, 1)
        self.LimitSresside_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.LimitSresside_lbl.setFont(font)
        self.LimitSresside_lbl.setObjectName("LimitSresside_lbl")
        self.gridLayout_3.addWidget(self.LimitSresside_lbl, 10, 0, 1, 1)
        self.deltaAres_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.deltaAres_input.setFont(font)
        self.deltaAres_input.setMinimumSize(QtCore.QSize(0, 26))
        self.deltaAres_input.setMaximum(255)
        self.deltaAres_input.setObjectName("deltaAres_input")
        self.gridLayout_3.addWidget(self.deltaAres_input, 13, 1, 1, 1)
        self.LimitAresside_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.LimitAresside_lbl.setFont(font)
        self.LimitAresside_lbl.setObjectName("LimitAresside_lbl")
        self.gridLayout_3.addWidget(self.LimitAresside_lbl, 4, 0, 1, 1)
        self.Tcalc2_lbl = QtWidgets.QLabel(self.groupBoxA)
        self.Tcalc2_lbl.setObjectName("Tcalc2_lbl")
        self.gridLayout_3.addWidget(self.Tcalc2_lbl, 12, 0, 1, 1)
        self.LOGS_LBL = QtWidgets.QLabel(self.groupBoxA)
        self.LOGS_LBL.setObjectName("LOGS_LBL")
        self.gridLayout_3.addWidget(self.LOGS_LBL, 2, 2, 1, 1)
        self.Tcalc2_input = QtWidgets.QSpinBox(self.groupBoxA)

        font.setPointSize(12)
        self.LOGS_LBL.setFont(font)
        self.Tcalc2_input.setFont(font)
        self.Tcalc2_input.setMinimumSize(QtCore.QSize(0, 26))

        font.setPointSize(14)
        self.Tcalc2_lbl.setFont(font)
        self.Tcalc2_input.setObjectName("Tcalc2_input")
        self.gridLayout_3.addWidget(self.Tcalc2_input, 12, 1, 1, 1)
        self.LimitSresfront_lbl = QtWidgets.QLabel(self.groupBoxA)

        font.setPointSize(14)
        self.LimitSresfront_lbl.setFont(font)
        self.LimitSresfront_lbl.setObjectName("LimitSresfront_lbl")
        self.gridLayout_3.addWidget(self.LimitSresfront_lbl, 8, 0, 1, 1)
        self.save_params_btn = QtWidgets.QPushButton(self.groupBoxA)
        self.save_params_btn.setCheckable(False)
        self.save_params_btn.setAutoRepeat(False)
        self.save_params_btn.setObjectName("save_params_btn")

        font.setPointSize(12)
        self.save_params_btn.setFont(font)
        self.gridLayout_3.addWidget(self.save_params_btn, 0, 2, 2, 1)
        self.PARAM_RESULT_BRS_2 = QtWidgets.QTextBrowser(self.groupBoxA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PARAM_RESULT_BRS_2.sizePolicy().hasHeightForWidth())
        self.PARAM_RESULT_BRS_2.setSizePolicy(sizePolicy)
        self.PARAM_RESULT_BRS_2.setFont(font)
        self.PARAM_RESULT_BRS_2.setObjectName("PARAM_RESULT_BRS_2")
        self.gridLayout_3.addWidget(self.PARAM_RESULT_BRS_2, 3, 2, 13, 1)
        self.gridLayout_2.addWidget(self.groupBoxA, 0, 0, 1, 1)
        self.groupBox143 = QtWidgets.QGroupBox(self.params_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox143.sizePolicy().hasHeightForWidth())
        self.groupBox143.setSizePolicy(sizePolicy)
        self.groupBox143.setMinimumSize(QtCore.QSize(500, 0))

        font.setPointSize(12)
        self.groupBox143.setFont(font)
        self.groupBox143.setObjectName("groupBox143")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox143)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.export_results_btn = QtWidgets.QPushButton(self.groupBox143)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_results_btn.sizePolicy().hasHeightForWidth())
        self.export_results_btn.setSizePolicy(sizePolicy)
        self.export_results_btn.setMinimumSize(QtCore.QSize(0, 83))

        font.setPointSize(14)
        self.export_results_btn.setFont(font)
        self.export_results_btn.setObjectName("export_results_btn")
        self.gridLayout_4.addWidget(self.export_results_btn, 5, 0, 1, 1)
        self.model_test_selector = QtWidgets.QComboBox(self.groupBox143)
        self.model_test_selector.setObjectName("model_test_selector")

        font.setPointSize(12)
        self.model_test_selector.setFont(font)
        os.chdir('pillows/test_folder')
        for dir in os.listdir():
            self.model_test_selector.addItem(str(dir))

        os.chdir('..')
        os.chdir('..')
        self.gridLayout_4.addWidget(self.model_test_selector, 1, 0, 1, 1)

        self.model_test_selector2 = QtWidgets.QComboBox(self.groupBox143)
        self.model_test_selector2.setObjectName("model_test_selector")
        self.model_test_selector2.setFont(font)
        self.gridLayout_4.addWidget(self.model_test_selector2, 2, 0, 1, 1)
        self.run_single_test_btn = QtWidgets.QPushButton(self.groupBox143)
        self.run_single_test_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_single_test_btn.sizePolicy().hasHeightForWidth())
        self.run_single_test_btn.setSizePolicy(sizePolicy)
        self.run_single_test_btn.setMinimumSize(QtCore.QSize(0, 83))

        font.setPointSize(14)
        self.run_single_test_btn.setFont(font)
        self.run_single_test_btn.setObjectName("run_single_test_btn")
        self.gridLayout_4.addWidget(self.run_single_test_btn, 4, 0, 1, 1)
        self.CHECK_PARAM_VALID_BTN = QtWidgets.QPushButton(self.groupBox143)
        self.CHECK_PARAM_VALID_BTN.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHECK_PARAM_VALID_BTN.sizePolicy().hasHeightForWidth())
        self.CHECK_PARAM_VALID_BTN.setSizePolicy(sizePolicy)
        self.CHECK_PARAM_VALID_BTN.setMinimumSize(QtCore.QSize(0, 83))
        self.CHECK_PARAM_VALID_BTN.setObjectName("CHECK_PARAM_VALID_BTN")
        self.gridLayout_4.addWidget(self.CHECK_PARAM_VALID_BTN, 6, 0, 1, 1)
        self.PARAM_RESULT_BRS = QtWidgets.QTextBrowser(self.groupBox143)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.PARAM_RESULT_BRS.sizePolicy().hasHeightForWidth())
        self.PARAM_RESULT_BRS.setSizePolicy(sizePolicy)
        font.setPointSize(12)
        self.PARAM_RESULT_BRS.setFont(font)
        self.PARAM_RESULT_BRS.setObjectName("single_test_result_brs")
        self.gridLayout_4.addWidget(self.PARAM_RESULT_BRS, 0, 1, 7, 1)
        self.gridLayout_2.addWidget(self.groupBox143, 2, 0, 1, 1)
        self.groupBox_2666 = QtWidgets.QGroupBox(self.params_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2666.sizePolicy().hasHeightForWidth())
        self.groupBox_2666.setSizePolicy(sizePolicy)

        font.setPointSize(14)
        self.groupBox_2666.setFont(font)
        self.groupBox_2666.setObjectName("groupBox_2666")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2666)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tendmin_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.tendmin_lbl.setObjectName("tendmin_lbl")
        self.gridLayout_5.addWidget(self.tendmin_lbl, 13, 0, 1, 1)
        self.tstmax_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.tstmax_lbl.setObjectName("tstmax_lbl")
        self.gridLayout_5.addWidget(self.tstmax_lbl, 2, 0, 1, 1)
        self.t2_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.t2_lbl.setObjectName("t2_lbl")
        self.gridLayout_5.addWidget(self.t2_lbl, 8, 0, 1, 1)
        self.tstmin_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.tstmin_lbl.setObjectName("tstmin_lbl")
        self.gridLayout_5.addWidget(self.tstmin_lbl, 3, 0, 1, 1)
        self.tstart_min_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.tstart_min_input.setObjectName("tstart_min_input")
        self.gridLayout_5.addWidget(self.tstart_min_input, 3, 1, 1, 1)
        #self.replace_to_plot = QtWidgets.QTextBrowser(self.groupBox_2666)
        #self.replace_to_plot.setObjectName("replace_to_plot")
        self.canvas = PlotCanvas(self)
        self.gridLayout_5.addWidget(self.canvas, 0, 0, 1, 3)
        self.aresrange_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.aresrange_lbl.setObjectName("aresrange_lbl")
        self.gridLayout_5.addWidget(self.aresrange_lbl, 16, 0, 1, 1)
        self.tstart_max_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.tstart_max_input.setObjectName("tstart_max_input")
        self.gridLayout_5.addWidget(self.tstart_max_input, 2, 1, 1, 1)
        self.limitares_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.limitares_lbl.setObjectName("limitares_lbl")
        self.gridLayout_5.addWidget(self.limitares_lbl, 17, 0, 1, 1)
        self.t1_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.t1_input.setObjectName("t1_input")
        self.gridLayout_5.addWidget(self.t1_input, 5, 1, 1, 1)
        self.t3_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.t3_input.setObjectName("t3_input")
        self.gridLayout_5.addWidget(self.t3_input, 9, 1, 1, 1)
        self.limit_ares_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.limit_ares_input.setObjectName("limit_ares_input")
        self.gridLayout_5.addWidget(self.limit_ares_input, 17, 1, 1, 1)
        self.t2_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.t2_input.setObjectName("t2_input")
        self.gridLayout_5.addWidget(self.t2_input, 8, 1, 1, 1)
        self.tendmax_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.tendmax_lbl.setObjectName("tendmax_lbl")
        self.gridLayout_5.addWidget(self.tendmax_lbl, 15, 0, 1, 1)
        self.tend_max_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.tend_max_input.setObjectName("tend_max_input")
        self.gridLayout_5.addWidget(self.tend_max_input, 15, 1, 1, 1)
        self.t4_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.t4_input.setObjectName("t4_input")
        self.gridLayout_5.addWidget(self.t4_input, 11, 1, 1, 1)
        self.t3_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.t3_lbl.setObjectName("t3_lbl")
        self.gridLayout_5.addWidget(self.t3_lbl, 9, 0, 1, 1)
        self.t4_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.t4_lbl.setObjectName("t4_lbl")
        self.gridLayout_5.addWidget(self.t4_lbl, 11, 0, 1, 1)
        self.t1_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.t1_lbl.setObjectName("t1_lbl")
        self.gridLayout_5.addWidget(self.t1_lbl, 5, 0, 1, 1)
        self.tend_min_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.tend_min_input.setObjectName("tend_min_input")
        self.gridLayout_5.addWidget(self.tend_min_input, 13, 1, 1, 1)
        self.sideinput = QtWidgets.QComboBox(self.groupBox_2666)
        self.sideinput.setObjectName("comboBox")
        self.sideinput.addItem("")
        self.sideinput.addItem("")
        self.sideinput.addItem("")
        self.sideinput.addItem("")
        self.gridLayout_5.addWidget(self.sideinput, 20, 1, 1, 1)
        self.timebeforecollis_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.timebeforecollis_input.setObjectName("timebeforecollis_input")
        self.gridLayout_5.addWidget(self.timebeforecollis_input, 19, 1, 1, 1)
        self.timestep_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.timestep_lbl.setObjectName("timestep_lbl")
        self.gridLayout_5.addWidget(self.timestep_lbl, 18, 0, 1, 1)
        self.timebeforecoll_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.timebeforecoll_lbl.setObjectName("timebeforecoll_lbl")
        self.gridLayout_5.addWidget(self.timebeforecoll_lbl, 19, 0, 1, 1)
        self.timestep_input = QtWidgets.QDoubleSpinBox(self.groupBox_2666)
        self.timestep_input.setObjectName("timestep_input")
        self.gridLayout_5.addWidget(self.timestep_input, 18, 1, 1, 1)
        self.collside_lbl = QtWidgets.QLabel(self.groupBox_2666)
        self.collside_lbl.setObjectName("collside_lbl")
        self.gridLayout_5.addWidget(self.collside_lbl, 20, 0, 1, 1)
        self.syntez_btn = QtWidgets.QPushButton(self.groupBox_2666)
        self.syntez_btn.setObjectName("syntez_btn")
        self.syntez_btn.setFont(font)
        self.gridLayout_5.addWidget(self.syntez_btn, 23, 0, 1, 3)
        self.ares_range_input = QtWidgets.QSpinBox(self.groupBox_2666)
        self.ares_range_input.setObjectName("ares_range_input")
        self.gridLayout_5.addWidget(self.ares_range_input, 16, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2666, 0, 2, 3, 1)
        self.groupBox1342 = QtWidgets.QGroupBox(self.params_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1342.sizePolicy().hasHeightForWidth())
        self.groupBox1342.setSizePolicy(sizePolicy)
        self.groupBox1342.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox1342.setTitle("")
        self.groupBox1342.setObjectName("groupBox1342")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox1342)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.read_params_btn = QtWidgets.QPushButton(self.groupBox1342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_params_btn.sizePolicy().hasHeightForWidth())
        self.read_params_btn.setSizePolicy(sizePolicy)
        self.read_params_btn.setMinimumSize(QtCore.QSize(0, 0))

        font.setPointSize(12)
        self.read_params_btn.setFont(font)
        self.read_params_btn.setObjectName("read_params_btn")
        self.gridLayout_6.addWidget(self.read_params_btn, 0, 1, 1, 1)
        self.UPDATE_PARAMS_BTN = QtWidgets.QPushButton(self.groupBox1342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UPDATE_PARAMS_BTN.sizePolicy().hasHeightForWidth())
        self.UPDATE_PARAMS_BTN.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.UPDATE_PARAMS_BTN.setFont(font)
        self.UPDATE_PARAMS_BTN.setObjectName("UPDATE_PARAMS_BTN")
        self.gridLayout_6.addWidget(self.UPDATE_PARAMS_BTN, 0, 0, 1, 1)
        self.UPDATE_PARAMS_LOCAL_BTN = QtWidgets.QPushButton(self.groupBox1342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UPDATE_PARAMS_LOCAL_BTN.sizePolicy().hasHeightForWidth())
        self.UPDATE_PARAMS_LOCAL_BTN.setSizePolicy(sizePolicy)

        font.setPointSize(12)
        self.UPDATE_PARAMS_LOCAL_BTN.setFont(font)
        self.UPDATE_PARAMS_LOCAL_BTN.setObjectName("UPDATE_PARAMS_LOCAL_BTN")
        self.gridLayout_6.addWidget(self.UPDATE_PARAMS_LOCAL_BTN, 1, 0, 1, 1)
        self.read_params_local_btn = QtWidgets.QPushButton(self.groupBox1342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_params_local_btn.sizePolicy().hasHeightForWidth())
        self.read_params_local_btn.setSizePolicy(sizePolicy)
        self.read_params_local_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.read_params_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.UPDATE_PARAMS_LOCAL_BTN.setMinimumSize(QtCore.QSize(0, 35))
        self.UPDATE_PARAMS_BTN.setMinimumSize(QtCore.QSize(0, 35))

        font.setPointSize(12)
        self.read_params_local_btn.setFont(font)
        self.read_params_local_btn.setObjectName("read_params_local_btn")
        self.gridLayout_6.addWidget(self.read_params_local_btn, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox1342, 1, 0, 1, 1)

        font.setPointSize(13)
        self.tstmax_lbl.setFont(font)
        self.tstmin_lbl.setFont(font)
        self.t1_lbl.setFont(font)
        self.t2_lbl.setFont(font)
        self.t3_lbl.setFont(font)
        self.t4_lbl.setFont(font)
        self.tendmax_lbl.setFont(font)
        self.tendmin_lbl.setFont(font)
        self.aresrange_lbl.setFont(font)
        self.limitares_lbl.setFont(font)
        self.timestep_lbl.setFont(font)
        self.timebeforecoll_lbl.setFont(font)
        self.collside_lbl.setFont(font)

        self.sideinput.setFont(font)
        self.timebeforecollis_input.setFont(font)
        self.tstart_min_input.setFont(font)
        self.tstart_max_input.setFont(font)
        self.t1_input.setFont(font)
        self.t2_input.setFont(font)
        self.t3_input.setFont(font)
        self.t4_input.setFont(font)
        self.tend_min_input.setFont(font)
        self.tend_max_input.setFont(font)
        self.limit_ares_input.setFont(font)
        self.ares_range_input.setFont(font)
        self.timestep_input.setFont(font)

        self.tstart_min_input.setMaximum(1000)
        self.tstart_max_input.setMaximum(1000)
        self.t1_input.setMaximum(1000)
        self.t2_input.setMaximum(1000)
        self.t3_input.setMaximum(1000)
        self.t4_input.setMaximum(1000)
        self.tend_min_input.setMaximum(1000)
        self.tend_max_input.setMaximum(1000)
        self.limit_ares_input.setMaximum(100)
        self.ares_range_input.setMaximum(100)
        self.timestep_input.setMaximum(1)

        self.tstart_min_input.setValue(4)
        self.tstart_max_input.setValue(0)
        self.t1_input.setValue(15)
        self.t2_input.setValue(25)
        self.t3_input.setValue(65)
        self.t4_input.setValue(85)
        self.tend_min_input.setValue(97)
        self.tend_max_input.setValue(109)
        self.limit_ares_input.setValue(20)
        self.ares_range_input.setValue(80)
        self.timestep_input.setValue(0.5)
        self.canvas.plot(self.tstart_min_input.value(), self.t1_input.value(), self.tstart_max_input.value(),
                         self.t2_input.value(), self.t3_input.value(), self.t4_input.value(),
                         self.limit_ares_input.value(), self.ares_range_input.value(), self.tend_min_input.value(),
                         self.tend_max_input.value())

        self.tabWidget.addTab(self.params_tab, "")
        self.reprogramming_tab = QtWidgets.QWidget()
        self.reprogramming_tab.setObjectName("reprogramming_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.reprogramming_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_23456789 = QtWidgets.QGroupBox(self.reprogramming_tab)

        font.setPointSize(12)
        self.groupBox_23456789.setFont(font)
        self.groupBox_23456789.setObjectName("groupBox_23456789")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_23456789)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_23456789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 50))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_4.addWidget(self.progressBar, 2, 1, 1, 2)
        self.LOG_BRS = QtWidgets.QTextBrowser(self.groupBox_23456789)
        self.LOG_BRS.setObjectName("LOG_BRS")
        self.LOG_BRS.setFont(font)
        self.gridLayout_4.addWidget(self.LOG_BRS, 3, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_23456789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 60))

        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 1, 1, 1, 2)
        self.toolButton = QtWidgets.QToolButton(self.groupBox_23456789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_4.addWidget(self.toolButton, 0, 1, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_23456789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 150))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setFont(font)
        self.gridLayout_4.addWidget(self.textBrowser_2, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_23456789, 1, 0, 2, 1)
        self.groupBox1565 = QtWidgets.QGroupBox(self.reprogramming_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1565.sizePolicy().hasHeightForWidth())
        self.groupBox1565.setSizePolicy(sizePolicy)
        self.groupBox1565.setMinimumSize(QtCore.QSize(0, 200))

        font.setPointSize(12)
        self.groupBox1565.setFont(font)
        self.groupBox1565.setObjectName("groupBox1565")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox1565)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.VER_LOG_BRS = QtWidgets.QTextBrowser(self.groupBox1565)
        self.VER_LOG_BRS.setObjectName("VER_LOG_BRS")
        self.gridLayout_3.addWidget(self.VER_LOG_BRS, 0, 7, 15, 1)
        self.BUTTONSGROUP_BOX = QtWidgets.QGroupBox(self.groupBox1565)
        self.BUTTONSGROUP_BOX.setTitle("")
        self.BUTTONSGROUP_BOX.setObjectName("BUTTONSGROUP_BOX")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.BUTTONSGROUP_BOX)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Manufacture_mode_btn = QtWidgets.QPushButton(self.BUTTONSGROUP_BOX)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Manufacture_mode_btn.sizePolicy().hasHeightForWidth())
        self.Manufacture_mode_btn.setSizePolicy(sizePolicy)
        self.Manufacture_mode_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.Manufacture_mode_btn.setObjectName("Manufacture_mode_btn")
        self.gridLayout_6.addWidget(self.Manufacture_mode_btn, 0, 1, 1, 1)
        self.WRITE_ACU_BTN = QtWidgets.QPushButton(self.BUTTONSGROUP_BOX)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WRITE_ACU_BTN.sizePolicy().hasHeightForWidth())
        self.WRITE_ACU_BTN.setSizePolicy(sizePolicy)
        self.WRITE_ACU_BTN.setMinimumSize(QtCore.QSize(350, 50))
        self.WRITE_ACU_BTN.setObjectName("WRITE_ACU_BTN")
        self.gridLayout_6.addWidget(self.WRITE_ACU_BTN, 0, 0, 1, 1)
        self.READ_VERSBTN = QtWidgets.QPushButton(self.BUTTONSGROUP_BOX)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.READ_VERSBTN.sizePolicy().hasHeightForWidth())
        self.READ_VERSBTN.setSizePolicy(sizePolicy)
        self.READ_VERSBTN.setMinimumSize(QtCore.QSize(0, 50))
        self.READ_VERSBTN.setObjectName("READ_VERSBTN")
        self.gridLayout_6.addWidget(self.READ_VERSBTN, 1, 1, 1, 1)
        self.SET_WM_BTN = QtWidgets.QPushButton(self.BUTTONSGROUP_BOX)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SET_WM_BTN.sizePolicy().hasHeightForWidth())
        self.SET_WM_BTN.setSizePolicy(sizePolicy)
        self.SET_WM_BTN.setMinimumSize(QtCore.QSize(0, 50))
        self.SET_WM_BTN.setObjectName("SET_WM_BTN")
        self.gridLayout_6.addWidget(self.SET_WM_BTN, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.BUTTONSGROUP_BOX, 0, 2, 1, 2)
        self.acu_gb = QtWidgets.QGroupBox(self.groupBox1565)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acu_gb.sizePolicy().hasHeightForWidth())
        #self.acu_gb.setMinimumSize(QtCore.QSize(0, 350))
        self.acu_gb.setSizePolicy(sizePolicy)
        self.acu_gb.setObjectName("acu_gb")
        self.acu_gb.setFont(font)
        self.gridLayout_5 = QtWidgets.QGridLayout(self.acu_gb)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RLSB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.RLSB_EN.setObjectName("RLSB_EN")
        self.gridLayout_5.addWidget(self.RLSB_EN, 6, 3, 1, 1)
        self.PSAB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PSAB_EN.setObjectName("PSAB_EN")
        self.gridLayout_5.addWidget(self.PSAB_EN, 5, 2, 1, 1)
        self.RCSB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.RCSB_EN.setObjectName("RCSB_EN")
        self.gridLayout_5.addWidget(self.RCSB_EN, 5, 3, 1, 1)
        self.PADI_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PADI_EN.setObjectName("PADI_EN")
        self.gridLayout_5.addWidget(self.PADI_EN, 2, 1, 1, 1)
        self.RRSB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.RRSB_EN.setObjectName("RRSB_EN")
        self.gridLayout_5.addWidget(self.RRSB_EN, 3, 3, 1, 1)
        self.DSB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.DSB_EN.setObjectName("DSB_EN")
        self.gridLayout_5.addWidget(self.DSB_EN, 6, 2, 1, 1)
        self.PPS_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PPS_EN.setObjectName("PPS_EN")
        self.gridLayout_5.addWidget(self.PPS_EN, 5, 1, 1, 1)
        self.DSAB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.DSAB_EN.setObjectName("DSAB_EN")
        self.gridLayout_5.addWidget(self.DSAB_EN, 3, 2, 1, 1)
        self.DAB_EN = QtWidgets.QCheckBox(self.acu_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DAB_EN.sizePolicy().hasHeightForWidth())
        self.DAB_EN.setSizePolicy(sizePolicy)
        self.DAB_EN.setMinimumSize(QtCore.QSize(20, 0))

        font.setPointSize(11)
        self.DAB_EN.setFont(font)
        self.DAB_EN.setObjectName("DAB_EN")
        self.gridLayout_5.addWidget(self.DAB_EN, 2, 0, 1, 1)
        self.PSB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PSB_EN.setObjectName("PSB_EN")
        self.gridLayout_5.addWidget(self.PSB_EN, 2, 3, 1, 1)
        self.PAB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PAB_EN.setMinimumSize(QtCore.QSize(20, 0))

        font.setPointSize(11)
        self.PAB_EN.setFont(font)
        self.PAB_EN.setObjectName("PAB_EN")
        self.gridLayout_5.addWidget(self.PAB_EN, 3, 0, 1, 1)
        self.DPT_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.DPT_EN.setMinimumSize(QtCore.QSize(20, 0))

        font.setPointSize(11)
        self.DPT_EN.setFont(font)
        self.DPT_EN.setObjectName("DPT_EN")
        self.gridLayout_5.addWidget(self.DPT_EN, 5, 0, 1, 1)
        self.LCAB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.LCAB_EN.setObjectName("LCAB_EN")
        self.gridLayout_5.addWidget(self.LCAB_EN, 6, 1, 1, 1)
        self.PADS_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PADS_EN.setObjectName("PADS_EN")
        self.gridLayout_5.addWidget(self.PADS_EN, 3, 1, 1, 1)
        self.PPT_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PPT_EN.setMinimumSize(QtCore.QSize(20, 0))

        font.setPointSize(11)
        self.PPT_EN.setFont(font)
        self.PPT_EN.setObjectName("PPT_EN")
        self.gridLayout_5.addWidget(self.PPT_EN, 6, 0, 1, 1)
        self.RCAB_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.RCAB_EN.setObjectName("RCAB_EN")
        self.gridLayout_5.addWidget(self.RCAB_EN, 2, 2, 1, 1)
        self.PGSAT_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PGSAT_EN.setObjectName("PGSAT_EN")
        self.gridLayout_5.addWidget(self.PGSAT_EN, 2, 4, 1, 1)
        self.DGSAT_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.DGSAT_EN.setObjectName("DGSAT_EN")
        self.gridLayout_5.addWidget(self.DGSAT_EN, 3, 4, 1, 1)
        self.PPSAT_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.PPSAT_EN.setObjectName("PPSAT_EN")
        self.gridLayout_5.addWidget(self.PPSAT_EN, 5, 4, 1, 1)
        self.DPSAT_EN = QtWidgets.QCheckBox(self.acu_gb)
        self.DPSAT_EN.setObjectName("DPSAT_EN")
        self.gridLayout_5.addWidget(self.DPSAT_EN, 6, 4, 1, 1)
        self.gridLayout_3.addWidget(self.acu_gb, 13, 2, 1, 2)
        self.groupBoxSEL = QtWidgets.QGroupBox(self.groupBox1565)
        self.groupBoxSEL.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBoxSEL)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.STO_VER_BTN = QtWidgets.QPushButton(self.groupBoxSEL)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STO_VER_BTN.sizePolicy().hasHeightForWidth())
        self.STO_VER_BTN.setSizePolicy(sizePolicy)
        self.STO_VER_BTN.setMinimumSize(QtCore.QSize(350, 50))
        self.STO_VER_BTN.setObjectName("STO_VER_BTN")
        self.gridLayout_7.addWidget(self.STO_VER_BTN, 0, 2, 1, 1)
        self.ACC_VER_BTN = QtWidgets.QPushButton(self.groupBoxSEL)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ACC_VER_BTN.sizePolicy().hasHeightForWidth())
        self.ACC_VER_BTN.setSizePolicy(sizePolicy)
        self.ACC_VER_BTN.setMinimumSize(QtCore.QSize(0, 50))
        self.ACC_VER_BTN.setObjectName("ACC_VER_BTN")
        self.gridLayout_7.addWidget(self.ACC_VER_BTN, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBoxSEL, 1, 2, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox1565, 3, 0, 1, 1)
        self.tabWidget.addTab(self.reprogramming_tab, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.groupBox_21 = QtWidgets.QGroupBox(self.Settings)
        self.groupBox_21.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.COM_PORT_SELECTOR = QtWidgets.QComboBox(self.groupBox_21)
        self.COM_PORT_SELECTOR.setFont(font)
        self.COM_PORT_SELECTOR.setObjectName("COM_PORT_SELECTOR")
        self.gridLayout_26.addWidget(self.COM_PORT_SELECTOR, 0, 0, 1, 1)
        self.COM_PORT_CONNECT_BTN = QtWidgets.QPushButton(self.groupBox_21)
        self.COM_PORT_CONNECT_BTN.setObjectName("COM_PORT_CONNECT_BTN")
        self.COM_PORT_CONNECT_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.COM_PORT_CONNECT_BTN.setFont(font)
        self.gridLayout_26.addWidget(self.COM_PORT_CONNECT_BTN, 1, 0, 1, 1)
        self.COM_PORT_CLOSE_BTN = QtWidgets.QPushButton(self.groupBox_21)
        self.COM_PORT_CLOSE_BTN.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.COM_PORT_CLOSE_BTN.setObjectName("COM_PORT_CONNECT_BTN")
        self.gridLayout_26.addWidget(self.COM_PORT_CLOSE_BTN, 3, 0, 1, 1)
        self.COM_PORT_BRS = QtWidgets.QTextBrowser(self.groupBox_21)
        self.COM_PORT_BRS.setObjectName("COM_PORT_BRS")
        self.COM_PORT_BRS.setFont(font)
        self.COM_PORT_CLOSE_BTN.setText("ЗАКРЫТЬ COM-PORT")

        self.manual_mode_btn = QtWidgets.QPushButton(self.groupBox_21)
        self.manual_mode_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.manual_mode_btn.setObjectName("COM_PORT2T_BTN")
        self.gridLayout_26.addWidget(self.manual_mode_btn, 4, 0, 1, 1)
        self.manual_mode_btn.setText("Ручной режим управления ремнями")
        self.manual_mode_btn.setFont(font)

        self.RLSB_EN.setFont(font)
        self.RCSB_EN.setFont(font)
        self.RRSB_EN.setFont(font)
        self.PADI_EN.setFont(font)
        self.PSAB_EN.setFont(font)
        self.DSAB_EN.setFont(font)
        self.DSB_EN.setFont(font)
        self.PSB_EN.setFont(font)
        self.PPS_EN.setFont(font)
        self.DAB_EN.setFont(font)
        self.PADS_EN.setFont(font)
        self.DPT_EN.setFont(font)
        self.LCAB_EN.setFont(font)
        self.PPT_EN.setFont(font)
        self.PAB_EN.setFont(font)
        self.RCAB_EN.setFont(font)
        self.PGSAT_EN.setFont(font)
        self.DGSAT_EN.setFont(font)
        self.PPSAT_EN.setFont(font)
        self.DPSAT_EN.setFont(font)
        self.groupBoxSEL.setFont(font)

        font.setPointSize(12)
        self.STO_VER_BTN.setFont(font)
        self.ACC_VER_BTN.setFont(font)
        self.WRITE_ACU_BTN.setFont(font)
        self.Manufacture_mode_btn.setFont(font)
        self.READ_VERSBTN.setFont(font)
        self.SET_WM_BTN.setFont(font)
        self.VER_LOG_BRS.setFont(font)
        portlist=list()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            portlist.append(port.device)
        for i in range(0,len(portlist)):
            self.COM_PORT_SELECTOR.addItem(portlist[i])
        if(len(portlist)>0):
            self.COM_PORT=portlist[0]
            self.UART=None#Nserial.Serial(self.COM_PORT,115200)
            #self.UART.close()
        self.gridLayout_26.addWidget(self.COM_PORT_BRS, 2, 0, 1, 1)
        self.tabWidget.addTab(self.Settings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.UDS_LED_SELECTOR.setDisabled(True)

        self.tstart_min_input.valueChanged.connect(self.update_plot)
        self.tstart_max_input.valueChanged.connect(self.update_plot)
        self.t1_input.valueChanged.connect(self.update_plot)
        self.t2_input.valueChanged.connect(self.update_plot)
        self.t3_input.valueChanged.connect(self.update_plot)
        self.t4_input.valueChanged.connect(self.update_plot)
        self.tend_min_input.valueChanged.connect(self.update_plot)
        self.tend_max_input.valueChanged.connect(self.update_plot)
        self.limit_ares_input.valueChanged.connect(self.update_plot)
        self.ares_range_input.valueChanged.connect(self.update_plot)

        self.syntez_btn.clicked.connect(self.on_click2)
        self.save_params_btn.clicked.connect(self.on_click3)
        self.save_params_btn.clicked.connect(self.PARAM_RESULT_BRS_2.clear)
        self.SET_WM_BTN.clicked.connect(self.run_set_working_mode)
        self.SET_WM_BTN.clicked.connect(self.VER_LOG_BRS.clear)

        self.READ_VERSBTN.clicked.connect(self.run_read_ecu_version)
        self.READ_VERSBTN.clicked.connect(self.VER_LOG_BRS.clear)

        self.Run_Init_btn.clicked.connect(self.run_test1)
        self.Run_Init_btn.clicked.connect(self.inittime_brs.clear)
        self.Run_Init_btn.clicked.connect(self.initresult_brs.clear)
        self.Run_Init_btn.clicked.connect(self.can_msg_brs.clear)
        self.Run_Init_btn.clicked.connect(self.DisableAll)

        self.perod_periodic_btn.clicked.connect(self.run_test2)
        self.perod_periodic_btn.clicked.connect(self.accepted_periodic_brs.clear)
        self.perod_periodic_btn.clicked.connect(self.measured_period_brs.clear)
        self.perod_periodic_btn.clicked.connect(self.result_periodic_brs.clear)
        self.perod_periodic_btn.clicked.connect(self.DisableAll)


        self.start_trig_btn.clicked.connect(self.run_test3_period)
        self.start_trig_btn.clicked.connect(self.accepted_trig_brs.clear)
        self.start_trig_btn.clicked.connect(self.measured_trig_brs.clear)
        self.start_trig_btn.clicked.connect(self.result_trig_brs.clear)
        self.start_trig_btn.clicked.connect(self.DisableAll)


        self.start_acc_btn.clicked.connect(self.run_accelerometer)
        self.start_acc_btn.clicked.connect(self.got_res_brs.clear)
        self.start_acc_btn.clicked.connect(self.CRASHDETECTED_BRS.clear)
        self.start_acc_btn.clicked.connect(self.DisableAll)

        self.UDS_RUN_BTN.clicked.connect(self.run_UDS)
        self.UDS_RUN_BTN.clicked.connect(self.UDS_MSG_BRS.clear)
        self.UDS_RUN_BTN.clicked.connect(self.DisableAll)

        self.UDS_TEST_SELECTOR.currentIndexChanged['int'].connect(self.UDS_test_changed)
        self.UDS_TEST_SELECTOR.currentIndexChanged['int'].connect(self.UDS_MSG_BRS.clear)

        self.UDS_LED_SELECTOR.currentIndexChanged['int'].connect(self.UDS_LED_changed)
        self.UDS_LED_SELECTOR.currentIndexChanged['int'].connect(self.UDS_MSG_BRS.clear)

        self.UDS_NRC_SELECTOR.currentIndexChanged['int'].connect(self.NRC_CHANGED)
        self.UDS_NRC_SELECTOR.currentIndexChanged['int'].connect(self.UDS_MSG_BRS.clear)

        self.start_SBR_btn.clicked.connect(self.run_SBR)
        self.start_SBR_btn.clicked.connect(self.acc_SBR_brs.clear)
        self.start_SBR_btn.clicked.connect(self.got_res_SBR_brs.clear)
        self.start_SBR_btn.clicked.connect(self.DisableAll)

        self.acc_selector.currentIndexChanged['int'].connect(self.acc_set_changed) # type: ignore
        self.SBR_test_selector.currentIndexChanged['int'].connect(self.SBR_test_changed) # type: ignore

        self.DIAG_RESET_BTN.clicked.connect(self.run_ECU_reset)
        self.DIAG_RESET_BTN.clicked.connect(self.DIAG_ACCEPTED_BRS.clear)
        self.DIAG_RESET_BTN.clicked.connect(self.DisableAll)


        self.DIAG_VIN0_BTN.clicked.connect(self.run_Write_VIN0)
        self.DIAG_VIN0_BTN.clicked.connect(self.DIAG_ACCEPTED_BRS.clear)
        self.DIAG_VIN0_BTN.clicked.connect(self.DisableAll)

        self.DIAG_VIN1_BTN.clicked.connect(self.run_Write_VIN1)
        self.DIAG_VIN1_BTN.clicked.connect(self.DIAG_ACCEPTED_BRS.clear)
        self.DIAG_VIN1_BTN.clicked.connect(self.DisableAll)

        self.DIAG_READ_0x08_BTN.clicked.connect(lambda:self.run_ReadDTC(0x08))
        self.DIAG_READ_0x08_BTN.clicked.connect(self.DIAG_ERRORS_BRS.clear)
        self.DIAG_READ_0x08_BTN.clicked.connect(self.DisableAll)

        self.DIAG_READ_0x09_BTN.clicked.connect(lambda:self.run_ReadDTC(0x09))
        self.DIAG_READ_0x09_BTN.clicked.connect(self.DIAG_ERRORS_BRS.clear)
        self.DIAG_READ_0x09_BTN.clicked.connect(self.DisableAll)

        self.DIAG_CLEAR_DTC_BTN.clicked.connect(self.run_ClearDTC)
        self.DIAG_CLEAR_DTC_BTN.clicked.connect(self.DIAG_ACCEPTED_BRS.clear)
        self.DIAG_CLEAR_DTC_BTN.clicked.connect(self.DisableAll)
        self.manual_mode_btn.clicked.connect(self.run_manual_mode)
        self.manual_mode_btn.clicked.connect(self.COM_PORT_BRS.clear)

        self.CHECK_PARAM_VALID_BTN.clicked.connect(self.run_thread_model_all)
        self.CHECK_PARAM_VALID_BTN.clicked.connect(self.PARAM_RESULT_BRS.clear)

        self.run_single_test_btn.clicked.connect(self.run_thread_model_single)
        self.run_single_test_btn.clicked.connect(self.PARAM_RESULT_BRS.clear)

        self.DIAG_UPD_CAN_MSG_BTN.clicked.connect(self.Send_periodic)

        self.DIAG_STOP_CAN_MSG_BTN.clicked.connect(self.Stop_Send_periodic)

        self.WRITE_ACU_BTN.clicked.connect(self.run_Write_ACU)
        self.WRITE_ACU_BTN.clicked.connect(self.DisableAll)
        self.WRITE_ACU_BTN.clicked.connect(self.VER_LOG_BRS.clear)

        self.EDR1_BTN.clicked.connect(lambda:self.run_EDR_read(1))
        self.EDR1_BTN.clicked.connect(self.DisableAll)
        self.EDR1_BTN.clicked.connect(lambda: self.EDR_STOP_BTN.setDisabled(False))
        self.EDR1_BTN.clicked.connect(lambda: self.EDR_OTHER_DATA_BRS.clear)

        self.EDR2_BTN.clicked.connect(lambda:self.run_EDR_read(2))
        self.EDR2_BTN.clicked.connect(self.DisableAll)
        self.EDR2_BTN.clicked.connect(lambda: self.EDR_STOP_BTN.setDisabled(False))
        self.EDR2_BTN.clicked.connect(lambda: self.EDR_OTHER_DATA_BRS.clear)

        self.EDR3_BTN.clicked.connect(lambda: self.run_EDR_read(3))
        self.EDR3_BTN.clicked.connect(self.DisableAll)
        self.EDR3_BTN.clicked.connect(lambda: self.EDR_STOP_BTN.setDisabled(False))
        self.EDR3_BTN.clicked.connect(lambda: self.EDR_OTHER_DATA_BRS.clear)

        self.CHECK_CRASH_DETECTION_BTN.clicked.connect(self.run_Check_CD)
        self.CHECK_CRASH_DETECTION_BTN.clicked.connect(self.DIAG_ACCEPTED_BRS.clear)
        self.CHECK_CRASH_DETECTION_BTN.clicked.connect(self.DisableAll)

        self.read_snap_btn.clicked.connect(self.run_snap_handler)
        self.read_snap_btn.clicked.connect(self.snap_brs.clear)
        self.read_snap_btn.clicked.connect(self.status_brs.clear)
        self.read_snap_btn.clicked.connect(self.lcdNumber_2.clear)
        self.read_snap_btn.clicked.connect(self.lcdNumber_3.clear)
        self.read_snap_btn.clicked.connect(self.lcdNumber_4.clear)
        self.read_snap_btn.clicked.connect(self.lcdNumber_5.clear)

        self.STOP_BTN_1.clicked.connect(self.close)
        self.STOP_BTN_1.clicked.connect(self.EnableAll)
        self.STOP_BTN_1.setDisabled(True)


        self.STOP_BTN_2.clicked.connect(self.close)
        self.STOP_BTN_2.clicked.connect(self.EnableAll)
        self.STOP_BTN_2.setDisabled(True)


        self.STOP_BTN_3.clicked.connect(self.close)
        self.STOP_BTN_3.clicked.connect(self.EnableAll)
        self.STOP_BTN_3.setDisabled(True)


        self.STOP_BTN_4.clicked.connect(self.close)
        self.STOP_BTN_4.clicked.connect(self.EnableAll)
        self.STOP_BTN_4.setDisabled(True)


        self.STOP_BTN_5.clicked.connect(self.close)
        self.STOP_BTN_5.clicked.connect(self.EnableAll)
        self.STOP_BTN_5.setDisabled(True)


        self.STOP_BTN_6.clicked.connect(self.close)
        self.STOP_BTN_6.clicked.connect(self.EnableAll)
        self.STOP_BTN_6.setDisabled(True)


        self.EDR_STOP_BTN.clicked.connect(self.close)
        self.READ_NUM_BTN.clicked.connect(self.run_EDR_num_read)
        self.EDR_STOP_BTN.clicked.connect(self.EnableAll)

        self.model_test_selector.currentIndexChanged.connect(lambda: self.testfolder_changed())


        self.STOP_BTN_8.clicked.connect(self.close)
        self.STOP_BTN_8.clicked.connect(lambda: self.START_VALID_AB_BTN.setDisabled(False))
        self.STOP_BTN_8.setDisabled(True)

        self.START_VALID_AB_BTN.clicked.connect(self.run_ValidAB)
        self.START_VALID_AB_BTN.clicked.connect(self.VALIDAB_BRS.clear)
        self.START_VALID_AB_BTN.clicked.connect(self.DisableAll)

        self.UPDATE_PARAMS_BTN.clicked.connect(self.run_update_params)
        self.UPDATE_PARAMS_BTN.clicked.connect(self.PARAM_RESULT_BRS_2.clear)

        self.read_params_btn.clicked.connect(self.run_read_params)
        self.read_params_btn.clicked.connect(self.PARAM_RESULT_BRS_2.clear)

        self.COM_PORT_SELECTOR.currentIndexChanged['int'].connect(self.COM_port_changed)
        self.COM_PORT_CONNECT_BTN.clicked.connect(self.CheckConnection_run)
        self.COM_PORT_CONNECT_BTN.clicked.connect(self.COM_PORT_BRS.clear)

        self.toolButton.clicked.connect(self.textBrowser_2.clear)
        self.toolButton.clicked.connect(self.on_click)
        self.pushButton_3.clicked.connect(self.Reprogrammer_run)
        self.pushButton_3.clicked.connect(self.LOG_BRS.clear)

        self.DIAG_SPEED_SELECTOR.valueChanged[int].connect(self.update_speed_label)
        self.DIAG_MILEAGE_SELECTOR.valueChanged[int].connect(self.update_mileage_label)

        self.snap_sel_1.currentTextChanged.connect(self.snap_changed)

        self.defined_params_selector.currentIndexChanged.connect(self.XGF_or_XGE)
        self.STO_VER_BTN.clicked.connect(lambda:self.run_Config_version(1))
        self.STO_VER_BTN.clicked.connect(self.VER_LOG_BRS.clear)
        self.ACC_VER_BTN.clicked.connect(lambda:self.run_Config_version(2))
        self.ACC_VER_BTN.clicked.connect(self.VER_LOG_BRS.clear)
        self.Manufacture_mode_btn.clicked.connect(self.run_to_manufacture_mode)
        self.Manufacture_mode_btn.clicked.connect(self.VER_LOG_BRS.clear)
        self.export_results_btn.clicked.connect(self.run_export_results)

        self.UPDATE_PARAMS_LOCAL_BTN.clicked.connect(self.run_file_updater)
        self.UPDATE_PARAMS_LOCAL_BTN.clicked.connect(self.PARAM_RESULT_BRS_2.clear)

        self.read_params_local_btn.clicked.connect(self.run_file_reader)
        self.read_params_local_btn.clicked.connect(self.PARAM_RESULT_BRS_2.clear)
        self.COM_PORT_CLOSE_BTN.clicked.connect(self.close_com)

        self.DisableAll()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "СТО СНПБ АВТОВАЗ"))
        self.testfolder_changed()
        os.chdir('icons')
        MainWindow.setWindowIcon(QtGui.QIcon("main_icon.ico"))
        self.toolButton.setIcon(QtGui.QIcon("reprogramming_icon.png"))
        os.chdir('..')
        self.Run_Init_btn.setText(_translate("MainWindow", "Старт"))
        self.Inittime_lbl.setText(_translate("MainWindow", "Измеренное время инциализации"))
        self.Initreuult_lbl.setText(_translate("MainWindow", "Результат проверки"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Проверка времени инициализации БУ СНПБ"))
        self.can_msg_lbl.setText(_translate("MainWindow", "Принятые сообщения CAN"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Проверка инициализации БУ СНПБ"))
        self.period_peciodic_title.setText(_translate("MainWindow", "Измерение периода CAN-сообщения 0х653 "))
        self.START_VALID_AB_BTN.setText(_translate("MainWindow", "Старт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.init_tab),_translate("MainWindow", "Проверка инициализации"))
        self.perod_periodic_btn.setText(_translate("MainWindow", "Старт"))
        self.label_5.setText(_translate("MainWindow", "Ожидаемый период"))
        self.label_6.setText(_translate("MainWindow", "Измеренный период"))
        self.label_8.setText(_translate("MainWindow", "Результат"))
        self.expected_period_brs.setText("100.000 мс.")
        self.expected_trig_brs.setText("4.000 мс.")
        self.label_7.setText(_translate("MainWindow", "Принятые CAN-сообщения"))
        self.label_9.setText(_translate("MainWindow", "Ожидаемый период"))
        self.start_trig_btn.setText(_translate("MainWindow", "Старт"))
        self.measured_trig_lbl.setText(_translate("MainWindow", "Измеренный период"))
        self.result_trig_lbl.setText(_translate("MainWindow", "Результат"))
        self.accepted_trig_lbl.setText(_translate("MainWindow", "Принятые CAN-сообщения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.can_tab),
                                  _translate("MainWindow", "Проверка периода CAN"))
        self.SET_WM_BTN.setText(_translate("MainWindow", "Перевести в working mode"))
        self.READ_VERSBTN.setText(_translate("MainWindow", "Прочитать текущую версию"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры испытания"))
        self.groupBox11.setTitle(_translate("MainWindow", "Ход чтения"))
        self.groupBox_243.setTitle(_translate("MainWindow", "Считанные данные"))
        self.groupBoxSEL.setTitle(_translate("MainWindow", "Выбор источника данных ускорений"))
        self.stat_snap.setText(_translate("MainWindow", "Cтатус ошибки"))
        self.speed_snap.setText(_translate("MainWindow", "Скорость"))
        self.errctr_snpa.setText(_translate("MainWindow", "Значение DTC occurence counter"))
        self.lifetime_snap.setText(_translate("MainWindow", "Значение lifetime timer"))
        self.probeg_snap.setText(_translate("MainWindow", "Пробег"))
        self.SNAP_GROUP.setTitle(_translate("MainWindow", "Выбор snapshot"))
        self.read_snap_btn.setText(_translate("MainWindow", "Прочитать Snapshot"))
        self.snap_sel_1_lbl.setText(_translate("MainWindow", "Блок"))
        self.snap_sel_2_lbl.setText(_translate("MainWindow", "Ошибка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SNAPSHOT_TAB),
                                  _translate("MainWindow", "Проверка чтения snapshot"))
        self.read_params_btn.setText("Прочитать текущие параметры")
        #self.AIRBAG_OFF_btn.setText(_translate("MainWindow", "Отключить ПБ переднего пассажира"))
        self.acc_selector_lbl.setText(_translate("MainWindow", "Выбор набора ускорений"))
        self.start_acc_btn.setText(_translate("MainWindow", "Старт"))
        self.expected_res_acc_lbl.setText(_translate("MainWindow", "Ожидаемый результат"))
        self.got_res_acc_lbl.setText(_translate("MainWindow", "Полученный результат"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Проверка срабатывания системы"))
        self.UDS_MSG_LBL.setText(_translate("MainWindow", "Ход проверки"))
        self.UDS_RUN_BTN.setText(_translate("MainWindow", "Старт"))
        self.UDS_TEST_LBL.setText(_translate("MainWindow", "Запускаемый тест"))
        self.EXP_UDS_LBL.setText(_translate("MainWindow", "Ожидаемый ход проверки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Проверка системы UDS"))
        self.start_SBR_btn.setText(_translate("MainWindow", "Старт"))
        self.SBR_test_selector.setItemText(0, _translate("MainWindow",
                                                         "Проверка корректности передачи состояний РБ по CAN шине"))
        self.SBR_test_selector.setItemText(1, _translate("MainWindow",
                                                         "Проверка активации системы при включении зажигания"))
        self.SBR_test_selector.setItemText(2, _translate("MainWindow",
                                                         "Проверка включения 1 уровня тревоги seat belt reminder"))
        self.SBR_test_selector.setItemText(3, _translate("MainWindow",
                                                         "Проверка включения 2 уровня тревоги seat belt reminder"))
        self.SBR_test_selector.setItemText(4, _translate("MainWindow",
                                                         "Проверка отключения сообщения о тревоге по таймауту"))
        self.SBR_test_selector.setItemText(5, _translate("MainWindow", "Проверка обнуления таймаута"))
        self.SBR_test_selector.setItemText(6,_translate("MainWindow", "Проверка отключения тревоги при открытии дверей"))
        self.SBR_test_selector.setItemText(7,
                                           _translate("MainWindow", "Проверка отключения тревоги при заднем ходе"))
        self.SBR_test_selector.setItemText(8,
                                           _translate("MainWindow", "Проверка ДНП переднего пассажира"))

        self.sbr_test_sel_lbl.setText(_translate("MainWindow", "Запускаемый тест"))
        self.exp_res_SBR_lbl.setText(_translate("MainWindow", "Ожидаемый результат"))
        self.got_res_SBR_lbl.setText(_translate("MainWindow", "Полученный результат"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Параметры"))
        self.Seatbelt_selector.setItemText(0, _translate("MainWindow", "Водитель"))
        self.Seatbelt_selector.setItemText(1, _translate("MainWindow", "Передний пассажир"))
        self.Seatbelt_selector.setItemText(3, _translate("MainWindow", "Центральный Задний пассажир"))
        self.Seatbelt_selector.setItemText(2, _translate("MainWindow", "Правый задний пассажир"))
        self.Seatbelt_selector.setItemText(4, _translate("MainWindow", "Левый задний пассажир"))
       # self.PARAM_RESULT_LBL.setText(_translate("MainWindow", "Результат"))
        self.SB_select_lbl.setText(_translate("MainWindow", "Селектор ремня безопасности"))
        self.CHECK_PARAM_VALID_BTN.setText(_translate("MainWindow", "Проверить валидность параметров"))
        self.accepted_SBR_title.setText(_translate("MainWindow", "Ход проверки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Проверка SBR"))
        self.DIAG_READ_0x09_BTN.setText(_translate("MainWindow", "Считать DTC 0x09"))
        self.DIAG_CLEAR_DTC_BTN.setText(_translate("MainWindow", "Очистить DTC"))
        self.DIAG_ERRORS_LBL.setText(_translate("MainWindow", "Считанные ошибки"))
        self.DIAG_READ_0x08_BTN.setText(_translate("MainWindow", "Считать DTC 0x08"))
        self.DIAG_RESET_BTN.setText(_translate("MainWindow", "Перезапустить БУ СНПБ"))
        self.DIAG_VIN0_BTN.setText(_translate("MainWindow", "Записать VIN≠0"))
        self.DIAG_VIN1_BTN.setText(_translate("MainWindow", "Записать VIN=0"))
        self.DIAG_UPD_CAN_MSG_BTN.setText(_translate("MainWindow", "Обновить данные"))
        self.DIAG_CAN_MSG_LBL.setText(_translate("MainWindow", "Отправляемые сообщения"))
        self.DIAG_DIAGENABLE_SELECTOR.setItemText(0, _translate("MainWindow", "0 (only faults reports and alerts that must remain active during cranking or sleeping periods are enabled)"))
        self.DIAG_DIAGENABLE_SELECTOR.setItemText(1, _translate("MainWindow", "1 (all faults reports and alerts not related to APC power level are enabled)"))
        self.DIAG_DIAGENABLE_SELECTOR.setItemText(2, _translate("MainWindow", "2 (all faults reports and alerts are enabled)"))
        self.DIAG_DIAGENABLE_SELECTOR.setItemText(3, _translate("MainWindow", "3 (unavalible)"))
        self.DIAG_SPEED_SELECTOR_2.setText(_translate("MainWindow", "Отправляемая скорость"))
        self.CHECK_CRASH_DETECTION_BTN.setText("Проверить CrashDetectionOutOfOrder")
        self.DIAG_DIAGENABLE_SELECTOR_2.setText(_translate("MainWindow", "Сигнал GenericApplicativeDiagEnable"))
        self.label_2.setText(_translate("MainWindow", "Принятые сообщения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Проверка самодиагностки"))
        self.label_3.setText(_translate("MainWindow", "Измерение периода CAN-сообщения 0x023"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EDR_tab), _translate("MainWindow", "Проверка чтения EDR"))
        self.COM_PORT_CONNECT_BTN.setText(_translate("MainWindow", "Подключиться"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Настройки"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Precrash data"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Other data"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Crash data"))
        self.pushButton_3.setText("Начать перепрошивку")
        self.LimitSresside_lbl.setText(_translate("MainWindow", "Limit Sres side (10\u207b\u2076 m)"))
        self.LimitAresfront_lbl.setText(_translate("MainWindow", "Limit Ares front (10\u207b\u00b9 m/s\u00B2)"))
        self.LimitSxSyfront_lbl.setText(_translate("MainWindow", "Limit Sx,Sy front (10\u207b\u2076 m)"))
        self.Time_to_stop_calc_lbl.setText(_translate("MainWindow", "Time to stop calculation (ms)"))
        self.Tcalc_lbl.setText(_translate("MainWindow", "T calc front (ms)"))
        self.Tcalc2_lbl.setText(_translate("MainWindow", "T calc side (ms)"))
        self.Sresimpactside_lbl.setText(_translate("MainWindow", "Sres impact side (10\u207b\u2076 m)"))
        self.groupBox143.setTitle(_translate("MainWindow", "Работа с БУ СНПБ"))
        self.groupBox_2666.setTitle(_translate("MainWindow", "Проверка модели"))
        self.LimitAresside_lbl.setText(_translate("MainWindow", "Limit Ares side (10\u207b\u00b9 m/s\u00B2)"))
        self.Sresimpactfront_lbl.setText(_translate("MainWindow", "Sres impact front (10\u207b\u2076 m)"))
        self.LOGS_LBL.setText(_translate("MainWindow", "Логи"))
        self.LimitSresfront_lbl.setText(_translate("MainWindow", "Limit Sres front"))
        self.save_params_btn.setText(_translate("MainWindow", "Сохранить набор"))
        self.read_params_btn.setText(_translate("MainWindow", "Считать текущие параметры БУ"))
        self.UPDATE_PARAMS_BTN.setText(_translate("MainWindow", "Загрузить параметры в БУ"))
        self.UPDATE_PARAMS_LOCAL_BTN.setText(_translate("MainWindow", "Обновить параметры локальной модели"))
        self.read_params_local_btn.setText(_translate("MainWindow", "Считать параметры локальной модели"))
        self.groupBox143.setTitle(_translate("MainWindow", "Проверка модели"))
        self.export_results_btn.setText(_translate("MainWindow", "Открыть файл с результатами"))
        self.run_single_test_btn.setText(_translate("MainWindow", "Запустить тест"))
        self.CHECK_PARAM_VALID_BTN.setText(_translate("MainWindow", "Запуск всех тестов из папки"))
        self.groupBox_2666.setTitle(_translate("MainWindow", "Синтез данных"))
        self.tendmin_lbl.setText(_translate("MainWindow",
                                            "<html><head/><body><p>t end <span style=\" vertical-align:sub;\">min</span>(ms)</p></body></html>"))
        self.tstmax_lbl.setText(_translate("MainWindow", "t start ₘₐₓ (ms) "))
        self.t2_lbl.setText(_translate("MainWindow", "t₂ (ms)"))
        self.tstmin_lbl.setText(_translate("MainWindow","<html><head/><body><p>t start <span style=\" vertical-align:sub;\">min </span>(ms)</p></body></html> "))
        self.aresrange_lbl.setText(_translate("MainWindow","<html><head/><body><p>A<span style=\" vertical-align:sub;\">res</span> range (g)</p></body></html>"))
        self.limitares_lbl.setText(_translate("MainWindow","<html><head/><body><p>Limit A<span style=\" vertical-align:sub;\">res</span>(g)</p></body></html>"))
        self.tendmax_lbl.setText(_translate("MainWindow", "t end ₘₐₓ (ms)"))
        self.t3_lbl.setText(_translate("MainWindow", "t₃ (ms)"))
        self.t4_lbl.setText(_translate("MainWindow", "t₄ (ms)"))
        self.t1_lbl.setText(_translate("MainWindow", "t₁ (ms)"))
        self.sideinput.setItemText(0, _translate("MainWindow", "front"))
        self.sideinput.setItemText(1, _translate("MainWindow", "left"))
        self.sideinput.setItemText(2, _translate("MainWindow", "right"))
        self.sideinput.setItemText(3, _translate("MainWindow", "rear"))
        self.timestep_lbl.setText(_translate("MainWindow", "Time step (ms)"))
        self.timebeforecoll_lbl.setText(_translate("MainWindow", "Time before collision (ms)"))
        self.collside_lbl.setText(_translate("MainWindow", "Collision side"))
        self.syntez_btn.setText(_translate("MainWindow", "Синтезировать"))
        self.deltaAres_lbl.setText(_translate("MainWindow", "delta Ares (m/s\u00B2)"))
        self.LimitSxSyside_lbl.setText(_translate("MainWindow", "Limit Sx,Sy side (10\u207b\u2076 m)"))
        self.LimitSresfront_lbl.setText(_translate("MainWindow", "Limit Sres front (10\u207b\u2076 m)"))
        self.defined_params_lbl.setText(_translate("MainWindow", "Готовые наборы параметров"))

        self.DIAG_STOP_CAN_MSG_BTN.setText("Остановить отправку")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.params_tab),
                                  _translate("MainWindow", "Изменение параметров модели"))
        self.STOP_BTN_1.setText(_translate("MainWindow", "Стоп"))
        self.STOP_BTN_2.setText(_translate("MainWindow", "Стоп"))
        self.STOP_BTN_3.setText(_translate("MainWindow", "Стоп"))
        self.STOP_BTN_4.setText(_translate("MainWindow", "Стоп"))
        self.STOP_BTN_5.setText(_translate("MainWindow", "Стоп"))
        self.STOP_BTN_6.setText(_translate("MainWindow", "Стоп"))
        self.EDR_STOP_BTN.setText(_translate("MainWindow", "Стоп"))
        self.STOP_BTN_8.setText(_translate("MainWindow", "Стоп"))
        self.defined_params_selector.addItem("Пользовательские параметры")
        os.chdir('parameters')
        for file in os.listdir():
            if(file.endswith('.txt')):
                self.defined_params_selector.addItem(file.replace('.txt',''))
        os.chdir('..')
        self.acu_gb.setTitle(_translate("MainWindow", "ACU configuration"))
        self.RLSB_EN.setText(_translate("MainWindow", "Rear left SB"))
        self.RCSB_EN.setText(_translate("MainWindow", "Rear center SB"))
        self.RRSB_EN.setText(_translate("MainWindow", "Rear right SB"))
        self.PADI_EN.setText(_translate("MainWindow", "PADI"))
        self.PSAB_EN.setText(_translate("MainWindow", "Passenger side AB"))
        self.DSAB_EN.setText(_translate("MainWindow", "Driver side AB"))
        self.DSB_EN.setText(_translate("MainWindow", "Driver SB"))
        self.PSB_EN.setText(_translate("MainWindow", "Passenger SB"))
        self.PPS_EN.setText(_translate("MainWindow", "Presence sensor"))
        self.DAB_EN.setText(_translate("MainWindow", "Driver AB"))
        self.PADS_EN.setText(_translate("MainWindow", "PADS"))
        self.DPT_EN.setText(_translate("MainWindow", "Driver Pretensioner"))
        self.LCAB_EN.setText(_translate("MainWindow", "Left curtain AB"))
        self.PPT_EN.setText(_translate("MainWindow", "Passenger pretensioner"))
        self.PAB_EN.setText(_translate("MainWindow", "Passenger AB"))
        self.RCAB_EN.setText(_translate("MainWindow", "Right curtain AB"))
        self.PGSAT_EN.setText(_translate("MainWindow", "Passenger front crash sensor"))
        self.DGSAT_EN.setText(_translate("MainWindow", "Driver front crash sensor"))
        self.PPSAT_EN.setText(_translate("MainWindow", "Passenger DPS"))
        self.DPSAT_EN.setText(_translate("MainWindow", "Driver DPS"))
        self.WRITE_ACU_BTN.setText(_translate("MainWindow", "Запись ACU configuration"))
        self.Manufacture_mode_btn.setText(_translate("MainWindow", "Сброс к заводским настройкам"))
        item = self.Crash_data_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", " "))
        item = self.Crash_data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time,ms"))
        item = self.Crash_data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Long dV"))
        item = self.Crash_data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lateral dV"))
        item = self.Precrash_data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time,S"))
        item = self.Precrash_data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vehicle Speed"))
        item = self.Precrash_data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Brake On/Off"))
        item = self.Precrash_data_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Engine RPM"))
        item = self.Precrash_data_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ABS Activity"))
        item = self.Precrash_data_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Stability control"))
        item = self.Precrash_data_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Steering Angle"))
        item = self.Precrash_data_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Yaw Rate"))
        item = self.Precrash_data_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Traction Control Status"))
        item = self.Precrash_data_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Cruise Control System"))
        item = self.Precrash_data_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Long acc,g"))
        item = self.Precrash_data_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Lateral acc,g"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Отслеживание сигнала CrashDetected"))
        self.groupBox1565.setTitle(_translate("MainWindow", "Конфигурация БУ СНПБ"))
        self.STO_VER_BTN.setText(_translate("MainWindow", "СТО"))
        self.ACC_VER_BTN.setText(_translate("MainWindow", "Внутренний акселерометр"))
        self.groupBox_23456789.setTitle(_translate("MainWindow", "Перепрошивка БУ СНПБ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reprogramming_tab), _translate("MainWindow", "Перепрошивка БУ СНПБ"))
        self.EXP_UDS_BRS.setText("Отправлено: 02 11 01\nПринято: 02 51 01\nДиагностический светодиод моргает")
        self.exp_res_SBR_brs.setText(
            "При пристёгнутом ремне соответствующий сигнал SafetyBeltState равен 0х02 (SB fastened) \nПри непристёгнутом ремне соответствующий сигнал SafetyBeltState равен 0х01 (SB unfastened)")
        self.pushButton_3.setEnabled(False)
        self.EDR1_BTN.setText(_translate("MainWindow", "EDR0"))
        self.EDR3_BTN.setText(_translate("MainWindow", "EDR2"))
        self.EDR2_BTN.setText(_translate("MainWindow", "EDR1"))
        self.READ_NUM_BTN.setText(_translate("MainWindow", "Прочитать текущий номер EDR"))
    def acc_set_changed(self):
        match (self.acc_selector.currentText()):
            case 'Front_100_50':
                self.exp_res_acc_brs.setText("TTF DriverAirbag=12 мс\nTTF PassengerAirbag=12 мс\nTTF DriverPretensioner=10 мс\nTTF PassengerPretensioner=10 мс\nTTF DriverSideAirbag=0 мс\nTTF PassengerSideAirbag=0 мс\nTTF DriverCurtainAirbag=0 мс\nTTF PassengerCurtainAirbag=0 мс\n")
            case 'Front_ARCAP':
                self.exp_res_acc_brs.setText("TTF DriverAirbag=35 мс\nTTF PassengerAirbag=30 мс\nTTF DriverPretensioner=20 мс\nTTF PassengerPretensioner=20 мс\nTTF DriverSideAirbag=0 мс\nTTF PassengerSideAirbag=0 мс\nTTF DriverCurtainAirbag=0 мс\nTTF PassengerCurtainAirbag=0 мс\n")
            case 'Front_R94':
                self.exp_res_acc_brs.setText( "TTF DriverAirbag=35 мс\nTTF PassengerAirbag=30 мс\nTTF DriverPretensioner=20 мс\nTTF PassengerPretensioner=20 мс\nTTF DriverSideAirbag=0 мс\nTTF PassengerSideAirbag=0 мс\nTTF DriverCurtainAirbag=0 мс\nTTF PassengerCurtainAirbag=0 мс\n")
            case 'Front_15kmh40' | 'Side_15kmh_100' | 'Rear_36':
                self.exp_res_acc_brs.setText("СНБП не срабатывает")
            case 'Side_R95':
                self.exp_res_acc_brs.setText("TTF DriverAirbag=0 мс\nTTF PassengerAirbag=0 мс\nTTF DriverPretensioner=7 мс\nTTF PassengerPretensioner=7 мс\nTTF DriverSideAirbag=7 мс\nTTF PassengerSideAirbag=7 мс\nTTF DriverCurtainAirbag=7 мс\nTTF PassengerCurtainAirbag=7 мс\n")
            case 'Side_25kmh_100':
                self.exp_res_acc_brs.setText("TTF DriverAirbag=0 мс\nTTF PassengerAirbag=0 мс\nTTF DriverPretensioner=22 мс\nTTF PassengerPretensioner=22 мс\nTTF DriverSideAirbag=22 мс\nTTF PassengerSideAirbag=22 мс\nTTF DriverCurtainAirbag=22 мс\nTTF PassengerCurtainAirbag=22 мс\n")
            case _:
                self.exp_res_acc_brs.setText("Unknown TTF")

    def NRC_CHANGED(self):
        match self.UDS_TEST_SELECTOR.currentIndex():
            case 0:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 11 01\nПринято: 02 51 01\nДиагностический светодиод моргает")
                    case 1:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 11 06\nПринято:03 7F 11 12\n")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 01 11\nПринято:03 7F 11 13\n")
            case 1:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.UDS_LED_SELECTOR.setDisabled(0)
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в SecurityAccess\nОтправлено: 05 2F 38 01 03 00\nПринято: 05 6F 38 01 03 xx, где хх-последнее состояние диагностического светодиода\nДиагностический светодиод загорелся")
                    case 1:
                        self.UDS_LED_SELECTOR.setDisabled(1)
                        self.EXP_UDS_BRS.setText("Отправлено: 03 2F 38 01 \nПринято: 03 7F 2F 13")
                    case 2:
                        self.UDS_LED_SELECTOR.setDisabled(1)
                        self.EXP_UDS_BRS.setText("Отправлено: 05 2F 38 01 03 00\nПринято: 03 7F 2F 22\n")
                    case 3:
                        self.UDS_LED_SELECTOR.setDisabled(1)
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в SecurityAccess\nОтправлено: 05 2F 38 01 03 08\nПринято: 03 7F 2F 31")
                    case 4:
                        self.UDS_LED_SELECTOR.setDisabled(1)
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в диагностическую сессию\nОтправлено: 05 2F 38 01 03 00\nПринято: 03 7F 2F 33")
            case 2:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 3E 00\nПринято: 02 7E 00")
                    case 1:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 3E 01 \nПринято: 03 7F 3E 12")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 01 3E \nПринято: 03 7F 3E 13")
            case 3:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в диагностическую сессию\nОтправлено: 03 28 01 01\nПринято: 02 68 01\nСообщения по CAN не принимаются\nОтправлено: 03 28 00 01\nПринято: 02 68 00\nСообщения по CAN принимаются")
                    case 1:
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в диагностическую сессию\nОтправлено: 03 28 04 01\nПринято: 03 7F 28 12")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 28 01 \nПринято: 03 7F 28 13")
                    case 3:
                        self.EXP_UDS_BRS.setText("Отправлено: 03 28 01 01\nПринято: 03 7F 28 22")
                    case 4:
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в диагностическую сессию\nОтправлено: 03 28 01 04 \nПринято: 03 7F 28 31")
            case 5:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("Коды ошибок стёрлись")
                    case 1:
                        self.EXP_UDS_BRS.setText("Отправлено: 03 14 FF FF\nПринято: 03 7F 14 13")
                    #case 2:
                        #self.EXP_UDS_BRS.setText("Отправлено: 02 28 01 \nПринято: 03 7F 28 13")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 04 14 00 00 00\nПринято: 03 7F 14 31")
            case 6:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("На экране появились все поддерживаемы DTC и их состояния")
                    case 1:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 19 0F \nПринято: 03 7F 19 12")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 01 19 \nПринято: 03 7F 19 13")
                    case 3:
                        self.EXP_UDS_BRS.setText("Отправлено: 03 19 01 10\nПринято: 03 7F 19 31")
            case 8:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в SecurityAccess")
                    case 1:
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в диагностическую сессию\nОтправлено: 03 27 05 00 \nПринято: 03 7F 27 12")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 01 27 01 00 \nПринято: 03 7F 27 13")
                    case 3:
                        self.EXP_UDS_BRS.setText("Отправлено: 03 27 01 00\nПринято: 03 7F 27 22")
                    case 4:
                        self.EXP_UDS_BRS.setText("1)В ответ на отправку неверного ключа принято: 03 7F 27 35\n2)После двух неудачных попыток входа в Security access в ответ на третью неудачную попытку принято: 03 7F 27 36\n3)При попытке запросить ключ в четвертый раз принято: 03 7F 27 37")
                    case 5:
                        self.EXP_UDS_BRS.setText("Блок успешно вошёл в диагностическую сессию\nОтправлено: 06 27 02 00 00 00 00\nПринято: 03 7f 27 24")
            case 9:
                match self.UDS_NRC_SELECTOR.currentIndex():
                    case 0:
                        self.EXP_UDS_BRS.setText("При чтении DID последний байт ответа 0хА5\nВизуально убедиться, что диагностический светодиод не моргает")
                    case 1:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 22 d1\nПринято: 03 7F 22 13")
                    case 2:
                        self.EXP_UDS_BRS.setText("Отправлено: 03 22 FF FF\nПринято: 03 7F 22 31")
                    case 3:
                        self.EXP_UDS_BRS.setText("Отправлено: 02 2E D1\nПринято: 03 7F 22 13")
                    case 4:
                        self.EXP_UDS_BRS.setText("Отправлено: 04 2E D1 FF FF\nПринято: 03 7F 22 31")
                    case 5:
                        self.EXP_UDS_BRS.setText("Отправлено: 04 2E D1 00 5A\nПринято: 03 7F 2E 33")

    def testfolder_changed(self):
        self.tests_dict.clear()
        self.model_test_selector2.clear()
        os.chdir('pillows/test_folder')
        os.chdir(f'{self.model_test_selector.currentText()}')
        folder=os.listdir()
        for dirs in folder:
            if dirs.startswith("~$"):
                continue
            if dirs.endswith('.csv'):
                self.model_test_selector2.addItem(dirs)
        for i in range(0, len(folder)):
            self.tests_dict.update({folder[i]: i + 1})
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')


    def UDS_test_changed(self):
        if self.UDS_TEST_SELECTOR.currentIndex() == 0:
            self.EXP_UDS_BRS.setText("Отправлено: 02 11 01\nПринято: 02 51 01\nДиагностический светодиод моргает")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("0x12-Subfunction not supported")
            self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
        elif self.UDS_TEST_SELECTOR.currentIndex() == 1:
            self.EXP_UDS_BRS.setText("Блок успешно вошёл в SecurityAccess\nОтправлено: 05 2F 38 01 03 00\nПринято: 05 6F 38 01 03 xx, где хх-последнее состояние диагностического светодиода\nДиагностический светодиод загорелся")
            self.UDS_LED_SELECTOR.setDisabled(False)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_LED_SELECTOR.addItem("Включение диагностического светодиода")
            self.UDS_LED_SELECTOR.addItem("Отключение диагностического светодиода")
            self.UDS_LED_SELECTOR.addItem("Включение светодиода отключения ПБ")
            self.UDS_LED_SELECTOR.addItem("Отключение светодиода отключения ПБ")
            self.UDS_LED_SELECTOR.addItem("Проверка subfunction Return control to ECU")
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
            self.UDS_NRC_SELECTOR.addItem("0x22-Conditions not correct")
            self.UDS_NRC_SELECTOR.addItem("0x31-Request out of range")
            self.UDS_NRC_SELECTOR.addItem("0x33-Security access denied")
        elif self.UDS_TEST_SELECTOR.currentIndex() == 2:
            self.EXP_UDS_BRS.setText("Отправлено: 02 3E 00\nПринято: 02 7E 00")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("0x12-Subfunction not supported")
            self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
        elif self.UDS_TEST_SELECTOR.currentIndex() == 3:
            self.EXP_UDS_BRS.setText("Отправлено: 03 28 01 01\nПринято: 02 68 01\nСообщения по CAN не принимаются\nОтправлено: 03 28 00 01\nПринято: 02 68 00\nСообщения по CAN принимаются")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("0x12-Subfunction not supported")
            self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
            self.UDS_NRC_SELECTOR.addItem("0x22-Conditions not correct")
            self.UDS_NRC_SELECTOR.addItem("0x31-Request out of range")
        elif self.UDS_TEST_SELECTOR.currentIndex() == 4:
            self.EXP_UDS_BRS.setText("Отправлено: 03 28 03 03\nПринято: 02 68 03\nСообщения по CAN не принимаются и не передаются")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(False)
        elif self.UDS_TEST_SELECTOR.currentIndex() == 5:
            self.EXP_UDS_BRS.setText("Коды ошибок стёрлись")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
            #self.UDS_NRC_SELECTOR.addItem("0x22-Conditions not correct")
            self.UDS_NRC_SELECTOR.addItem("0x31-Request out of range")
        elif self.UDS_TEST_SELECTOR.currentIndex() == 6:
            self.EXP_UDS_BRS.setText("На экране появились все поддерживаемые DTC и их состояния")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("0x12-Subfunction not supported")
            self.UDS_NRC_SELECTOR.addItem("0x13-Invalid message length/format")
            self.UDS_NRC_SELECTOR.addItem("0x31-Request out of range")
        elif self.UDS_TEST_SELECTOR.currentIndex() == 7:
            self.EXP_UDS_BRS.setText("После отключения самодиагностики не считан DTC 0xc14087(Lost communication with uBCM)\nПосле включения самодиагностики считан DTC 0xc14087(Lost communication with uBCM)")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setDisabled(True)
            self.UDS_NRC_SELECTOR.clear()
        elif self.UDS_TEST_SELECTOR.currentIndex() == 8:
            self.EXP_UDS_BRS.setText("Блок успешно вошёл в security access")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("Request seed: 0x12-Subfunction not supported")
            self.UDS_NRC_SELECTOR.addItem("Request seed: 0x13-Invalid message length/format")
            self.UDS_NRC_SELECTOR.addItem("Request seed: 0x22-Conditions not correct")
            self.UDS_NRC_SELECTOR.addItem("Request seed: 0x37-Required time delay has not expired + Send key: 0x35-Invalid Key + Send key: 0x36-Exceed number of attempts")
            self.UDS_NRC_SELECTOR.addItem("Send key: 0x24-Request sequence error")


        elif self.UDS_TEST_SELECTOR.currentIndex() == 9:
            self.EXP_UDS_BRS.setText("При чтении DID последний байт ответа 0хА5\nВизуально убедиться, что диагностический светодиод не моргает")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_LED_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.setEnabled(True)
            self.UDS_NRC_SELECTOR.clear()
            self.UDS_NRC_SELECTOR.addItem("No NRC")
            self.UDS_NRC_SELECTOR.addItem("Read Data: 0x13-Invalid message length/format")
            self.UDS_NRC_SELECTOR.addItem("Read Data: 0x31-Request out of range")
            self.UDS_NRC_SELECTOR.addItem("Write Data: 0x13-Invalid message length/format")
            self.UDS_NRC_SELECTOR.addItem("Write Data: 0x31-Request out of range")
            self.UDS_NRC_SELECTOR.addItem("Write Data: 0x33-Security access denied")

        elif self.UDS_TEST_SELECTOR.currentIndex() == 10:
            self.EXP_UDS_BRS.setText("При чтении DID последний байт ответа 0х5A\nВизуально убедиться, что диагностический светодиод моргает с частотой 1Гц")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_NRC_SELECTOR.setEnabled(False)
            self.UDS_NRC_SELECTOR.clear()
        elif self.UDS_TEST_SELECTOR.currentIndex() == 11:
            self.EXP_UDS_BRS.setText("1)При первом чтении DID 0xE180 последний байт в ответе 0хFF\n2)Импульс на пиропатроне водтеля не задетектирован\n3)При чтении DID 0xE180 после перезагрузки последний байт ответа 0хFE\n4)При первом чтениии DID 0xE182 последний байт ответа 0xFF\n5)При чтениии DID 0xE182 после перезагрузки последний байт ответа 0xFE\n6)Состояния ремня безопасности водителя изменилось на not monitored")
            self.UDS_LED_SELECTOR.setDisabled(True)
            self.UDS_NRC_SELECTOR.setEnabled(False)
            self.UDS_NRC_SELECTOR.clear()
        elif self.UDS_TEST_SELECTOR.currentIndex() == 12:
            self.EXP_UDS_BRS.setText("На экране появилось значение, прочитанное с помощью DID")
            self.UDS_LED_SELECTOR.clear()
            self.UDS_LED_SELECTOR.setEnabled(True)
            self.UDS_LED_SELECTOR.addItem("Driver Airbag Resistance")
            self.UDS_LED_SELECTOR.addItem("Passenger Airbag Resistance")
            self.UDS_LED_SELECTOR.addItem("Driver Pretensioner Resistance")
            self.UDS_LED_SELECTOR.addItem("Passenger Pretensioner Resistance")
            self.UDS_LED_SELECTOR.addItem("Driver Side Airbag Resistance")
            self.UDS_LED_SELECTOR.addItem("Passenger Side Airbag Resistance")
            self.UDS_LED_SELECTOR.addItem("Left Curtain Airbag Resistance")
            self.UDS_LED_SELECTOR.addItem("Right Curtain Airbag Resistance")
            self.UDS_LED_SELECTOR.addItem("PAB Deactivation Indicator Status")
            self.UDS_LED_SELECTOR.addItem("PAB Deactivation Indicator switch Resistance")
            self.UDS_LED_SELECTOR.addItem("Vehicle Speed")
            self.UDS_LED_SELECTOR.addItem("Battery Voltage")
            self.UDS_LED_SELECTOR.addItem("ECU`s Lifetime timer")
            self.UDS_LED_SELECTOR.addItem("Passenger Presence Sensor Resistance")
            self.UDS_LED_SELECTOR.addItem("SRS Warning Lamp")
            self.UDS_LED_SELECTOR.addItem("Mileage")
            self.UDS_LED_SELECTOR.addItem("ECU`s Key-on timer")
            self.UDS_LED_SELECTOR.addItem("Occupant Input")
            self.UDS_LED_SELECTOR.addItem("ECU Operating State")
            self.UDS_LED_SELECTOR.addItem("ACU configuration 1")
            self.UDS_LED_SELECTOR.addItem("ACU configuration 2")
            self.UDS_LED_SELECTOR.addItem("ACU configuration 3")
            self.UDS_NRC_SELECTOR.setEnabled(False)
            self.UDS_NRC_SELECTOR.clear()

    def XGF_or_XGE(self):
        os.chdir('parameters')
        file=open(self.defined_params_selector.currentText()+'.txt','r')
       # print(file.read())

        line = (file.readline())
        #print(line)
        line=line.split('=')
        #print(float(line[1]))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        #print(float(line[1]))

        line = (file.readline())
        #print(line)
        line = line.split('=')
        self.LimitAresfront_input.setValue(int(float(line[1])*10))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        self.LimitSxSyfront_input.setValue(int(float(line[1])*10e5))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        self.LimitSresfront_input.setValue(int(float(line[1])*10e5))

        line = (file.readline())
       # print(line)
        line=line.split('=')
        self.deltaAres_input.setValue(int(float(line[1])))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        self.LimitAresside_input.setValue(int(float(line[1])*10))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        self.LimitSxSyside_input.setValue(int(float(line[1])*10e5))

        line = (file.readline())
       # print(line)
        line=line.split('=')
        self.LimitSresside_input.setValue(int(float(line[1])*10e5))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        self.Tcalc_input.setValue(int(float(line[1])))

        line = (file.readline())
       # print(line)
        line=line.split('=')
        self.Tcalc2_input.setValue(int(float(line[1])))

        line = (file.readline())
        #print(line)
        line=line.split('=')
        self.Timetostopcalc_input.setValue(int(float(line[1])))

        line = (file.readline())
        #print(line)
        line = line.split('=')
        self.Sresimpactfront_input.setValue(int(float(line[1])*10e5))

        line = (file.readline())
        #print(line)
        line = line.split('=')
        self.Sresimpact_side_input.setValue(int(float(line[1])*10e5))

        os.chdir('..')


    def UDS_LED_changed(self):
        match (self.UDS_TEST_SELECTOR.currentIndex()):
            case 1:
                if self.UDS_LED_SELECTOR.currentIndex() == 0:
                    self.EXP_UDS_BRS.setText("Отправлено: 05 2F 38 01 03 00\nПринято: 05 6F 38 01 03 xx, где хх-последнее состояние диагностического светодиода\nДиагностический светодиод загорелся")
                elif self.UDS_LED_SELECTOR.currentIndex() == 1:
                    self.EXP_UDS_BRS.setText("Отправлено: 05 2F 38 01 03 01\nПринято: 05 6F 38 01 03 xx, где хх-последнее состояние диагностического светодиода\nДиагностический светодиод погас")
                elif self.UDS_LED_SELECTOR.currentIndex() == 2:
                    self.EXP_UDS_BRS.setText("Отправлено: 05 2F 38 02 03 00\nПринято: 05 6F 38 02 03 xx, где хх-последнее состояние диагностического светодиода\nСветодиод отключения ПБ переднего пассажира горит")
                elif self.UDS_LED_SELECTOR.currentIndex() == 3:
                    self.EXP_UDS_BRS.setText("Отправлено: 05 2F 38 02 03 01\nПринято: 05 6F 38 02 03 xx, где хх-последнее состояние диагностического светодиода\nСветодиод отключения ПБ переднего пассажира погас")
                elif self.UDS_LED_SELECTOR.currentIndex() == 4:
                    self.EXP_UDS_BRS.setText("Отправлено:04 2f 38 01 00, \nПринято: 05 6f 38 01 00 xx, где хх-последнее состояние диагностического светодиода\n")
            case 12:
                pass

    def SBR_test_changed(self):
        if self.SBR_test_selector.currentIndex() == 0:
            self.exp_res_SBR_brs.setText("При пристёгнутом ремне соответствующий сигнал SafetyBeltState равен 0х02 (SB fastened) \nПри непристёгнутом ремне соответствующий сигнал SafetyBeltState равен 0х01 (SB unfastened)")
        elif self.SBR_test_selector.currentIndex() == 1:
            self.exp_res_SBR_brs.setText("Соответствующий сигнал SafetyBeltReminder равен 0 (No warning)")
        elif self.SBR_test_selector.currentIndex() == 2:
            self.exp_res_SBR_brs.setText("Соответствующий сигнал SafetyBeltReminder равен 1 (Warning level 1)")
        elif self.SBR_test_selector.currentIndex() == 3:
            self.exp_res_SBR_brs.setText("Соответствующий сигнал SafetyBeltReminder  равен 2 (Warning level 2)")
        elif self.SBR_test_selector.currentIndex() == 4:
            self.exp_res_SBR_brs.setText("Соответствующий сигнал SafetyBeltReminder  равен 0 (No warning)")
        elif self.SBR_test_selector.currentIndex() == 5:
            self.exp_res_SBR_brs.setText(
                "По истечении таймаута SafetyBeltReminder равен 0 (No warning)\nПосле сброса сигнал SafetyBeltReminder  равен 1 (Warning level 1)")
        elif self.SBR_test_selector.currentIndex() == 6:
            self.exp_res_SBR_brs.setText("Cоответствующий cигнал SafetyBeltReminder равен 0 (No warning)")
        elif self.SBR_test_selector.currentIndex() == 7:
            self.exp_res_SBR_brs.setText("При GearLeverPosition drive Сигнал SafetyBeltReminder равен 1\nПри GearLeverPosition reverse Сигнал SafetyBeltReminder равен 0")
        elif self.SBR_test_selector.currentIndex() == 8:
            self.exp_res_SBR_brs.setText("При отсутствии пассажира:PassengerPresenceState: 0x1\nПри наличии пассажира PassengerPresenceState: 0x2")
        elif self.SBR_test_selector.currentIndex() == 9:
            self.exp_res_SBR_brs.setText("При отключенной ПБ сигнал PassengerAIRBAG_Inhibition равен 1\nПри включенной ПБ сигнал PassengerAIRBAG_Inhibition равен 0")
    def snap_changed(self):
        match self.snap_sel_1.currentIndex():
            case 0:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Vehicle Option Fault")
                self.snap_sel_2.addItem("VIN absence")
                self.snap_sel_2.addItem("Internal Module Fault")
                self.snap_sel_2.addItem("WatchDog Continues Fault ")
            case 1:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Crash stored in memory")
                self.snap_sel_2.addItem("Crash recorded in frontal airbag ")
                self.snap_sel_2.addItem("Crash recorded in Driver side airbag ")
                self.snap_sel_2.addItem("Crash recorded in Passenger side airbag ")
                self.snap_sel_2.addItem("Crash recorded in Belt pretensioner")
                self.snap_sel_2.addItem("Crash recorded in Rear")
            case 2:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Vbatt too high")
                self.snap_sel_2.addItem("Vbatt too low")
            case 3:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 4:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 5:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 6:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 7:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 8:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 9:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 10:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Resistance too high")
                self.snap_sel_2.addItem("Resistance too low")
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Short to Vbatt")
            case 11:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Open/Short to Vbatt")
            case 12:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("Short to GND")
                self.snap_sel_2.addItem("Open/Short to Vbatt")
            case 13:
                self.snap_sel_2.clear()
                self.snap_sel_2.addItem("CAN Bus-off")
                self.snap_sel_2.addItem("Lost communication with ABS/ESC (0x5D7)")
                self.snap_sel_2.addItem("Lost communication with uBCM (0x350)")
                self.snap_sel_2.addItem("Lost communication with Cluster (0x4F8)")

    def COM_port_changed(self):
        self.COM_PORT_BRS.clear()
        time.sleep(0.01)
        self.COM_PORT=self.COM_PORT_SELECTOR.currentText()
        try:
            self.UART = serial.Serial(self.COM_PORT, 115200)
            self.UART.close()
        except:
            self.COM_PORT_BRS.append("Выбранный COM-порт занят")

    def ReadDTC(self,status_byte):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x51
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        try:
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            if (len(Result.frame[0].data) < 8):
                self.DIAG_ERRORS_BRS.append("No DTC found")
            else:
                DTC_list = self.parse_UDS_errors(Result, status_byte)
                if (len(DTC_list) == 1 and self.match_DTC(hex(DTC_list[0])) == None or len(DTC_list)==0):
                    self.DIAG_ERRORS_BRS.append("No DTC found")
                for i in range(0,len(DTC_list)):
                    if (self.match_DTC(hex(DTC_list[i])) != None):
                        self.DIAG_ERRORS_BRS.append(f"{str(hex(DTC_list[i]))}:{self.match_DTC(hex(DTC_list[i]))}")
                        time.sleep(0.05)
        except:
            self.DIAG_ERRORS_BRS.append("Возникла ошибка. Попробуйте ещё раз")
        self.UART.close()
        self.EnableAll()

    def run_ReadDTC(self,status_byte):
        Receiver=threading.Thread(target=self.ReadDTC,args=(status_byte,))
        Receiver.start()

    def ClearDTC(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x53
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        bytes_read = self.UART.read(int(received_len, 16))
        try:
            Result.ParseFromString(bytes_read)
            self.DIAG_ACCEPTED_BRS.append("Очистка DTC:")
            time.sleep(0.01)
            self.DIAG_ACCEPTED_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
        except:
            self.DIAG_ACCEPTED_BRS.append("Ошибка очистки DTC. Перезапустите СТО и попробуйте снова")
            time.sleep(0.01)
        self.UART.close()
        self.EnableAll()
    def run_ClearDTC(self):
        Receiver=threading.Thread(target=self.ClearDTC)
        Receiver.start()
    def ECU_reset(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x56
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.DIAG_ACCEPTED_BRS.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len, 16))
            self.UART.close()
            Result.ParseFromString(bytes_read)
            self.DIAG_ACCEPTED_BRS.append("Перезагрузка блока")
            time.sleep(0.05)
            self.DIAG_ACCEPTED_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
        self.UART.close()
        self.EnableAll()
    def run_ECU_reset(self):
        Receiver=threading.Thread(target=self.ECU_reset)
        Receiver.start()

    def Check_CD(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x5B
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.DIAG_ACCEPTED_BRS.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            self.DIAG_ACCEPTED_BRS.append(f"CrashDetectionOutOfOrder:{int(Result.measuredValue[0])}")
        self.UART.close()
        self.EnableAll()
    def run_Check_CD(self):
        Receiver = threading.Thread(target=self.Check_CD)
        Receiver.start()
    def Write_ACU(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        B1=0x80
        B2=0
        B3=0
        if(self.DAB_EN.isChecked()==True):
            B1|=0x01
        if (self.PAB_EN.isChecked() == True):
            B1 |= 0x02
        if (self.DPT_EN.isChecked() == True):
            B1 |= 0x04
        if (self.PPT_EN.isChecked() == True):
            B1 |= 0x08
        if (self.PADI_EN.isChecked() == True):
            B1 |= 0x10
        if (self.PADS_EN.isChecked() == True):
            B1 |= 0x20
        if (self.PPS_EN.isChecked() == True):
            B1 |= 0x40


        if (self.LCAB_EN.isChecked() == True):
            B2 |= 0x01
        if (self.RCAB_EN.isChecked() == True):
            B2 |= 0x02
        if (self.DSAB_EN.isChecked() == True):
            B2 |= 0x04
        if (self.PSAB_EN.isChecked() == True):
            B2 |= 0x08
        if (self.PGSAT_EN.isChecked() == True):
            B2 |= 0x10
        if (self.DGSAT_EN.isChecked() == True):
            B2 |= 0x20
        if (self.PPSAT_EN.isChecked() == True):
            B2 |= 0x40
        if (self.DPSAT_EN.isChecked() == True):
            B2 |= 0x80

        if (self.DSB_EN.isChecked() == True):
            B3 |= 0x01
        if (self.PSB_EN.isChecked() == True):
            B3 |= 0x02
        if (self.RRSB_EN.isChecked() == True):
            B3 |= 0x04
        if (self.RCSB_EN.isChecked() == True):
            B3 |= 0x08
        if (self.RLSB_EN.isChecked() == True):
            B3 |= 0x10
        B3 |= 0x20
        B3 |= 0x40
        B3 |= 0x80

        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x5A
        Command = Command.SerializeToString()
        self.UART.write(Command)
        time.sleep(1)
        cfgbytes=bytearray([B1,B2,B3])
        self.UART.write(cfgbytes)
        try:
            received_len = self.UART.read(2).hex()
            if (received_len == ''):
                self.VER_LOG_BRS.append("Остановлено")
            else:
                bytes_read = self.UART.read(int(received_len, 16))
                Result.ParseFromString(bytes_read)
                self.VER_LOG_BRS.append("ACU configuration записана")
                time.sleep(0.02)
                self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                time.sleep(0.02)
                self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
                time.sleep(0.02)
                self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                time.sleep(0.02)
        except:
            self.VER_LOG_BRS.append("Ошибка записи ACU configuration. Попробуйте ещё раз")
        self.UART.close()
        self.EnableAll()
    def run_Write_ACU(self):
        Receiver=threading.Thread(target=self.Write_ACU)
        Receiver.start()
    def Write_VIN0(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x54
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.DIAG_ACCEPTED_BRS.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            self.DIAG_ACCEPTED_BRS.append(
                f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\nОтправлено:{str(Result.frame[8].data.hex())}\nОтправлено:{str(Result.frame[9].data.hex())}\nПринято:{str(Result.frame[10].data.hex())}")
        self.UART.close()
        self.EnableAll()
    def run_Write_VIN0(self):
        Receiver=threading.Thread(target=self.Write_VIN0)
        Receiver.start()
    def Write_VIN1(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x55
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.DIAG_ACCEPTED_BRS.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len, 16))

            Result.ParseFromString(bytes_read)
            self.DIAG_ACCEPTED_BRS.append(
                f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\nОтправлено:{str(Result.frame[8].data.hex())}\nОтправлено:{str(Result.frame[9].data.hex())}\nПринято:{str(Result.frame[10].data.hex())}")
        self.UART.close()
        self.EnableAll()
    def run_Write_VIN1(self):
        Receiver=threading.Thread(target=self.Write_VIN1)
        Receiver.start()


    def Send_periodic(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x59
        Command.vehicle_speed=self.DIAG_SPEED_SELECTOR.value()
        Command.mileage=self.DIAG_MILEAGE_SELECTOR.value()
        Command.GenDiagEnable=self.DIAG_DIAGENABLE_SELECTOR.currentIndex()
        Command = Command.SerializeToString()
        self.UART.write(Command)
        self.UART.close()

    def Stop_Send_periodic(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x58
        Command = Command.SerializeToString()
        self.UART.write(Command)
        self.UART.close()


    def LOG_print(self,text):
        if(text!=None):
            self.LOG_BRS.append(text)

    def parse_UDS_errors(self,Result,Status_Byte):
        '''----------------Парсинг ошибок 0х09 ----------------------------'''
        DTC_list=[]
        indexes=[]
        tmp=0
        length=len(Result.frame)
        for num in range(0, length):
            for index in range(0, len(Result.frame[num].data)):
                Status_Byte_index = Result.frame[num].data.find(Status_Byte, index)
                if (Status_Byte_index != tmp):
                    indexes.append(Status_Byte_index)
                tmp = Status_Byte_index
            # заполняем массив indexes, который содержит позиции status байта в посылке
            for i in range(0, len(indexes)):
                if (indexes[i] > 3 and indexes[i] != -1):
                    DTC = hex(((Result.frame[num].data[indexes[i] - 3]) << 16) + (
                                (Result.frame[num].data[indexes[i] - 2]) << 8) + (
                              Result.frame[num].data[indexes[i] -1]))

                    DTC_list.append(int(DTC,16))
                elif (indexes[i] == 3 and num>0):
                    DTC = hex(((Result.frame[num-1].data[7]) << 16) + ((Result.frame[num].data[1]) << 8) + (Result.frame[num].data[2]))

                    DTC_list.append(int(DTC,16))
                elif (indexes[i] == 2 and num>0):
                    DTC = hex(((Result.frame[num-1].data[6]) << 16) + ((Result.frame[num-1].data[7]) << 8) + (
                    Result.frame[num].data[1]))

                    DTC_list.append(int(DTC,16))
                elif (indexes[i] == 1 and num>0):#and num!=length-1):  #####
                    DTC = hex(((Result.frame[num-1].data[5]) << 16) + ((Result.frame[num -1].data[6]) << 8) + (Result.frame[num-1].data[7]))

                    DTC_list.append(int(DTC,16))
                '''elif (indexes[i] == 7):
                    DTC = hex(((Result.frame[num + 1].data[1]) << 16) + ((Result.frame[num + 1].data[2]) << 8) + (
                    Result.frame[num + 1].data[3]))
                    DTC_list.append(DTC)'''
            indexes.clear()
        return DTC_list
    def match_DTC(self,dtc):
        match int(dtc,16):
            case int(DTC.Vehicle_option_fault):
                return str("Vehicle option fault")
            case 0x901800:
                return "Vin absence"
            case int(DTC.Internal_mode_fault):
                return "Internal mode fault"
            case int(DTC.WatchDog_Continues_Fault):
                return "WatchDog Continues Fault"
            case int(DTC.Crash_stored_in_memory):
                return "Crash stored in memory"
            case int(DTC.Crash_recorded_in_frontal_airbag_only):
                return "Crash recorded in frontal airbag"
            case int(DTC.Crash_recorded_in_Driver_side_airbag_only):
                return "Crash recorded in Driver side airbag"
            case int(DTC.Crash_recorded_in_Passenger_side_airbag_only):
                return "Crash recorded in Passenger side airbag "
            case int(DTC.Crash_recorded_in_Belt_pretensioner_only):
                return "Crash recorded in Belt pretensioner"
            case int(DTC.Crash_recorded_in_Rear):
                return "Crash recorded in Rear"
            case int(DTC.Vbatt_too_high):
                return "Voltage too high"
            case int(DTC.Vbatt_too_low):
                return "Voltage too low"
            case int(DTC.Front_airbag_driver_resistance_too_high):
                return "Front Airbag Driver resistance too high"
            case int(DTC.Front_airbag_driver_resistance_too_low):
                return "Front Airbag Driver resistance too low"
            case int(DTC.Front_airbag_driver_short_to_GND):
                return "Front Airbag Driver short to GND"
            case int(DTC.Front_airbag_driver_short_to_Vbatt):
                return "Front Airbag Driver short to battery"
            case int(DTC.Front_airbag_passenger_resistance_too_high):
                return "Front Airbag Passenger resistance too high"
            case int(DTC.Front_airbag_passenger_resistance_too_low):
                return "Front Airbag Passenger resistance too low"
            case int(DTC.Front_airbag_passenger_short_to_GND):
                return "Front Airbag Passenger short to GND"
            case int(DTC.Front_airbag_passenger_short_to_Vbatt):
                return "Front Airbag Passenger short to battery"
            case int(DTC.Pretensioner_Driver_resistance_too_high):
                return "Pretensioner driver resistance too high"
            case int(DTC.Pretensioner_Driver_resistance_too_low):
                return "Pretensioner driver resistance too low"
            case int(DTC.Pretensioner_Driver_short_to_GND):
                return "Pretensioner driver short to GND"
            case int(DTC.Pretensioner_Driver_short_to_Vbatt):
                return "Pretensioner driver short to battery"
            case int(DTC.Pretensioner_Passenger_resistance_too_high):
                return "Pretensioner Passenger resistance too high"
            case int(DTC.Pretensioner_Passenger_resistance_too_low):
                return "Pretensioner Passenger resistance too low"
            case int(DTC.Pretensioner_Passenger_short_to_GND):
                return "Pretensioner Passenger short to GND"
            case int(DTC.Pretensioner_Passenger_short_to_Vbatt):
                return "Pretensioner Passenger short to battery"
            case int(DTC.Side_airbag_driver_resistance_too_high):
                return "Side Airbag Driver resistance too high"
            case int(DTC.Side_airbag_driver_resistance_too_low):
                return "Side Airbag Driver resistance too low"
            case int(DTC.Side_airbag_driver_short_to_GND):
                return "Side Airbag Driver short to GND"
            case int(DTC.Side_airbag_driver_short_to_Vbatt):
                return "Side Airbag Driver short to battery"
            case int(DTC.Side_airbag_passenger_resistance_too_high):
                return "Side Airbag Passenger resistance too high"
            case int(DTC.Side_airbag_passenger_resistance_too_low):
                return "Side Airbag Passenger resistance too low"
            case int(DTC.Side_airbag_passenger_short_to_GND):
                return "Side Airbag Passenger short to GND"
            case int(DTC.Side_airbag_passenger_short_to_Vbatt):
                return "Side Airbag Passenger short to battery"
            case int(DTC.Curtain_airbag_driver_resistance_too_high):
                return "Curtain Airbag Driver resistance too high"
            case int(DTC.Curtain_airbag_driver_resistance_too_low):
                return "Curtain Airbag Driver resistance too low"
            case int(DTC.Curtain_airbag_driver_short_to_GND):
                return "Curtain Airbag Driver short to GND"
            case int(DTC.Curtain_airbag_driver_short_to_Vbatt):
                return "Curtain Airbag Driver short to battery"
            case int(DTC.Curtain_airbag_passenger_resistance_too_high):
                return "Curtain Airbag Passenger resistance too high"
            case int(DTC.Curtain_airbag_passenger_resistance_too_low):
                return "Curtain Airbag Passenger resistance too low"
            case int(DTC.Curtain_airbag_passenger_short_to_GND):
                return "Curtain Airbag Passenger short to GND"
            case int(DTC.Curtain_airbag_passenger_short_to_Vbatt):
                return "Curtain Airbag Passenger short to battery"

            case int(DTC.Driver_side_impact_sensor_wrong_characreristics):
                return "Driver SIS – Wrong characteristics"
            case int(DTC.Driver_side_impact_sensor_communication_error):
                return "Driver SIS – Communication error"
            case int(DTC.Driver_side_impact_sensor_short_to_battery):
                return "Driver SIS – Short to battery"
            case int(DTC.Driver_side_impact_sensor_short_to_GND):
                return "Driver SIS – Short to GND"

            case int(DTC.Passenger_side_impact_sensor_wrong_characreristics):
                return "Passenger SIS – Wrong characteristics"
            case int(DTC.Passenger_side_impact_sensor_communication_error):
                return "Passenger SIS – Communication error"
            case int(DTC.Passenger_side_impact_sensor_short_to_battery):
                return "Passenger SIS – Short to battery"
            case int(DTC.Passenger_side_impact_sensor_short_to_GND):
                return "Passenger SIS – Short to GND"

            case int(DTC.Driver_door_pressure_sensor_wrong_characreristics):
                return "Driver DPS – Wrong characteristics"
            case int(DTC.Driver_door_pressure_sensor_communication_error):
                return "Driver DPS – Communication error"
            case int(DTC.Driver_door_pressure_sensor_short_to_battery):
                return "Driver DPS – Short to battery"
            case int(DTC.Driver_door_pressure_sensor_short_to_GND):
                return "Driver DPS – Short to GND"

            case int(DTC.Passenger_door_pressure_sensor_wrong_characreristics):
                return "Passenger DPS – Wrong characteristics"
            case int(DTC.Passenger_door_pressure_sensor_communication_error):
                return "Passenger DPS – Communication error"
            case int(DTC.Passenger_door_pressure_sensor_short_to_battery):
                return "Passenger DPS – Short to battery"
            case int(DTC.Passenger_door_pressure_sensor_short_to_GND):
                return "Passenger DPS – Short to GND"

            case int(DTC.Passenger_Airbag_Cutoff_switch_short_to_Vbatt):
                return "Passenger Airbag Cutoff Switch Open/Short to Vbatt"
            case int(DTC.Passenger_Airbag_Cutoff_switch_short_to_GND):
                return "Passenger Airbag Cutoff Switch Short to GND"

            case int(DTC.Passenger_presence_sensor_short_to_Vbatt):
                return "Passenger Presence Sensor Open/Short to Vbatt"
            case int(DTC.Passenger_presence_sensor_short_to_GND):
                return "Passenger Presence Sensor Short to GND"

            case int(DTC.CAN_Bus_off):
                return "CAN Bus-off"
            case int(DTC.Lost_communication_with_ABS_ESC):
                return "Lost communication with ABS/ESC (0x5D7)"
            case int(DTC.Lost_communication_with_Cluster):
                return "Lost communication with Cluster (0x4F8)"
            case int(DTC.Lost_communication_with_uBCM):
                return "Lost communication with uBCM (0x350)"
    def matchCrashDetected(self,signal):
        if(signal==0):
            return "No crash detected"
        elif(signal==1):
            return "Crash detected"
        else:
            return "Wrong signal"
    def matchACU(self, signal):
        if (signal == 0):
            return "Disabled"
        elif (signal == 1):
            return "Enabled"
        else:
            return "Wrong signal"
    def matchSB(self, signal):
        if (signal == 0):
            return "Unfastened"
        elif (signal == 1):
            return "Fastened"
        else:
            return "Wrong signal"
    def checkTTF(self,expected_ttf,experimental_ttf):
        if(experimental_ttf<expected_ttf+3 and experimental_ttf>expected_ttf-3):
            return 1
        else:
            return 0
    def Test1_handler(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.STOP_BTN_3.setEnabled(True)
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x11
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if(received_len==''):
            self.can_msg_brs.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len,16))
            Result.ParseFromString(bytes_read)
            self.can_msg_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
            time.sleep(0.05)
            self.inittime_brs.append(str(Result.measuredValue[0]/1000))
            time.sleep(0.05)
            if(Result.measuredValue[0]/1000<300):
                self.initresult_brs.append("Success")
            else:
                self.initresult_brs.append("Fail")
        self.UART.close()
        self.EnableAll()
        self.STOP_BTN_3.setEnabled(False)
    def run_test1(self):
        Receiver=threading.Thread(target=self.Test1_handler)
        Receiver.start()
    def ValidAB_handler(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.STOP_BTN_8.setEnabled(True)
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x14
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.VALIDAB_BRS.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len,16))
            Result.ParseFromString(bytes_read)
            self.VALIDAB_BRS.append(f"Timestamp:{str(Result.frame[2].timestamp)}   id:{str(hex(Result.frame[2].id))}   DLC:{str(Result.frame[2].length)}   Data:{str(Result.frame[2].data.hex())}")
            time.sleep(0.05)
            self.VALIDAB_BRS.append(
                f"Timestamp:{str(Result.frame[3].timestamp)}   id:{str(hex(Result.frame[3].id))}   DLC:{str(Result.frame[3].length)}   Data:{str(Result.frame[3].data.hex())}")
            time.sleep(0.05)
            self.VALIDAB_BRS.append("После перезагрузки:")
            time.sleep(0.05)
            if(Result.measuredValue[0]==0):
                self.VALIDAB_BRS.append("No valid airbag information")
            else:
                self.VALIDAB_BRS.append("Valid airbag information")
            time.sleep(0.05)
            self.VALIDAB_BRS.append("Поcле инициализации:")
            time.sleep(0.05)
            if (Result.measuredValue[1] == 0):
                self.VALIDAB_BRS.append("No valid airbag information")
            else:
                self.VALIDAB_BRS.append("Valid airbag information")
        self.UART.close()
        self.EnableAll()
        self.STOP_BTN_8.setEnabled(False)
    def run_ValidAB(self):
        Receiver=threading.Thread(target=self.ValidAB_handler)
        Receiver.start()

    def Test2_handler(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.STOP_BTN_1.setEnabled(True)
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x12
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len=self.UART.read(2).hex()
        if (received_len == ''):
            self.accepted_periodic_brs.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len,16))
            Result.ParseFromString(bytes_read)
            for i in range(0,4):
                self.accepted_periodic_brs.append(f"Timestamp:{str(Result.frame[i].timestamp)}   id:{str(hex(Result.frame[i].id))}   DLC:{str(Result.frame[i].length)}   Data:{str(Result.frame[i].data.hex())}")
                time.sleep(0.01)
            self.measured_period_brs.append(f"{str(Result.measuredValue[0]/1000)} мс.")
            time.sleep(0.02)
            if (Result.measuredValue[0]/1000 < 110 and Result.measuredValue[0]/1000 > 90):
                #self.result_periodic_brs.setStyleSheet("QTextEdit {color:green}")
                self.result_periodic_brs.append("Success")
            else:
                #self.result_periodic_brs.setStyleSheet("QTextEdit {color:red}")
                self.result_periodic_brs.append("Fail")
        self.UART.close()
        self.EnableAll()
        self.STOP_BTN_1.setEnabled(False)

    def run_test2(self):
        Receiver=threading.Thread(target=self.Test2_handler)
        Receiver.start()
    def Test3_period_handler(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.STOP_BTN_2.setEnabled(True)
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x22
        Command.accDataNumber = self.acc_selector.currentIndex() + 1
        #Command.AIRBAG_OFF = self.AIRBAG_OFF_btn.isChecked()
        accX = []
        accY = []
        X_new = []
        Y_new = []
        length = []
        i = 0
        self.accfile = 'FRONT ARCAP.csv'
        os.chdir("acceleration_synthesis")
        os.chdir("Generated_acc")
        with open(self.accfile, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                try:
                    accX.insert(i, int(lines[0].split(';')[0], 16))
                    accY.insert(i, int(lines[0].split(';')[1], 16))
                    i += 1
                except:
                    pass
            accX.pop(0)
            accY.pop(0)
            file.close()
        os.chdir("..")
        os.chdir("..")
        for i in range(0, len(accY)):
            X_new.insert(4 * i, (accX[i] & 0xFF000000) >> 24)
            X_new.insert(4 * i + 1, (accX[i] & 0x00FF0000) >> 16)
            X_new.insert(4 * i + 2, (accX[i] & 0x0000FF00) >> 8)
            X_new.insert(4 * i + 3, accX[i] & 0x000000FF)
            Y_new.insert(4 * i, (accY[i] & 0xFF000000) >> 24)
            Y_new.insert(4 * i + 1, (accY[i] & 0x00FF0000) >> 16)
            Y_new.insert(4 * i + 2, (accY[i] & 0x0000FF00) >> 8)
            Y_new.insert(4 * i + 3, accY[i] & 0x000000FF)
        X_new = bytearray(X_new)
        Y_new = bytearray(Y_new)
        Command.accDataNumber=2
        Command.UDS_NRC=1
        Command = Command.SerializeToString()
        self.UART.write(Command)
        length.insert(0, (len(X_new) >> 8) & 0xff)
        length.insert(1, (len(X_new)) & 0xff)
        length = bytearray(length)
        time.sleep(2)
        self.UART.flushInput()
        self.UART.flushOutput()
        self.UART.write(length)
        bytes_read = self.UART.read(2)
        if (bytes_read == length):
            self.UART.write(X_new)
            time.sleep(0.5)
            time.sleep(0.5)
            self.UART.write(Y_new)
            received_len=self.UART.read(2).hex()
            if (received_len == ''):
                self.accepted_trig_brs.append("Остановлено")
            else:
                bytes_read = self.UART.read(int(received_len,16))
                Result.ParseFromString(bytes_read)
                for i in range(0,4):
                    self.accepted_trig_brs.append(f"Timestamp:{str(Result.frame[i].timestamp)}   id:{str(hex(Result.frame[i].id))}   DLC:{str(Result.frame[i].length)}   Data:{str(Result.frame[i].data.hex())}")
                    time.sleep(0.01)
                self.measured_trig_brs.append(f"{str(Result.measuredValue[0]/1000)} мс.")
                time.sleep(0.01)
                if (Result.measuredValue[0]/1000 < 4.4 and Result.measuredValue[0]/1000 > 3.6):
                    self.result_trig_brs.append("Success")
                else:
                    self.result_trig_brs.append("Fail")
        self.UART.close()
        self.EnableAll()
        self.STOP_BTN_2.setEnabled(False)

    def run_test3_period(self):
        Receiver=threading.Thread(target=self.Test3_period_handler)
        Receiver.start()
    def Accelerometer_handler(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.STOP_BTN_4.setEnabled(True)
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x22
        Command.accDataNumber=self.acc_selector.currentIndex()+1
#        Command.AIRBAG_OFF=self.AIRBAG_OFF_btn.isChecked()
        accX=[]
        accY=[]
        X_new=[]
        Y_new=[]
        length=[]
        i=0
        self.accfile=self.acc_selector.currentText()+'.csv'
        os.chdir("pillows")
        os.chdir("test_folder")
        os.chdir("XGF")
        with open(self.accfile, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                try:
                    accX.insert(i, int(lines[0].split(';')[2], 16))
                    accY.insert(i, int(lines[0].split(';')[3], 16))
                    i += 1
                except:
                    pass
            accX.pop(0)
            accY.pop(0)
            file.close()
        for i in range(0, len(accY)):
            X_new.insert(4*i,(accX[i] & 0xFF000000) >> 24)
            X_new.insert(4*i+1,(accX[i] & 0x00FF0000) >> 16)
            X_new.insert(4*i+2,(accX[i] & 0x0000FF00) >> 8)
            X_new.insert(4*i+3, accX[i] & 0x000000FF)
            Y_new.insert(4*i,(accY[i] & 0xFF000000) >> 24)
            Y_new.insert(4*i+1,(accY[i] & 0x00FF0000) >> 16)
            Y_new.insert(4*i+2,(accY[i] & 0x0000FF00) >> 8)
            Y_new.insert(4*i+3,accY[i] & 0x000000FF)
        X_new = bytearray(X_new)
        Y_new = bytearray(Y_new)
        Cmd = Command.SerializeToString()
        self.UART.write(Cmd)
        length.insert(0,(len(X_new) >> 8) & 0xff)
        length.insert(1,(len(X_new)) & 0xff)
        length = bytearray(length)
        time.sleep(2)
        self.UART.flushInput()
        self.UART.flushOutput()
        self.UART.write(length)
        bytes_read=self.UART.read(2)
        if(bytes_read==length):
            self.UART.write(X_new)
            time.sleep(0.5)
            time.sleep(0.5)
            self.UART.write(Y_new)
            received_len=self.UART.read(2).hex()
            if (received_len == ''):
                self.got_res_brs.append("Остановлено")
            else:
                bytes_read = self.UART.read(int(received_len,16))
                Result.ParseFromString(bytes_read)
                self.CRASHDETECTED_BRS.append(
                    f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                time.sleep(0.02)
                self.CRASHDETECTED_BRS.append(
                    f"Timestamp:{str(Result.frame[1].timestamp)}   id:{str(hex(Result.frame[1].id))}   DLC:{str(Result.frame[1].length)}   Data:{str(Result.frame[1].data.hex())}")
                time.sleep(0.02)
                self.CRASHDETECTED_BRS.append(f"До столкновения:{(Result.frame[0].data[0]&0b10000000)>>7} ({self.matchCrashDetected((Result.frame[0].data[0]&0b10000000)>>7)})\nПосле столкновения:{(Result.frame[1].data[0]&0b10000000)>>7} ({self.matchCrashDetected(int((Result.frame[1].data[0]&0b10000000)>>7))})")
                time.sleep(0.02)

                self.got_res_brs.append(f"TTF DriverAirbag={round(Result.measuredValue[0]/1000,2)} мс\nTTF PassengerAirbag={round(Result.measuredValue[1]/1000,2)} мс\nTTF DriverPretensioner={round(Result.measuredValue[2]/1000,2)} мс\nTTF PassengerPretensioner={round(Result.measuredValue[3]/1000,2)} мс\nTTF DriverSideAirbag={round(Result.measuredValue[4]/1000,2)} мс\nTTF PassengerSideAirbag={round(Result.measuredValue[5]/1000,2)} мс\nTTF DriverCurtainAirbag={round(Result.measuredValue[6]/1000,2)} мс\nTTF PassengerCurtainAirbag={round(Result.measuredValue[7]/1000,2)} мс")
                time.sleep(0.02)
                #if(self.checkTTF(TTF_DAB,Result.measuredValue[0]/1000)==1 and self.checkTTF(TTF_PAB,Result.measuredValue[1]/1000)==1 and self.checkTTF(TTF_DPT,Result.measuredValue[2]/1000)==1 and self.checkTTF(TTF_PPT,Result.measuredValue[3]/1000)==1 and self.checkTTF(TTF_DSAB,Result.measuredValue[4]/1000)==1 and self.checkTTF(TTF_PSAB,Result.measuredValue[5]/1000)==1 and self.checkTTF(TTF_DCAB,Result.measuredValue[6]/1000)==1):
                 #   self.got_res_brs.append("Success")
               # else:
                    #self.got_res_brs.append("Fail")
        self.UART.close()
        self.STOP_BTN_4.setEnabled(False)
        time.sleep(0.1)
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        self.EnableAll()
    def run_accelerometer(self):
        Receiver=threading.Thread(target=self.Accelerometer_handler)
        Receiver.start()
    def UDS_handler(self):
        try:
            try:
                self.UART.open()
            except:
                self.UART.close()
                self.UART.open()
            self.STOP_BTN_6.setEnabled(True)

            Command = Messages.TestData()
            Result = Messages.TestData()
            Command.method = 0
            Command.testNumber = self.UDS_TEST_SELECTOR.currentIndex()+0x31
            if(Command.testNumber==0x32 or Command.testNumber==0x3D):
                Command.UDS_subtest=self.UDS_LED_SELECTOR.currentIndex()+1
            if(self.UDS_NRC_SELECTOR.currentIndex()!=-1):
                Command.UDS_NRC = self.UDS_NRC_SELECTOR.currentIndex()
            Cmd = Command.SerializeToString()
            self.UART.write(Cmd)
            received_len = self.UART.read(2).hex()
            if (received_len == ''):
                self.UDS_MSG_BRS.append("Остановлено")
            else:
                bytes_read = self.UART.read(int(received_len, 16))
                Result.ParseFromString(bytes_read)
                match Result.testNumber:
                    case 0x31:  #ECU reset
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                    case 0x32:  #InputOutputControlByIdentifier
                        match Command.UDS_NRC:
                            case 0:
                                self.UDS_MSG_BRS.append(
                                    f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\nОтправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\nОтправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                                time.sleep(0.02)
                                if (Result.frame[5].data[1] == 0x67 and Result.frame[5].data[2] == 0x02):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в security access")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа в security access")
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}")
                            case 1|2:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                            case 3:
                                self.UDS_MSG_BRS.append( f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\nОтправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\nОтправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                                time.sleep(0.02)
                                if (Result.frame[5].data[1] == 0x67 and Result.frame[5].data[2] == 0x02):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в security access")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа в security access")
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}")
                            case 4:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                                time.sleep(0.02)
                                if(Result.frame[1].data[1]==0x50):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в диагностическую сессию")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа в диагностическую сессию")
                                time.sleep(0.02)
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
                    case 0x33:  #Проверка Tester Present 0x3E
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                    case 0x34:  #Проверка CommunicationControl 0x28 disable tx
                        match Command.UDS_NRC:
                            case 0:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                                time.sleep(0.01)
                                if(Result.measuredValue[0]==0):
                                    self.UDS_MSG_BRS.append("Сообщения по CAN не принимаются ")
                                else:
                                    self.UDS_MSG_BRS.append("Сообщения по CAN принимаются ")
                                time.sleep(0.01)
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
                                time.sleep(0.01)
                                if (Result.measuredValue[1] == 0):
                                    self.UDS_MSG_BRS.append("Сообщения по CAN не принимаются ")
                                else:
                                    self.UDS_MSG_BRS.append("Сообщения по CAN принимаются ")
                            case 1:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                                time.sleep(0.02)
                                if(Result.frame[1].data[1]==0x50):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в диагностическую сессию")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа  в диагностическую сессию")
                                time.sleep(0.02)
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
                            case 2:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                            case 3:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                            case 4:
                                self.UDS_MSG_BRS.append(
                                    f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                                time.sleep(0.02)
                                if (Result.frame[1].data[1] == 0x50):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в диагностическую сессию")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа  в диагностическую сессию")
                                time.sleep(0.02)
                                self.UDS_MSG_BRS.append(
                                    f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")

                    case 0x35: #Проверка CommunicationControl 0x28 disable tx,rx
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                        time.sleep(0.01)
                        if (Result.measuredValue[0] == 0):
                            self.UDS_MSG_BRS.append("Сообщения по CAN не принимаются и не передаются ")
                        else:
                            self.UDS_MSG_BRS.append("Сообщения по CAN принимаются")
                        #ПРОВЕРИТЬ FDCAN->PSR И ЕСЛИ ОН МЕНЯЕТ СОСТОЯНИЕ ДОБАВИТЬ В OUTPUT
                    case 0x36:#Проверка ClearDiagnosticInformation 0x14
                        match(Command.UDS_NRC):
                            case 0:
                                DTC_list=self.parse_UDS_errors(Result, 0x09)
                                self.UDS_MSG_BRS.append("Считанные ошибки:\n")
                                time.sleep(0.02)
                                for i in range(1, len(DTC_list)):
                                    self.UDS_MSG_BRS.append(f"{str(hex(DTC_list[i]))}:{self.match_DTC(hex(DTC_list[i]))}")
                                    time.sleep(0.02)
                                received_len = self.UART.read(2).hex()

                                bytes_read = self.UART.read(int(received_len, 16))
                                Result.ParseFromString(bytes_read)
                                self.UDS_MSG_BRS.append("\nОчистка ошибок")
                                time.sleep(0.02)
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\n")
                                time.sleep(0.02)
                                received_len = self.UART.read(2).hex()

                                bytes_read = self.UART.read(int(received_len, 16))
                                Result.ParseFromString(bytes_read)
                                DTC_list2= self.parse_UDS_errors(Result, 0x09)
                                self.UDS_MSG_BRS.append("\nСчитанные ошибки:\n")
                                if(len(Result.frame[0].data)<8):
                                    self.UDS_MSG_BRS.append("None")
                                else:
                                    time.sleep(0.01)
                                    for i in range(1, len(DTC_list2)):
                                        self.UDS_MSG_BRS.append(f"{str(hex(DTC_list2[i]))}:{self.match_DTC(hex(DTC_list2[i]))}")
                                        time.sleep(0.02)
                            case 1:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                            case 2:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")

                    case 0x37:   #read supported dtc
                        match (Command.UDS_NRC):
                            case 0:
                                if (len(Result.frame[0].data) < 8):
                                    self.UDS_MSG_BRS.append("No DTC found")
                                else:
                                    DTC_list1 = self.parse_UDS_errors(Result, 0x09)
                                    for i in range(0, len(DTC_list1)):
                                        if (self.match_DTC(hex(DTC_list1[i])) != None):
                                            self.UDS_MSG_BRS.append(f"{str(hex(DTC_list1[i]))}:{self.match_DTC(hex(DTC_list1[i]))} Status:Active")
                                            time.sleep(0.05)
                                    DTC_list2 = self.parse_UDS_errors(Result, 0x08)
                                    for i in range(0, len(DTC_list2)):
                                        if (self.match_DTC(hex(DTC_list2[i])) != None):
                                            self.UDS_MSG_BRS.append(f"{str(hex(DTC_list2[i]))}:{self.match_DTC(hex(DTC_list2[i]))} Status:DTC confirmed")
                                            time.sleep(0.05)
                                    DTC_list3 = self.parse_UDS_errors(Result, 0x00)
                                    for i in range(0, len(DTC_list3)):
                                        if(self.match_DTC(hex(DTC_list3[i]))!=None):
                                            self.UDS_MSG_BRS.append(f"{str(hex(DTC_list3[i]))}:{self.match_DTC(hex(DTC_list3[i]))} Status:Not active")
                                            time.sleep(0.05)
                            case 1:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                            case 2:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                            case 3:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")

                    case 0x38:#control dtcsetting
                        self.UDS_MSG_BRS.append("Очистка DTC:")
                        time.sleep(0.02)
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\n")
                        time.sleep(0.02)
                        self.UDS_MSG_BRS.append("Отключение самодиагностики")
                        time.sleep(0.02)
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\n")
                        received_len = self.UART.read(2).hex()
                        bytes_read = self.UART.read(int(received_len, 16))
                        Result.ParseFromString(bytes_read)
                        DTC_list = self.parse_UDS_errors(Result, 0x09)
                        self.UDS_MSG_BRS.append("Чтение DTC")
                        time.sleep(0.02)
                        if(len(DTC_list)>1):
                            for i in range(1, len(DTC_list)):
                                self.UDS_MSG_BRS.append(f"{str(hex(DTC_list[i]))}:{self.match_DTC(hex(DTC_list[i]))} Status:Active")
                                time.sleep(0.05)
                        else:
                            self.UDS_MSG_BRS.append("NO ACTIVE DTC")
                        received_len = self.UART.read(2).hex()
                        bytes_read = self.UART.read(int(received_len, 16))
                        Result.ParseFromString(bytes_read)
                        self.UDS_MSG_BRS.append("\nВключение самодиагностики")
                        time.sleep(0.02)
                        self.UDS_MSG_BRS.append( f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\n")
                        received_len = self.UART.read(2).hex()
                        bytes_read = self.UART.read(int(received_len, 16))
                        Result.ParseFromString(bytes_read)
                        DTC_list = self.parse_UDS_errors(Result, 0x09)
                        self.UDS_MSG_BRS.append("Чтение DTC")
                        time.sleep(0.02)
                        if (len(DTC_list) > 1):
                            for i in range(1, len(DTC_list)):
                                self.UDS_MSG_BRS.append(
                                    f"{str(hex(DTC_list[i]))}:{self.match_DTC(hex(DTC_list[i]))} Status:Active")
                                time.sleep(0.05)
                        else:
                            self.UDS_MSG_BRS.append("NO ACTIVE DTC")
                    case 0x39:#security access
                        match (Command.UDS_NRC):
                            case 0:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\nОтправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\nОтправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                                time.sleep(0.02)
                                if(Result.frame[5].data[1]==0x67 and Result.frame[5].data[2]==0x02):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в security access")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа в security access")
                            case 1:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\n")
                                time.sleep(0.02)
                                if(Result.frame[1].data[1]==0x50):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в диагностическую сессию")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа в диагностическую сессию")
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\n")
                            case 2|3:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\n")
                            case 4:
                                for i in range(0,7):
                                    self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2*i].data.hex())}\nПринято:{str(Result.frame[2*i+1].data.hex())}")
                                    time.sleep(0.02)
                            case 5:
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                                time.sleep(0.02)
                                if (Result.frame[1].data[1] == 0x50):
                                    self.UDS_MSG_BRS.append("Блок успешно вошёл в диагностическую сессию")
                                else:
                                    self.UDS_MSG_BRS.append("Ошибка входа в диагностическую сессию")
                                time.sleep(0.02)
                                self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
                    case 0x3A: #DID ECU OPERATING STATES
                        match(Command.UDS_NRC):
                                case 0:
                                    self.UDS_MSG_BRS.append("Вход в расширенную диагностическую сессию:")
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\n")
                                    time.sleep(0.01)
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append("Изменение режима работы на Working:")
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\n")
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append("Перезагрузка блока:")
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[8].data.hex())}\nПринято:{str(Result.frame[9].data.hex())}\n")
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append("Чтение DID:")
                                    time.sleep(0.01)
                                    self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[10].data.hex())}\nПринято:{str(Result.frame[11].data.hex())}")
                                case 1|2|3|4|5:
                                    self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\n")
                                    time.sleep(0.01)
                    case 0x3B:  # DID ECU OPERATING STATES
                        self.UDS_MSG_BRS.append("Вход в SecurityAccess:")
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\nОтправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\nОтправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                        time.sleep(0.02)
                        self.UDS_MSG_BRS.append("\nИзменение режима работы на Plant:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append("Перезагрузка блока:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[8].data.hex())}\nПринято:{str(Result.frame[9].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append("Чтение DID:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[10].data.hex())}\nПринято:{str(Result.frame[11].data.hex())}")
                    case 0x3C: #DID ACU Configuration
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\nОтправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\nОтправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                        time.sleep(0.02)
                        if (Result.frame[5].data[1] == 0x67 and Result.frame[5].data[2] == 0x02):
                            self.UDS_MSG_BRS.append("Блок успешно вошёл в security access\n")
                        else:
                            self.UDS_MSG_BRS.append("Ошибка входа в security access\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append("Чтение DID 0xE180:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append("Отключение передней подушки:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[8].data.hex())}\nПринято:{str(Result.frame[9].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append("Перезагрузка блока:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[10].data.hex())}\nПринято:{str(Result.frame[11].data.hex())}\n")
                        time.sleep(0.01)
                        if(Result.measuredValue[0]==0):
                            self.UDS_MSG_BRS.append("Импульс на пиропатроне водителя не зарегистрирован\n")
                        else:
                            self.UDS_MSG_BRS.append("Импульс на пиропатроне водителя зарегистрирован\n")
                        self.UDS_MSG_BRS.append("Чтение DID 0хE180 после перезагрузки:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[12].data.hex())}\nПринято:{str(Result.frame[13].data.hex())}\n")
                        self.UDS_MSG_BRS.append("Чтение DID 0хE182")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[14].data.hex())}\nПринято:{str(Result.frame[15].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append("Отключение ремня безопасности водителя")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(
                            f"Отправлено:{str(Result.frame[16].data.hex())}\nПринято:{str(Result.frame[17].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(f"Состояние ремня безопасности водителя:")
                        time.sleep(0.01)
                        if (Result.measuredValue[1] == 0):
                            self.UDS_MSG_BRS.append("Not monitored")
                        elif(Result.measuredValue[1] == 1):
                            self.UDS_MSG_BRS.append("Unfastened")
                        elif(Result.measuredValue[1] == 2):
                            self.UDS_MSG_BRS.append("Fastened")
                        elif(Result.measuredValue[1] == 3):
                            self.UDS_MSG_BRS.append("Unavalible")
                        self.UDS_MSG_BRS.append("\nПерезагрузка блока:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[18].data.hex())}\nПринято:{str(Result.frame[19].data.hex())}\n")
                        self.UDS_MSG_BRS.append("Чтение DID 0xE182 после перезагрузки:")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[20].data.hex())}\nПринято:{str(Result.frame[21].data.hex())}\n")
                        time.sleep(0.01)
                        self.UDS_MSG_BRS.append(f"Состояние ремня безопасности водителя:")
                        time.sleep(0.01)
                        if(Result.measuredValue[2]==0):
                            self.UDS_MSG_BRS.append("Not monitored")
                        elif (Result.measuredValue[2] == 1):
                            self.UDS_MSG_BRS.append("Unfastened")
                        elif (Result.measuredValue[2] == 2):
                            self.UDS_MSG_BRS.append("Fastened")
                        elif (Result.measuredValue[2] == 3):
                            self.UDS_MSG_BRS.append("Unavalible")
                    case 0x3D: #Read DID
                        self.UDS_MSG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
                        match(Command.UDS_subtest):
                            case 1|2|3|4|5|6|7|8:
                                Resisatnce =0.01*((Result.frame[1].data[4]<<8)+Result.frame[1].data[5])
                                time.sleep(0.01)
                                self.UDS_MSG_BRS.append(f"\nResistance:{str(round(Resisatnce,1))} Ohm")
                            case  10:
                                Resisatnce = ((Result.frame[1].data[4] << 8) + Result.frame[1].data[5])
                                time.sleep(0.01)
                                self.UDS_MSG_BRS.append(f"\nResistance:{str(round(Resisatnce,1))} Ohm")
                            case 14:
                                Resisatnce = 0.1*((Result.frame[1].data[4] << 8) + Result.frame[1].data[5])
                                time.sleep(0.01)
                                self.UDS_MSG_BRS.append(f"\nResistance:{str(round(Resisatnce,1))} Ohm")
                            case 9:
                                Indicator_status=Result.frame[1].data[4]
                                if(Indicator_status==0):
                                    self.UDS_MSG_BRS.append("\nPAB Deactivation Indicator Status: No indication")
                                else:
                                    self.UDS_MSG_BRS.append("\nPAB Deactivation Indicator Status: Indication requested")
                            case 11:
                                Vehicle_spd = ((Result.frame[1].data[4])+Result.frame[1].data[5])
                                self.UDS_MSG_BRS.append(f"\nVehicle Speed:{Vehicle_spd} km/h")
                            case 12:
                                VLT = (Result.frame[1].data[4])
                                self.UDS_MSG_BRS.append(f"\nBattery voltage:{round(0.1*VLT,1)} V")
                            case 13:
                                TMR = ((Result.frame[1].data[4] << 24) + (Result.frame[1].data[5] << 16) + (Result.frame[1].data[6]<<8) + Result.frame[1].data[7])
                                self.UDS_MSG_BRS.append(f"\nLifetime timer value:{TMR} s")
                            case 15:
                                WL_status = Result.frame[1].data[4]
                                if (WL_status == 0):
                                    self.UDS_MSG_BRS.append("\nWarning Lamp Status: No warning")
                                else:
                                    self.UDS_MSG_BRS.append("\nWarning Lamp Status: Warning")
                            case 16:
                                Mil = ((Result.frame[1].data[4] << 16) + (Result.frame[1].data[5] << 8) + (Result.frame[1].data[6]))
                                self.UDS_MSG_BRS.append(f"\nMileage:{round(0.01*Mil,1)} km")
                            case 17:
                                TIM = ((Result.frame[1].data[4] << 8) + (Result.frame[1].data[5]))
                                self.UDS_MSG_BRS.append(f"\nKey-on timer value:{TIM} s")
                            case 18:
                                DSB = (Result.frame[1].data[5] & 0x1)
                                PSB_PPS = ((Result.frame[1].data[5] & 0x1E) >> 1)
                                match(PSB_PPS):
                                    case 0:
                                        PSB_PPS='Passenger not present'
                                    case 1:
                                        PSB_PPS='Passenger present,not fastened'
                                    case 2:
                                        PSB_PPS='Passenger present,fastened'
                                    case _:
                                        PSB_PPS='Sensor value out of range'
                                RRSB = ((Result.frame[1].data[5] & 0x20) >> 5)
                                CRSB = ((Result.frame[1].data[5] & 0x40) >> 6)
                                LRSB = ((Result.frame[1].data[5] & 0x80) >> 7)
                                PADS_ST = ((Result.frame[1].data[4] & 0x1) >> 1)
                                BRSB = ((Result.frame[1].data[4] & 0x2) >> 2)
                                BLSB = ((Result.frame[1].data[4] & 0x4) >> 3)
                                self.UDS_MSG_BRS.append(f"\nDriver SB:{self.matchSB(DSB)}\nPassenger SB:{(PSB_PPS)}\nRear right SB:{self.matchSB(RRSB)}\nRear left SB:{self.matchSB(LRSB)}\nPADS_ST:{self.matchACU(PADS_ST)}\n3rd row right SB:{self.matchSB(BRSB)}\n3rd row left SB:{self.matchSB(BLSB)}\n")
                            case 19:
                                OPST = (Result.frame[1].data[4])
                                if(OPST==0xA5):
                                    self.UDS_MSG_BRS.append("\nWorking mode")
                                if (OPST == 0x5A):
                                    self.UDS_MSG_BRS.append("\nPlant mode")
                            case 20:
                                DAB = (Result.frame[1].data[4] & 0x1)
                                PAB = ((Result.frame[1].data[4] & 0x2) >> 1)
                                DPT = ((Result.frame[1].data[4] & 0x4) >> 2)
                                PPT = ((Result.frame[1].data[4] & 0x8) >> 3)
                                PADI = ((Result.frame[1].data[4] & 0x10) >> 4)
                                PADS = ((Result.frame[1].data[4] & 0x20) >> 5)
                                PPS = ((Result.frame[1].data[4] & 0x40) >> 6)
                                self.UDS_MSG_BRS.append(f"\nDriver Airbag:{self.matchACU(DAB)}\nPassenger Airbag:{self.matchACU(PAB)}\nDriver Pretensioner:{self.matchACU(DPT)}\nPassenger Pretensioner:{self.matchACU(PPT)}\nPADI:{self.matchACU(PADI)}\nPADS:{self.matchACU(PADS)}\nPassenger Presence sensor:{self.matchACU(PPS)}\n")
                            case 21:
                                LCAB = (Result.frame[1].data[4] & 0x1)
                                RCAB = ((Result.frame[1].data[4] & 0x2) >> 1)
                                DSAB = ((Result.frame[1].data[4] & 0x4) >> 2)
                                PSAB = ((Result.frame[1].data[4] & 0x8) >> 3)
                                PGSAT = ((Result.frame[1].data[4] & 0x10) >> 4)
                                DGSAT = ((Result.frame[1].data[4] & 0x20) >> 5)
                                PPSAT = ((Result.frame[1].data[4] & 0x40) >> 6)
                                DPSAT = ((Result.frame[1].data[4] & 0x80) >> 7)
                                self.UDS_MSG_BRS.append(f"\nLeft Curtain Airbag:{self.matchACU(LCAB)}\nRight Curtain Airbag:{self.matchACU(RCAB)}\nDriver Side Airbag:{self.matchACU(DSAB)}\nPassenger Side Airbag:{self.matchACU(PSAB)}\nPassenger front side crash sensor:{self.matchACU(PGSAT)}\nDriver front side crash sensor:{self.matchACU(DGSAT)}\nPassenger door pressure sensor:{self.matchACU(PPSAT)}\nDriver door pressure sensor:{self.matchACU(DPSAT)}\n")

                            case 22:
                                DSB = (Result.frame[1].data[4] & 0x1)
                                PSB = ((Result.frame[1].data[4] & 0x2)>>1)
                                RRSB = ((Result.frame[1].data[4] & 0x4)>>2)
                                RCSB = ((Result.frame[1].data[4] & 0x8)>>3)
                                RLSB = ((Result.frame[1].data[4] & 0x10)>>4)
                                self.UDS_MSG_BRS.append(f"\nDriver SB:{self.matchACU(DSB)}\nPassenger SB:{self.matchACU(PSB)}\nRear right SB:{self.matchACU(RRSB)}\nRear Center SB:{self.matchACU(RCSB)}\nRear left SB:{self.matchACU(RLSB)}\n")
        except:
            self.UDS_MSG_BRS.append("Ошибка. Попробуйте ещё раз")
        self.UART.close()
        time.sleep(0.1)
        self.EnableAll()
        self.STOP_BTN_6.setEnabled(False)
    def run_UDS(self):
        Receiver=threading.Thread(target=self.UDS_handler)
        Receiver.start()
    def snap_handler(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber=0x304
        match(self.snap_sel_1.currentIndex()):
            case 0:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 1
                    case 1:
                        Command.UDS_snap = 2
                    case 2:
                        Command.UDS_snap = 3
                    case 3:
                        Command.UDS_snap = 4
            case 1:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 5
                    case 1:
                        Command.UDS_snap = 6
                    case 2:
                        Command.UDS_snap = 7
                    case 3:
                        Command.UDS_snap = 8
                    case 4:
                        Command.UDS_snap = 9
                    case 5:
                        Command.UDS_snap = 10
            case 2:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 11
                    case 1:
                        Command.UDS_snap = 12
            case 3:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 13
                    case 1:
                        Command.UDS_snap = 14
                    case 2:
                        Command.UDS_snap = 15
                    case 3:
                        Command.UDS_snap = 16
            case 4:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 17
                    case 1:
                        Command.UDS_snap = 18
                    case 2:
                        Command.UDS_snap = 19
                    case 3:
                        Command.UDS_snap = 20
            case 5:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 21
                    case 1:
                        Command.UDS_snap = 22
                    case 2:
                        Command.UDS_snap = 23
                    case 3:
                        Command.UDS_snap = 24
            case 6:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 25
                    case 1:
                        Command.UDS_snap = 26
                    case 2:
                        Command.UDS_snap = 27
                    case 3:
                        Command.UDS_snap = 28
            case 7:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 29
                    case 1:
                        Command.UDS_snap = 30
                    case 2:
                        Command.UDS_snap = 31
                    case 3:
                        Command.UDS_snap = 32
            case 8:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 33
                    case 1:
                        Command.UDS_snap = 34
                    case 2:
                        Command.UDS_snap = 35
                    case 3:
                        Command.UDS_snap = 36
            case 9:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 37
                    case 1:
                        Command.UDS_snap = 38
                    case 2:
                        Command.UDS_snap = 39
                    case 2:
                        Command.UDS_snap = 40

            case 10:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 41
                    case 1:
                        Command.UDS_snap = 42
                    case 2:
                        Command.UDS_snap = 43
                    case 2:
                        Command.UDS_snap = 44
            case 11:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 45
                    case 1:
                        Command.UDS_snap = 46
            case 12:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 47
                    case 1:
                        Command.UDS_snap = 48
            case 13:
                match (self.snap_sel_2.currentIndex()):
                    case 0:
                        Command.UDS_snap = 49
                    case 1:
                        Command.UDS_snap = 50
                    case 2:
                        Command.UDS_snap = 51
                    case 3:
                        Command.UDS_snap = 52

        Cmd = Command.SerializeToString()
        self.UART.write(Cmd)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.snap_brs.append("Остановлено")
            self.UART.close()
        else:
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            try:
                self.snap_brs.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}\nОтправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}\nПринято:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
                time.sleep(0.02)
                if (Result.frame[1].data[7] == 0x09):
                    self.status_brs.append("ACTIVE")
                else:
                    self.status_brs.append("INACTIVE")
                time.sleep(0.02)
                self.lcdNumber_2.append(f"{round(float(((Result.frame[3].data[5] << 8) + (Result.frame[3].data[6])) * 0.01),1)} km/h")
                time.sleep(0.02)
                self.lcdNumber_3.append(f"{int(((Result.frame[4].data[7] << 24)+(Result.frame[5].data[1] << 16) + (Result.frame[5].data[2] << 8) + (Result.frame[5].data[3] >>4)) * 0.01)} km")
                time.sleep(0.02)
                self.lcdNumber_4.append(f"{int(((Result.frame[4].data[2] << 16) + (Result.frame[4].data[3] << 8) + (Result.frame[4].data[4])) * 5)}  min")
                time.sleep(0.02)
                self.lcdNumber_5.append(f"{int((Result.frame[5].data[6]))}")
                self.UART.close()
            except:
                self.snap_brs.append("Ошибка чтения snapshot.Попробуйте ещё раз")
        self.UART.close()
        self.EnableAll()


    def run_snap_handler(self):
        Receiver = threading.Thread(target=self.snap_handler)
        Receiver.start()
    def SBR_handler(self):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.STOP_BTN_5.setEnabled(True)
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = self.SBR_test_selector.currentIndex()+0x41
        Command.Seatbelt_position=self.Seatbelt_selector.currentIndex()+1
        match Command.testNumber:
            case 0x41: #Проверка корректности передачи состояний РБ по CAN шине
                Command.VehicleStateExtended=1
                Command.vehicle_speed = 0
            case 0x42: #Проверка активации системы при включении зажигания
                Command.VehicleStateExtended=0
                Command.vehicle_speed=0
            case 0x43: #Проверка включения 1 уровня тревоги seat belt reminder. Скорость < 20 km/h
                Command.VehicleStateExtended = 1
                Command.vehicle_speed = 0
            case 0x44: #Проверка включения 2 уровня тревоги seat belt reminder. Скорость > 20 km/h
                Command.VehicleStateExtended = 1
                Command.vehicle_speed = 1
            case 0x45:  # Проверка отключения сообщения о тревоге по таймауту
                Command.VehicleStateExtended = 1
                Command.vehicle_speed = 0
            case 0x46:  # Проверка обнуления таймаута
                Command.VehicleStateExtended = 1
                Command.vehicle_speed = 0
            case 0x47:  # Проверка отключения тревоги при открытии дверей
                Command.VehicleStateExtended = 1
                Command.vehicle_speed = 0
            case 0x48:  # Проверка отключения тревоги при заднем ходе
                Command.VehicleStateExtended = 1
                Command.vehicle_speed = 0
        Cmd = Command.SerializeToString()
        self.UART.write(Cmd)
        try:
            received_len=self.UART.read(2).hex()
            if (received_len == ''):
                self.got_res_SBR_brs.append("Остановлено")
            else:
                bytes_read = self.UART.read(int(received_len,16))
                Result.ParseFromString(bytes_read)
                match Result.testNumber:
                    case 0x41:
                        for i in range(0, 2):
                            self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[i].timestamp)}   id:{str(hex(Result.frame[i].id))}   DLC:{str(Result.frame[i].length)}   Data:{str(Result.frame[i].data.hex())}")
                        time.sleep(0.02)
                        match Result.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(f"При пристегнутом ремне: {hex((Result.frame[0].data[0] & DriverSafetyBeltState.Unavalible) >> DriverSafetyBeltState.shift)}\nПри непристегнутом ремне: {hex((Result.frame[1].data[0] & DriverSafetyBeltState.Unavalible) >> DriverSafetyBeltState.shift)}")
                                time.sleep(0.02)
                                if (Result.frame[0].data[0] & DriverSafetyBeltState.Unavalible == DriverSafetyBeltState.SB_fastened and Result.frame[1].data[0] & DriverSafetyBeltState.Unavalible == DriverSafetyBeltState.SB_unfastened):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"При пристегнутом ремне: {hex((Result.frame[1].data[0] & FrontPassengerSafetyBeltState.Unavalible) >> FrontPassengerSafetyBeltState.shift)}\nПри непристегнутом ремне: {hex((Result.frame[0].data[0] &FrontPassengerSafetyBeltState.Unavalible) >> FrontPassengerSafetyBeltState.shift)}")
                                time.sleep(0.05)
                                if (Result.frame[1].data[0] & FrontPassengerSafetyBeltState.Unavalible == FrontPassengerSafetyBeltState.SB_fastened and Result.frame[0].data[0] & FrontPassengerSafetyBeltState.Unavalible == FrontPassengerSafetyBeltState.SB_unfastened):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"При пристегнутом ремне: {hex((Result.frame[0].data[2] & SecondRowCenterSafetyBeltState.Unavalible) >> SecondRowCenterSafetyBeltState.shift)}\nПри непристегнутом ремне: {hex((Result.frame[1].data[2] & SecondRowCenterSafetyBeltState.Unavalible) >> SecondRowCenterSafetyBeltState.shift)}")
                                time.sleep(0.05)
                                if (Result.frame[0].data[2] & SecondRowCenterSafetyBeltState.Unavalible == SecondRowCenterSafetyBeltState.SB_fastened and Result.frame[1].data[2] & SecondRowCenterSafetyBeltState.Unavalible == SecondRowCenterSafetyBeltState.SB_unfastened):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"При пристегнутом ремне: {hex((Result.frame[0].data[3] & SecondRowRightSafetyBeltState.Unavalible) >> SecondRowRightSafetyBeltState.shift)}\nПри непристегнутом ремне: {hex((Result.frame[1].data[3] & SecondRowRightSafetyBeltState.Unavalible) >> SecondRowRightSafetyBeltState.shift)}")
                                time.sleep(0.05)
                                if (Result.frame[0].data[3] & SecondRowRightSafetyBeltState.Unavalible == SecondRowRightSafetyBeltState.SB_fastened and Result.frame[1].data[3] & SecondRowRightSafetyBeltState.Unavalible== SecondRowRightSafetyBeltState.SB_unfastened):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"При пристегнутом ремне: {hex(((Result.frame[0].data[2] <<8)+(Result.frame[0].data[3])&0b0000000110000000)>>7)}\nПри непристегнутом ремне: {hex(((Result.frame[1].data[2] <<8)+(Result.frame[1].data[3])&0b0000000110000000)>>7)}")
                                time.sleep(0.05)
                                if (int(hex(((Result.frame[0].data[2] <<8)+(Result.frame[0].data[3])&0b0000000110000000)>>7),16)==0x2 and int(hex(((Result.frame[1].data[2] <<8)+(Result.frame[1].data[3])&0b0000000110000000)>>7),16)==0x1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                    case 0x42:
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.02)
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used) )}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.No_Warning ):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used))}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.No_Warning ):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used) >> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")

                    case 0x43:
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.05)
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift )}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.Warning_level_1 ):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used))}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.Warning_level_1 ):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift )}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                    case 0x44:
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.05)
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift )}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.Warning_level_2):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.Warning_level_2 ):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used) )}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.Warning_level_2 ):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.Warning_level_2):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.Warning_level_2):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                    case 0x45:
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.05)
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[1].timestamp)}   id:{str(hex(Result.frame[1].id))}   DLC:{str(Result.frame[1].length)}   Data:{str(Result.frame[1].data.hex())}")
                        time.sleep(0.05)
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder до истечения таймаута: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                time.sleep(0.05)
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder после истечения таймаута: {hex((Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                if (Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used >0 and Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder до истечения таймаута: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.05)
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder после истечения таймаута: {hex((Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used != FrontPassengerSafetyBeltReminder.No_Warning and Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning до истечения таймаута: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used))}")
                                time.sleep(0.05)
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning после истечения таймаута: {hex((Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used) )}")
                                if (Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used != SecondRowCenterSafetyBeltWarning.No_Warning and Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning до истечения таймаута: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.05)
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning после истечения таймаута: {hex((Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                if (Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used != SecondRowRightSafetyBeltWarning.No_Warning and Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append( f"Значение SecondRowLeftSafetyBeltWarning до истечения таймаута: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.05)
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning после истечения таймаута: {hex((Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used != SecondRowLeftSafetyBeltWarning.No_Warning and Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")

                    case 0x46:
                        for i in range(0,2):
                            self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[i].timestamp)}   id:{str(hex(Result.frame[i].id))}   DLC:{str(Result.frame[i].length)}   Data:{str(Result.frame[i].data.hex())}")
                        time.sleep(0.05)
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(
                                    f"Значение DriverSafetyBeltReminder по истечении таймаута: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}\nЗначение DriverSafetyBeltReminder после сброса: {hex((Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.No_Warning and Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder по истечении таймаута: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}\nЗначение FrontPassengerSafetyBeltReminder после сброса: {hex((Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.No_Warning and Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning по истечении таймаута: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used) )}\nЗначение SecondRowCenterSafetyBeltWarning после сброса: {hex((Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used) )}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.No_Warning and Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning по истечении таймаута: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}\nЗначение SecondRowRightSafetyBeltWarning после сброса: {hex((Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.No_Warning and Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning по истечении таймаута: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}\nЗначение SecondRowLeftSetyBeltWarning после сброса: {hex((Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.No_Warning and Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.Warning_level_1):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                    case 0x47:
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.02)
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[1].timestamp)}   id:{str(hex(Result.frame[1].id))}   DLC:{str(Result.frame[1].length)}   Data:{str(Result.frame[1].data.hex())}")
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append( f"Значение DriverSafetyBeltReminder при закрытой двери: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                time.sleep(0.02)
                                self.got_res_SBR_brs.append( f"Значение DriverSafetyBeltReminder при открытой двери: {hex((Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used != DriverSafetyBeltReminder.No_Warning and Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder при закрытой двери: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder при открытой двери: {hex((Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used != FrontPassengerSafetyBeltReminder.No_Warning and Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append( f"Значение SecondRowCenterSafetyBeltWarning при закрытой двери: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used) )}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning при открытой двери: {hex((Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used))}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used != SecondRowCenterSafetyBeltWarning.No_Warning and Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning при закрытой двери: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append( f"Значение SecondRowRightSafetyBeltWarning при открытой двери: {hex((Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used != SecondRowRightSafetyBeltWarning.No_Warning and Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning при закрытой двери:: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning при открытой двери:: {hex((Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used) >> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used != SecondRowLeftSafetyBeltWarning.No_Warning and Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                    case 0x48:
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.01)
                        self.acc_SBR_brs.append(f"Timestamp:{str(Result.frame[1].timestamp)}   id:{str(hex(Result.frame[1].id))}   DLC:{str(Result.frame[1].length)}   Data:{str(Result.frame[1].data.hex())}")
                        match Command.Seatbelt_position:
                            case 1:
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder при Gear Lever drive: {hex((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение DriverSafetyBeltReminder при Gear Lever reverse: {hex((Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used)>>DriverSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if ((Result.frame[0].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.Warning_level_1) and (Result.frame[1].data[1] & DriverSafetyBeltReminder.Not_used == DriverSafetyBeltReminder.No_Warning)):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 2:
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder при Gear Lever drive: {hex((Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение FrontPassengerSafetyBeltReminder при Gear Lever reverse: {hex((Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used) >> FrontPassengerSafetyBeltReminder.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.Warning_level_1 and Result.frame[1].data[1] & FrontPassengerSafetyBeltReminder.Not_used == FrontPassengerSafetyBeltReminder.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 4:
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning при Gear Lever drive: {hex((Result.frame[0].data[1] & SecondRowCenterSafetyBeltWarning.Not_used) )}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение SecondRowCenterSafetyBeltWarning при Gear Lever reverse: {hex((Result.frame[1].data[1] & SecondRowCenterSafetyBeltWarning.Not_used))}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[1] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.Warning_level_1 and Result.frame[1].data[1] & SecondRowRightSafetyBeltWarning.Not_used == SecondRowRightSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 3:
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning при Gear Lever drive: {hex((Result.frame[0].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение SecondRowRightSafetyBeltWarning при Gear Lever reverse: {hex((Result.frame[1].data[2] & SecondRowRightSafetyBeltWarning.Not_used) >> SecondRowRightSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.Warning_level_1 and Result.frame[1].data[2] & SecondRowCenterSafetyBeltWarning.Not_used == SecondRowCenterSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")
                            case 5:
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning при Gear Lever drive: {hex((Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                self.got_res_SBR_brs.append(f"Значение SecondRowLeftSafetyBeltWarning при Gear Lever reverse: {hex((Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used)>> SecondRowLeftSafetyBeltWarning.shift)}")
                                time.sleep(0.01)
                                if (Result.frame[0].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.Warning_level_1 and Result.frame[1].data[2] & SecondRowLeftSafetyBeltWarning.Not_used == SecondRowLeftSafetyBeltWarning.No_Warning):
                                    self.got_res_SBR_brs.append("Success")
                                else:
                                    self.got_res_SBR_brs.append("Fail")

                    case 0x49:
                        self.acc_SBR_brs.append(
                            f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.02)
                        self.acc_SBR_brs.append(
                            f"Timestamp:{str(Result.frame[1].timestamp)}   id:{str(hex(Result.frame[1].id))}   DLC:{str(Result.frame[1].length)}   Data:{str(Result.frame[1].data.hex())}")

                        self.got_res_SBR_brs.append("При отсутствии пассажира")
                        time.sleep(0.02)
                        self.got_res_SBR_brs.append(f"PassengerPresenceState: {hex((Result.frame[0].data[0] & 0b00000011))}")
                        time.sleep(0.02)
                        self.got_res_SBR_brs.append("При наличии пассажира")
                        time.sleep(0.01)
                        self.got_res_SBR_brs.append(f"PassengerPrecsenceState: {hex((Result.frame[1].data[0] & 0b00000011))}")
                        if((Result.frame[0].data[0] & 0b00000011)==1 and (Result.frame[1].data[0] & 0b00000011) ==2):
                            self.got_res_SBR_brs.append("Success")
                        else:
                            self.got_res_SBR_brs.append("Fail")
                    case 0x4A:
                        self.acc_SBR_brs.append(
                            f"Timestamp:{str(Result.frame[0].timestamp)}   id:{str(hex(Result.frame[0].id))}   DLC:{str(Result.frame[0].length)}   Data:{str(Result.frame[0].data.hex())}")
                        time.sleep(0.02)
                        self.acc_SBR_brs.append(
                            f"Timestamp:{str(Result.frame[1].timestamp)}   id:{str(hex(Result.frame[1].id))}   DLC:{str(Result.frame[1].length)}   Data:{str(Result.frame[1].data.hex())}")
                        time.sleep(0.02)
                        self.got_res_SBR_brs.append(f"PassengerAIRBAG_inhibition при отключенной ПБ: {hex((Result.frame[0].data[1] & 0b00001000) >> 3)}")
                        time.sleep(0.02)
                        self.got_res_SBR_brs.append(f"PassengerAIRBAG_inhibition при включенной ПБ: {hex((Result.frame[1].data[1] & 0b00001000) >> 3)}")
                        time.sleep(0.02)
                        if(int(hex((Result.frame[0].data[1] & 0b00001000) >> 3),16)==1 and int(hex((Result.frame[1].data[1] & 0b00001000) >> 3),16)==0):
                            self.got_res_SBR_brs.append("Success")
                        else:
                            self.got_res_SBR_brs.append("Fail")
        except:
            self.got_res_SBR_brs.append("Возникла ошибка.Попробуйте ещё раз")
        self.EnableAll()
        self.STOP_BTN_5.setEnabled(False)
        self.UART.close()

    def run_SBR(self):
        Receiver=threading.Thread(target=self.SBR_handler)
        Receiver.start()

    def EDR_num_read(self):
        self.EDR_OTHER_DATA_BRS.clear()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Result=Messages.TestData()
        Command = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x64
        Command = Command.SerializeToString()
        self.UART.write(Command)
        try:
            received_len = self.UART.read(2).hex()
            if (received_len != ''):
                bytes_read = self.UART.read(int(received_len, 16))
                Result.ParseFromString(bytes_read)
                listWidgetItem = QtWidgets.QListWidgetItem(f"Отправлено:{Result.frame[0].data.hex()}")
                self.EDR_OTHER_DATA_BRS.addItem(listWidgetItem)
                listWidgetItem = QtWidgets.QListWidgetItem(f"Принято:{Result.frame[1].data.hex()}")
                self.EDR_OTHER_DATA_BRS.addItem(listWidgetItem)
                listWidgetItem = QtWidgets.QListWidgetItem(f"Номер EDR:{Result.frame[1].data[4]}")
                self.EDR_OTHER_DATA_BRS.addItem(listWidgetItem)
        except:
            self.EDR_OTHER_DATA_BRS.addItem("Возникла ошибка. Попробуйте ещё раз")
        self.UART.flush()
        self.UART.close()
        self.EnableAll()
        self.EDR_STOP_BTN.setEnabled(False)

    def run_EDR_num_read(self):
        Receiver = threading.Thread(target=self.EDR_num_read)
        Receiver.start()
    def EDR_read(self,num):
        self.Precrash_data_table.clearContents()
        self.Crash_data_table.clearContents()
        self.EDR_OTHER_DATA_BRS.clear()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        #self.READ_NUM_BTN.setDisabled(True)
        #self.EDR_STOP_BTN.setDisabled(True)
        Command = Messages.TestData()
        Command.method = 0
        match(num):
            case 1:
                Command.testNumber = 0x61
            case 2:
                Command.testNumber = 0x62
            case 3:
                Command.testNumber = 0x63
        Command.accDataNumber=7
        Command = Command.SerializeToString()
        self.UART.write(Command)
        try:
            received_len = self.UART.read(2).hex()
            if(received_len!=''):
                bytes_read = self.UART.read(int(received_len, 16))
                '''f = open('EDR2.txt', 'w')
                for index in bytes_read:
                    f.write(str(hex(bytes_read[index]))+' ')'''
                Result = Parse_EDR(bytes_read)
                for i in range(10, 260, 10):
                    self.Crash_data_table.setItem(int(i / 10) -1, 0, QtWidgets.QTableWidgetItem(f"{i}"))
                    self.Crash_data_table.setItem(int(i / 10) - 1, 1, QtWidgets.QTableWidgetItem(f"{Result[0][int(i/10) - 1]}"))
                    self.Crash_data_table.setItem(int(i / 10) - 1, 2, QtWidgets.QTableWidgetItem(f"{Result[1][int(i/10) - 1]}"))
                for i in range(11):
                    self.Precrash_data_table.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{Result[2][i]}"))
                    self.Precrash_data_table.setItem(i , 1, QtWidgets.QTableWidgetItem(f"{Result[3][i]}"))
                    self.Precrash_data_table.setItem(i, 2, QtWidgets.QTableWidgetItem(f"{Result[4][i]}"))
                    self.Precrash_data_table.setItem(i, 3, QtWidgets.QTableWidgetItem(f"{Result[5][i]}"))
                    self.Precrash_data_table.setItem(i, 4, QtWidgets.QTableWidgetItem(f"{Result[6][i]}"))
                    self.Precrash_data_table.setItem(i, 5, QtWidgets.QTableWidgetItem(f"{Result[7][i]}"))
                    self.Precrash_data_table.setItem(i, 6, QtWidgets.QTableWidgetItem(f"{Result[8][i]}"))
                    self.Precrash_data_table.setItem(i, 7, QtWidgets.QTableWidgetItem(f"{Result[9][i]}"))
                    self.Precrash_data_table.setItem(i, 8, QtWidgets.QTableWidgetItem(f"{Result[10][i]}"))
                    self.Precrash_data_table.setItem(i, 9, QtWidgets.QTableWidgetItem(f"{Result[11][i]}"))
                    self.Precrash_data_table.setItem(i, 10, QtWidgets.QTableWidgetItem(f"{Result[12][i]}"))
                    self.Precrash_data_table.setItem(i, 11, QtWidgets.QTableWidgetItem(f"{Result[13][i]}"))
                for i in range(0,40):#?
                    listWidgetItem = QtWidgets.QListWidgetItem(f"{Result[14][i]}")
                    self.EDR_OTHER_DATA_BRS.addItem(listWidgetItem)
                Result.clear()
                bytes_read=bytearray(bytes_read)
                for i in range(0,len(bytes_read)):
                    bytes_read[i]=0
        except:
            self.EDR_OTHER_DATA_BRS.addItem("Ошибка чтения EDR. Попробуйте ещё раз")
        self.UART.flush()
        self.UART.close()
        self.EnableAll()

        self.EDR_STOP_BTN.setEnabled(False)

    def run_EDR_read(self, num):
        Receiver = threading.Thread(target=self.EDR_read,args=(num,))
        Receiver.start()
    def update_params(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x90
        Command = Command.SerializeToString()
        self.UART.write(Command)

        Limit_Ares_front = self.LimitAresfront_input.value()

        Limit_Sx_Sy_front = self.LimitSxSyfront_input.value()

        Limit_Sres_front = self.LimitSresfront_input.value()

        delta_Ares = self.deltaAres_input.value()

        Limit_Ares_side = self.LimitAresside_input.value()

        Limit_Sx_Sy_side = self.LimitSxSyside_input.value()

        Limit_Sres_side = self.LimitSresside_input.value()

        T_calc_front = self.Tcalc_input.value()

        T_calc_side = self.Tcalc2_input.value()

        Time_to_stop_calc = self.Timetostopcalc_input.value()

        Sres_impact_front = self.Sresimpactfront_input.value()

        Sres_impact_side = self.Sresimpact_side_input.value()
        PARAMS_ARRAY=bytearray([(Limit_Ares_front>>8)&0xff,(Limit_Ares_front)&0xff,(Limit_Ares_side)>>8&0xff,(Limit_Ares_side)&0xff,(Limit_Sx_Sy_front>>8)&0xff,(Limit_Sx_Sy_front)&0xff,(Limit_Sx_Sy_side>>8)&0xff,(Limit_Sx_Sy_side)&0xff,(Limit_Sres_front>>8)&0xff,Limit_Sres_front&0xff,(Limit_Sres_side>>8)&0xff,Limit_Sres_side&0xff,T_calc_front,T_calc_side,Time_to_stop_calc,(Sres_impact_front>>8)&0xff,(Sres_impact_front)&0xff,(Sres_impact_side>>8)&0xff,(Sres_impact_side)&0xff,delta_Ares])
        time.sleep(1)
        self.UART.write(PARAMS_ARRAY)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.PARAM_RESULT_BRS_2.append("Остановлено")
        else:
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            if((hex(Result.frame[1].data[1])=='0x6e'and hex(Result.frame[3].data[1])=='0x6e'and hex(Result.frame[5].data[1])=='0x6e'and hex(Result.frame[7].data[1])=='0x6e'and hex(Result.frame[9].data[1])=='0x6e'and hex(Result.frame[11].data[1])=='0x6e'and hex(Result.frame[13].data[1])=='0x6e'and hex(Result.frame[15].data[1])=='0x6e'and hex(Result.frame[1].data[1])=='0x6e'and hex(Result.frame[17].data[1])=='0x6e'and hex(Result.frame[19].data[1])=='0x6e'and hex(Result.frame[21].data[1])=='0x6e'and hex(Result.frame[23].data[1])=='0x6e')):
                self.PARAM_RESULT_BRS_2.append("Успешное обновление")
            else:
                self.PARAM_RESULT_BRS_2.append("Ошибка обновления параметров")
            for i in range(0,12):
                self.PARAM_RESULT_BRS_2.append(f"Отправлено:{str(Result.frame[2*i].data.hex())}\nПринято:{str(Result.frame[2*i+1].data.hex())}")
                time.sleep(0.02)
        self.UART.close()
        self.EnableAll()
    def run_update_params(self):
        Receiver = threading.Thread(target=self.update_params)
        Receiver.start()
    def read_params(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x91
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        if (received_len == ''):
            self.PARAM_RESULT_BRS_2.append("Остановлено")
        else:
            try:
                bytes_read = self.UART.read(int(received_len, 16))
                Result.ParseFromString(bytes_read)
                self.PARAM_RESULT_BRS_2.append(f"Limit Ares front (10\u207b\u00b9 m/s\u00B2):{(int((Result.frame[1].data[4])<<8)+int(Result.frame[1].data[5]))}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Limit Ares side (10\u207b\u00b9 m/s\u00B2):{(int((Result.frame[3].data[4])<<8)+int(Result.frame[3].data[5]))}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Limit Sx,Sy front (10\u207b\u2076 m):{round((((Result.frame[5].data[4])<<8)+int(Result.frame[5].data[5])) ,0)}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Limit Sx,Sy side (10\u207b\u2076 m):{round((((Result.frame[7].data[4])<<8)+int(Result.frame[7].data[5])) ,0)}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Limit Sres front (10\u207b\u2076 m):{round((((Result.frame[9].data[4])<<8)+int(Result.frame[9].data[5])) ,0)}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Limit Sres side (10\u207b\u2076 m):{round((((Result.frame[11].data[4])<<8)+int(Result.frame[11].data[5])) ,0)}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"T calc front (ms):{(int(Result.frame[13].data[4]))}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"T calc side(ms):{(int(Result.frame[15].data[4]))}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Time to stop calculation(ms):{(int(Result.frame[17].data[4]))}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Sres impact front (10\u207b\u2076 m):{round((((Result.frame[19].data[4])<<8)+int(Result.frame[19].data[5])) ,0)}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Sres impact side (10\u207b\u2076 m):{round((((Result.frame[21].data[4])<<8)+int(Result.frame[21].data[5])) ,0)}")
                time.sleep(0.02)
                self.PARAM_RESULT_BRS_2.append(f"Delta Ares(m/s\u00B2):{(int(Result.frame[23].data[4]))}")
                time.sleep(0.02)
            except:
                self.PARAM_RESULT_BRS_2.append("Ошибка чтения парметров. Попробуйте ещё раз")
        self.UART.close()
        self.EnableAll()

    def run_read_params(self):
        Receiver = threading.Thread(target=self.read_params)
        Receiver.start()
    def save_params(self,f_name):
        try:
            file = open(f_name, "w")
            file.write(f"Limit_Ax = 0\n")
            file.write(f"Limit_Ay = 0\n")
            file.write(f"Limit_Ares_front = {self.LimitAresfront_input.value() / 10}\n")
            self.PARAM_RESULT_BRS_2.append(f"Limit_Ares_front = {self.LimitAresfront_input.value() / 10}")
            time.sleep(0.02)
            file.write(f"Limit_Sx_Sy_front = {self.LimitSxSyfront_input.value() / 100}e-4\n")
            self.PARAM_RESULT_BRS_2.append(f"Limit_Sx_Sy_front = {self.LimitSxSyfront_input.value() / 100}e-4")
            time.sleep(0.02)
            file.write(f"Limit_Sres_front = {self.LimitSresfront_input.value() / 100}e-4\n")
            self.PARAM_RESULT_BRS_2.append(f"Limit_Sres_front = {self.LimitSresfront_input.value() / 100}e-4")
            time.sleep(0.02)
            file.write(f"delta_Ares = {self.deltaAres_input.value()}\n")
            self.PARAM_RESULT_BRS_2.append(f"delta_Ares = {self.deltaAres_input.value()}")
            time.sleep(0.02)
            file.write(f"Limit_Ares_side = {self.LimitAresside_input.value() / 10}\n")
            self.PARAM_RESULT_BRS_2.append(f"Limit_Ares_side = {self.LimitAresside_input.value() / 10}")
            time.sleep(0.02)
            file.write(f"Limit_Sx_Sy_side = {self.LimitSxSyside_input.value() / 100}e-4\n")
            self.PARAM_RESULT_BRS_2.append(f"Limit_Sx_Sy_side = {self.LimitSxSyside_input.value() / 100}e-4")
            time.sleep(0.02)
            file.write(f"Limit_Sres_side = {self.LimitSresside_input.value() / 100}e-4\n")
            self.PARAM_RESULT_BRS_2.append(f"Limit_Sres_side = {self.LimitSresside_input.value() / 100}e-4")
            time.sleep(0.02)
            file.write(f"T_calc_front = {self.Tcalc_input.value()}\n")
            self.PARAM_RESULT_BRS_2.append(f"T_calc_front = {self.Tcalc_input.value()}")
            time.sleep(0.02)
            file.write(f"T_calc_side = {self.Tcalc2_input.value()}\n")
            self.PARAM_RESULT_BRS_2.append(f"T_calc_side = {self.Tcalc2_input.value()}")
            time.sleep(0.02)
            file.write(f"Time_to_stop = {self.Timetostopcalc_input.value() / 1000}e3\n")
            self.PARAM_RESULT_BRS_2.append(f"Time_to_stop = {self.Timetostopcalc_input.value() / 1000}e3")
            time.sleep(0.02)
            file.write(f"Sres_impact_front = {self.Sresimpactfront_input.value() / 100}e-4\n")
            self.PARAM_RESULT_BRS_2.append(f"Sres_impact_front = {self.Sresimpactfront_input.value() / 100}e-4")
            time.sleep(0.02)
            file.write(f"Sres_impact_side = {self.Sresimpact_side_input.value() / 100}e-4\n")
            self.PARAM_RESULT_BRS_2.append(f"Sres_impact_side = {self.Sresimpact_side_input.value() / 100}e-4")
            time.sleep(0.02)
            file.close()
            self.PARAM_RESULT_BRS_2.append("\nНабор успешно сохранён")
            time.sleep(0.02)
        except:
            self.PARAM_RESULT_BRS_2.append('Возникла ошибка')
    def run_save_params(self,file):
        Receiver = threading.Thread(target=self.save_params,args=(file,))
        Receiver.start()
    def Reprogrammer(self):
        self.DisableAll()
        self.progressBar.setValue(0)
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x88
        start=time.time()
        Command = Command.SerializeToString()
        self.UART.write(Command)
        self.UART.close()

        appHex = HexOp(self.file)
        appHex.readHex()
        hexsize = appHex.getHexZise()
        requestDownload2[1] = (hexsize & 0xFF0000) >> 16
        requestDownload2[2] = (hexsize & 0x00FF00) >> 8
        requestDownload2[3] = (hexsize & 0x0000FF)
        signal = Communicate()
        signal.progress_changed.connect(self.update_progress_bar)
        UARTDriver = UART_Transmitter(self.COM_PORT,signal.progress_changed,appHex)

        UARTDriver.Sizebuf[0] = ((hexsize + 0x18000) & 0xFF0000) >> 16
        UARTDriver.Sizebuf[1] = ((hexsize + 0x18000) & 0x00FF00) >> 8
        UARTDriver.Sizebuf[2] = ((hexsize + 0x18000) & 0x0000FF)
        crc = appHex.CalculateHexCRC32(0x08018000, 0x08018000 + hexsize)
        CRCbuf=UARTDriver.determineCRC(crc)
        time.sleep(1)
        UARTDriver.UART_send_no_resp(CRCbuf)
        time.sleep(1)
        UARTDriver.UART_send_no_resp(UARTDriver.Sizebuf)
        self.LOG_print(UARTDriver.receive_status_message())
        time.sleep(5.5)
        self.LOG_print(UARTDriver.receive_status_message())
        while True:
            self.LOG_print(UARTDriver.receive_status_message())
            UARTDriver.requestDownload()
            self.LOG_print(UARTDriver.receive_status_message())
            self.LOG_print(UARTDriver.receive_status_message())
            time.sleep(0.02)
            UARTDriver.transmitProgramm()
            self.LOG_print(UARTDriver.receive_status_message())
            self.LOG_print(UARTDriver.receive_status_message())
            self.LOG_print(UARTDriver.receive_status_message())
            break

        self.LOG_print(UARTDriver.receive_status_message())
        #time.sleep(3)
        appHex.clear()
        end=time.time()
        timetaken=end-start
        time.sleep(1)
        signal.progress_changed.emit(98)
        time.sleep(1)
        signal.progress_changed.emit(99)
        time.sleep(1)
        signal.progress_changed.emit(100)
        self.LOG_print(f"ECU was reprogrammed in{round(timetaken/60,0)} min and {round(timetaken%60,0)} sec.")
        self.EnableAll()
        UARTDriver.stopUART()
        return

    def Reprogrammer_run(self):
        Receiver = threading.Thread(target=self.Reprogrammer)
        Receiver.start()

    def close(self):
        self.UART.flushInput()
        self.UART.flushOutput()
        self.UART.close()
    def CheckConnection(self):
        try:
            self.UART.open()
            self.UART.timeout = 2
            check=bytes([0xbb])
            self.UART.write(check)
            bytes_read=self.UART.read(1)
            if(len(bytes_read)==0):
                bytes_read=bytes([0x70])
            if(bytes_read[0]==0xBB):
                self.COM_PORT_BRS.append("Связь с СТО установлена")
                self.EnableAll()
                self.UART.timeout = 300
                self.UART.close()
            else:
                self.COM_PORT_BRS.append("Ошибка подключения.Попробуйте ещё раз")
                time.sleep(0.02)
                return
        except:
            time.sleep(0.01)
            self.COM_PORT_BRS.append("Ошибка подключения.Попробуйте ещё раз")
            time.sleep(0.02)
            return

    def EnableAll(self):
        self.start_SBR_btn.setEnabled(True)
        self.start_acc_btn.setEnabled(True)
        self.Run_Init_btn.setEnabled(True)
        self.CHECK_CRASH_DETECTION_BTN.setEnabled(True)
        self.UDS_RUN_BTN.setEnabled(True)
        self.perod_periodic_btn.setEnabled(True)
        self.start_trig_btn.setEnabled(True)
        self.DIAG_CLEAR_DTC_BTN.setEnabled(True)
        self.DIAG_READ_0x08_BTN.setEnabled(True)
        self.DIAG_READ_0x09_BTN.setEnabled(True)
        self.DIAG_VIN0_BTN.setEnabled(True)
        self.DIAG_VIN1_BTN.setEnabled(True)
        self.DIAG_RESET_BTN.setEnabled(True)
        self.READ_NUM_BTN.setEnabled(True)
        self.START_VALID_AB_BTN.setEnabled(True)
        self.toolButton.setEnabled(True)
        self.DIAG_UPD_CAN_MSG_BTN.setEnabled(True)
        self.DIAG_STOP_CAN_MSG_BTN.setEnabled(True)
        self.read_snap_btn.setEnabled(True)
        self.UPDATE_PARAMS_BTN.setEnabled(True)
        self.STO_VER_BTN.setEnabled(True)
        self.ACC_VER_BTN.setEnabled(True)
        self.Manufacture_mode_btn.setEnabled(True)
        self.read_params_btn.setEnabled(True)
        self.WRITE_ACU_BTN.setEnabled(True)
        self.EDR1_BTN.setEnabled(True)
        self.EDR2_BTN.setEnabled(True)
        self.EDR3_BTN.setEnabled(True)
        self.EDR_STOP_BTN.setEnabled(True)
        self.READ_VERSBTN.setEnabled(True)
        self.SET_WM_BTN.setEnabled(True)
        self.manual_mode_btn.setEnabled(True)
    def DisableAll(self):
        self.STO_VER_BTN.setDisabled(True)
        self.ACC_VER_BTN.setDisabled(True)
        self.Manufacture_mode_btn.setDisabled(True)
        self.start_SBR_btn.setDisabled(True)
        self.start_acc_btn.setDisabled(True)
        self.Run_Init_btn.setDisabled(True)
        self.CHECK_CRASH_DETECTION_BTN.setDisabled(True)
        self.UDS_RUN_BTN.setDisabled(True)
        self.EDR1_BTN.setDisabled(True)
        self.EDR2_BTN.setDisabled(True)
        self.EDR3_BTN.setDisabled(True)
        self.EDR_STOP_BTN.setDisabled(True)
        self.perod_periodic_btn.setDisabled(True)
        self.read_params_btn.setDisabled(True)
        self.start_trig_btn.setDisabled(True)
        self.DIAG_CLEAR_DTC_BTN.setDisabled(True)
        self.DIAG_READ_0x08_BTN.setDisabled(True)
        self.DIAG_READ_0x09_BTN.setDisabled(True)
        self.DIAG_VIN0_BTN.setDisabled(True)
        self.DIAG_VIN1_BTN.setDisabled(True)
        self.DIAG_RESET_BTN.setDisabled(True)
        self.START_VALID_AB_BTN.setDisabled(True)
        self.toolButton.setDisabled(True)
        self.DIAG_UPD_CAN_MSG_BTN.setDisabled(True)
        self.DIAG_STOP_CAN_MSG_BTN.setDisabled(True)
        self.read_snap_btn.setDisabled(True)
        self.UPDATE_PARAMS_BTN.setDisabled(True)
        self.WRITE_ACU_BTN.setDisabled(True)
        self.READ_NUM_BTN.setDisabled(True)
        self.READ_VERSBTN.setDisabled(True)
        self.SET_WM_BTN.setDisabled(True)
        self.manual_mode_btn.setDisabled(True)
    def CheckConnection_run(self):
        Receiver = threading.Thread(target=self.CheckConnection)
        Receiver.start()


    def run_model_all(self):
        select_all_tests = str(1)
        main_fold_dict = dict()
        os.chdir("pillows")
        folder = self.model_test_selector.currentText()
        os.chdir('test_folder')
        main_fold = os.listdir()
        for i in range(0, len(main_fold)):
            main_fold_dict.update({main_fold[i]: i + 1})
        #print(main_fold_dict)
        os.chdir('..')
        #print(main_fold_dict.get(folder))
        tmp_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        proc = subprocess.Popen(['main.exe', select_all_tests, str(main_fold_dict.get(folder))],stdout=subprocess.PIPE)
        os.chdir('..')
        time.sleep(1)
        sys.stdout = tmp_stdout
        while True:
            try:
                line = proc.stdout.read()
                #line = proc.stdout.readline()
                decoded = line.decode("utf-8")
                self.PARAM_RESULT_BRS.append(decoded)
                time.sleep(0.1)
                break
            except:
                self.PARAM_RESULT_BRS.append(f"Error occured, please try again")
                break
        proc.terminate()



    def run_thread_model_single(self):
        Receiver = threading.Thread(target=self.run_model_single)
        Receiver.start()
    def run_model_single(self):
        select_all_tests = str(0)
        main_fold_dict = dict()
        os.chdir("pillows")
        folder = self.model_test_selector.currentText()
        test = self.model_test_selector2.currentText()
        os.chdir('test_folder')
        main_fold = os.listdir()
        for i in range(0, len(main_fold)):
            main_fold_dict.update({main_fold[i]: i + 1})
        #print(main_fold_dict)
        os.chdir('..')
        #print(main_fold_dict.get(folder))
        tmp_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        proc = subprocess.Popen(['main.exe', select_all_tests, str(main_fold_dict.get(folder)), str(self.tests_dict.get(test))], stdout=subprocess.PIPE)
        os.chdir('..')
        time.sleep(1)
        sys.stdout = tmp_stdout
        while True:
            try:
                line = proc.stdout.read()
                # line = proc.stdout.readline()
                decoded = line.decode("utf-8")
                self.PARAM_RESULT_BRS.append(decoded)
                time.sleep(0.1)
                break
            except:
                self.PARAM_RESULT_BRS.append(f"Error occured, please try again")
                break
        proc.terminate()
    def run_thread_model_all(self):
        Receiver = threading.Thread(target=self.run_model_all)
        Receiver.start()
    def export_results(self):
        os.chdir("D:\STO_gui\pillows")
        subprocess.call("Results.csv", shell=True)
        os.chdir("..")
        #process = subprocess.Popen(["D:\STO_gui\pillows\lib\TEST_RESULT.csv"],stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
    def run_export_results(self):
        Receiver = threading.Thread(target=self.export_results)
        Receiver.start()
    def update_progress_bar(self, value):
        self.progressBar.setValue(value)

    def to_manufacture_mode(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x94
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        bytes_read = self.UART.read(int(received_len, 16))
        Result.ParseFromString(bytes_read)
        self.VER_LOG_BRS.append("Вход в Security access:")
        self.VER_LOG_BRS.append(
            f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
        time.sleep(0.02)
        self.VER_LOG_BRS.append(
            f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
        time.sleep(0.02)
        self.VER_LOG_BRS.append(
            f"Отправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}\n")
        time.sleep(0.02)
        self.VER_LOG_BRS.append("Cброс к заводским настройкам:")
        self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}")
        self.UART.close()
        self.EnableAll()


    def run_to_manufacture_mode(self):
        Receiver = threading.Thread(target=self.to_manufacture_mode)
        Receiver.start()
    def set_working_mode(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x95
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        bytes_read = self.UART.read(int(received_len, 16))
        Result.ParseFromString(bytes_read)
        self.VER_LOG_BRS.append("Вход в Security access:")
        self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
        time.sleep(0.02)
        self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
        time.sleep(0.02)
        self.VER_LOG_BRS.append( f"Отправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}")
        time.sleep(0.02)
        self.VER_LOG_BRS.append("\nCмена режима")
        time.sleep(0.02)
        self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}")
        time.sleep(0.02)
        self.VER_LOG_BRS.append("\nПерезагрузка")
        time.sleep(0.02)
        self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[8].data.hex())}\nПринято:{str(Result.frame[9].data.hex())}")
        time.sleep(0.02)
        self.UART.close()
        self.EnableAll()

    def run_set_working_mode(self):
        Receiver = threading.Thread(target=self.set_working_mode)
        Receiver.start()

    def manual_mode(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x98
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        bytes_read = self.UART.read(int(received_len, 16))
        Result.ParseFromString(bytes_read)
        if(Result.measuredValue[0]==1):
            self.COM_PORT_BRS.append("Переведено в ручной режим")
        self.UART.close()
        self.EnableAll()

    def run_manual_mode(self):
        Receiver = threading.Thread(target=self.manual_mode)
        Receiver.start()
    def read_ecu_version(self):
        self.DisableAll()
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        Command.testNumber = 0x96
        Command = Command.SerializeToString()
        self.UART.write(Command)
        try:
            received_len = self.UART.read(2).hex()
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
            time.sleep(0.02)
            if(Result.frame[1].data[4] == 0x01):
                self.VER_LOG_BRS.append("Работа с СТО")
            if (Result.frame[1].data[4] == 0x00):
                self.VER_LOG_BRS.append("Работа с внутренним акселерометром")
        except:
            self.VER_LOG_BRS.append("Возникла ошибка.Попробуйте ещё раз")
        self.UART.close()
        self.EnableAll()

    def run_read_ecu_version(self):
        Receiver = threading.Thread(target=self.read_ecu_version)
        Receiver.start()
    def file_updater(self):
        os.chdir('pillows')
        file =open("input_value.txt","w")
        file.write(f"Limit_Ax = 0\n")
        file.write(f"Limit_Ay = 0\n")
        file.write(f"Limit_Ares_front = {self.LimitAresfront_input.value()/10}\n")
        self.PARAM_RESULT_BRS_2.append(f"Limit_Ares_front = {self.LimitAresfront_input.value()/10}")
        file.write(f"Limit_Sx_Sy_front = {self.LimitSxSyfront_input.value()/100}e-4\n")
        self.PARAM_RESULT_BRS_2.append(f"Limit_Sx_Sy_front = {self.LimitSxSyfront_input.value()/100}e-4")
        file.write(f"Limit_Sres_front = {self.LimitSresfront_input.value()/100}e-4\n")
        self.PARAM_RESULT_BRS_2.append(f"Limit_Sres_front = {self.LimitSresfront_input.value()/100}e-4")
        file.write(f"delta_Ares = {self.deltaAres_input.value()}\n")
        self.PARAM_RESULT_BRS_2.append(f"delta_Ares = {self.deltaAres_input.value()}")
        file.write(f"Limit_Ares_side = {self.LimitAresside_input.value()/10}\n")
        self.PARAM_RESULT_BRS_2.append(f"Limit_Ares_side = {self.LimitAresside_input.value()/10}")
        file.write(f"Limit_Sx_Sy_side = {self.LimitSxSyside_input.value()/100}e-4\n")
        self.PARAM_RESULT_BRS_2.append(f"Limit_Sx_Sy_side = {self.LimitSxSyside_input.value()/100}e-4")
        file.write(f"Limit_Sres_side = {self.LimitSresside_input.value()/100}e-4\n")
        self.PARAM_RESULT_BRS_2.append(f"Limit_Sres_side = {self.LimitSresside_input.value()/100}e-4")
        file.write(f"T_calc_front = {self.Tcalc_input.value()}\n")
        self.PARAM_RESULT_BRS_2.append(f"T_calc_front = {self.Tcalc_input.value()}")
        file.write(f"T_calc_side = {self.Tcalc2_input.value()}\n")
        self.PARAM_RESULT_BRS_2.append(f"T_calc_side = {self.Tcalc2_input.value()}")
        file.write(f"Time_to_stop = {self.Timetostopcalc_input.value()/1000}e3\n")
        self.PARAM_RESULT_BRS_2.append(f"Time_to_stop = {self.Timetostopcalc_input.value()/1000}e3")
        file.write(f"Sres_impact_front = {self.Sresimpactfront_input.value()/100}e-4\n")
        self.PARAM_RESULT_BRS_2.append(f"Sres_impact_front = {self.Sresimpactfront_input.value()/100}e-4")
        file.write(f"Sres_impact_side = {self.Sresimpact_side_input.value()/100}e-4\n")
        self.PARAM_RESULT_BRS_2.append(f"Sres_impact_side = {self.Sresimpact_side_input.value()/100}e-4")
        file.close()
        os.chdir('..')


    def run_file_updater(self):
        Receiver = threading.Thread(target=self.file_updater)
        Receiver.start()

    def file_reader(self):
        os.chdir('pillows')
        file =open("input_value.txt","r")
        l=file.readline()
        l = file.readline()
        self.PARAM_RESULT_BRS_2.append('Считанные парамтеры:')
        time.sleep(0.01)
        self.PARAM_RESULT_BRS_2.append(file.read())
        file.close()
        os.chdir('..')


    def run_file_reader(self):
        Receiver = threading.Thread(target=self.file_reader)
        Receiver.start()


    def Config_version(self,ver):
        try:
            self.UART.open()
        except:
            self.UART.close()
            self.UART.open()
        self.DisableAll()
        Command = Messages.TestData()
        Result = Messages.TestData()
        Command.method = 0
        if ver == 1:
            Command.testNumber = 0x92
        else:
            Command.testNumber = 0x93
        Command = Command.SerializeToString()
        self.UART.write(Command)
        received_len = self.UART.read(2).hex()
        try:
            bytes_read = self.UART.read(int(received_len, 16))
            Result.ParseFromString(bytes_read)
            self.VER_LOG_BRS.append("Вход в Security access:\n")
            self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[0].data.hex())}\nПринято:{str(Result.frame[1].data.hex())}")
            self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[2].data.hex())}\nПринято:{str(Result.frame[3].data.hex())}")
            self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[4].data.hex())}\nПринято:{str(Result.frame[5].data.hex())}\n")
            self.VER_LOG_BRS.append("Изменение режима:\n")
            self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[6].data.hex())}\nПринято:{str(Result.frame[7].data.hex())}\n")
            self.VER_LOG_BRS.append("Перезагрузка:")
            self.VER_LOG_BRS.append(f"Отправлено:{str(Result.frame[8].data.hex())}\nПринято:{str(Result.frame[9].data.hex())}")
        except:
            self.VER_LOG_BRS.append("Ошибка конфигурации. Перезапустите СТО и попробуйте ещё раз:\n")
        self.UART.close()
        self.EnableAll()

    def run_Config_version(self, ver):
        Receiver = threading.Thread(target=self.Config_version,args=(ver,))
        Receiver.start()

    def on_click(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self.reprogramming_tab, 'Open File', './', " (*.hex)")
        if file:
            self.textBrowser_2.append(file)
            self.file=file
            self.pushButton_3.setEnabled(True)

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def update_speed_label(self, value):
        # Обновляем текст метки с учетом шага 0.1
        self.DIAG_SPEED_SELECTOR_2.setText(f"Отправляемая скорость: {value / 100:.1f}")
    def update_mileage_label(self, value):
        # Обновляем текст метки с учетом шага 0.1
        self.DIAG_MILEAGE_SELECTOR_2.setText(f"Отправляемый пробег: {int(value/100)} км")

    def close_com(self):
        self.UART.close()
        self.DisableAll()
    def update_plot(self):
        self.tstart_min_input.setMaximum(self.t1_input.value()-1)
        self.tstart_max_input.setMaximum(self.t2_input.value()-1)
        self.t1_input.setMinimum(1)
        self.t1_input.setMaximum(self.t3_input.value()-1)
        self.t2_input.setMinimum(1)
        self.t2_input.setMaximum(self.t3_input.value()-1)
        self.t3_input.setMinimum(self.t2_input.value()+1)
        self.t3_input.setMaximum(self.tend_max_input.value()-1)
        self.t4_input.setMaximum(self.tend_min_input.value()-1)
        self.t4_input.setMinimum(self.t1_input.value() + 1)
        self.tend_min_input.setMaximum(self.tend_max_input.value()-1)
        self.tend_max_input.setMaximum(500)
        self.limit_ares_input.setMaximum(100-self.ares_range_input.value())
        self.ares_range_input.setMaximum(100-self.limit_ares_input.value())

        self.tstart_min = self.tstart_min_input.value()
        self.tstart_max = self.tstart_max_input.value()
        self.t1 = self.t1_input.value()
        self.t2 = self.t2_input.value()
        self.t3 = self.t3_input.value()
        self.t4 = self.t4_input.value()
        self.tend_min = self.tend_min_input.value()
        self.tend_max = self.tend_max_input.value()
        self.limit_ares = self.limit_ares_input.value()
        self.ares_range = self.ares_range_input.value()
        self.canvas.plot(self.tstart_min,self.t1,self.tstart_max,self.t2,self.t3,self.t4,self.limit_ares,self.ares_range,self.tend_min,self.tend_max)


    def nevjebacca_generator(self):
        self.syntez_btn.setDisabled(True)
        absolute_path = os.path.dirname(__file__)
        relative_path = "acceleration_synthesis\\gen3.exe"
        full_path = os.path.join(absolute_path, relative_path)
#        os.chdir('acceleration_synthesis')
        Limit_ares = str(self.limit_ares_input.value())
        Ares_range = str(self.ares_range_input.value())
        side_of_collision = self.sideinput.currentText()
        time_start_max = str(self.tstart_max_input.value())# начало коридора  # ms
        time_end_max = str(self.tend_max_input.value())  # конец коридора  # ms
        time_up_max = str(self.t2_input.value()-self.tstart_max_input.value())  # ширина коридора (время) # ms  < (time_end - time_start)/2/(1+Limit_Ares/(Limit_Ares+Ares_range))
        time_down_max = str(self.tend_max_input.value()-self.t3_input.value())
        time_start_min = str(self.tstart_max_input.value())
        time_end_min = str(self.tend_min_input.value())
        time_up_min = str(self.t1_input.value()-self.tstart_min_input.value())
        time_down_min = str(self.tend_min_input.value()-self.t4_input.value())
        time_step = str(self.timestep_input.value())
        time_before_collision = str(60)#str(self.timebeforecollis_input.value())
        name_of_output_file = self.file
        proc= subprocess.Popen(
            [full_path, Limit_ares, Ares_range, side_of_collision, time_start_max, time_end_max, time_up_max,
             time_down_max, time_start_min, time_end_min, time_up_min, time_down_min, time_step, time_before_collision,
             name_of_output_file],stdout=subprocess.PIPE)
        #os.chdir('..')
        self.syntez_btn.setEnabled(True)
    def run_nevjebacca_generator(self):
        Receiver = threading.Thread(target=self.nevjebacca_generator)
        Receiver.start()

    def on_click2(self):
        os.chdir('acceleration_synthesis')
        os.chdir('Generated_acc')
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self.params_tab, 'Save as', './', " (*.csv)")
        if file:
            self.file = file
           # print(self.file)
        self.run_nevjebacca_generator()
        os.chdir('..')
        os.chdir('..')

    def on_click3(self):
        os.chdir('parameters')
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self.params_tab, 'Save as', './', " (*.txt)")
        if file:
            self.file = file
            #print(self.file)
        self.run_save_params(file)
        os.chdir('..')



class Communicate(QtCore.QObject):
    progress_changed = QtCore.pyqtSignal(int)

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        super(PlotCanvas, self).__init__(fig)
#        self.setParent(parent)

    def plot(self,tstart_min,t1,tstart_max,t2,t3,t4,limit_ares,ares_range,tend_min,tend_max):
        # Example data

        x_left1 = np.linspace(tstart_min, t1, 300)
        x_left2 = np.linspace(tstart_max, t2, 300)
        x_mid2 = np.linspace(t2, t3, t3-t2)
        x_mid1 = np.linspace(t1, t4, t4-t1)
        x_right1= np.linspace(t4,tend_min, 300)
        x_right2 = np.linspace(t3, tend_max, 300)
        k1=limit_ares/(t1-tstart_min)
        b1=-k1*tstart_min
        k2=(limit_ares+ares_range)/(t2-tstart_max)
        b2 = -k2 * tstart_max
        k5=limit_ares/(t4-tend_min)
        k6=(limit_ares+ares_range)/(t3-tend_max)
        b5 = -k5 * tend_min
        b6 = -k6 * tend_max
        y1 = k1*x_left1+b1
        y2=k2*x_left2+b2
        y3 = [limit_ares+ares_range for i in range(t2,t3)]
        y4 = [limit_ares for i in range(t1,t4)]
        y5 = (k5 * x_right1 + b5)
        y6 = (k6 * x_right2 + b6)
        self.ax.clear()  # Clear the previous graph
        self.ax.plot(x_left1, y1,color='#CD5C5C')
        plt.grid(True)
        plt.xlim(min([tstart_min,tstart_max,tend_min,tend_max,t1,t2,t3,t4]),max([tstart_min,tstart_max,tend_min,tend_max,t1,t2,t3,t4])+10)
        plt.ylim(0, 120)
        self.ax.plot(x_left2, y2,color='#CD5C5C')
        self.ax.plot(x_mid1, y4,color='#CD5C5C')
        self.ax.plot(x_mid2, y3,color='#CD5C5C')
        self.ax.plot(x_right1, y5,color='#CD5C5C')
        self.ax.plot(x_right2, y6,color='#CD5C5C')
        plt.axvline(t1,linestyle='--')
        plt.scatter(t1, 0, marker='*')
        plt.text(t1, -40, "t1")
        plt.axvline(t2, linestyle='--')
        plt.scatter(t2, 0, marker='*')
        plt.text(t2, -40, "t2")
        plt.axvline(t3, linestyle='--')
        plt.scatter(t3, 0, marker='*')
        plt.text(t3, -40, "t3")
        plt.axvline(t4, linestyle='--')
        plt.scatter(t4, 0, marker='*')
        plt.text(t4, -40, "t4")
        plt.scatter(tstart_min,0,marker='*')
        plt.text(tstart_min,-40,"$t_{start}{ min}$")
        plt.scatter(tstart_max, 0, marker='*')
        plt.text(tstart_max, -40, "$t_{start}  {max}$")
        plt.scatter(tend_min, 0, marker='*')
        plt.text(tend_min, -40, "$t_{end}  {min}$")
        plt.scatter(tend_max, 0, marker='*')
        plt.text(tend_max, -40, "$t_{end}  {max}$")
#        self.ax.legend()
        self.draw()  # Refresh the canvasb v

def load_stylesheet(file_name):
    with open(file_name, "r") as file:
        return file.read()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stylesheet = load_stylesheet("style.qss")
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

