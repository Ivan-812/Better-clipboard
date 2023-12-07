import os
import re

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QColorDialog
import configparser

from user_interface.home_settings_ui import Ui_home_button_settings



class HomeSettingsDialog(QtWidgets.QDialog, Ui_home_button_settings):
    home_settings_update = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(HomeSettingsDialog, self).__init__(*args, **kwargs)
        self.settings = QtCore.QSettings("Company", "App")
        self.setupUi(self)
        self.update_ui()


    # UI
    def update_ui(self):
        # Always on top
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        option_combo = getattr(self, 'option_choice')
        option_combo.currentIndexChanged.connect(self.on_option_combo_changed)
        for i in range(14):
            option_combo.addItem(f'{i+1}')

        getattr(self, 'color_button').clicked.connect(self.open_color_dialog)

    def open_color_dialog(self):
        color_dialog = QColorDialog(self)
        color_dialog.setWindowFlags(color_dialog.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        color_dialog.show()  # Redraw the dialog
        if color_dialog.exec_():
            color = color_dialog.selectedColor()
            if color.isValid():
                getattr(self, 'color_button').setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color.name()};
                    }}
                    QPushButton:hover {{
                        background-color: {color.lighter(120).name()};
                    }}
                """)

    # Set text-box to current choice
    def on_option_combo_changed(self, index):
        choice = self.option_choice.currentText()
        if self.settings.contains(f'home_button_{choice}_title'):
            # set Title
            self.title_text.setText(self.settings.value(f'home_button_{choice}_title'))
            # set Content
            if self.settings.value(f'home_button_{choice}_content')[:5] == 'm=cmd':
                self.type_choice.setCurrentIndex(2)
                self.content_text.setText(self.settings.value(f'home_button_{choice}_content')[5:])
            elif self.settings.value(f'home_button_{choice}_content')[:5] == 'm=fdr':
                self.type_choice.setCurrentIndex(1)
                self.content_text.setText(self.settings.value(f'home_button_{choice}_content')[5:])
            else:
                self.type_choice.setCurrentIndex(0)
                self.content_text.setText(self.settings.value(f'home_button_{choice}_content'))
            # set Color
            if self.settings.contains(f'home_button_{choice}_color'):
                getattr(self, 'color_button').setStyleSheet(self.settings.value(f'home_button_{choice}_color'))
            else:
                getattr(self, 'color_button').setStyleSheet("QTextEdit:enabled { background-color: #3E5771 }")
        else:
            self.title_text.setText("")
            self.content_text.setText("")

    def accept(self):
        title = getattr(self, 'title_text')
        content = getattr(self, 'content_text')
        type_choice = getattr(self, 'type_choice').currentText()
        color = getattr(self, 'color_button').styleSheet()
        edit = True if getattr(self, 'edit_radio').isChecked() else False
        index = getattr(self, 'option_choice').currentText()

        if edit:
            self.settings.setValue(f'home_button_{index}_title', title.toPlainText())
            self.settings.setValue(f'home_button_{index}_color', color)
            if type_choice == 'Command':
                self.settings.setValue(f'home_button_{index}_content', 'm=cmd' + content.toPlainText())
            elif type_choice == 'Folder':
                self.settings.setValue(f'home_button_{index}_content', 'm=fdr' + content.toPlainText())
            else:
                self.settings.setValue(f'home_button_{index}_content', content.toPlainText())
        else:
            self.settings.remove(f'home_button_{index}_title')
            self.settings.remove(f'home_button_{index}_content')

        self.home_settings_update.emit()
        super().accept()

    def reject(self):

        super().reject()
