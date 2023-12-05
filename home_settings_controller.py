import os
import re

from PyQt5 import QtWidgets, QtGui, QtCore
import configparser

from user_interface.home_settings_ui import Ui_home_button_settings



class HomeSettingsDialog(QtWidgets.QDialog, Ui_home_button_settings):
    home_settings_update = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(HomeSettingsDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.update_ui()
        self.settings = QtCore.QSettings("Company", "App")

    # UI
    def update_ui(self):
        # Always on top
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        option_combo = getattr(self, 'option_choice')
        for i in range(8):
            option_combo.addItem(f'{i+1}')


    def accept(self):
        title = getattr(self, 'title_text')
        content = getattr(self, 'content_text')
        edit = True if getattr(self, 'edit_radio').isChecked() else False
        index = getattr(self, 'option_choice').currentText()

        if edit:
            self.settings.setValue(f'home_button_{index}_title', title.toPlainText())
            self.settings.setValue(f'home_button_{index}_content', content.toPlainText())
        else:
            self.settings.remove(f'home_button_{index}_title')
            self.settings.remove(f'home_button_{index}_content')

        title.setText('')
        content.setText('')
        self.home_settings_update.emit()
        super().accept()

    def reject(self):

        super().reject()
