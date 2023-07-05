from PyQt5 import QtWidgets
import sys

import ui as ui_class
import hotkey_controller
import clip

class UiController(QtWidgets.QMainWindow):
    def __init__(self):
	    # in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.ui = ui_class.Ui_BetterClipboard()
        self.ui.setupUi(self)
        self.init()

        self.hotkey_listener = hotkey_controller.HotkeyListener()

    def init(self):
        self.ui.current_value.setText(clip.get_json('recent'))
        for i in range(10):
            widget_name = f'entry_textEdit_{i}'
            widget = getattr(self.ui, widget_name)
            widget.setText(clip.get_json(i))
            widget.setEnabled(False)

            # self.ui.entry_edit_button_0.setText()

            # Edit buttons
            edit_name = f'entry_edit_button_{i}'
            edit = getattr(self.ui, edit_name)
            edit.setText('Edit')
            edit.clicked.connect(lambda check, i=i: self.set_edit_button(i))

            # Copy buttons
            copy_name = f'entry_copy_button_{i}'
            copy = getattr(self.ui, copy_name)
            copy.setText('Copy')
            copy.clicked.connect(lambda check, i=i: self.set_copy_button(i))
    
    def set_edit_button(self, i):
        text_edit = getattr(self.ui, f'entry_textEdit_{i}')
        edit = getattr(self.ui, f'entry_edit_button_{i}')
        copy = getattr(self.ui, f'entry_copy_button_{i}')
        if text_edit.isEnabled():
            edit.setText('Edit')
            copy.setText('Copy')
            clip.save_to_index(i, text_edit.toPlainText())
        else:
            edit.setText('Save')
            copy.setText('Save Recent')
        text_edit.setEnabled(not text_edit.isEnabled())
    
    def set_copy_button(self, i):
        text_edit = getattr(self.ui, f'entry_textEdit_{i}')
        if text_edit.isEnabled():
            return


# Function way
# def start():
#     app = QtWidgets.QApplication(sys.argv)
#     BetterClipboard = QtWidgets.QMainWindow()
#     ui = ui_class.Ui_BetterClipboard()
#     ui.setupUi(BetterClipboard)

#     # load_data(ui)

#     # For knowing have what function
#     # ui.entry_textEdit_0.toPlainText()

#     ui.current_value.setText(clip.get_json('recent'))
#     for i in range(10):
#         widget_name = f'entry_textEdit_{i}'
#         widget = getattr(ui, widget_name)
#         widget.setText(clip.get_json(i))
#         widget.setEnabled(False)

#         edit_name = f'entry_edit_button_{i}'
#         edit = getattr(ui, edit_name)
#         print(i)
#         edit.clicked.connect(lambda check, i=i: set_edit_button(ui, i))
#         print(i)
    



#     BetterClipboard.show()
#     sys.exit(app.exec_())

# def set_edit_button(ui, i):
#     text_edit = getattr(ui, f'entry_textEdit_{i}')
#     if text_edit.isEnabled():
#         clip.save_to_index(i, text_edit.toPlainText())
#     text_edit.setEnabled(not text_edit.isEnabled())

if __name__ == '__main__':
    # start()
    
    app = QtWidgets.QApplication(sys.argv)
    BetterClipboard = UiController()
    BetterClipboard.show()
    sys.exit(app.exec_())