from fileinput import filename
from msilib.schema import Font
import os
import sys

from tkinter import font
from tkinter import Spinbox
import matplotlib
from matplotlib.pyplot import flag

# from PyQt5.uic import loadUiType
# from os import path

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPlainTextEdit,
    QInputDialog,
    QFileDialog,
    QAction,
    QToolBar,
    QShortcut,
    QMessageBox,
    QTextEdit,
    QColorDialog,
    QFontDialog,
    QTextEdit,
)
from PyQt5.QtGui import QFontDatabase, QFont, QKeySequence, QIcon
import numpy as np
from time import sleep

Form = uic.loadUiType(os.path.join(os.getcwd(), "untitled.ui"))[0]


class MainWindow(QMainWindow, Form):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.flag_bold = 0
        self.flag_italic = 0
        self.flag_underline = 0
        self.setupUi(self)
        self.setWindowTitle("Text editor")
        self.setStyleSheet("background-color: none;")
        self.spinBox.setValue(8)
        # self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)
        # self.setCentralWidget(self.editor)
        # setting icon
        self.leftAlignButton.setIcon(QIcon("./Resources/left_align.png"))
        self.rightAlignButton.setIcon(QIcon("./Resources/right_align.png"))
        self.centerAlignButton.setIcon(QIcon("./Resources/center_align.png"))
        # Setup the QTextEdit editor configuration

        # self.editor.setFont(fixedfont)
        self.NewButton.clicked.connect(self.Newpage)
        self.BoldButton.clicked.connect(self.Bold)
        self.italicButton.clicked.connect(self.italic)
        self.underlineButton.clicked.connect(self.underline)
        self.saveButton.clicked.connect(self.Save__File)
        self.OpenButton.clicked.connect(self.open_dialog_box)
        self.centerAlignButton.clicked.connect(self.center_align)
        self.leftAlignButton.clicked.connect(self.lef_align)
        self.rightAlignButton.clicked.connect(self.rig_align)
        self.ColorButton.clicked.connect(self.text_color)
        self.FontButton.clicked.connect(self.text_font)
        self.spinBox.valueChanged.connect(self.font_size)

        # getting current value
        self.spinBox.setValue(8)
        self.spinBox.valueChanged.connect(self.Font_change)

        # self.redoButton.clicked.connect(self.Redo_text)

        self.BoldButton.setStyleSheet("background-color : white")
        self.italicButton.setStyleSheet("background-color : white")
        self.BoldButton.setStyleSheet("background-color : white")
        self.underlineButton.setStyleSheet("background-color : white")
        self.NewButton.setStyleSheet("background-color : white")
        self.OpenButton.setStyleSheet("background-color : white")
        self.saveButton.setStyleSheet("background-color : white")
        self.ColorButton.setStyleSheet("background-color : white")
        self.FontButton.setStyleSheet("background-color : white")
        self.spinBox.setStyleSheet("background-color : white")

        # shortcuts
        self.open_new_file_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.open_new_file_shortcut.activated.connect(self.open_dialog_box)

        self.save_file_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.save_file_shortcut.activated.connect(self.Save__File)

        self.italic_text_shortcut = QShortcut(QKeySequence("Ctrl+I"), self)
        self.italic_text_shortcut.activated.connect(self.italic)

        self.bold_text_shortcut = QShortcut(QKeySequence("Ctrl+B"), self)
        self.bold_text_shortcut.activated.connect(self.Bold)

        self.underline_text_shortcut = QShortcut(QKeySequence("Ctrl+U"), self)
        self.underline_text_shortcut.activated.connect(self.underline)

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

        # cut action
        cut_action = QAction("Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.textEdit.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        # copy action
        copy_action = QAction("Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.textEdit.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        # paste action
        paste_action = QAction("Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.textEdit.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        # select all action
        select_action = QAction("Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.textEdit.selectAll)
        edit_toolbar.addAction(select_action)
        edit_menu.addAction(select_action)

        # fekr konam font ro darim okay mikonim inja
        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(5000000)
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)

    def underline(self):
        print("underline")
        # self.textEdit.setFontUnderline(True)
        print(self.flag_underline)
        if self.flag_underline == 0:
            self.textEdit.setFontUnderline(True)
            self.flag_underline = 1
            print(self.flag_underline)
        else:
            print(self.flag_underline)
            self.textEdit.setFontUnderline(False)
            self.flag_underline = 0
            print(self.flag_underline)

    def Newpage(self, event):
        print("newpage")
        messageBox = QMessageBox()
        title = "New page?"
        message = "WARNING !!\n\nIf you quit without saving, any changes made to the file will be lost.\n\nSave file before quiting?"

        reply = messageBox.question(
            self,
            title,
            message,
            messageBox.Yes | messageBox.No | messageBox.Cancel,
            messageBox.Cancel,
        )
        if reply == messageBox.Yes:
            return_value = self.Save__File()
            if return_value == False:
                event.ignore()
        elif reply == messageBox.No:
            self.textEdit.clear()
        else:
            messageBox.close()
        # self.open_dialog_box()

    def Bold(self):
        print("Bold clicked")
        print(self.flag_bold)
        if self.flag_bold == 0:
            self.textEdit.setFontWeight(QFont.Bold)
            self.flag_bold = 1
            print(self.flag_bold)
        else:
            print(self.flag_bold)
            self.textEdit.setFontWeight(QFont.Normal)
            self.flag_bold = 0
            print(self.flag_bold)

    def italic(self):
        print("italic clicked")
        print(self.flag_italic)
        if self.flag_italic == 0:
            self.textEdit.setFontItalic(True)
            self.flag_italic = 1
            print(self.flag_italic)
        else:
            print(self.flag_italic)
            self.textEdit.setFontItalic(False)
            self.flag_italic = 0
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
        if path:
            with open(path, "r") as f:
                # print(f.readline())
                # _text = f.readline()
                _text=f.read()
                self.textEdit.setText(_text)

    def Save__File(self):
        # S_File will get the directory path and extension.
        S__File = QFileDialog.getSaveFileName(
            None, "SaveTextFile", "/", "Text Files (*.txt)"
        )

        # This will let you access the test in your QTextEdit
        Text = self.textEdit.toPlainText()

        # This will prevent you from an error if pressed cancel on file dialog.
        if S__File[0]:
            # Finally this will Save your file to the path selected.
            with open(S__File[0], "w") as file:
                file.write(Text)

    def Font_change(self):
        value = self.spinBox.value()
        print(value)
        self.textEdit.setFontPointSize(value)

    def closeEvent(self, event):
        # if self.textEdit.empty() == 1:
        #     self.close()
        # self.
        messageBox = QMessageBox()
        title = "Quit Application?"
        message = "WARNING !!\n\nIf you quit without saving, any changes made to the file will be lost.\n\nSave file before quitting?"

        reply = messageBox.question(
            self,
            title,
            message,
            messageBox.Yes | messageBox.No | messageBox.Cancel,
            messageBox.Cancel,
        )
        if reply == messageBox.Yes:
            return_value = self.Save__File()
            if return_value == False:
                event.ignore()
        elif reply == messageBox.No:
            event.accept()
        else:
            event.ignore()

    def text_color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def text_font(self):
        # pass
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def font_size(self):
        # pass
        val = self.spinBox.value()
        self.textEdit.setFontPointSize(val)

    # alignments
    def center_align(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)

    def lef_align(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft)

    def rig_align(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
