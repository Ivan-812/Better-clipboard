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
        self.clipboard_manager = clip.ClipboardManager()
        self.num_of_clipboard = self.clipboard_manager.get_num_of_clipboards()

        self.hotkey_listener = hotkey_controller.HotkeyListener()
        self.hotkey_listener.send_signal.connect(self.on_hotkey_signal)

        self.init_ui_elements()
        self.update_ui()


    def init_ui_elements(self):

        self.clipboard_manager.clip()
        self.ui.current_value.setText(self.clipboard_manager.get_clipboard_data('recent'))
        self.ui.clipboard_active.toggled.connect(self.activate_clipboard_functions)

        # Create an instance of the SettingsDialog class
        self.settings_dialog = settings_controller.SettingsDialog()
        self.settings_dialog.setting_updated.connect(self.on_settings_updated)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.on_settings_updated()

        # Combo box (choose clipboard set)
        combo = self.ui.clipboard_set_combo
        recent = self.clipboard_manager.get_recent_clipboard()
        for i in range(self.num_of_clipboard):
            self.clipboard_manager.change_working_clipboard(i)
            combo.addItem(self.clipboard_manager.get_clipboard_data('name'))
        combo.addItem('Add new...')
        combo.activated.connect(self.combo_on_activated)
        self.clipboard_manager.change_working_clipboard(recent)

        for i in range(10):
            widget_name = f'entry_textEdit_{i}'
            widget = getattr(self.ui, widget_name)
            widget.setText(self.clipboard_manager.get_clipboard_data(i))
            widget.setEnabled(False)
            widget.setStyleSheet("QTextEdit:enabled { background-color: #3E5771 }")

            # Edit buttons
            edit_name = f'entry_edit_button_{i}'
            edit = getattr(self.ui, edit_name)
            edit.clicked.connect(lambda check, i=i: self.edit_button_onclick(i))

            # Copy buttons
            copy_name = f'entry_copy_button_{i}'
            copy = getattr(self.ui, copy_name)
            copy.clicked.connect(lambda check, i=i: self.copy_button_onclick(i))

        self.activate_clipboard_functions(True)

    def update_ui(self, index=-1):
        self.clipboard_manager.change_working_clipboard(index)
        if index < 0:
            index = self.clipboard_manager.get_recent_clipboard()
        self.ui.clipboard_set_combo.setCurrentIndex(index)
        self.ui.current_value.setText(self.clipboard_manager.get_clipboard_data('recent'))
        for i in range(10):
            widget_name = f'entry_textEdit_{i}'
            widget = getattr(self.ui, widget_name)
            widget.setText(self.clipboard_manager.get_clipboard_data(i))

    def open_settings(self):
        self.settings_dialog.exec_()

    def on_settings_updated(self):
        opacity = self.settings_dialog.get_config('opacity')
        hotkey = self.settings_dialog.get_config('hotkey')

        self.hotkey_listener.change_hotkeys(hotkey)
        self.setWindowOpacity(0.15 + (int(opacity) - 1) * 0.85/99)

    def button_sets_states(self, i, is_editing, enable=True):
        edit = getattr(self.ui, f'entry_edit_button_{i}')
        copy = getattr(self.ui, f'entry_copy_button_{i}')
        combo = self.ui.clipboard_set_combo

        edit.setEnabled(enable)
        copy.setEnabled(enable)
        # combo.setEnabled(enable)
        if is_editing:
            edit.setText('Save')
            copy.setText('Save Recent')
        else:
            edit.setText('Edit')
            copy.setText('Copy')

    def edit_button_onclick(self, i):
        text_edit = getattr(self.ui, f'entry_textEdit_{i}')
        if text_edit.isEnabled():
            self.button_sets_states(i, is_editing=False)
            self.clipboard_manager.save_to_index(i, text_edit.toPlainText())
        else:
            self.button_sets_states(i, is_editing=True)
        text_edit.setEnabled(not text_edit.isEnabled())
    
    def copy_button_onclick(self, i):
        text_edit = getattr(self.ui, f'entry_textEdit_{i}')
        if text_edit.isEnabled():
            self.clipboard_manager.save_to_index(i, self.clipboard_manager.get_clipboard_data('recent'))
            text_edit.setText(self.clipboard_manager.get_clipboard_data(i))
            text_edit.setEnabled(False)
            self.button_sets_states(i, is_editing=False)
        else:
            self.clipboard_manager.save_to_copy(self.clipboard_manager.get_clipboard_data(i))
            self.update_ui()

    def combo_on_activated(self, i):
        combo = self.ui.clipboard_set_combo
        text = combo.itemText(i)

        if text == 'Add new...':
            new_item, ok = QtWidgets.QInputDialog.getText(combo, "New Item", "Enter the name of the new item:\n(Type an existing name to DELETE)")
            # Check if the user clicked OK
            if ok:
                if new_item != '' and new_item != 'Default' and new_item != 'Add new...':
                    for j in range(combo.count()-1):
                        if combo.itemText(j) == new_item:
                            combo.removeItem(j)
                            self.clipboard_manager.manage_clipboards(new_item, 'delete')
                            self.update_ui(-2)
                            return
                    combo.insertItem(combo.count() - 1, new_item)
                    self.clipboard_manager.manage_clipboards(new_item, 'create')
                    self.update_ui(combo.count() - 2)
        else:
            self.update_ui(i)

    def activate_clipboard_functions(self, active):
        self.hotkey_listener.function_active = active
        for i in range(10):
            if active:
                self.button_sets_states(i, is_editing=False)
            else:
                self.button_sets_states(i, is_editing=False, enable=False)
                text_edit = getattr(self.ui, f'entry_textEdit_{i}')
                text_edit.setEnabled(False)

    @pyqtSlot(str, int)
    def on_hotkey_signal(self, function, i):
        if function == 'on_copy':
            self.clipboard_manager.clip()
            self.update_ui()
        elif function == 'paste_hotkey_onclick':
            self.clipboard_manager.paste_index(i)


if __name__ == '__main__':
    # start()
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    BetterClipboard = UiController()
    BetterClipboard.show()
    sys.exit(app.exec_())