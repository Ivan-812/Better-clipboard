from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import sys
import qdarkstyle

import ui as ui_class
import settings_controller
import hotkey_controller
import clip

class UiController(QtWidgets.QTabWidget, QObject):
    def __init__(self):
	    # in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.ui = ui_class.Ui_BetterClipboard()
        self.ui.setupUi(self)
        self.init()


    def init(self):

        clip.clip()
        self.ui.current_value.setText(clip.get_json('recent'))
        self.ui.clipboard_active.toggled.connect(self.switch)

        # Create an instance of the SettingsDialog class
        self.settings_dialog = settings_controller.SettingsDialog()
        self.settings_dialog.setting_updated.connect(self.on_settings_updated)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.on_settings_updated()

        self.hotkey_listener = hotkey_controller.HotkeyListener()
        self.hotkey_listener.hotkey_pressed.connect(self.on_copy)

        for i in range(10):
            widget_name = f'entry_textEdit_{i}'
            widget = getattr(self.ui, widget_name)
            widget.setText(clip.get_json(i))
            widget.setEnabled(False)
            widget.setStyleSheet("QTextEdit:enabled { background-color: #3E5771 }")

            # self.ui.entry_edit_button_0.setText()

            # Edit buttons
            edit_name = f'entry_edit_button_{i}'
            edit = getattr(self.ui, edit_name)
            edit.setText('Edit')
            edit.clicked.connect(lambda check, i=i: self.edit_button_onclick(i))

            # Copy buttons
            copy_name = f'entry_copy_button_{i}'
            copy = getattr(self.ui, copy_name)
            copy.setText('Copy')
            copy.clicked.connect(lambda check, i=i: self.copy_button_onclick(i))

    def on_settings_updated(self):
        config = self.settings_dialog.get_config()

        self.setWindowOpacity(0.15 + (int(config['Settings']['opacity']) - 1) * 0.85/99)

    def update(self):
        self.ui.current_value.setText(clip.get_json('recent'))
        for i in range(10):
            widget_name = f'entry_textEdit_{i}'
            widget = getattr(self.ui, widget_name)
            widget.setText(clip.get_json(i))

    def edit_button_onclick(self, i):
        text_edit = getattr(self.ui, f'entry_textEdit_{i}')
        if text_edit.isEnabled():
            self.button_sets_states(i, is_editing=False)
            clip.save_to_index(i, text_edit.toPlainText())
        else:
            self.button_sets_states(i, is_editing=True)
        text_edit.setEnabled(not text_edit.isEnabled())
    
    def copy_button_onclick(self, i):
        text_edit = getattr(self.ui, f'entry_textEdit_{i}')
        if text_edit.isEnabled():
            clip.save_to_index(i, clip.get_json('recent'))
            text_edit.setText(clip.get_json(i))
            text_edit.setEnabled(False)
            self.button_sets_states(i, is_editing=False)
        else:
            clip.save_to_copy(clip.get_json(i))
            self.update()

    def button_sets_states(self, i, is_editing, enable=True):
        edit = getattr(self.ui, f'entry_edit_button_{i}')
        copy = getattr(self.ui, f'entry_copy_button_{i}')

        edit.setEnabled(enable)
        copy.setEnabled(enable)
        if is_editing:
            edit.setText('Save')
            copy.setText('Save Recent')
        else:
            edit.setText('Edit')
            copy.setText('Copy')

    def switch(self, checked):
        self.hotkey_listener.function_active = checked
        for i in range(10):
            if checked:
                self.button_sets_states(i, is_editing=False)
            else:
                self.button_sets_states(i, is_editing=False, enable=False)
                text_edit = getattr(self.ui, f'entry_textEdit_{i}')
                text_edit.setEnabled(False)


    def open_settings(self):
        self.settings_dialog.exec_()

    @pyqtSlot(str)
    def on_copy(self, function):
        if function == 'on_copy':
            self.update()


if __name__ == '__main__':
    # start()
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    BetterClipboard = UiController()
    BetterClipboard.show()
    sys.exit(app.exec_())