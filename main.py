from fileinput import filename
import os
import sys
import matplotlib
from matplotlib.pyplot import flag

# from PyQt5.uic import loadUiType
# from os import path

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPlainTextEdit,
    QInputDialog,
    QFileDialog,
    QAction,
    QToolBar
)
from PyQt5.QtGui import QFontDatabase, QFont
import numpy as np
from time import sleep

Form = uic.loadUiType(os.path.join(os.getcwd(), "untitled.ui"))[0]


class MainWindow(QMainWindow, Form):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.flag_bold = 0
        self.flag_italic=0
        self.flag_underline=0
        self.setupUi(self)
        # self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)
        # self.setCentralWidget(self.editor)

        # Setup the QTextEdit editor configuration
        # fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        # fixedfont.setPointSize(12)
        # self.editor.setFont(fixedfont)
        self.NewButton.clicked.connect(self.Newpage)
        self.BoldButton.clicked.connect(self.Bold)
        self.italicButton.clicked.connect(self.italic)
        self.underlineButton.clicked.connect(self.underline)
        self.saveButton.clicked.connect(self.Save__File)
        self.OpenButton.clicked.connect(self.open_dialog_box)
        # self.redoButton.clicked.connect(self.Redo_text)

####################################################
        edit_toolbar = QToolBar("Edit")
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")
####################################################
        # undo action
        undo_action = QAction("UNDO", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.textEdit.undo)
        edit_toolbar.addAction(undo_action)
        edit_menu.addAction(undo_action)

        # redo action
        redo_action = QAction("REDO", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.textEdit.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)




        # fekr konam font ro darim okay mikonim inja
        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(5000000)
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)
    def underline(self):
        print("underline")
        # self.textEdit.setFontUnderline(True)
        print(self.flag_underline)
        if (self.flag_underline==0):
            self.textEdit.setFontUnderline(True)
            self.flag_underline=1
            print(self.flag_underline)
        else:
            print(self.flag_underline)
            self.textEdit.setFontUnderline(False)
            self.flag_underline=0
            print(self.flag_underline)
    def Newpage(self):
        print("newpage")
        self.textEdit.clear()
        # self.open_dialog_box()

    def Bold(self):
        print("Bold clicked")
        print(self.flag_bold)
        if (self.flag_bold==0):
            self.textEdit.setFontWeight(QFont.Bold)
            self.flag_bold=1
            print(self.flag_bold)
        else:
            print(self.flag_bold)
            self.textEdit.setFontWeight(QFont.Normal)
            self.flag_bold=0
            print(self.flag_bold)
    def italic(self):
        print("italic clicked")
        print(self.flag_italic)
        if (self.flag_italic==0):
            self.textEdit.setFontItalic(True)
            self.flag_italic=1
            print(self.flag_italic)
        else:
            print(self.flag_italic)
            self.textEdit.setFontItalic(False)
            self.flag_italic=0
            print(self.flag_italic)

            

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        print(filename)
        # if path[0]:
        #     in__data = open(path[0],'r')
        #     with in__data:
        #         Text__ = in__data.read()
        #         self.textEdit.setText(Text__)
        with open(path,"r") as f:
            # print(f.readline())
            _text = f.readline()
            self.textEdit.setText(_text)

    def Save__File(self):
        # S_File will get the directory path and extension.
        S__File = QFileDialog.getSaveFileName(None,'SaveTextFile','/', "Text Files (*.txt)")
    
        # This will let you access the test in your QTextEdit
        Text = self.textEdit.toPlainText()
    
        # This will prevent you from an error if pressed cancel on file dialog.
        if S__File[0]: 
        # Finally this will Save your file to the path selected.
            with open(S__File[0], 'w') as file:
                file.write(Text)


    def Redo_text(self):
        pass

# class PlotThread(QtCore.QThread):
#     update_trigger = QtCore.pyqtSignal(np.ndarray, np.ndarray)
#     finished_trigger = QtCore.pyqtSignal()

#     def __init__(self, window, decay):
#         QtCore.QThread.__init__(self, parent=window)
#         self.decay = decay
#         self.window = window

#     def run(self):
#         x = np.linspace(0, 2 * np.pi, 1000)
#         for n in range(20):
#             y = np.cos(n * x) * np.exp(-self.decay * x)
#             self.update_trigger.emit(x, y)
#             sleep(0.1)
#         self.finished_trigger.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
