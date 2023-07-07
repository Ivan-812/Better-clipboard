from PyQt5 import QtWidgets, uic, QtGui, QtCore
import configparser

class SettingsDialog(QtWidgets.QDialog):

    setting_updated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("settings.ui", self)  # Load the settings form

        # open config
        self.config = configparser.ConfigParser()
        try:
            self.config.read("settings.ini")
        except:
            self.save('opacity', '95')


        # Set slider
        self.opacity_value.setValidator(QtGui.QIntValidator(1, 100))
        self.opacity_slider.valueChanged.connect(self.opacity_slider_onchange)
        self.opacity_value.textChanged.connect(self.opacity_text_onchange)
        self.opacity_value.setText(self.config["Settings"]['opacity'])

        # Save/ leave
        self.button_box.accepted.connect(self.accept)
        self.button_box.accepted.connect(self.reject)


    def opacity_slider_onchange(self, value):
        self.opacity_value.setText(str(value))

    def opacity_text_onchange(self, text):
        if text:
            self.opacity_slider.setValue(int(text))


    # Config
    def get_config(self):
        return self.config

    def accept(self):
        self.config["Settings"]['opacity'] = self.opacity_value.text()

        with open("settings.ini", "w") as configfile:
            self.config.write(configfile)
        self.setting_updated.emit()
        super().accept()

    def reject(self):
        self.opacity_value.setText(self.config["Settings"]['opacity'])
        super().reject()