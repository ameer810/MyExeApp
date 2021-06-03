# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1246, 745)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("\n"
"/*\n"
"ABOUT\n"
"============================================================================================================\n"
"version 2.05\n"
"QT theme (stylesheet) specially developed for FreeCAD (http://www.freecadweb.org/).\n"
"It might work with other software that uses QT styling.\n"
"\n"
"\n"
"LICENSE\n"
"============================================================================================================\n"
"Copyright (c) 2016 Pablo Gil Fern?ndez\n"
"\n"
"This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.\n"
"To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.\n"
"\n"
"\n"
"INSTALLATION\n"
"============================================================================================================\n"
"1) Place the .qss files and /images/ folder in the path that fits your OS:\n"
"    OSX = /Users/[YOUR_USER_NAME]/Library/Preferences/FreeCAD/Gui/Stylesheets/\n"
"    WINDOWS = C:/[INSTALLATION_PATH]/FreeCAD/data/Gui/Stylesheets/\n"
"    LINUX = /home/[YOUR_USER_NAME]/.FreeCAD/Gui/Stylesheets/\n"
"\n"
"2) In order to display correctly images:\n"
"    2.1) FreeCAD 0.16 (development builds newer than commit 5b3d50a): that\'s it, you are done!\n"
"\n"
"    2.2) FreeCAD 0.15: Images used in the theme need ABSOLUTE paths to be found by FreeCAD, so you should search the string \"qss:images\" (without \"\") and replace with the real path of your computer. It should be done with all the .qss files you want to install-use\n"
"        find = qss:images\n"
"        replace = /Users/myName/Library/Preferences/FreeCAD/Gui/Stylesheets/images\n"
"\n"
"\n"
"CUSTOMIZATION\n"
"============================================================================================================\n"
"If you would like to change the overall look/style of the theme, just find and replace following colors in the whole file:\n"
"    BACKGROUND (darker to ligher)\n"
"        black\n"
"        #505050\n"
"        #6e6e6e\n"
"        #828282\n"
"        #a2a2a0\n"
"        #b6b6b6\n"
"        #c8c8c8\n"
"        #c3c3c3\n"
"        #d2d2d2\n"
"        #dcdcdc\n"
"        #e0e0e0\n"
"        #e6e6e6\n"
"        #f0f0f0\n"
"        #f5f5f5 = main background color\n"
"        white\n"
"\n"
"    SELECTION (darker to lighter)\n"
"        #1b3774\n"
"        #2053c0\n"
"        #3874f2\n"
"        #5e90fa = main selection color\n"
"        #6f9efa = used to build QSpinBox up and down buttons, it\'s used as color in the middle\n"
"        #7cabf9\n"
"        #adc5ed\n"
"        #cbd8e6\n"
"\n"
"\n"
"\n"
"\n"
"KNOWN BUGS and TO DO\n"
"============================================================================================================\n"
"    - please, follow the link to get updated information: http://forum.freecadweb.org/viewtopic.php?f=10&t=12417\n"
"*/\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Reset elements\n"
"==================================================================================================*/\n"
"/* Reseting everything helps to unify styles across different operating systems */\n"
"* {\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"    border-style: none;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* specific reset for elements inside QToolBar */\n"
"QToolBar * {\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Main window\n"
"==================================================================================================*/\n"
"QMainWindow,\n"
"QDialog,\n"
"QDockWidget,\n"
"QToolBar  {\n"
"    background-color: #f5f5f5; /* main background color */\n"
"}\n"
"\n"
"QMdiArea {\n"
"    background-image: url(qss:images/background_freecad.png);\n"
"    background-position: center center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"MENUS\n"
"==================================================================================================*/\n"
"QMenuBar,\n"
"QMenuBar::item {\n"
"    color: black;\n"
"    background-color: #f5f5f5; /* main background color */\n"
"}\n"
"\n"
"QMenu,\n"
"QMenu::item {\n"
"    color: black;\n"
"    background-color: #f5f5f5; /* main background color */\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QMenuBar::item:selected,\n"
"QMenuBar::item:pressed,\n"
"QMenu::item:selected,\n"
"QMenu::item:pressed {\n"
"    color: white;\n"
"    background-color: #5e90fa;\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    image:url(qss:images/right_arrow_dark.png);\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QMenu::right-arrow:selected {\n"
"    image:url(qss:images/right_arrow_lighter.png);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 16px 2px 26px; /* make room for icon at left */\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::icon {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: rgba(0,0,0,30);\n"
"    margin: 6px 4px;\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    color: white;\n"
"}\n"
"\n"
"/* Fix for elements inside a drop-down menu */\n"
"QMenu QRadioButton,\n"
"QMenu QCheckBox,\n"
"QMenu QPushButton,\n"
"QMenu QToolButton {\n"
"    color: black; /* same as regular QRadioButton and QCheckBox */\n"
"}\n"
"\n"
"QMenu QRadioButton:hover,\n"
"QMenu QCheckBox:hover,\n"
"QMenu QPushButton:hover,\n"
"QMenu QToolButton:hover,\n"
"QMenu QPushButton:pressed,\n"
"QMenu QToolButton:pressed,\n"
"QMenu QPushButton:selected,\n"
"QMenu QToolButton:selected {\n"
"    color: white;\n"
"    background-color: #5e90fa; /* same as QMenu::item:selected and QMenu::item:pressed */\n"
"}\n"
"\n"
"QMenu QRadioButton:disabled,\n"
"QMenu QCheckBox:disabled {\n"
"    color: #6e6e6e;\n"
"}\n"
"\n"
"QMenu QRadioButton::indicator:disabled,\n"
"QMenu QCheckBox::indicator:disabled {\n"
"    color: #6e6e6e;\n"
"    background-color: transparent;\n"
"    border: 1px solid #6e6e6e;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tool bar\n"
"==================================================================================================*/\n"
"QToolBar {\n"
"    border: none;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolBar::handle:top,\n"
"QToolBar::handle:bottom,\n"
"QToolBar::handle:horizontal {\n"
"    background-image: url(qss:images/Hmovetoolbar_dark.png);\n"
"    width: 10px;\n"
"    margin: 4px 2px;\n"
"    background-position: top right;\n"
"    background-repeat: repeat-y;\n"
"}\n"
"\n"
"QToolBar::handle:left,\n"
"QToolBar::handle:right,\n"
"QToolBar::handle:vertical {\n"
"    background-image: url(qss:images/Vmovetoolbar_dark.png);\n"
"    height: 10px;\n"
"    margin: 2px 4px;\n"
"    background-position: left bottom;\n"
"    background-repeat: repeat-x;\n"
"}\n"
"\n"
"QToolBar::separator:top,\n"
"QToolBar::separator:bottom,\n"
"QToolBar::separator:horizontal {\n"
"    width: 1px;\n"
"    margin: 6px 4px;\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"QToolBar::separator:left,\n"
"QToolBar::separator:right,\n"
"QToolBar::separator:vertical {\n"
"    height: 1px;\n"
"    margin: 4px 6px;\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Group box\n"
"==================================================================================================*/\n"
"QGroupBox {\n"
"    color: rgba(0,0,0,120);\n"
"    border:1px solid rgba(0, 0, 0, 20); /* lighter than its own border-color */;\n"
"    border-radius: 3px;\n"
"    margin-top: 10px;\n"
"    padding: 6px;\n"
"    background-color: rgba(255, 255, 255, 15);\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    top: -8px;\n"
"    left: 12px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tooltip\n"
"==================================================================================================*/\n"
"QToolTip {\n"
"    color: white;\n"
"    background-color: #828282;\n"
"    /*opacity: 90%; doesn\'t correctly work */\n"
"    padding: 4px;\n"
"    border-radius: 3px; /* has no effect */\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Dock widget\n"
"==================================================================================================*/\n"
"QDockWidget {\n"
"    color: rgba(0,0,0,120);\n"
"    titlebar-close-icon: url(qss:images/close_dark.png);\n"
"    titlebar-normal-icon: url(qss:images/undock_dark.png);\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: center;\n"
"    background-color: rgba(0,0,0,10);\n"
"    border: 4px solid #f5f5f5; /* fix to simulate margin between this :title and tabs */ /* same as main background color */\n"
"    border-radius: 6px; /* bigger than normal due to previous border fix */\n"
"    padding: 4px 0px; /* also needed because of previous border fix */\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button {\n"
"    border: none;\n"
"    background: transparent;\n"
"    border-radius: 3px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"    right: 4px;\n"
"}\n"
"    \n"
"QDockWidget::float-button {\n"
"    right: 22px;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover,\n"
"QDockWidget::float-button:hover {\n"
"    background-color: rgba(0,0,0,15);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed,\n"
"QDockWidget::float-button:pressed {\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"/* fix for Python Console (probably there is a smarter way to arrive to it) */\n"
"QDockWidget > QFrame {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #c3c3c3;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Progress bar\n"
"==================================================================================================*/\n"
"QProgressBar,\n"
"QProgressBar:horizontal {\n"
"    color: white;\n"
"    background-color: rgba(0,0,0,10);\n"
"    text-align: center;\n"
"    border: 1px solid rgba(0,0,0,80);\n"
"    padding: 1px;\n"
"    border-radius: 3px;\n"
"}\n"
"QProgressBar::chunk,\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #3874f2, stop:1 #5e90fa);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Scroll\n"
"==================================================================================================*/\n"
"QAbstractScrollArea {\n"
"    border-radius: 2px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: transparent;\n"
"    height: 15px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgba(0,0,0,80);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgba(0,0,0,100);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 5px;\n"
"    border-radius: 3px;\n"
"    margin: 4px 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    margin: 1px 3px 0px 3px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/left_arrow_dark.png);\n"
"    width: 6px;\n"
"    height: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    margin: 1px 3px 0px 3px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/right_arrow_dark.png);\n"
"    width: 6px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on {\n"
"    border-image: url(qss:images/left_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::add-line:horizontal:on {\n"
"    border-image: url(qss:images/right_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: transparent;\n"
"    width: 15px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 5px;\n"
"    border-radius: 3px;\n"
"    margin: 15px 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    margin: 3px 0px 3px 1px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/up_arrow_dark.png);\n"
"    height: 6px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    margin: 3px 0px 3px 1px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/down_arrow_dark.png);\n"
"    height: 6px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on {\n"
"    border-image: url(qss:images/up_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on {\n"
"    border-image: url(qss:images/down_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tab bar\n"
"==================================================================================================*/\n"
"QTabWidget::pane {\n"
"    background-color: transparent; /* temporal (transparent background) */ /* tab content background color */\n"
"    position: absolute;\n"
"}\n"
"\n"
"QTabWidget::pane:top {\n"
"    top: -1px;\n"
"    border-top: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom {\n"
"    bottom: -1px;\n"
"    border-bottom: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::pane:left {\n"
"    right: -1px;\n"
"    border-right: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::pane:right {\n"
"    left: -1px;\n"
"    border-left: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top,\n"
"QTabWidget::tab-bar:bottom {\n"
"    left: 10px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left,\n"
"QTabWidget::tab-bar:right {\n"
"    top: 10px;\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0; /* important */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Workaround for QTabBars created from docked QDockWidgets which don\'t draw the border if not set and reseted as follows: */\n"
"QTabBar {\n"
"    border-top: 1px solid #d2d2d2;  /* set color for all QTabBars */\n"
"}\n"
"QDockWidget QTabBar {\n"
"    border-color: transparent; /* set color for all QTabBars but ones created from QDockWidget */\n"
"}\n"
"QDialog QTabBar {\n"
"    border-color: transparent; /* set color for QTabBars inside Preferences dialog */\n"
"}\n"
"/* end fix */\n"
"\n"
"QTabBar::tab {\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top,\n"
"QTabBar::tab:bottom {\n"
"    border-top-width: 4px; /* same as selected tab colored border in order to center close-button */\n"
"    border-bottom-width: 4px; /* same as selected tab colored border in order to center close-button */\n"
"    min-width: 11ex;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left,\n"
"QTabBar::tab:right {\n"
"    border-left-width: 4px; /* same as selected tab colored border in order to center close-button */\n"
"    border-right-width: 4px; /* same as selected tab colored border in order to center close-button */\n"
"    min-height: 14ex;\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #f5f5f5; /* same as tab content background color */\n"
"    border-color: #d2d2d2;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-top: 4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2); /* selection color */\n"
"    border-bottom-color: #f5f5f5; /* same as tab content background color */\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-bottom: 4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2); /* selection color */\n"
"    border-top-color: #f5f5f5; /* same as tab content background color */\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-left: 4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5e90fa, stop:1 #3874f2); /* selection color */\n"
"    border-right-color: #f5f5f5; /* same as tab content background color */\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-right: 4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5e90fa, stop:1 #3874f2); /* selection color */\n"
"    border-left-color: #f5f5f5; /* same as tab content background color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    color: rgba(0,0,0,160);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: rgba(0,0,0,220);\n"
"    background-color: rgba(0,0,0,20);\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"}\n"
"\n"
"/* hack to access Preference TabBar background */\n"
"QDialog#Gui__Dialog__DlgPreferences > QFrame QFrame {\n"
"    background-color: transparent; /* main background color (in Windows is #f5f5f5) */\n"
"}\n"
"\n"
"/* fix for previous hack that broke QTabWidget background on Windows */\n"
"QDialog#Gui__Dialog__DlgPreferences QTabWidget::pane {\n"
"    background-color: transparent; /* temporal (transparent background) */\n"
"}\n"
"\n"
"/* hack to correctly align Preferences icon list on OSX */\n"
"QDialog#Gui__Dialog__DlgPreferences > QListView {\n"
"    min-width: 130px;\n"
"}\n"
"\n"
"/* unique styles for sections inside Preferences */\n"
"QDialog#Gui__Dialog__DlgPreferences > QListView::item {\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QDialog#Gui__Dialog__DlgPreferences > QListView::item:hover {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"\n"
"QDialog#Gui__Dialog__DlgPreferences > QListView::item:selected {\n"
"    color: white;\n"
"    background-color: #5e90fa;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tab bar buttons\n"
"==================================================================================================*/\n"
"/* Close button */\n"
"QTabBar::close-button {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: center right; /* only works for QT 4.6 and newer */;\n"
"    border-radius: 2px;\n"
"    background-image: url(qss:images/close_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    background-color: rgba(0,0,0,20);\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"/* Fix for lists inside Model tab */\n"
"QDockWidget QTreeView,\n"
"QDockWidget QListView,\n"
"QDockWidget QTableView {\n"
"    margin: 6px;\n"
"    border: 1px solid #c3c3c3; /* same as regular QTreeView, QListView and QTableView */\n"
"    min-height: 40px; /* neccesary in some areas of FreeCAD */\n"
"}\n"
"\n"
"/* Buttons to scroll tabs if there is not space to show all of them: */\n"
"QTabBar::scroller {\n"
"    width: 20px; /* the width of the scroll buttons */\n"
"}\n"
"\n"
"QTabBar QToolButton,\n"
"QTabBar QToolButton:hover {\n"
"    background-color: #f5f5f5; /* same as main background color */\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(qss:images/right_arrow_dark.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled,\n"
"QTabBar QToolButton::right-arrow:off {\n"
"     image: url(qss:images/right_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:hover {\n"
"     image: url(qss:images/right_arrow_darker.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(qss:images/left_arrow_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled,\n"
" QTabBar QToolButton::left-arrow:off {\n"
"     image: url(qss:images/left_arrow_disabled_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::left-arrow:hover {\n"
"     image: url(qss:images/left_arrow_darker.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::up-arrow:enabled {\n"
"     image: url(qss:images/up_arrow_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::up-arrow:disabled,\n"
" QTabBar QToolButton::up-arrow:off {\n"
"     image: url(qss:images/up_arrow_disabled_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::up-arrow:hover {\n"
"     image: url(qss:images/up_arrow_darker.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::down-arrow:enabled {\n"
"     image: url(qss:images/down_arrow_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::down-arrow:disabled,\n"
" QTabBar QToolButton::down-arrow:off {\n"
"     image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::down-arrow:hover {\n"
"     image: url(qss:images/down_arrow_darker.png);\n"
"}\n"
"\n"
"QTabBar::tear {\n"
"    /* default OS tear better */\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tree and list views\n"
"==================================================================================================*/\n"
"QTreeView,\n"
"QListView,\n"
"QTableView {\n"
"    background-color: #f0f0f0;\n"
"    alternate-background-color: #e6e6e6; /* related with QListView background  */\n"
"    border: 1px solid #c3c3c3; \n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa; /* should be similar to QListView::item selected background-color */\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QListView::item:hover,\n"
"QTreeView::item:hover  {\n"
"    background-color: transparent; /* fix to homogenize it on all OSs */\n"
"}\n"
"\n"
"QListView::item:selected,\n"
"QTreeView::item:selected  {\n"
"    color: white; /* should be similar to QListView selection-color */\n"
"    background-color: #5e90fa; /* should be similar to QListView selection-background-color */\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"/* Property Editor QTreeView (FreeCAD custom widget) */\n"
"Gui--PropertyEditor--PropertyEditor {\n"
"    gridline-color: #d2d2d2; /* same as Group header background */\n"
"}\n"
"\n"
"/* fix for column items background when a link is present */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QFrame:focus {\n"
"    background-color: #cbd8e6; /* same as focused background color */\n"
"}\n"
"\n"
"/* hack to hide weird redundant information inside the value of a Placement cell */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QLabel,\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QLabel:disabled {\n"
"    color: transparent;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* hack to hide non editable cells inside Property values */\n"
"Gui--PropertyEditor--PropertyEditor QLineEdit:read-only,\n"
"Gui--PropertyEditor--PropertyEditor QLineEdit:disabled,\n"
"Gui--PropertyEditor--PropertyEditor QAbstractSpinBox:read-only,\n"
"Gui--PropertyEditor--PropertyEditor QAbstractSpinBox:disabled {\n"
"    color: transparent;\n"
"    border-color: transparent;\n"
"    background-color: transparent;\n"
"    selection-color: transparent;\n"
"    selection-background-color: transparent;\n"
"}\n"
"\n"
"/* hack to disable margin inside Property values to following elements */\n"
"Gui--PropertyEditor--PropertyEditor QSpinBox,\n"
"Gui--PropertyEditor--PropertyEditor QDoubleSpinBox,\n"
"Gui--PropertyEditor--PropertyEditor QAbstractSpinBox,\n"
"Gui--PropertyEditor--PropertyEditor QLineEdit,\n"
"Gui--PropertyEditor--PropertyEditor QComboBox {\n"
"    margin-left: 0px;\n"
"    margin-right: 0px;\n"
"    padding-top: 0px;\n"
"    padding-bottom: 0px;\n"
"}\n"
"\n"
"/* reset min-height to 0px inside list views */\n"
"QTreeView > QWidget > QComboBox,\n"
"QTreeView > QWidget > QAbstractSpinBox,\n"
"QTreeView > QWidget > QSpinBox,\n"
"QTreeView > QWidget > QDoubleSpinBox,\n"
"QTreeView > QWidget > QLineEdit,\n"
"QTreeView > QWidget > QTextEdit,\n"
"QTreeView > QWidget > QTimeEdit,\n"
"QTreeView > QWidget > QDateEdit,\n"
"QTreeView > QWidget > QDateTimeEdit,\n"
"QTreeView > QWidget > Gui--ColorButton {\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"/* set border-radius to 0px inside list views */\n"
"QTreeView > QWidget > QComboBox,\n"
"QTreeView > QWidget > QAbstractSpinBox,\n"
"QTreeView > QWidget > QSpinBox,\n"
"QTreeView > QWidget > QDoubleSpinBox,\n"
"QTreeView > QWidget > QLineEdit,\n"
"QTreeView > QWidget > QTextEdit,\n"
"QTreeView > QWidget > QTimeEdit,\n"
"QTreeView > QWidget > QDateEdit,\n"
"QTreeView > QWidget > QDateTimeEdit,\n"
"QTreeView > QWidget > QComboBox:drop-down,\n"
"QTreeView > QWidget > QAbstractSpinBox:up-button,\n"
"QTreeView > QWidget > QSpinBox:up-button,\n"
"QTreeView > QWidget > QDoubleSpinBox:up-button,\n"
"QTreeView > QWidget > QTimeEdit:up-button,\n"
"QTreeView > QWidget > QDateEdit:up-button,\n"
"QTreeView > QWidget > QDateTimeEdit:up-button,\n"
"QTreeView > QWidget > QAbstractSpinBox:down-button,\n"
"QTreeView > QWidget > QSpinBox:down-button,\n"
"QTreeView > QWidget > QDoubleSpinBox:down-button,\n"
"QTreeView > QWidget > QTimeEdit:down-button,\n"
"QTreeView > QWidget > QDateEdit:down-button,\n"
"QTreeView > QWidget > QDateTimeEdit:down-button,\n"
"QTreeView > QWidget > Gui--ColorButton {\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* set focus colors to best viewing the editable fields */\n"
"QTreeView > QWidget > QComboBox:focus,\n"
"QTreeView > QWidget > QAbstractSpinBox:focus,\n"
"QTreeView > QWidget > QSpinBox:focus,\n"
"QTreeView > QWidget > QDoubleSpinBox:focus,\n"
"QTreeView > QWidget > QLineEdit:focus,\n"
"QTreeView > QWidget > QTextEdit:focus,\n"
"QTreeView > QWidget > QTimeEdit:focus,\n"
"QTreeView > QWidget > QDateEdit:focus,\n"
"QTreeView > QWidget > QDateTimeEdit:focus {\n"
"    border-color: #cbd8e6; /* same as focused background color */\n"
"    border-bottom-color: #7cabf9; /* same as focused border color */\n"
"}\n"
"\n"
"QTreeView > QWidget > QAbstractSpinBox:read-only,\n"
"QTreeView > QWidget > QSpinBox:read-only,\n"
"QTreeView > QWidget > QDoubleSpinBox:read-only,\n"
"QTreeView > QWidget > QLineEdit:read-only,\n"
"QTreeView > QWidget > QTextEdit:read-only,\n"
"QTreeView > QWidget > QTimeEdit:read-only,\n"
"QTreeView > QWidget > QDateEdit:read-only,\n"
"QTreeView > QWidget > QDateTimeEdit:read-only {\n"
"    color: transparent;\n"
"    background-color: transparent;\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"/* Fix to correctly (not totally) draw QTextEdit on OSX at Page properties: \"Page result\", \"Template\" and \"Editable Texts\" */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QWidget {\n"
"    min-height: 14px;\n"
"    border-radius: 0px; /* reset */\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Header of tree and list views\n"
"==================================================================================================*/\n"
"QHeaderView {\n"
"    background-color: #c3c3c3;\n"
"    border-top-left-radius: 2px; /* 1px less than its container */\n"
"    border-top-right-radius: 2px; /* 1px less than its container */\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border:none;\n"
"    padding: 4px 6px;\n"
"    background-color: #c3c3c3;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    padding: 4px 6px; /* left and right value similar to QHeaderView::section */\n"
"    border-right: 1px solid rgba(0,0,0,30);\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border-bottom: 1px solid rgba(0,0,0,30);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #c3c3c3;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: 1px solid rgba(0,0,0,30);\n"
"    border-bottom: 1px solid rgba(0,0,0,30);\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-right: none;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(qss:images/up_arrow_dark.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow:hover {\n"
"    image: url(qss:images/up_arrow_darker.png);\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    image: url(qss:images/down_arrow_dark.png);\n"
"}\n"
"\n"
"QHeaderView::down-arrow:hover {\n"
"    image: url(qss:images/down_arrow_darker.png);\n"
"}\n"
"\n"
"/* Group header inside Property Editor (FreeCAD custom widget) */\n"
"Gui--PropertyEditor--PropertyEditor {\n"
"    qproperty-groupTextColor: #828282; /* same as main background color */\n"
"    qproperty-groupBackground: #d2d2d2; /* same as item gridlines */\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Branch system for QTreeViews\n"
"==================================================================================================*/\n"
"QTreeView::branch  {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item  {\n"
"    border-image: url(qss:images/branch_vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item  {\n"
"    border-image: url(qss:images/branch_more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item  {\n"
"    border-image: url(qss:images/branch_end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings  {\n"
"    image: url(qss:images/branch_closed_dark.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed  {\n"
"    image: url(qss:images/branch_closed_dark.png);\n"
"    border-image: url(qss:images/branch_end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(qss:images/branch_open_dark.png);\n"
"    border-image: url(qss:images/branch_more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings  {\n"
"    image: url(qss:images/branch_open_dark.png);\n"
"    border-image: url(qss:images/branch_end.png) 0;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Splitter and windows separator\n"
"==================================================================================================*/\n"
"QSplitter::handle {\n"
"    margin: 0px 11px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    background-image: url(qss:images/splitter_vertical_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"    margin: 4px 2px 4px 2px;\n"
"    width: 2px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    background-image: url(qss:images/splitter_horizontal_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"    margin: 2px 4px 2px 4px;\n"
"    height: 2px;\n"
"}\n"
"\n"
"/* Similar to the splitter is the following window separator (but horizontal/vertical is on the opposite way) */\n"
"QMainWindow::separator {\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"    height: 2px;\n"
"    background-image: url(qss:images/splitter_horizontal_dark.png);\n"
"    margin: 4px 2px 4px 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"    width: 2px;\n"
"    background-image: url(qss:images/splitter_vertical_dark.png);\n"
"    margin: 2px 4px 2px 4px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Text/Python editor (macros, etc...)\n"
"==================================================================================================*/\n"
"QPlainTextEdit,\n"
"QPlainTextEdit:focus {\n"
"    background-color: #f0f0f0;\n"
"    selection-color: white;\n"
"    selection-background-color: #3874f2;\n"
"    border: 1px solid #c3c3c3;\n"
"    border-radius: 3px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tasks panel (custom FreeCAD class)\n"
"==================================================================================================*/\n"
"/* Action group */\n"
"QFrame[class=\"panel\"] {\n"
"    background-color: transparent; /* temporal (transparent background) */\n"
"}\n"
"\n"
"QSint--ActionGroup {\n"
"    padding: 0px; /* if not reset, it might create problems with QPushButtons and other elements */\n"
"    margin: 0px; /* if not reset, it might create problems with QPushButtons and other elements */\n"
"}\n"
"\n"
"/* Separator line */\n"
"QSint--ActionGroup QFrame[height=\"1\"],\n"
"QSint--ActionGroup QFrame[height=\"2\"],\n"
"QSint--ActionGroup QFrame[height=\"3\"],\n"
"QSint--ActionGroup QFrame[width=\"1\"],\n"
"QSint--ActionGroup QFrame[width=\"2\"],\n"
"QSint--ActionGroup QFrame[width=\"3\"] {\n"
"    border-color: rgba(0,0,0,60);\n"
"}\n"
"\n"
"/* Panel header */\n"
"QSint--ActionGroup QFrame[class=\"header\"] {\n"
"    border: none;\n"
"    background-color: #b6b6b6; /* Task Panel Header background color */\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"]:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"header\"] {\n"
"    color: white; /* Task Panel Header text color */\n"
"    text-align: left;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel {\n"
"    background-color: transparent;\n"
"    background-image: url(qss:images/down_arrow_light.png);\n"
"    background-repeat: none;\n"
"    background-position: center center;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel:hover {\n"
"    background-color: transparent;\n"
"    background-image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel[fold=\"true\"] {\n"
"    background-color: transparent;\n"
"    background-image: url(qss:images/up_arrow_light.png);\n"
"    background-repeat: none;\n"
"    background-position: center center;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel[fold=\"true\"]:hover {\n"
"    background-color: transparent;\n"
"    background-image: url(qss:images/up_arrow_lighter.png);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] {\n"
"    background-color: #e6e6e6; /* Task Panel background color */\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    border: none;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] > QWidget {\n"
"    background-color: #e6e6e6; /* Task Panel background color */\n"
"}\n"
"\n"
"/* Fixs for tabs inside Task Panel */\n"
"QSint--ActionGroup QFrame[class=\"content\"] QTabBar::tab:top:selected {\n"
"    border-bottom-color: #e6e6e6; /* same as Task Panel background color */\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QTabBar::tab:bottom:selected {\n"
"    border-top-color: #e6e6e6; /* same as Task Panel background color */\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QTabBar::tab:right:selected {\n"
"    border-right-color: #e6e6e6; /* same as Task Panel background color */\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QTabBar::tab:left:selected {\n"
"    border-left-color: #e6e6e6; /* same as Task Panel background color */\n"
"}\n"
"\n"
"/* Fix for buttons with icons that showed cropped (still not happy with result) */\n"
"QSint--ActionGroup QFrame[class=\"content\"] > QWidget > QPushButton {\n"
"    padding: 2px; /* bigger padding crops text and icons... */\n"
"    margin: 0px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Buttons\n"
"==================================================================================================*/\n"
"/* Common */\n"
"QComboBox,\n"
"QAbstractSpinBox,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QLineEdit,\n"
"QTextEdit,\n"
"QTimeEdit,\n"
"QDateEdit,\n"
"QDateTimeEdit {\n"
"    color: #6e6e6e;\n"
"    background-color: #e0e0e0;\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 3px;\n"
"    min-width: 50px; /* it ensures the default value is correctly displayed */\n"
"    min-height: 20px; /* important to be a pair number in order to up/down buttons to be divisible by two (if not set could create a blank line in Ubuntu. Its downside is that it\'s needed to reset it (min-width: 0px) on following elements that can\'t have it such as fields inside QToolBar and inside QTreeView (Property editor) */\n"
"    padding: 1px 2px; /* temporal: could don\'t be compatible with elements inside Tree/List view */\n"
"}\n"
"\n"
"/* shifts text/number editable field to the left to make space for the up/down or drop-down buttons */\n"
"QComboBox,\n"
"QAbstractSpinBox,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTimeEdit,\n"
"QDateEdit,\n"
"QDateTimeEdit {\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"/* when QTextEdit are no editable */\n"
"QTextEdit:!editable {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #c3c3c3;\n"
"}\n"
"\n"
"QComboBox:focus,\n"
"QAbstractSpinBox:focus,\n"
"QSpinBox:focus,\n"
"QDoubleSpinBox:focus,\n"
"QLineEdit:focus,\n"
"QTextEdit:focus,\n"
"QTimeEdit:focus,\n"
"QDateEdit:focus,\n"
"QDateTimeEdit:focus {\n"
"    color: black;\n"
"    border-color: #7cabf9;\n"
"    border-right-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #7cabf9); /* same as up/down or drop-down button color */\n"
"    background-color: #cbd8e6;\n"
"}\n"
"\n"
"QComboBox:disabled,\n"
"QAbstractSpinBox:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled,\n"
"QLineEdit:disabled,\n"
"QTextEdit:disabled,\n"
"QTimeEdit:disabled,\n"
"QDateEdit:disabled,\n"
"QDateTimeEdit:disabled {\n"
"    color: #c3c3c3;\n"
"    background-color: #e0e0e0; /* same as enabled color */\n"
"    border-color: #e0e0e0; /* same as enabled color */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button,\n"
"QSpinBox:up-button,\n"
"QDoubleSpinBox:up-button,\n"
"QTimeEdit:up-button,\n"
"QDateEdit:up-button,\n"
"QDateTimeEdit:up-button,\n"
"QAbstractSpinBox:down-button,\n"
"QSpinBox:down-button,\n"
"QDoubleSpinBox:down-button,\n"
"QTimeEdit:down-button,\n"
"QDateEdit:down-button,\n"
"QDateTimeEdit:down-button {\n"
"    background-color: #d2d2d2;\n"
"    subcontrol-origin: border; /* important */\n"
"    width: 20px; /* same as QComboBox ... QDateTimeEdit padding-right */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button,\n"
"QSpinBox:up-button,\n"
"QDoubleSpinBox:up-button,\n"
"QTimeEdit:up-button,\n"
"QDateEdit:up-button,\n"
"QDateTimeEdit:up-button {\n"
"    subcontrol-position: top right;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button,\n"
"QSpinBox:down-button,\n"
"QDoubleSpinBox:down-button,\n"
"QTimeEdit:down-button,\n"
"QDateEdit:down-button,\n"
"QDateTimeEdit:down-button {\n"
"    subcontrol-position: bottom right;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button:focus,\n"
"QSpinBox:up-button:focus,\n"
"QDoubleSpinBox:up-button:focus,\n"
"QTimeEdit:up-button:focus,\n"
"QDateEdit:up-button:focus,\n"
"QDateTimeEdit:up-button:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #6f9efa, stop:1 #7cabf9);\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button:focus,\n"
"QSpinBox:down-button:focus,\n"
"QDoubleSpinBox:down-button:focus,\n"
"QTimeEdit:down-button:focus,\n"
"QDateEdit:down-button:focus,\n"
"QDateTimeEdit:down-button:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #6f9efa);\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button:disabled,\n"
"QSpinBox:up-button:disabled,\n"
"QDoubleSpinBox:up-button:disabled,\n"
"QTimeEdit:up-button:disabled,\n"
"QDateEdit:up-button:disabled,\n"
"QDateTimeEdit:up-button:disabled,\n"
"QAbstractSpinBox:down-button:disabled,\n"
"QSpinBox:down-button:disabled,\n"
"QDoubleSpinBox:down-button:disabled,\n"
"QTimeEdit:down-button:disabled,\n"
"QDateEdit:down-button:disabled,\n"
"QDateTimeEdit:down-button:disabled {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QTimeEdit::up-arrow,\n"
"QDateEdit::up-arrow,\n"
"QDateTimeEdit::up-arrow {\n"
"    image: url(qss:images/up_arrow_dark.png);\n"
"    top: 2px; /* fix symmetry between up and down images */\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:focus,\n"
"QSpinBox::up-arrow:focus,\n"
"QDoubleSpinBox::up-arrow:focus,\n"
"QTimeEdit::up-arrow:focus,\n"
"QDateEdit::up-arrow:focus,\n"
"QDateTimeEdit::up-arrow:focus {\n"
"    image: url(qss:images/up_arrow_lighter.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:off,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:off,\n"
"QTimeEdit::up-arrow:off,\n"
"QDateEdit::up-arrow:off,\n"
"QDateTimeEdit::up-arrow:off {\n"
"    image: url(qss:images/up_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QTimeEdit::up-arrow:disabled,\n"
"QDateEdit::up-arrow:disabled,\n"
"QDateTimeEdit::up-arrow:disabled {\n"
"    image: url(qss:images/up_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QTimeEdit::down-arrow,\n"
"QDateEdit::down-arrow,\n"
"QDateTimeEdit::down-arrow {\n"
"    image: url(qss:images/down_arrow_dark.png);\n"
"    bottom: 0px; /* fix simetry between up and down images */\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:focus,\n"
"QSpinBox::down-arrow:focus,\n"
"QDoubleSpinBox::down-arrow:focus,\n"
"QTimeEdit::down-arrow:focus,\n"
"QDateEdit::down-arrow:focus,\n"
"QDateTimeEdit::down-arrow:focus {\n"
"    image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:off,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:off,\n"
"QTimeEdit::down-arrow:off,\n"
"QDateEdit::down-arrow:off,\n"
"QDateTimeEdit::down-arrow:off {\n"
"    image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QTimeEdit::down-arrow:disabled,\n"
"QDateEdit::down-arrow:disabled,\n"
"QDateTimeEdit::down-arrow:disabled {\n"
"    image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox::drop-down {\n"
"    background-color: #d2d2d2;\n"
"    subcontrol-origin: border; /* important */\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:on,\n"
"QComboBox::drop-down:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #7cabf9);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(qss:images/down_arrow_dark.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:focus {\n"
"    image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:off,\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"/* ComboBox menu */\n"
"QComboBox {\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #6e6e6e; /* same as regular QComboBox color */\n"
"    background-color: transparent;\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"    border-width: 5px 0px 5px 0px;\n"
"    border-style: solid;\n"
"    border-color: transparent;\n"
"    margin: 0px -1px 0px 0px; /* temporal: hack for Mac... try it on Windows and Linux */\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Push button\n"
"==================================================================================================*/\n"
"\n"
"\n"
"/* Fix for Expressions description QFrame that is \"broken\" with initial reset */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QWidget > QWidget > QFrame {\n"
"    background-color: #f5f5f5; /* main background color */\n"
"    border: 1px solid #dcdcdc;\n"
"    border-radius: 2px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #5e90fa;\n"
"    border-color: #3874f2;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tool button inside QDialogs that works as QPushButtons\n"
"==================================================================================================*/\n"
"/* found under Tools -> Customize -> Macros -> Pixmap \"...\" button */\n"
"QDialog QToolButton {\n"
"    color: #6e6e6e;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.3, x2:0, y2:1, stop:0 #f5f5f5, stop:1 #e6e6e6);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"    padding: 0px; /* different than regular QPushButton */\n"
"    margin: 2px; /* different than regular QPushButton */\n"
"    min-height: 16px; /* same as QTabBar QPushButton min-width */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QDialog QToolButton:hover,\n"
"QDialog QToolButton:focus {\n"
"    color: white;\n"
"    border-color: #3874f2;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"}\n"
"\n"
"QDialog QToolButton:disabled,\n"
"QDialog QToolButton:disabled:checked {\n"
"    color: #b6b6b6;\n"
"    border-color: #e6e6e6;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QDialog QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tool button inside Task Panel content that works as QPushButtons\n"
"==================================================================================================*/\n"
"/* found inside Part Design Workbench and \"make a draft on a face\" Task panel options */\n"
"QSint--ActionGroup QFrame[class=\"content\"] QToolButton {\n"
"    color: #6e6e6e;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.3, x2:0, y2:1, stop:0 #f5f5f5, stop:1 #e6e6e6);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"    padding: 2px 6px; /* different than regular QPushButton */\n"
"    margin: 2px; /* different than regular QPushButton */\n"
"    min-height: 16px; /* same as QTabBar QPushButton min-width */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QToolButton:hover,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QToolButton:focus {\n"
"    color: white;\n"
"    border-color: #3874f2;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QToolButton:disabled,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QToolButton:disabled:checked {\n"
"    color: #b6b6b6;\n"
"    border-color: #e6e6e6;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Radio button\n"
"==================================================================================================*/\n"
"QRadioButton::indicator:unchecked{\n"
"    color: #505050;\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"    border: 1px solid #505050;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #5e90fa; /* QCheckBox has the same color */\n"
"    border: 1px solid #3874f2; /* QCheckBox has the same color */\n"
"    image:url(qss:images/radiobutton_light.png);\n"
"}\n"
"\n"
"QRadioButton,\n"
"QRadioButton:disabled {\n"
"    color: #505050;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 11px;\n"
"    height: 11px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    border-color: #adc5ed;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    color: #6e6e6e;\n"
"    background-color: transparent;\n"
"    border: 1px solid #6e6e6e;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Checkbox\n"
"==================================================================================================*/\n"
"QCheckBox,\n"
"QCheckBox:disabled {\n"
"    color: #505050;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    color: #c8c8c8;\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #505050;\n"
"    width: 11px;\n"
"    height: 11px;\n"
"    border-radius:2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed,\n"
"QCheckBox::indicator:non-exclusive:checked:pressed,\n"
"QCheckBox::indicator:indeterminate:pressed,\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border-color: #adc5ed;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5e90fa; /* QRadioButton has the same color */\n"
"    border: 1px solid #3874f2; /* QRadioButton has the same color */\n"
"    image:url(qss:images/checkbox_light.png);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgba(0,0,0,40);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid rgba(0,0,0,20);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"    background-color: #5e90fa;\n"
"    border: 1px solid #3874f2;\n"
"    image: url(qss:images/checkbox_indeterminate_light.png);\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Checkboxs inside QListWidget and QTreeView\n"
"==================================================================================================*/\n"
"QListWidget::indicator,\n"
"QTreeView::indicator {\n"
"    color: #c8c8c8;\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #505050;\n"
"    width: 11px;\n"
"    height: 11px;\n"
"    border-radius:2px;\n"
"}\n"
"\n"
"/* fix for QTreeView::indicator loosing its margin */\n"
"QTreeView::indicator {\n"
"    margin: 3px;\n"
"}\n"
"\n"
"QListWidget::indicator:selected,\n"
"QTreeView::indicator:selected {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QListWidget::indicator:checked:selected,\n"
"QListWidget::indicator:indeterminate:selected,\n"
"QTreeView::indicator:checked:selected,\n"
"QTreeView::indicator:indeterminate:selected {\n"
"    background-color: #7cabf9; /* slighly lighter than default */\n"
"    border-color: #2053c0; /* slighly darker than default */\n"
"}\n"
"\n"
"QListWidget::indicator:pressed,\n"
"QListWidget::indicator:non-exclusive:checked:pressed,\n"
"QListWidget::indicator:indeterminate:pressed,\n"
"QListWidget::indicator:checked:pressed,\n"
"QTreeView::indicator:pressed,\n"
"QTreeView::indicator:non-exclusive:checked:pressed,\n"
"QTreeView::indicator:indeterminate:pressed,\n"
"QTreeView::indicator:checked:pressed {\n"
"    border-color: #adc5ed;\n"
"}\n"
"\n"
"QListWidget::indicator:checked,\n"
"QTreeView::indicator:checked {\n"
"    background-color: #5e90fa; /* QRadioButton has the same color */\n"
"    border: 1px solid #3874f2; /* QRadioButton has the same color */\n"
"    image:url(qss:images/checkbox_light.png);\n"
"}\n"
"\n"
"QListWidget::indicator:disabled,\n"
"QTreeView::indicator:disabled {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid rgba(0,0,0,20);\n"
"}\n"
"\n"
"QListWidget::indicator:indeterminate,\n"
"QTreeView::indicator:indeterminate {\n"
"    background-color: #5e90fa;\n"
"    border: 1px solid #3874f2;\n"
"    image: url(qss:images/checkbox_indeterminate_light.png);\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Slider\n"
"==================================================================================================*/\n"
"QSlider,\n"
"QSlider:active,\n"
"QSlider:!active {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSlider:horizontal {\n"
"    padding: 0px 10px;\n"
"}\n"
"\n"
"QSlider:vertical {\n"
"    padding: 10px 0px;\n"
"}\n"
"\n"
"QSlider::groove {\n"
"    background-color: rgba(0,0,0,30);\n"
"    border: 1px solid rgba(0,0,0,40);\n"
"    border-radius: 5px;\n"
"    margin: 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 8px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled,\n"
"QSlider::groove:vertical:disabled {\n"
"    border-color:  #dcdcdc;\n"
"    background-color: #dcdcdc;\n"
"}\n"
"\n"
"QSlider::handle:horizontal,\n"
"QSlider::handle:vertical {\n"
"    background-color: #b6b6b6;\n"
"    border: 1px solid #b6b6b6;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    margin: -4px 0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    margin: 0 -4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover,\n"
"QSlider::handle:vertical:hover,\n"
"QSlider::handle:horizontal:pressed,\n"
"QSlider::handle:vertical:pressed {\n"
"    border-color: #5e90fa;\n"
"    background-color: #5e90fa;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled,\n"
"QSlider::handle:vertical:disabled {\n"
"    border-color: #dcdcdc;\n"
"    background-color: #dcdcdc;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Toolbar buttons\n"
"==================================================================================================*/\n"
"/*QToolBar > QComboBox,   disabled because creates different margins for body and drop-down button */\n"
"QToolBar > QAbstractSpinBox,\n"
"QToolBar > QSpinBox,\n"
"QToolBar > QDoubleSpinBox,\n"
"QToolBar > QLineEdit,\n"
"QToolBar > QTextEdit,\n"
"QToolBar > QTimeEdit,\n"
"QToolBar > QDateEdit,\n"
"QToolBar > QDateTimeEdit {\n"
"    margin: 0px 2px;\n"
"    padding: 0px;\n"
"    min-width: 70px; /* necessary to show its content */\n"
"}\n"
"\n"
"QToolBar > QComboBox,\n"
"QToolBar > QAbstractSpinBox,\n"
"QToolBar > QSpinBox,\n"
"QToolBar > QDoubleSpinBox,\n"
"QToolBar > QLineEdit,\n"
"QToolBar > QTextEdit,\n"
"QToolBar > QTimeEdit,\n"
"QToolBar > QDateEdit,\n"
"QToolBar > QDateTimeEdit {\n"
"    min-height: 0px; /* reset it inside Tool Bar due to the user ability to set the \"size of toolbar icons\" inside Preferences  */\n"
"}\n"
"\n"
"QToolBar > QPushButton {\n"
"    padding: 0px;\n"
"    margin: 1px; /* doesn\'t work with :left, :right:, :top or :bottom sub-controls */\n"
"    min-width: 16px; /* could not be larger due to switchable Preferences \"Size of toolbar icons\" */\n"
"    min-height: 16px; /* could not be larger due to switchable Preferences \"Size of toolbar icons\" */\n"
"    border-radius: 4px; /* same as regular QPushButton */\n"
"}\n"
"\n"
"QToolBar > QPushButton:checked {\n"
"    border: 1px solid #7cabf9;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #cbd8e6, stop:1 #7cabf9);\n"
"}\n"
"\n"
"QToolBar > QPushButton:!checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.3, x2:0, y2:1, stop:0 #f5f5f5, stop:1 #e6e6e6);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"}\n"
"\n"
"QToolBar > QPushButton:checked:hover {\n"
"    border-color: #6f9efa;\n"
"}\n"
"\n"
"QToolBar > QPushButton:!checked:hover {\n"
"    color: black;\n"
"    border-color: #b6b6b6;\n"
"}\n"
"\n"
"QToolBar > QPushButton:checked:pressed {\n"
"    background-color: #7cabf9;\n"
"}\n"
"\n"
"QToolBar > QPushButton:!checked:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #b6b6b6, stop:1 #e6e6e6);\n"
"}\n"
"\n"
"QToolBar > QPushButton:checked:disabled,\n"
"QToolBar > QPushButton:!checked:disabled {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolBar > QToolButton {\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QToolBar > QToolButton:hover {\n"
"    background-color: rgba(0,0,0,20);\n"
"}\n"
"\n"
"QToolBar > QToolButton:pressed {\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"/* ToolBar menu buttons (buttons with drop-down menu) */\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton {\n"
"    padding-right: 20px; /* Hack to add more width to buttons with menu */\n"
"    border: 1px solid transparent;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton:hover,\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton:pressed,\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton:open {\n"
"    border: 1px solid #7cabf9;\n"
"}\n"
"\n"
"QToolBar QToolButton::menu-button,\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton::menu-button {\n"
"    border: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    width: 16px; /* 16px width + 4px for border = 20px allocated above */\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton::menu-button:hover,\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton::menu-button:pressed,\n"
"QToolBar > QToolButton#qt_toolbutton_menubutton::menu-button:open {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #7cabf9);\n"
"}\n"
"\n"
"QToolBar > QToolButton::menu-arrow {\n"
"    background-image: url(qss:images/down_arrow_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    height: 10px; /* same as arrow image */\n"
"}\n"
"\n"
"QToolBar > QToolButton::menu-arrow:hover {\n"
"    background-image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QToolBar > QToolButton::menu-arrow:open {\n"
"    background-image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"/* when QToolButton is checked: */\n"
"QToolButton:checked {\n"
"    border: 1px solid #7cabf9;\n"
"    background-color: rgba(124,171,249,60); /* transparency for #7cabf9 color */\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"    border: 1px solid #7cabf9;\n"
"    background-color: rgba(124,171,249,80); /* transparency for #7cabf9 color */\n"
"}\n"
"\n"
"/*The \"show more\" button  (it can also be stylable with \"QToolBarExtension\" */\n"
"QToolBar QToolButton#qt_toolbar_ext_button {\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    /*background-image: url(qss:images/more_dark.png);*/\n"
"    image: transparent;\n"
"    background-repeat: none;\n"
"    background-position: center left;\n"
"}\n"
"\n"
"QToolBar QToolButton#qt_toolbar_ext_button:hover {\n"
"    /*background-image: url(qss:images/more_light.png);*/\n"
"    border-color: #e0e0e0;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QToolBar QToolButton#qt_toolbar_ext_button:on {\n"
"    /*background-image: url(qss:images/more_light.png);*/\n"
"    border-color: #e0e0e0;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tables (spreadsheets)\n"
"==================================================================================================*/\n"
"QTableView {\n"
"    gridline-color: #d2d2d2;\n"
"    selection-color: #1b3774;\n"
"    selection-background-color: #cbd8e6;\n"
"}\n"
"\n"
"QTableView::item:hover  {\n"
"    background-color: rgba(0,0,0,10);  /* temporal: is it displayed in Linux or Windows? on OSX it isn\'t */\n"
"}\n"
"\n"
"QTableView::item:disabled  {\n"
"    color: #e6e6e6;\n"
"}\n"
"\n"
"QTableView::item:selected  {\n"
"    color: #1b3774;\n"
"    border-color: #cbd8e6; /* same as focused background color */\n"
"    border-bottom-color: #7cabf9; /* same as focused border color */\n"
"}\n"
"\n"
"/* fix for elements inside the cells */\n"
"QTableView > QWidget > QComboBox,\n"
"QTableView > QWidget > QAbstractSpinBox,\n"
"QTableView > QWidget > QSpinBox,\n"
"QTableView > QWidget > QDoubleSpinBox,\n"
"QTableView > QWidget > QLineEdit,\n"
"QTableView > QWidget > QTextEdit,\n"
"QTableView > QWidget > QTimeEdit,\n"
"QTableView > QWidget > QDateEdit,\n"
"QTableView > QWidget > QDateTimeEdit,\n"
"QTableView > QWidget > QComboBox:drop-down,\n"
"QTableView > QWidget > QAbstractSpinBox:up-button,\n"
"QTableView > QWidget > QSpinBox:up-button,\n"
"QTableView > QWidget > QDoubleSpinBox:up-button,\n"
"QTableView > QWidget > QTimeEdit:up-button,\n"
"QTableView > QWidget > QDateEdit:up-button,\n"
"QTableView > QWidget > QDateTimeEdit:up-button,\n"
"QTableView > QWidget > QAbstractSpinBox:down-button,\n"
"QTableView > QWidget > QSpinBox:down-button,\n"
"QTableView > QWidget > QDoubleSpinBox:down-button,\n"
"QTableView > QWidget > QTimeEdit:down-button,\n"
"QTableView > QWidget > QDateEdit:down-button,\n"
"QTableView > QWidget > QDateTimeEdit:down-button,\n"
"QTableView > QWidget > Gui--ColorButton {\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView > QWidget > QComboBox,\n"
"QTableView > QWidget > QAbstractSpinBox,\n"
"QTableView > QWidget > QSpinBox,\n"
"QTableView > QWidget > QDoubleSpinBox,\n"
"QTableView > QWidget > QLineEdit,\n"
"QTableView > QWidget > QTextEdit,\n"
"QTableView > QWidget > QTimeEdit,\n"
"QTableView > QWidget > QDateEdit,\n"
"QTableView > QWidget > QDateTimeEdit {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"QTableView > QWidget > QComboBox:drop-down,\n"
"QTableView > QWidget > QAbstractSpinBox:up-button,\n"
"QTableView > QWidget > QSpinBox:up-button,\n"
"QTableView > QWidget > QDoubleSpinBox:up-button,\n"
"QTableView > QWidget > QTimeEdit:up-button,\n"
"QTableView > QWidget > QDateEdit:up-button,\n"
"QTableView > QWidget > QDateTimeEdit:up-button,\n"
"QTableView > QWidget > QAbstractSpinBox:down-button,\n"
"QTableView > QWidget > QSpinBox:down-button,\n"
"QTableView > QWidget > QDoubleSpinBox:down-button,\n"
"QTableView > QWidget > QTimeEdit:down-button,\n"
"QTableView > QWidget > QDateEdit:down-button,\n"
"QTableView > QWidget > QDateTimeEdit:down-button,\n"
"QTableView > QWidget > Gui--ColorButton {\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"QTableView > QWidget > QComboBox:focus,\n"
"QTableView > QWidget > QAbstractSpinBox:focus,\n"
"QTableView > QWidget > QSpinBox:focus,\n"
"QTableView > QWidget > QDoubleSpinBox:focus,\n"
"QTableView > QWidget > QLineEdit:focus,\n"
"QTableView > QWidget > QTextEdit:focus,\n"
"QTableView > QWidget > QTimeEdit:focus,\n"
"QTableView > QWidget > QDateEdit:focus,\n"
"QTableView > QWidget > QDateTimeEdit:focus {\n"
"    color: #1b3774;\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"    border-color: #cbd8e6;\n"
"    background-color: #cbd8e6;\n"
"}\n"
"\n"
"QTableView > QWidget > QComboBox:disabled,\n"
"QTableView > QWidget > QAbstractSpinBox:disabled,\n"
"QTableView > QWidget > QSpinBox:disabled,\n"
"QTableView > QWidget > QDoubleSpinBox:disabled,\n"
"QTableView > QWidget > QLineEdit:disabled,\n"
"QTableView > QWidget > QTextEdit:disabled,\n"
"QTableView > QWidget > QTimeEdit:disabled,\n"
"QTableView > QWidget > QDateEdit:disabled,\n"
"QTableView > QWidget > QDateTimeEdit:disabled {\n"
"    color: rgba(0,0,0,120);\n"
"    background-color: transparent;\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"QTableView > QWidget > QComboBox:read-only,\n"
"QTableView > QWidget > QAbstractSpinBox:read-only,\n"
"QTableView > QWidget > QSpinBox:read-only,\n"
"QTableView > QWidget > QDoubleSpinBox:read-only,\n"
"QTableView > QWidget > QLineEdit:read-only,\n"
"QTableView > QWidget > QTextEdit:read-only,\n"
"QTableView > QWidget > QTimeEdit:read-only,\n"
"QTableView > QWidget > QDateEdit:read-only,\n"
"QTableView > QWidget > QDateTimeEdit:read-only {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"EXPERIMENTAL\n"
"==================================================================================================*/\n"
"\n"
"/* Fix for preventing elements in different rows to accidentaly overlap */\n"
"QDialog QGroupBox QFrame {\n"
"    margin: 2px 0px;\n"
"}\n"
"\n"
"*[mandatoryField=\"true\"] { background-color: cyan }\n"
"QPushButton {\n"
"    border-radius: 20px;\n"
"    color: rgb(230, 230, 230);\n"
"    text-align: center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"    padding: 4px 22px;\n"
"    margin: 4px 4px;\n"
"    min-height: 16px; /* same as QTabBar QPushButton min-width */\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"    color: white;\n"
"    border: 1px solid rgb(49, 44, 113);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.512438 rgba(69, 124, 225, 255), stop:1 rgba(82, 157, 255, 255))\n"
"}\n"
"\n"
"QPushButton:disabled,\n"
"QPushButton:disabled:checked {\n"
"    color: #b6b6b6;\n"
"    border-color: #e6e6e6;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(35, 72, 147);\n"
"    border-color: #3874f2;\n"
"}\n"
"\n"
"/* Color Buttons */\n"
"Gui--ColorButton,\n"
"Gui--ColorButton:disabled {\n"
"    padding: 0px; /* reset */\n"
"    margin: 0px; /* reset */\n"
"}\n"
"\n"
"Gui--ColorButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.3, x2:0, y2:1, stop:0 #f5f5f5, stop:1 #e6e6e6);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"}\n"
"\n"
"Gui--ColorButton:disabled {\n"
"    border-color: transparent;\n"
"    background-color: rgba(0,0,0,10);\n"
"}\n"
"\n"
"Gui--ColorButton:hover,\n"
"Gui--ColorButton:focus {\n"
"    border-color: #3874f2;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"}\n"
"\n"
"Gui--ColorButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}\n"
"\n"
"/* Pushbutton style for \"...\" inside Placement cell which launches Placement tool */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QPushButton {\n"
"    background-color: #b6b6b6;\n"
"    border: 1px solid #828282;\n"
"    min-width: 16px; /* reset it due to larger value on regular QPushButton, same or bigger value as regular QPushButton min-height */\n"
"    border-radius: 0px;\n"
"    margin: 0px; /* reset */\n"
"    padding: 0px; /* reset */\n"
"}\n"
"\n"
"/* Fix for Expressions description QFrame that is \"broken\" with initial reset */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QWidget > QWidget > QFrame {\n"
"    background-color: #f5f5f5; /* main background color */\n"
"    border: 1px solid #dcdcdc;\n"
"    border-radius: 2px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #5e90fa;\n"
"    border-color: #3874f2;\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(198, 198, 198);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.512438 rgba(112, 174, 234, 255), stop:1 rgba(82, 157, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(1020, -30, 261, 741))
        self.groupBox.setStyleSheet("QPushButton{\n"
"border-radius: 40px;\n"
"color:rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(198, 198, 198);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.512438 rgba(112, 174, 234, 255), stop:1 rgba(82, 157, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(49, 44, 113);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e80fa, stop:1 #3874f2);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(15, 60, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(True)
        self.pushButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons8-sales-performance-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 170, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons8-test-tube-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(18, 400, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons8-order-history-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 54))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(17, 510, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons8-settings-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(16, 290, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons8-user-group-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(75, 72))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(18, 620, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, -10, 1011, 771))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 189, 651, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:20px;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 279, 651, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:20px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 439, 591, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 349, 651, 71))
        self.groupBox_2.setStyleSheet("border-radius:20px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(260, 17, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 14, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(794, 187, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(827, 278, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_38 = QtWidgets.QPushButton(self.tab)
        self.pushButton_38.setEnabled(True)
        self.pushButton_38.setGeometry(QtCore.QRect(50, 280, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_38.setStyleSheet("")
        self.pushButton_38.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_38.setIcon(icon5)
        self.pushButton_38.setObjectName("pushButton_38")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(784, 230, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 232, 651, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border-radius:20px;")
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 340, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_21.setGeometry(QtCore.QRect(100, 340, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setObjectName("pushButton_21")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 1011, 711))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tabWidget_5.setFont(font)
        self.tabWidget_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_5.setGeometry(QtCore.QRect(0, -10, 1001, 671))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 100, 981, 531))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_27.setGeometry(QtCore.QRect(330, 36, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setStyleSheet("border-radius:20px;")
        self.lineEdit_27.setPlaceholderText("")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_60 = QtWidgets.QLabel(self.groupBox_5)
        self.label_60.setEnabled(True)
        self.label_60.setGeometry(QtCore.QRect(740, 27, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_36.setGeometry(QtCore.QRect(10, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setObjectName("pushButton_36")
        self.tabWidget_5.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.label_53 = QtWidgets.QLabel(self.tab_18)
        self.label_53.setGeometry(QtCore.QRect(800, -2, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_29.setGeometry(QtCore.QRect(320, 5, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons8-search-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_29.setIcon(icon6)
        self.pushButton_29.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_10.setGeometry(QtCore.QRect(0, 61, 1011, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_10)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 40, 1011, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(7)
        self.tableWidget_4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_18)
        self.spinBox_2.setGeometry(QtCore.QRect(579, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("border-radius:20px;")
        self.spinBox_2.setMaximum(1000000000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_11.setGeometry(QtCore.QRect(-1, 261, 1011, 421))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.groupBox_11)
        self.tableWidget_9.setGeometry(QtCore.QRect(0, 34, 1011, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_9.setFont(font)
        self.tableWidget_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(4)
        self.tableWidget_9.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_42.setGeometry(QtCore.QRect(30, 5, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_42.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_42.setIcon(icon6)
        self.pushButton_42.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_42.setObjectName("pushButton_42")
        self.tabWidget_5.addTab(self.tab_18, "")
        self.tabWidget.addTab(self.widget, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QtCore.QRect(-10, 10, 1021, 751))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setGeometry(QtCore.QRect(690, 0, 321, 661))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_35 = QtWidgets.QLabel(self.groupBox_6)
        self.label_35.setEnabled(True)
        self.label_35.setGeometry(QtCore.QRect(10, 65, 101, 41))
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_14.setEnabled(True)
        self.comboBox_14.setGeometry(QtCore.QRect(11, 237, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_14.setFont(font)
        self.comboBox_14.setStyleSheet("")
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_36 = QtWidgets.QLabel(self.groupBox_6)
        self.label_36.setEnabled(True)
        self.label_36.setGeometry(QtCore.QRect(256, 230, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_6)
        self.label_37.setEnabled(True)
        self.label_37.setGeometry(QtCore.QRect(258, 160, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_6)
        self.label_38.setEnabled(True)
        self.label_38.setGeometry(QtCore.QRect(120, 360, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_7.setEnabled(True)
        self.spinBox_7.setGeometry(QtCore.QRect(11, 168, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_7.setFont(font)
        self.spinBox_7.setStyleSheet("border-radius: 10px;\n"
"")
        self.spinBox_7.setMinimum(-1000000)
        self.spinBox_7.setMaximum(1000000)
        self.spinBox_7.setProperty("value", 20)
        self.spinBox_7.setObjectName("spinBox_7")
        self.comboBox_15 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_15.setEnabled(True)
        self.comboBox_15.setGeometry(QtCore.QRect(10, 306, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_15.setFont(font)
        self.comboBox_15.setStyleSheet("")
        self.comboBox_15.setEditable(True)
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit.setGeometry(QtCore.QRect(20, 410, 291, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 30px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_30 = QtWidgets.QLabel(self.groupBox_6)
        self.label_30.setGeometry(QtCore.QRect(216, 161, 41, 51))
        self.label_30.setStyleSheet("image: url(:/icons8-age-64 (1).png);")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.groupBox_6)
        self.label_31.setGeometry(QtCore.QRect(217, 238, 41, 51))
        self.label_31.setStyleSheet("image: url(:/lavatory.png);")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.label_39 = QtWidgets.QLabel(self.groupBox_6)
        self.label_39.setEnabled(True)
        self.label_39.setGeometry(QtCore.QRect(250, 300, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_4.setGeometry(QtCore.QRect(13, 80, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_42 = QtWidgets.QLabel(self.groupBox_6)
        self.label_42.setEnabled(True)
        self.label_42.setGeometry(QtCore.QRect(103, 34, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_7.setEnabled(True)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 0, 681, 721))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_40 = QtWidgets.QLabel(self.groupBox_7)
        self.label_40.setEnabled(True)
        self.label_40.setGeometry(QtCore.QRect(618, 75, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setOpenExternalLinks(True)
        self.label_40.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.label_40.setObjectName("label_40")
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_16.setEnabled(True)
        self.comboBox_16.setGeometry(QtCore.QRect(242, 80, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_16.setFont(font)
        self.comboBox_16.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox_16.setEditable(True)
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.label_41 = QtWidgets.QLabel(self.groupBox_7)
        self.label_41.setEnabled(True)
        self.label_41.setGeometry(QtCore.QRect(594, 142, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setObjectName("label_41")
        self.comboBox_17 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_17.setEnabled(True)
        self.comboBox_17.setGeometry(QtCore.QRect(60, 150, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboBox_17.setFont(font)
        self.comboBox_17.setStyleSheet("border-radius: 20px;\n"
"")
        self.comboBox_17.setObjectName("comboBox_17")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_5.setEnabled(True)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 280, 681, 291))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setStyleSheet("")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(6)
        self.tableWidget_5.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setGeometry(QtCore.QRect(100, 210, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons8-add-new-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon7)
        self.pushButton_17.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_17.setCheckable(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_18.setEnabled(True)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 570, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_18.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons8-print-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon8)
        self.pushButton_18.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_44 = QtWidgets.QLabel(self.groupBox_7)
        self.label_44.setEnabled(True)
        self.label_44.setGeometry(QtCore.QRect(570, 573, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_24.setEnabled(True)
        self.lineEdit_24.setGeometry(QtCore.QRect(392, 577, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.lineEdit_24.setText("")
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setPlaceholderText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_54 = QtWidgets.QLabel(self.groupBox_7)
        self.label_54.setEnabled(True)
        self.label_54.setGeometry(QtCore.QRect(596, 20, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_32.setEnabled(True)
        self.pushButton_32.setGeometry(QtCore.QRect(330, 579, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_32.setStyleSheet("")
        self.pushButton_32.setText("")
        self.pushButton_32.setIcon(icon5)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_34.setEnabled(True)
        self.pushButton_34.setGeometry(QtCore.QRect(160, 570, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_34.setStyleSheet("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_35.setEnabled(True)
        self.pushButton_35.setGeometry(QtCore.QRect(54, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_35.setStyleSheet("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_21.setEnabled(True)
        self.lineEdit_21.setGeometry(QtCore.QRect(60, 150, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setStyleSheet("border-radius: 20px;\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(60, 150, 541, 51))
        self.doubleSpinBox_7.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.doubleSpinBox_7.setMinimum(-1111111111111.0)
        self.doubleSpinBox_7.setMaximum(1e+19)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_30.setEnabled(True)
        self.pushButton_30.setGeometry(QtCore.QRect(312, 21, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_30.setStyleSheet("")
        self.pushButton_30.setText("")
        self.pushButton_30.setIcon(icon6)
        self.pushButton_30.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_30.setObjectName("pushButton_30")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox.setGeometry(QtCore.QRect(376, 25, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("border-radius: 20px;\n"
"")
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_43.setEnabled(True)
        self.pushButton_43.setGeometry(QtCore.QRect(151, 21, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_43.setStyleSheet("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_44.setGeometry(QtCore.QRect(50, 73, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setObjectName("pushButton_44")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_8.setGeometry(QtCore.QRect(0, -20, 1001, 661))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_25.setGeometry(QtCore.QRect(330, 39, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setStyleSheet("border-radius: 20px;\n"
"")
        self.lineEdit_25.setPlaceholderText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 33, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_19.setStyleSheet("border-radius: 20px;\n"
"")
        self.pushButton_19.setIcon(icon6)
        self.pushButton_19.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_19.setObjectName("pushButton_19")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.groupBox_8)
        self.tableWidget_6.setGeometry(QtCore.QRect(10, 100, 981, 521))
        self.tableWidget_6.setStyleSheet("border-radius: 60px;\n"
"")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(4)
        self.tableWidget_6.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        self.label_55 = QtWidgets.QLabel(self.groupBox_8)
        self.label_55.setEnabled(True)
        self.label_55.setGeometry(QtCore.QRect(740, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 10, 1011, 711))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.comboBox_19 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_19.setGeometry(QtCore.QRect(340, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_19.setFont(font)
        self.comboBox_19.setStyleSheet("border-radius:20px;")
        self.comboBox_19.setEditable(False)
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_20.setGeometry(QtCore.QRect(20, 16, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_20.setStyleSheet("border-radius:25px;")
        self.pushButton_20.setIcon(icon6)
        self.pushButton_20.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_20.setObjectName("pushButton_20")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_26.setGeometry(QtCore.QRect(670, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setStyleSheet("border-radius:20px;")
        self.lineEdit_26.setPlaceholderText("")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_7.setEnabled(True)
        self.tableWidget_7.setGeometry(QtCore.QRect(10, 100, 981, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_7.sizePolicy().hasHeightForWidth())
        self.tableWidget_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_7.setFont(font)
        self.tableWidget_7.setToolTip("")
        self.tableWidget_7.setWhatsThis("")
        self.tableWidget_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_7.setAutoFillBackground(False)
        self.tableWidget_7.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Iraq))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(6)
        self.tableWidget_7.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_4.setGeometry(QtCore.QRect(520, -4, 491, 671))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("border-radius:20px;")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_45 = QtWidgets.QLabel(self.groupBox_4)
        self.label_45.setGeometry(QtCore.QRect(350, 50, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_28.setGeometry(QtCore.QRect(50, 50, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_46 = QtWidgets.QLabel(self.groupBox_4)
        self.label_46.setGeometry(QtCore.QRect(340, 310, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_48 = QtWidgets.QLabel(self.groupBox_4)
        self.label_48.setGeometry(QtCore.QRect(360, 463, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_26.setGeometry(QtCore.QRect(40, 585, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_26.setIcon(icon7)
        self.pushButton_26.setIconSize(QtCore.QSize(53, 53))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_56 = QtWidgets.QLabel(self.groupBox_4)
        self.label_56.setGeometry(QtCore.QRect(360, 170, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.comboBox_22 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_22.setGeometry(QtCore.QRect(50, 180, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_22.setFont(font)
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.label_58 = QtWidgets.QLabel(self.groupBox_4)
        self.label_58.setGeometry(QtCore.QRect(361, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.comboBox_23 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_23.setGeometry(QtCore.QRect(51, 120, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_23.setFont(font)
        self.comboBox_23.setEditable(True)
        self.comboBox_23.setObjectName("comboBox_23")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 300, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_47 = QtWidgets.QLabel(self.groupBox_4)
        self.label_47.setGeometry(QtCore.QRect(370, 400, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 410, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_5.setGeometry(QtCore.QRect(53, 470, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setStyleSheet("border-radius:20px")
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_61 = QtWidgets.QLabel(self.groupBox_4)
        self.label_61.setGeometry(QtCore.QRect(360, 230, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.comboBox_30 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_30.setGeometry(QtCore.QRect(50, 240, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_30.setFont(font)
        self.comboBox_30.setEditable(True)
        self.comboBox_30.setObjectName("comboBox_30")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_39.setEnabled(True)
        self.pushButton_39.setGeometry(QtCore.QRect(1, 235, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_39.setStyleSheet("")
        self.pushButton_39.setText("")
        self.pushButton_39.setIcon(icon7)
        self.pushButton_39.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_46.setEnabled(True)
        self.pushButton_46.setGeometry(QtCore.QRect(0, 113, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_46.setStyleSheet("")
        self.pushButton_46.setText("")
        self.pushButton_46.setIcon(icon7)
        self.pushButton_46.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_46.setObjectName("pushButton_46")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_9.setGeometry(QtCore.QRect(0, -4, 501, 691))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("border-radius:20px;")
        self.groupBox_9.setObjectName("groupBox_9")
        self.comboBox_21 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_21.setGeometry(QtCore.QRect(20, 50, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_21.setFont(font)
        self.comboBox_21.setEditable(True)
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_27.setGeometry(QtCore.QRect(280, 585, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_28.setGeometry(QtCore.QRect(30, 585, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_28.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons8-delete-bin-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_28.setIcon(icon9)
        self.pushButton_28.setIconSize(QtCore.QSize(53, 53))
        self.pushButton_28.setObjectName("pushButton_28")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_4.setGeometry(QtCore.QRect(14, 462, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_49 = QtWidgets.QLabel(self.groupBox_9)
        self.label_49.setGeometry(QtCore.QRect(399, 452, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_9)
        self.label_50.setGeometry(QtCore.QRect(409, 516, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.comboBox_31 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_31.setGeometry(QtCore.QRect(106, 296, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_31.setFont(font)
        self.comboBox_31.setEditable(True)
        self.comboBox_31.setObjectName("comboBox_31")
        self.label_57 = QtWidgets.QLabel(self.groupBox_9)
        self.label_57.setGeometry(QtCore.QRect(406, 226, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_5.setGeometry(QtCore.QRect(15, 356, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_51 = QtWidgets.QLabel(self.groupBox_9)
        self.label_51.setGeometry(QtCore.QRect(352, 366, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_59 = QtWidgets.QLabel(self.groupBox_9)
        self.label_59.setGeometry(QtCore.QRect(408, 166, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.label_52 = QtWidgets.QLabel(self.groupBox_9)
        self.label_52.setGeometry(QtCore.QRect(397, 106, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_29.setGeometry(QtCore.QRect(19, 106, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_62 = QtWidgets.QLabel(self.groupBox_9)
        self.label_62.setGeometry(QtCore.QRect(418, 286, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_6.setGeometry(QtCore.QRect(22, 526, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.spinBox_6.setFont(font)
        self.spinBox_6.setStyleSheet("border-radius:20px")
        self.spinBox_6.setWrapping(False)
        self.spinBox_6.setProperty("showGroupSeparator", False)
        self.spinBox_6.setObjectName("spinBox_6")
        self.comboBox_25 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_25.setGeometry(QtCore.QRect(19, 236, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_25.setFont(font)
        self.comboBox_25.setObjectName("comboBox_25")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_26 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_26.setGeometry(QtCore.QRect(70, 176, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_26.setFont(font)
        self.comboBox_26.setEditable(True)
        self.comboBox_26.setObjectName("comboBox_26")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_40.setEnabled(True)
        self.pushButton_40.setGeometry(QtCore.QRect(57, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_40.setStyleSheet("")
        self.pushButton_40.setText("")
        self.pushButton_40.setIcon(icon7)
        self.pushButton_40.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_41.setEnabled(True)
        self.pushButton_41.setGeometry(QtCore.QRect(3, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_41.setStyleSheet("")
        self.pushButton_41.setText("")
        self.pushButton_41.setIcon(icon9)
        self.pushButton_41.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_71 = QtWidgets.QLabel(self.groupBox_9)
        self.label_71.setGeometry(QtCore.QRect(420, 45, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_45.setEnabled(True)
        self.pushButton_45.setGeometry(QtCore.QRect(13, 170, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_45.setStyleSheet("")
        self.pushButton_45.setText("")
        self.pushButton_45.setIcon(icon7)
        self.pushButton_45.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_45.setObjectName("pushButton_45")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_8.setGeometry(QtCore.QRect(0, 107, 981, 571))
        self.tableWidget_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(4)
        self.tableWidget_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        self.comboBox_20 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_20.setGeometry(QtCore.QRect(230, 46, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_20.setFont(font)
        self.comboBox_20.setStyleSheet("border-radius:20px;")
        self.comboBox_20.setEditable(False)
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_24 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_24.setGeometry(QtCore.QRect(585, 47, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_24.setFont(font)
        self.comboBox_24.setStyleSheet("border-radius:20px;")
        self.comboBox_24.setObjectName("comboBox_24")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.label_15 = QtWidgets.QLabel(self.tab_6)
        self.label_15.setGeometry(QtCore.QRect(880, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_6)
        self.label_16.setGeometry(QtCore.QRect(497, 40, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_22.setGeometry(QtCore.QRect(0, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("border-radius: 20px;\n"
"")
        self.pushButton_22.setIcon(icon9)
        self.pushButton_22.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_22.setObjectName("pushButton_22")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_7)
        self.tabWidget_4.setEnabled(True)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 1011, 711))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget_4.setStyleSheet("")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 140, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 50px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_11.setGeometry(QtCore.QRect(370, 342, 261, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    outline: none;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #D1DBCB;\n"
"    background-color: #31363B;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #76797C;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 140, 261, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("/* QPushButton ------------------------------------------------------------ */\n"
"\n"
"QPushButton {\n"
"    background-color: #505F69 ;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #32414B;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #32414B;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #19232D;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:selected,\n"
"QPushButton:checked:selected{\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------ */\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    margin: 0px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #19232D;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolButton:hover,\n"
"QToolButton:checked:hover{\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"    padding: 2px;\n"
"    padding-right: 12px;     /* only for MenuButtonPopup */\n"
"    border: 1px solid #32414B;   /* make way for the popup button */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"    padding: 2px;\n"
"    padding-right: 12px;      /* only for InstantPopup */\n"
"    border: 1px solid #32414B;    /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    padding: 2px;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover,\n"
"QToolButton::menu-button:checked:hover {\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -8px;     /* shift it a bit */\n"
"    left: -4px;    /* shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCommandLinkButton ----------------------------------------------------- */\n"
"\n"
"QCommandLinkButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"    background-color: transparent;\n"
"    color: #787878;\n"
"}\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 340, 261, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 3px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_15.setGeometry(QtCore.QRect(670, 242, 261, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget_4.addTab(self.tab_14, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.label_19 = QtWidgets.QLabel(self.tab_10)
        self.label_19.setGeometry(QtCore.QRect(670, 108, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setGeometry(QtCore.QRect(140, 110, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setPlaceholderText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_20 = QtWidgets.QLabel(self.tab_10)
        self.label_20.setGeometry(QtCore.QRect(670, 228, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_15.setEnabled(True)
        self.lineEdit_15.setGeometry(QtCore.QRect(140, 230, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setPlaceholderText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_24.setEnabled(True)
        self.pushButton_24.setGeometry(QtCore.QRect(260, 400, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet("border-radius:20px;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_16.setEnabled(True)
        self.lineEdit_16.setGeometry(QtCore.QRect(530, 56, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("border-radius:20px;")
        self.lineEdit_16.setPlaceholderText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_64 = QtWidgets.QLabel(self.tab_13)
        self.label_64.setEnabled(True)
        self.label_64.setGeometry(QtCore.QRect(810, 50, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_18.setEnabled(True)
        self.lineEdit_18.setGeometry(QtCore.QRect(90, 57, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("border-radius:20px;")
        self.lineEdit_18.setPlaceholderText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_65 = QtWidgets.QLabel(self.tab_13)
        self.label_65.setEnabled(True)
        self.label_65.setGeometry(QtCore.QRect(370, 51, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_19.setEnabled(True)
        self.lineEdit_19.setGeometry(QtCore.QRect(90, 183, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("border-radius:20px;")
        self.lineEdit_19.setPlaceholderText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_20.setEnabled(True)
        self.lineEdit_20.setGeometry(QtCore.QRect(530, 182, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("border-radius:20px;")
        self.lineEdit_20.setPlaceholderText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_69 = QtWidgets.QLabel(self.tab_13)
        self.label_69.setEnabled(True)
        self.label_69.setGeometry(QtCore.QRect(810, 176, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.tab_13)
        self.label_70.setEnabled(True)
        self.label_70.setGeometry(QtCore.QRect(370, 177, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_22.setEnabled(True)
        self.lineEdit_22.setGeometry(QtCore.QRect(90, 306, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setStyleSheet("border-radius:20px;")
        self.lineEdit_22.setPlaceholderText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_23.setEnabled(True)
        self.lineEdit_23.setGeometry(QtCore.QRect(530, 305, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setStyleSheet("border-radius:20px;")
        self.lineEdit_23.setPlaceholderText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_72 = QtWidgets.QLabel(self.tab_13)
        self.label_72.setEnabled(True)
        self.label_72.setGeometry(QtCore.QRect(810, 299, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.tab_13)
        self.label_73.setEnabled(True)
        self.label_73.setGeometry(QtCore.QRect(370, 300, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_34.setEnabled(True)
        self.lineEdit_34.setGeometry(QtCore.QRect(90, 516, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setStyleSheet("border-radius:20px;")
        self.lineEdit_34.setPlaceholderText("")
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_74 = QtWidgets.QLabel(self.tab_13)
        self.label_74.setEnabled(True)
        self.label_74.setGeometry(QtCore.QRect(390, 510, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_35.setEnabled(True)
        self.lineEdit_35.setGeometry(QtCore.QRect(90, 376, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setStyleSheet("border-radius:20px;")
        self.lineEdit_35.setPlaceholderText("")
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_37.setEnabled(True)
        self.lineEdit_37.setGeometry(QtCore.QRect(530, 375, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setStyleSheet("border-radius:20px;")
        self.lineEdit_37.setPlaceholderText("")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_75 = QtWidgets.QLabel(self.tab_13)
        self.label_75.setEnabled(True)
        self.label_75.setGeometry(QtCore.QRect(790, 369, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.tab_13)
        self.label_76.setEnabled(True)
        self.label_76.setGeometry(QtCore.QRect(340, 370, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.tab_13)
        self.label_77.setEnabled(True)
        self.label_77.setGeometry(QtCore.QRect(350, 444, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_41.setEnabled(True)
        self.lineEdit_41.setGeometry(QtCore.QRect(530, 449, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setStyleSheet("border-radius:20px;")
        self.lineEdit_41.setPlaceholderText("")
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_78 = QtWidgets.QLabel(self.tab_13)
        self.label_78.setEnabled(True)
        self.label_78.setGeometry(QtCore.QRect(780, 443, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_42.setEnabled(True)
        self.lineEdit_42.setGeometry(QtCore.QRect(90, 450, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setStyleSheet("border-radius:20px;")
        self.lineEdit_42.setPlaceholderText("")
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_79 = QtWidgets.QLabel(self.tab_13)
        self.label_79.setEnabled(True)
        self.label_79.setGeometry(QtCore.QRect(780, 514, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_43.setEnabled(True)
        self.lineEdit_43.setGeometry(QtCore.QRect(530, 520, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setStyleSheet("border-radius:20px;")
        self.lineEdit_43.setPlaceholderText("")
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_31.setEnabled(True)
        self.pushButton_31.setGeometry(QtCore.QRect(240, 578, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_31.setStyleSheet("border-radius:20px;")
        self.pushButton_31.setObjectName("pushButton_31")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_44.setEnabled(True)
        self.lineEdit_44.setGeometry(QtCore.QRect(90, 116, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setStyleSheet("border-radius:20px;")
        self.lineEdit_44.setPlaceholderText("")
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_45.setEnabled(True)
        self.lineEdit_45.setGeometry(QtCore.QRect(530, 115, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_45.setFont(font)
        self.lineEdit_45.setStyleSheet("border-radius:20px;")
        self.lineEdit_45.setPlaceholderText("")
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_80 = QtWidgets.QLabel(self.tab_13)
        self.label_80.setEnabled(True)
        self.label_80.setGeometry(QtCore.QRect(810, 109, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.tab_13)
        self.label_81.setEnabled(True)
        self.label_81.setGeometry(QtCore.QRect(370, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.tab_13)
        self.label_82.setEnabled(True)
        self.label_82.setGeometry(QtCore.QRect(810, 239, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_46.setEnabled(True)
        self.lineEdit_46.setGeometry(QtCore.QRect(530, 245, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setStyleSheet("border-radius:20px;")
        self.lineEdit_46.setPlaceholderText("")
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_47.setEnabled(True)
        self.lineEdit_47.setGeometry(QtCore.QRect(90, 246, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_47.setFont(font)
        self.lineEdit_47.setStyleSheet("border-radius:20px;")
        self.lineEdit_47.setPlaceholderText("")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.label_83 = QtWidgets.QLabel(self.tab_13)
        self.label_83.setEnabled(True)
        self.label_83.setGeometry(QtCore.QRect(370, 240, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.tabWidget_4.addTab(self.tab_13, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_15)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(-1, 150, 1041, 431))
        self.tableWidget_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_16.setEnabled(True)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 77, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("border-radius:20px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_15)
        self.dateEdit.setEnabled(True)
        self.dateEdit.setGeometry(QtCore.QRect(490, 88, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("border-radius:20px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label_7 = QtWidgets.QLabel(self.tab_15)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(213, 7, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_15)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(730, 85, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_15)
        self.lineEdit_13.setEnabled(True)
        self.lineEdit_13.setGeometry(QtCore.QRect(650, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("border-radius:20px;")
        self.lineEdit_13.setPlaceholderText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_12 = QtWidgets.QLabel(self.tab_15)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(890, 14, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.tab_15)
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QtCore.QRect(550, 10, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_15)
        self.spinBox_3.setEnabled(True)
        self.spinBox_3.setGeometry(QtCore.QRect(355, 19, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("border-radius:20px;")
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_8 = QtWidgets.QSpinBox(self.tab_15)
        self.spinBox_8.setEnabled(True)
        self.spinBox_8.setGeometry(QtCore.QRect(20, 18, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.spinBox_8.setFont(font)
        self.spinBox_8.setStyleSheet("border-radius:20px;")
        self.spinBox_8.setObjectName("spinBox_8")
        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_5.setGeometry(QtCore.QRect(630, 23, 291, 51))
        self.comboBox_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_5.setStyleSheet("border-radius:20px;")
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_21 = QtWidgets.QLabel(self.tab_16)
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QtCore.QRect(930, 20, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_68 = QtWidgets.QLabel(self.tab_16)
        self.label_68.setGeometry(QtCore.QRect(300, 20, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.tab_16)
        self.dateEdit_6.setGeometry(QtCore.QRect(360, 22, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_6.setFont(font)
        self.dateEdit_6.setStyleSheet("border-radius:20px;")
        self.dateEdit_6.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_6.setCalendarPopup(True)
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.label_66 = QtWidgets.QLabel(self.tab_16)
        self.label_66.setGeometry(QtCore.QRect(560, 20, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.tab_16)
        self.label_67.setGeometry(QtCore.QRect(234, 24, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab_16)
        self.dateEdit_5.setGeometry(QtCore.QRect(0, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_5.setFont(font)
        self.dateEdit_5.setStyleSheet("border-radius:20px;")
        self.dateEdit_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_5.setCalendarPopup(True)
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_23.setGeometry(QtCore.QRect(220, 110, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_23.setStyleSheet("border-radius:26px;")
        self.pushButton_23.setIcon(icon6)
        self.pushButton_23.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_23 = QtWidgets.QLabel(self.tab_16)
        self.label_23.setEnabled(True)
        self.label_23.setGeometry(QtCore.QRect(820, 196, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_30.setEnabled(True)
        self.lineEdit_30.setGeometry(QtCore.QRect(570, 199, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.lineEdit_30.setText("")
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setPlaceholderText("")
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_31.setEnabled(True)
        self.lineEdit_31.setGeometry(QtCore.QRect(570, 437, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.lineEdit_31.setText("")
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setPlaceholderText("")
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_24 = QtWidgets.QLabel(self.tab_16)
        self.label_24.setEnabled(True)
        self.label_24.setGeometry(QtCore.QRect(820, 434, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_32.setEnabled(True)
        self.lineEdit_32.setGeometry(QtCore.QRect(570, 530, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.lineEdit_32.setText("")
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setPlaceholderText("")
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_25 = QtWidgets.QLabel(self.tab_16)
        self.label_25.setEnabled(True)
        self.label_25.setGeometry(QtCore.QRect(820, 527, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_33.setEnabled(True)
        self.lineEdit_33.setGeometry(QtCore.QRect(570, 286, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.lineEdit_33.setText("")
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setPlaceholderText("")
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.label_26 = QtWidgets.QLabel(self.tab_16)
        self.label_26.setEnabled(True)
        self.label_26.setGeometry(QtCore.QRect(820, 283, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.widget_2 = QtWidgets.QWidget(self.tab_16)
        self.widget_2.setGeometry(QtCore.QRect(490, 180, 6, 441))
        self.widget_2.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.widget_2.setObjectName("widget_2")
        self.label_27 = QtWidgets.QLabel(self.tab_16)
        self.label_27.setEnabled(True)
        self.label_27.setGeometry(QtCore.QRect(280, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_16)
        self.label_28.setEnabled(True)
        self.label_28.setGeometry(QtCore.QRect(265, 260, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_16)
        self.label_29.setEnabled(True)
        self.label_29.setGeometry(QtCore.QRect(290, 333, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_32 = QtWidgets.QLabel(self.tab_16)
        self.label_32.setEnabled(True)
        self.label_32.setGeometry(QtCore.QRect(270, 410, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_16)
        self.label_33.setEnabled(True)
        self.label_33.setGeometry(QtCore.QRect(270, 540, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_16)
        self.label_34.setEnabled(True)
        self.label_34.setGeometry(QtCore.QRect(290, 470, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_36.setEnabled(True)
        self.lineEdit_36.setGeometry(QtCore.QRect(570, 363, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setStyleSheet("border-radius: 20px;\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.lineEdit_36.setText("")
        self.lineEdit_36.setReadOnly(True)
        self.lineEdit_36.setPlaceholderText("")
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_43 = QtWidgets.QLabel(self.tab_16)
        self.label_43.setEnabled(True)
        self.label_43.setGeometry(QtCore.QRect(820, 360, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.comboBox = QtWidgets.QComboBox(self.tab_16)
        self.comboBox.setGeometry(QtCore.QRect(2, 410, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_6.setGeometry(QtCore.QRect(2, 260, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_7.setGeometry(QtCore.QRect(2, 336, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_8.setGeometry(QtCore.QRect(1, 190, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_9.setGeometry(QtCore.QRect(1, 478, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_10.setGeometry(QtCore.QRect(0, 545, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_10.setFont(font)
        self.comboBox_10.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"Segoe UI\";\n"
"")
        self.comboBox_10.setObjectName("comboBox_10")
        self.tabWidget_4.addTab(self.tab_16, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_3.setGeometry(QtCore.QRect(221, 153, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:20px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(self.tab_19)
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QtCore.QRect(701, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_19)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 220, 1011, 451))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3.setStyleSheet("border-radius:20px")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_15.setGeometry(QtCore.QRect(300, 70, 681, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.checkBox_40 = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox_40.setGeometry(QtCore.QRect(250, 25, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_40.setFont(font)
        self.checkBox_40.setObjectName("checkBox_40")
        self.checkBox_41 = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox_41.setGeometry(QtCore.QRect(250, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_41.setFont(font)
        self.checkBox_41.setObjectName("checkBox_41")
        self.checkBox_42 = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox_42.setGeometry(QtCore.QRect(250, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_42.setFont(font)
        self.checkBox_42.setObjectName("checkBox_42")
        self.checkBox_43 = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox_43.setGeometry(QtCore.QRect(300, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_43.setFont(font)
        self.checkBox_43.setObjectName("checkBox_43")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 24, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QtCore.QRect(840, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_25.setGeometry(QtCore.QRect(152, 373, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_37.setGeometry(QtCore.QRect(10, 373, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_37.setStyleSheet("")
        self.pushButton_37.setIcon(icon9)
        self.pushButton_37.setIconSize(QtCore.QSize(43, 43))
        self.pushButton_37.setObjectName("pushButton_37")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(160, 29, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.groupBox_19 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_19.setGeometry(QtCore.QRect(300, 70, 681, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setObjectName("groupBox_19")
        self.checkBox_44 = QtWidgets.QCheckBox(self.groupBox_19)
        self.checkBox_44.setGeometry(QtCore.QRect(250, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_44.setFont(font)
        self.checkBox_44.setObjectName("checkBox_44")
        self.checkBox_45 = QtWidgets.QCheckBox(self.groupBox_19)
        self.checkBox_45.setGeometry(QtCore.QRect(250, 160, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_45.setFont(font)
        self.checkBox_45.setObjectName("checkBox_45")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_20.setGeometry(QtCore.QRect(300, 70, 681, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setObjectName("groupBox_20")
        self.checkBox_46 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_46.setGeometry(QtCore.QRect(370, 25, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_46.setFont(font)
        self.checkBox_46.setObjectName("checkBox_46")
        self.checkBox_47 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_47.setGeometry(QtCore.QRect(350, 200, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_47.setFont(font)
        self.checkBox_47.setObjectName("checkBox_47")
        self.checkBox_48 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_48.setGeometry(QtCore.QRect(370, 260, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_48.setFont(font)
        self.checkBox_48.setObjectName("checkBox_48")
        self.checkBox_49 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_49.setGeometry(QtCore.QRect(370, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_49.setFont(font)
        self.checkBox_49.setObjectName("checkBox_49")
        self.checkBox_50 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_50.setGeometry(QtCore.QRect(350, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_50.setFont(font)
        self.checkBox_50.setObjectName("checkBox_50")
        self.checkBox_51 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_51.setGeometry(QtCore.QRect(80, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_51.setFont(font)
        self.checkBox_51.setObjectName("checkBox_51")
        self.checkBox_52 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_52.setGeometry(QtCore.QRect(80, 70, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_52.setFont(font)
        self.checkBox_52.setObjectName("checkBox_52")
        self.checkBox_53 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_53.setGeometry(QtCore.QRect(80, 110, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_53.setFont(font)
        self.checkBox_53.setObjectName("checkBox_53")
        self.checkBox_54 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_54.setGeometry(QtCore.QRect(80, 160, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_54.setFont(font)
        self.checkBox_54.setObjectName("checkBox_54")
        self.checkBox_57 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_57.setGeometry(QtCore.QRect(80, 244, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_57.setFont(font)
        self.checkBox_57.setObjectName("checkBox_57")
        self.checkBox_58 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_58.setGeometry(QtCore.QRect(80, 204, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_58.setFont(font)
        self.checkBox_58.setObjectName("checkBox_58")
        self.checkBox_56 = QtWidgets.QCheckBox(self.groupBox_20)
        self.checkBox_56.setGeometry(QtCore.QRect(80, 280, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_56.setFont(font)
        self.checkBox_56.setObjectName("checkBox_56")
        self.groupBox_16 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_16.setGeometry(QtCore.QRect(300, 70, 681, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_16)
        self.checkBox_7.setGeometry(QtCore.QRect(230, 80, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_16)
        self.checkBox_11.setGeometry(QtCore.QRect(250, 160, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_16)
        self.checkBox_12.setGeometry(QtCore.QRect(190, 230, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_55 = QtWidgets.QCheckBox(self.groupBox_16)
        self.checkBox_55.setGeometry(QtCore.QRect(250, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_55.setFont(font)
        self.checkBox_55.setObjectName("checkBox_55")
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_21.setGeometry(QtCore.QRect(300, 70, 681, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setObjectName("groupBox_21")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox_8.setGeometry(QtCore.QRect(250, 65, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox_13.setGeometry(QtCore.QRect(250, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox_14.setGeometry(QtCore.QRect(250, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox_15.setGeometry(QtCore.QRect(250, 120, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox_16.setGeometry(QtCore.QRect(300, 180, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox_9.setGeometry(QtCore.QRect(250, 15, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.label_18 = QtWidgets.QLabel(self.tab_19)
        self.label_18.setEnabled(True)
        self.label_18.setGeometry(QtCore.QRect(701, 152, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.tab_19)
        self.label_17.setEnabled(True)
        self.label_17.setGeometry(QtCore.QRect(701, 74, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_17.setEnabled(True)
        self.lineEdit_17.setGeometry(QtCore.QRect(221, 75, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("border-radius:20px;")
        self.lineEdit_17.setText("")
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_17.setPlaceholderText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_33.setEnabled(True)
        self.pushButton_33.setGeometry(QtCore.QRect(160, 73, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_33.setStyleSheet("")
        self.pushButton_33.setText("")
        self.pushButton_33.setIcon(icon5)
        self.pushButton_33.setObjectName("pushButton_33")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_4.setGeometry(QtCore.QRect(226, 13, 411, 51))
        self.lineEdit_4.setStyleSheet("border-radius:20px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_19)
        self.comboBox_3.setGeometry(QtCore.QRect(221, 13, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_3.setStyleSheet("border-radius:20px;")
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.frame = QtWidgets.QFrame(self.tab_19)
        self.frame.setGeometry(QtCore.QRect(300, 300, 691, 361))
        self.frame.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget_4.addTab(self.tab_19, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(510, 30, 481, 571))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_18.setEnabled(True)
        self.comboBox_18.setGeometry(QtCore.QRect(20, 307, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_18.setFont(font)
        self.comboBox_18.setStyleSheet("border-radius:20px;")
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.label_63 = QtWidgets.QLabel(self.groupBox_12)
        self.label_63.setGeometry(QtCore.QRect(316, 280, 61, 111))
        self.label_63.setStyleSheet("image: url(:/lavatory.png);")
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.label_84 = QtWidgets.QLabel(self.groupBox_12)
        self.label_84.setEnabled(True)
        self.label_84.setGeometry(QtCore.QRect(400, 300, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.groupBox_12)
        self.label_85.setEnabled(True)
        self.label_85.setGeometry(QtCore.QRect(339, 160, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 170, 311, 61))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_47 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_47.setGeometry(QtCore.QRect(70, 450, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_47.setObjectName("pushButton_47")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_13.setGeometry(QtCore.QRect(0, 30, 481, 571))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_6.setGeometry(QtCore.QRect(11, 170, 311, 61))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_27 = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_27.setEnabled(True)
        self.comboBox_27.setGeometry(QtCore.QRect(11, 307, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_27.setFont(font)
        self.comboBox_27.setStyleSheet("border-radius:20px;")
        self.comboBox_27.setObjectName("comboBox_27")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.label_86 = QtWidgets.QLabel(self.groupBox_13)
        self.label_86.setEnabled(True)
        self.label_86.setGeometry(QtCore.QRect(391, 300, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.groupBox_13)
        self.label_87.setGeometry(QtCore.QRect(307, 280, 61, 111))
        self.label_87.setStyleSheet("image: url(:/lavatory.png);")
        self.label_87.setText("")
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.groupBox_13)
        self.label_88.setEnabled(True)
        self.label_88.setGeometry(QtCore.QRect(330, 160, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.pushButton_48 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_48.setGeometry(QtCore.QRect(240, 450, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_49.setGeometry(QtCore.QRect(10, 450, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_49.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_49.setStyleSheet("")
        self.pushButton_49.setIcon(icon9)
        self.pushButton_49.setIconSize(QtCore.QSize(63, 63))
        self.pushButton_49.setObjectName("pushButton_49")
        self.label_89 = QtWidgets.QLabel(self.groupBox_13)
        self.label_89.setEnabled(True)
        self.label_89.setGeometry(QtCore.QRect(360, 72, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.comboBox_28 = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_28.setEnabled(True)
        self.comboBox_28.setGeometry(QtCore.QRect(13, 70, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_28.setFont(font)
        self.comboBox_28.setStyleSheet("")
        self.comboBox_28.setEditable(True)
        self.comboBox_28.setObjectName("comboBox_28")
        self.comboBox_28.addItem("")
        self.tabWidget_4.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tab_7, "")
        self.tabWidget.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "المبيعات"))
        self.pushButton_2.setText(_translate("MainWindow", "التحاليل  "))
        self.pushButton_3.setText(_translate("MainWindow", "السجل"))
        self.pushButton_4.setText(_translate("MainWindow", "الاعدادات"))
        self.pushButton_5.setText(_translate("MainWindow", "المراجعين   "))
        self.pushButton_12.setText(_translate("MainWindow", "تسجيل الدخول   "))
        self.pushButton_7.setText(_translate("MainWindow", "تسجيل الدخول"))
        self.label.setText(_translate("MainWindow", "          هل نسيت كلمة المرور        "))
        self.pushButton_8.setText(_translate("MainWindow", "استعادة كلمة المرور"))
        self.label_2.setText(_translate("MainWindow", "اسم المستخدم"))
        self.label_3.setText(_translate("MainWindow", "   كلمة المرور"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_5.setText(_translate("MainWindow", "اسم المستخدم"))
        self.pushButton_10.setText(_translate("MainWindow", "استعادة كلمة المرور"))
        self.pushButton_21.setText(_translate("MainWindow", "عودة لتسجيل الدخول"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "الرقم التعريفي"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "اسم المراجع"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "عمر المراجع"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "طبيب المراجع"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "التاريخ"))
        self.label_60.setText(_translate("MainWindow", "الاسم الكامل للمراجع"))
        self.pushButton_36.setText(_translate("MainWindow", "بحث"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), _translate("MainWindow", "كل المراجعين"))
        self.label_53.setText(_translate("MainWindow", "الرقم التعريفي للمراجع"))
        self.pushButton_29.setText(_translate("MainWindow", "بحث    "))
        self.groupBox_10.setTitle(_translate("MainWindow", "المعلومات العامة للمراجع"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "الاسم"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "العمر"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الجنس"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "الطبيب"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "عدد التحليلات"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "التحاليل المعمولة"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "المبلغ المدفوع"))
        self.groupBox_11.setTitle(_translate("MainWindow", "تحاليل المراجع"))
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "الاسم"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "التحليل"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "النتيجة"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "التاريخ"))
        self.pushButton_42.setText(_translate("MainWindow", "بحث بالتاريخ"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("MainWindow", "معلومات المراجع"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Page"))
        self.groupBox_6.setTitle(_translate("MainWindow", "معلومات المراجع"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "انثى"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "ذكر"))
        self.label_36.setText(_translate("MainWindow", "الجنس"))
        self.label_37.setText(_translate("MainWindow", "العمر"))
        self.label_38.setText(_translate("MainWindow", "ملاحظات"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "عدوية شمس سعيد"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "داود سلمان"))
        self.label_39.setText(_translate("MainWindow", "الطبيب"))
        self.label_42.setText(_translate("MainWindow", "اسم المراجع"))
        self.groupBox_7.setTitle(_translate("MainWindow", "التحليل"))
        self.label_40.setText(_translate("MainWindow", "التحليل"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "--------------------------"))
        self.label_41.setText(_translate("MainWindow", "النتيجة"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "الاسم"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "التحليل"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "النتيجة"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "الطبيب"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "السعر"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "حذف"))
        self.pushButton_17.setText(_translate("MainWindow", "اضافة"))
        self.pushButton_18.setText(_translate("MainWindow", "طباعة  "))
        self.label_44.setText(_translate("MainWindow", "السعر الكلي"))
        self.label_54.setText(_translate("MainWindow", "المراجع"))
        self.pushButton_34.setText(_translate("MainWindow", "معاينة"))
        self.pushButton_35.setText(_translate("MainWindow", "تفريغ"))
        self.pushButton_43.setText(_translate("MainWindow", "بحث بالتاريخ"))
        self.pushButton_44.setText(_translate("MainWindow", "اكثر من تحليل"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "البيع اليومي"))
        self.pushButton_19.setText(_translate("MainWindow", "بحث"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "الرقم التعريفي"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الاسم"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "العمر"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "الطبيب"))
        self.label_55.setText(_translate("MainWindow", "الاسم الكامل للمراجع"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "مبيعات اليوم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "----------------------"))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "اسم التحليل المطابق"))
        self.comboBox_19.setItemText(2, _translate("MainWindow", "السعر المطابق"))
        self.comboBox_19.setItemText(3, _translate("MainWindow", "الصنف"))
        self.pushButton_20.setText(_translate("MainWindow", "بحث"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "اسم التحليل"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "نوع النتيجة"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "النتيجة الطبيعية"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "الوحدة"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "السعر"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "الصنف"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "كل التحليلات"))
        self.groupBox_4.setTitle(_translate("MainWindow", "اضافة تحليل"))
        self.label_45.setText(_translate("MainWindow", "اسم التحليل"))
        self.label_46.setText(_translate("MainWindow", "النتيجة الطبيعية"))
        self.label_48.setText(_translate("MainWindow", "السعر"))
        self.pushButton_26.setText(_translate("MainWindow", "اضافة"))
        self.label_56.setText(_translate("MainWindow", "نوع النتيجة"))
        self.comboBox_22.setItemText(0, _translate("MainWindow", "----------------------"))
        self.comboBox_22.setItemText(1, _translate("MainWindow", "حقل كتابة"))
        self.comboBox_22.setItemText(2, _translate("MainWindow", "خيارات"))
        self.comboBox_22.setItemText(3, _translate("MainWindow", "خيارات مع تعديل"))
        self.comboBox_22.setItemText(4, _translate("MainWindow", "عدد"))
        self.label_58.setText(_translate("MainWindow", "الصنف"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "النتيجة الطبيعية التي سوف تطبع "))
        self.label_47.setText(_translate("MainWindow", "الوحدة"))
        self.label_61.setText(_translate("MainWindow", "الخيارات"))
        self.groupBox_9.setTitle(_translate("MainWindow", "تعديل تحليل"))
        self.comboBox_21.setItemText(0, _translate("MainWindow", "----------------------"))
        self.pushButton_27.setText(_translate("MainWindow", "حفظ"))
        self.pushButton_28.setText(_translate("MainWindow", "حذف"))
        self.label_49.setText(_translate("MainWindow", "الوحدة"))
        self.label_50.setText(_translate("MainWindow", "السعر"))
        self.label_57.setText(_translate("MainWindow", "نوع النتيجة"))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "النتيجة الطبيعية التي سوف تطبع "))
        self.label_51.setText(_translate("MainWindow", "النتيجة الطبيعية"))
        self.label_59.setText(_translate("MainWindow", "الصنف"))
        self.label_52.setText(_translate("MainWindow", "اسم التحليل"))
        self.label_62.setText(_translate("MainWindow", "الخيارات"))
        self.comboBox_25.setItemText(0, _translate("MainWindow", "----------------------"))
        self.comboBox_25.setItemText(1, _translate("MainWindow", "حقل كتابة"))
        self.comboBox_25.setItemText(2, _translate("MainWindow", "خيارات"))
        self.comboBox_25.setItemText(3, _translate("MainWindow", "خيارات مع تعديل"))
        self.comboBox_25.setItemText(4, _translate("MainWindow", "عدد"))
        self.label_71.setText(_translate("MainWindow", "التحليل"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "اضافة تحليل"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "المستخدم"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "العملية"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الحقل"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "التاريخ"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "--------------"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "مبيع يومي"))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "تحليل"))
        self.comboBox_20.setItemText(3, _translate("MainWindow", "مشتريات"))
        self.comboBox_20.setItemText(4, _translate("MainWindow", "مراجعين"))
        self.comboBox_20.setItemText(5, _translate("MainWindow", "مستخدم"))
        self.comboBox_24.setItemText(0, _translate("MainWindow", "--------------"))
        self.comboBox_24.setItemText(1, _translate("MainWindow", "تسجيل دخول"))
        self.comboBox_24.setItemText(2, _translate("MainWindow", "تسجيل خروج"))
        self.comboBox_24.setItemText(3, _translate("MainWindow", "اضافة"))
        self.comboBox_24.setItemText(4, _translate("MainWindow", "تعديل"))
        self.comboBox_24.setItemText(5, _translate("MainWindow", "حذف"))
        self.comboBox_24.setItemText(6, _translate("MainWindow", "بحث"))
        self.comboBox_24.setItemText(7, _translate("MainWindow", "طباعة"))
        self.label_15.setText(_translate("MainWindow", "العملية"))
        self.label_16.setText(_translate("MainWindow", "الحقل"))
        self.pushButton_22.setText(_translate("MainWindow", "حذف الكل    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.pushButton_9.setText(_translate("MainWindow", "برتقالي غامق"))
        self.pushButton_11.setText(_translate("MainWindow", "رصاصي غامق"))
        self.pushButton_13.setText(_translate("MainWindow", "ازرق غامق"))
        self.pushButton_14.setText(_translate("MainWindow", "ازرق غامق 2"))
        self.pushButton_15.setText(_translate("MainWindow", "ازرق فاتح"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MainWindow", "الشكل"))
        self.label_19.setText(_translate("MainWindow", "مسار ملفات التحاليل"))
        self.label_20.setText(_translate("MainWindow", "مسار حفظ الملفات"))
        self.pushButton_24.setText(_translate("MainWindow", "تطبيق"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("MainWindow", "المسارات"))
        self.label_64.setText(_translate("MainWindow", "اسم المريض"))
        self.label_65.setText(_translate("MainWindow", "لقب المريض"))
        self.label_69.setText(_translate("MainWindow", "اسم الطبيب"))
        self.label_70.setText(_translate("MainWindow", "لقب الطبيب"))
        self.label_72.setText(_translate("MainWindow", "رقم الهاتف 1"))
        self.label_73.setText(_translate("MainWindow", "رقم الهاتف 2"))
        self.label_74.setText(_translate("MainWindow", "العنوان"))
        self.label_75.setText(_translate("MainWindow", "اسم الموظف 1"))
        self.label_76.setText(_translate("MainWindow", "شهادة الموظف 1"))
        self.label_77.setText(_translate("MainWindow", "شهادة الموظف 2"))
        self.label_78.setText(_translate("MainWindow", "اسم الموظف 2"))
        self.label_79.setText(_translate("MainWindow", "اسم المختبر"))
        self.pushButton_31.setText(_translate("MainWindow", "تطبيق"))
        self.label_80.setText(_translate("MainWindow", "اسم المريضة"))
        self.label_81.setText(_translate("MainWindow", "لقب المريضة"))
        self.label_82.setText(_translate("MainWindow", "اسم الطبيبة"))
        self.label_83.setText(_translate("MainWindow", "لقب الطبيبة"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), _translate("MainWindow", "تعديل شكل التقارير"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "الاسم"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الكمية"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "سعر القطعة"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "السعر الكلي"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "تاريخ الشراء"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "حذف"))
        self.pushButton_16.setText(_translate("MainWindow", "اضافة"))
        self.label_7.setText(_translate("MainWindow", "سعر القطعة"))
        self.label_8.setText(_translate("MainWindow", "تاريخ الشراء"))
        self.label_12.setText(_translate("MainWindow", "أسم المنتج"))
        self.label_14.setText(_translate("MainWindow", "الكمية"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), _translate("MainWindow", "المشتريات"))
        self.label_21.setText(_translate("MainWindow", "العنصر"))
        self.label_68.setText(_translate("MainWindow", "|"))
        self.label_66.setText(_translate("MainWindow", "من"))
        self.label_67.setText(_translate("MainWindow", "الى"))
        self.pushButton_23.setText(_translate("MainWindow", "بحث"))
        self.label_23.setText(_translate("MainWindow", "المبلغ المصروف"))
        self.label_24.setText(_translate("MainWindow", "الربح الكلي"))
        self.label_25.setText(_translate("MainWindow", "نسبة الربح"))
        self.label_26.setText(_translate("MainWindow", "المبلغ العائد"))
        self.label_27.setText(_translate("MainWindow", "الاصناف الاعلى مبيعاً"))
        self.label_28.setText(_translate("MainWindow", "الاصناف الاعلى حصداً للمال"))
        self.label_29.setText(_translate("MainWindow", "التحاليل الاعلى مبيعاً"))
        self.label_32.setText(_translate("MainWindow", "التحاليل الاعلى حصداً للمال"))
        self.label_33.setText(_translate("MainWindow", "الايام الاعلى حصداً للمال"))
        self.label_34.setText(_translate("MainWindow", "الايام الاعلى مبيعاً"))
        self.label_43.setText(_translate("MainWindow", "مرات البيع"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), _translate("MainWindow", "الاحصائيات"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "                      example@gmail.com"))
        self.label_13.setText(_translate("MainWindow", "أسم المستخدم"))
        self.groupBox_3.setTitle(_translate("MainWindow", "الصلاحيات"))
        self.groupBox_15.setTitle(_translate("MainWindow", "صفحة التحاليل"))
        self.checkBox_40.setText(_translate("MainWindow", "الدخول للصفحة"))
        self.checkBox_41.setText(_translate("MainWindow", "حذف تحليل"))
        self.checkBox_42.setText(_translate("MainWindow", "اضافة تحليل"))
        self.checkBox_43.setText(_translate("MainWindow", "تعديل تحليل"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "---------------------------------"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "المبيع اليومي"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "التحاليل"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "المراجعين"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "السجل"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "الاعدادات"))
        self.label_22.setText(_translate("MainWindow", "الصفحة"))
        self.pushButton_25.setText(_translate("MainWindow", "اضافة"))
        self.pushButton_37.setText(_translate("MainWindow", "حذف   "))
        self.checkBox.setText(_translate("MainWindow", "كامل الصلاحيات"))
        self.groupBox_19.setTitle(_translate("MainWindow", "صفحة السجل"))
        self.checkBox_44.setText(_translate("MainWindow", "الدخول للصفحة"))
        self.checkBox_45.setText(_translate("MainWindow", "حذف كل السجل"))
        self.groupBox_20.setTitle(_translate("MainWindow", "صفحة الاعدادات"))
        self.checkBox_46.setText(_translate("MainWindow", "الدخول للصفحة"))
        self.checkBox_47.setText(_translate("MainWindow", "تعديل شكل التقرير"))
        self.checkBox_48.setText(_translate("MainWindow", "اضافة مشتريات"))
        self.checkBox_49.setText(_translate("MainWindow", "تغيير الشكل"))
        self.checkBox_50.setText(_translate("MainWindow", "تغيير مسار الملفات"))
        self.checkBox_51.setText(_translate("MainWindow", "اضافة موظف"))
        self.checkBox_52.setText(_translate("MainWindow", "تعديل موظف"))
        self.checkBox_53.setText(_translate("MainWindow", "حذف موظف"))
        self.checkBox_54.setText(_translate("MainWindow", "اظهار الاحصائيات"))
        self.checkBox_57.setText(_translate("MainWindow", "تعديل موظف"))
        self.checkBox_58.setText(_translate("MainWindow", "اضافة موظف"))
        self.checkBox_56.setText(_translate("MainWindow", "حذف موظف"))
        self.groupBox_16.setTitle(_translate("MainWindow", "صفحة المراجعين"))
        self.checkBox_7.setText(_translate("MainWindow", "اظهار كل المراجعين"))
        self.checkBox_11.setText(_translate("MainWindow", "البحث عن مراجع"))
        self.checkBox_12.setText(_translate("MainWindow", "اظهار معلومات مراجع"))
        self.checkBox_55.setText(_translate("MainWindow", "الدخول للصفحة"))
        self.groupBox_21.setTitle(_translate("MainWindow", "صفحة المبيع اليومي"))
        self.checkBox_8.setText(_translate("MainWindow", "اضافة مبيع يومي"))
        self.checkBox_13.setText(_translate("MainWindow", "بحث في المبيعات اليومية"))
        self.checkBox_14.setText(_translate("MainWindow", "بحث بالتاريخ"))
        self.checkBox_15.setText(_translate("MainWindow", "معاينة التقرير"))
        self.checkBox_16.setText(_translate("MainWindow", "طبع التقرير"))
        self.checkBox_9.setText(_translate("MainWindow", "الدخول للصفحة"))
        self.label_18.setText(_translate("MainWindow", "الايميل"))
        self.label_17.setText(_translate("MainWindow", "كلمة المرور"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_19), _translate("MainWindow", "الموظفين"))
        self.groupBox_12.setTitle(_translate("MainWindow", "اضافة طبيب"))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "انثى"))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "ذكر"))
        self.label_84.setText(_translate("MainWindow", "الجنس"))
        self.label_85.setText(_translate("MainWindow", "اسم الطبيب"))
        self.lineEdit_5.setStyleSheet(_translate("MainWindow", "border-radius:20px;"))
        self.pushButton_47.setText(_translate("MainWindow", "اضافة"))
        self.groupBox_13.setTitle(_translate("MainWindow", "تعديل , حذف طبيب"))
        self.lineEdit_6.setStyleSheet(_translate("MainWindow", "border-radius:20px;"))
        self.comboBox_27.setItemText(0, _translate("MainWindow", "انثى"))
        self.comboBox_27.setItemText(1, _translate("MainWindow", "ذكر"))
        self.label_86.setText(_translate("MainWindow", "الجنس"))
        self.label_88.setText(_translate("MainWindow", "اسم الطبيب"))
        self.pushButton_48.setText(_translate("MainWindow", "حفظ"))
        self.pushButton_49.setText(_translate("MainWindow", "حذف   "))
        self.label_89.setText(_translate("MainWindow", "الطبيب"))
        self.comboBox_28.setItemText(0, _translate("MainWindow", "-----------------------------"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_3), _translate("MainWindow", "اضافة طبيب"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
