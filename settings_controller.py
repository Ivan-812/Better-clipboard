import os
import re

from PyQt5 import QtWidgets, QtGui, QtCore
import configparser

from user_interface.settings_ui import Ui_settings

class SettingsDialog(QtWidgets.QDialog, Ui_settings):

    # For adding new settings, change below:
    # 1. reset_default_config
    # 2. get_config
    # 3. update_ui
    # 4. accept

    setting_updated = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        # super().__init__(parent)
        # uic.loadUi("settings.ui", self)  # Load the settings form

        super(SettingsDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # open config
        self.config = configparser.ConfigParser()
        self.read_config_file()

        self.init_hotkey()

        # Set slider
        self.opacity_value.setValidator(QtGui.QIntValidator(1, 100))
        self.opacity_slider.valueChanged.connect(self.opacity_slider_onchange)
        self.opacity_value.textChanged.connect(self.opacity_text_onchange)

        # Save/ leave
        self.button_box.accepted.connect(self.accept)
        self.button_box.accepted.connect(self.reject)

        self.update_ui()

    # Hotkey
    def init_hotkey(self):
        self.key_reset_button.clicked.connect(self.reset_default_config)
        for i in range(10):
            text_name = f'hotkey_text_{i}'
            label = getattr(self, text_name)
            label.setText(str(i))

            button_name = f'hotkey_button_{i}'
            button = getattr(self, button_name)
            button.setText('Save')
            # button.clicked.connect(lambda check, i=i: self.on_hotkey_edit(i))

            key_seq_text = f'key_seq_{i}'
            key_seq = getattr(self, key_seq_text)
            key = f'Alt+{i}'
            key_seq.setKeySequence(QtGui.QKeySequence(key))
            # key_seq.setEnabled(False)

    def on_hotkey_edit(self, i):
        key_seq = getattr(self, f'key_seq_{i}')
        button = getattr(self, f'hotkey_button_{i}')
        if key_seq.isEnabled():
            button.setText('Edit')
        else:
            button.setText('Save')
        key_seq.setEnabled(not key_seq.isEnabled())

    # Opacity
    def opacity_slider_onchange(self, value):
        self.opacity_value.setText(str(value))

    def opacity_text_onchange(self, text):
        if text:
            self.opacity_slider.setValue(int(text))

    # Config
    def read_config_file(self, filename='config/settings.ini'):
        if os.path.exists(filename):
            self.config.read(filename)
        else:
            self.reset_default_config()
            with open(filename, 'w') as configfile:
                self.config.write(configfile)

    def reset_default_config(self):
        self.config['APP_SETTINGS'] = {'opacity': '95', 'stay_on_top': 'False', 'delete_extra_key': 'False', 'toggle_frame': 'True'}
        self.config['HOTKEY_CLIPBOARD'] = {
            '1': '<alt>+1',
            '2': '<alt>+2',
            '3': '<alt>+3',
            '4': '<alt>+4',
            '5': '<alt>+5',
            '6': '<alt>+6',
            '7': '<alt>+7',
            '8': '<alt>+8',
            '9': '<alt>+9',
            '0': '<alt>+0',
        }
        self.update_ui()

    def get_config(self, name=None):
        if name is None:
            return self.config
        elif name == 'opacity':
            return self.config['APP_SETTINGS']['opacity']
        elif name == 'hotkey':
            return self.config['HOTKEY_CLIPBOARD']
        elif name == 'stay_on_top':
            return self.config['APP_SETTINGS']['stay_on_top']
        elif name == 'delete_extra_key':
            return self.config['APP_SETTINGS']['delete_extra_key']
        elif name == 'toggle_frame':
            return self.config['APP_SETTINGS']['toggle_frame']
        else:
            return None

    # UI
    def update_ui(self):
        self.opacity_value.setText(self.config['APP_SETTINGS']['opacity'])
        self.stay_on_top.setChecked(bool(self.config['APP_SETTINGS']['stay_on_top'] == 'True'))
        self.delete_extra_key.setChecked(bool(self.config['APP_SETTINGS']['delete_extra_key'] == 'True'))
        self.toggle_frame.setChecked(bool(self.config['APP_SETTINGS']['toggle_frame'] == 'True'))

        if self.config['APP_SETTINGS']['stay_on_top'] == 'True':
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

        for i in range(10):
            key_seq = getattr(self, f'key_seq_{i}')
            key_string = self.config['HOTKEY_CLIPBOARD'][str(i)]
            key_seq.setKeySequence(QtGui.QKeySequence(re.sub(r'<(ctrl|alt|shift|super)>', lambda m: m.group(1).title(), key_string)))

    def accept(self):
        self.config["APP_SETTINGS"]['opacity'] = self.opacity_value.text()
        self.config['APP_SETTINGS']['stay_on_top'] = str(self.stay_on_top.isChecked())
        self.config['APP_SETTINGS']['delete_extra_key'] = str(self.delete_extra_key.isChecked())
        self.config['APP_SETTINGS']['toggle_frame'] = str(self.toggle_frame.isChecked())

        for i in range(10):
            key_seq = getattr(self, f'key_seq_{i}')
            self.config['HOTKEY_CLIPBOARD'][str(i)] = key_seq.keySequence().toString().lower().replace('ctrl', '<ctrl>').replace('alt', '<alt>').replace('shift', '<shift>').replace('meta', '<super>')

        with open("config/settings.ini", "w") as configfile:
            self.config.write(configfile)
        self.setting_updated.emit()
        super().accept()

    def reject(self):
        self.read_config_file()
        self.update_ui()
        super().reject()
