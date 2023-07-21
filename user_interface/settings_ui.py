# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(310, 399)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.opacity = QtWidgets.QVBoxLayout()
        self.opacity.setObjectName("opacity")
        self.hotkey_group = QtWidgets.QGroupBox(settings)
        self.hotkey_group.setObjectName("hotkey_group")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.hotkey_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.key_title = QtWidgets.QHBoxLayout()
        self.key_title.setObjectName("key_title")
        self.key_title_text = QtWidgets.QLabel(self.hotkey_group)
        self.key_title_text.setObjectName("key_title_text")
        self.key_title.addWidget(self.key_title_text)
        self.key_reset_button = QtWidgets.QPushButton(self.hotkey_group)
        self.key_reset_button.setObjectName("key_reset_button")
        self.key_title.addWidget(self.key_reset_button)
        self.key_title.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.key_title)
        self.hotkey_1 = QtWidgets.QHBoxLayout()
        self.hotkey_1.setObjectName("hotkey_1")
        self.hotkey_text_1 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_1.setObjectName("hotkey_text_1")
        self.hotkey_1.addWidget(self.hotkey_text_1)
        self.key_seq_1 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_1.setObjectName("key_seq_1")
        self.hotkey_1.addWidget(self.key_seq_1)
        self.hotkey_button_1 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_1.setObjectName("hotkey_button_1")
        self.hotkey_1.addWidget(self.hotkey_button_1)
        self.verticalLayout_2.addLayout(self.hotkey_1)
        self.hotkey_2 = QtWidgets.QHBoxLayout()
        self.hotkey_2.setObjectName("hotkey_2")
        self.hotkey_text_2 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_2.setObjectName("hotkey_text_2")
        self.hotkey_2.addWidget(self.hotkey_text_2)
        self.key_seq_2 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_2.setObjectName("key_seq_2")
        self.hotkey_2.addWidget(self.key_seq_2)
        self.hotkey_button_2 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_2.setObjectName("hotkey_button_2")
        self.hotkey_2.addWidget(self.hotkey_button_2)
        self.verticalLayout_2.addLayout(self.hotkey_2)
        self.hotkey_3 = QtWidgets.QHBoxLayout()
        self.hotkey_3.setObjectName("hotkey_3")
        self.hotkey_text_3 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_3.setObjectName("hotkey_text_3")
        self.hotkey_3.addWidget(self.hotkey_text_3)
        self.key_seq_3 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_3.setObjectName("key_seq_3")
        self.hotkey_3.addWidget(self.key_seq_3)
        self.hotkey_button_3 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_3.setObjectName("hotkey_button_3")
        self.hotkey_3.addWidget(self.hotkey_button_3)
        self.verticalLayout_2.addLayout(self.hotkey_3)
        self.hotkey_4 = QtWidgets.QHBoxLayout()
        self.hotkey_4.setObjectName("hotkey_4")
        self.hotkey_text_4 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_4.setObjectName("hotkey_text_4")
        self.hotkey_4.addWidget(self.hotkey_text_4)
        self.key_seq_4 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_4.setObjectName("key_seq_4")
        self.hotkey_4.addWidget(self.key_seq_4)
        self.hotkey_button_4 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_4.setObjectName("hotkey_button_4")
        self.hotkey_4.addWidget(self.hotkey_button_4)
        self.verticalLayout_2.addLayout(self.hotkey_4)
        self.hotkey_5 = QtWidgets.QHBoxLayout()
        self.hotkey_5.setObjectName("hotkey_5")
        self.hotkey_text_5 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_5.setObjectName("hotkey_text_5")
        self.hotkey_5.addWidget(self.hotkey_text_5)
        self.key_seq_5 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_5.setObjectName("key_seq_5")
        self.hotkey_5.addWidget(self.key_seq_5)
        self.hotkey_button_5 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_5.setObjectName("hotkey_button_5")
        self.hotkey_5.addWidget(self.hotkey_button_5)
        self.verticalLayout_2.addLayout(self.hotkey_5)
        self.hotkey_6 = QtWidgets.QHBoxLayout()
        self.hotkey_6.setObjectName("hotkey_6")
        self.hotkey_text_6 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_6.setObjectName("hotkey_text_6")
        self.hotkey_6.addWidget(self.hotkey_text_6)
        self.key_seq_6 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_6.setObjectName("key_seq_6")
        self.hotkey_6.addWidget(self.key_seq_6)
        self.hotkey_button_6 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_6.setObjectName("hotkey_button_6")
        self.hotkey_6.addWidget(self.hotkey_button_6)
        self.verticalLayout_2.addLayout(self.hotkey_6)
        self.hotkey_7 = QtWidgets.QHBoxLayout()
        self.hotkey_7.setObjectName("hotkey_7")
        self.hotkey_text_7 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_7.setObjectName("hotkey_text_7")
        self.hotkey_7.addWidget(self.hotkey_text_7)
        self.key_seq_7 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_7.setObjectName("key_seq_7")
        self.hotkey_7.addWidget(self.key_seq_7)
        self.hotkey_button_7 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_7.setObjectName("hotkey_button_7")
        self.hotkey_7.addWidget(self.hotkey_button_7)
        self.verticalLayout_2.addLayout(self.hotkey_7)
        self.hotkey_8 = QtWidgets.QHBoxLayout()
        self.hotkey_8.setObjectName("hotkey_8")
        self.hotkey_text_8 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_8.setObjectName("hotkey_text_8")
        self.hotkey_8.addWidget(self.hotkey_text_8)
        self.key_seq_8 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_8.setObjectName("key_seq_8")
        self.hotkey_8.addWidget(self.key_seq_8)
        self.hotkey_button_8 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_8.setObjectName("hotkey_button_8")
        self.hotkey_8.addWidget(self.hotkey_button_8)
        self.verticalLayout_2.addLayout(self.hotkey_8)
        self.hotkey_9 = QtWidgets.QHBoxLayout()
        self.hotkey_9.setObjectName("hotkey_9")
        self.hotkey_text_9 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_9.setObjectName("hotkey_text_9")
        self.hotkey_9.addWidget(self.hotkey_text_9)
        self.key_seq_9 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_9.setObjectName("key_seq_9")
        self.hotkey_9.addWidget(self.key_seq_9)
        self.hotkey_button_9 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_9.setObjectName("hotkey_button_9")
        self.hotkey_9.addWidget(self.hotkey_button_9)
        self.verticalLayout_2.addLayout(self.hotkey_9)
        self.hotkey_0 = QtWidgets.QHBoxLayout()
        self.hotkey_0.setObjectName("hotkey_0")
        self.hotkey_text_0 = QtWidgets.QLabel(self.hotkey_group)
        self.hotkey_text_0.setObjectName("hotkey_text_0")
        self.hotkey_0.addWidget(self.hotkey_text_0)
        self.key_seq_0 = QtWidgets.QKeySequenceEdit(self.hotkey_group)
        self.key_seq_0.setObjectName("key_seq_0")
        self.hotkey_0.addWidget(self.key_seq_0)
        self.hotkey_button_0 = QtWidgets.QPushButton(self.hotkey_group)
        self.hotkey_button_0.setObjectName("hotkey_button_0")
        self.hotkey_0.addWidget(self.hotkey_button_0)
        self.verticalLayout_2.addLayout(self.hotkey_0)
        self.opacity.addWidget(self.hotkey_group)
        self.verticalLayout.addLayout(self.opacity)
        self.app_group = QtWidgets.QGroupBox(settings)
        self.app_group.setObjectName("app_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.app_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.opacity_container = QtWidgets.QHBoxLayout()
        self.opacity_container.setContentsMargins(5, 5, 5, 5)
        self.opacity_container.setObjectName("opacity_container")
        self.opacity_text = QtWidgets.QLabel(self.app_group)
        self.opacity_text.setObjectName("opacity_text")
        self.opacity_container.addWidget(self.opacity_text)
        self.opacity_slider = QtWidgets.QSlider(self.app_group)
        self.opacity_slider.setMinimum(1)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setProperty("value", 95)
        self.opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.opacity_slider.setObjectName("opacity_slider")
        self.opacity_container.addWidget(self.opacity_slider)
        self.opacity_value = QtWidgets.QLineEdit(self.app_group)
        self.opacity_value.setObjectName("opacity_value")
        self.opacity_container.addWidget(self.opacity_value)
        self.opacity_container.setStretch(0, 1)
        self.opacity_container.setStretch(1, 5)
        self.opacity_container.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.opacity_container)
        self.switch_container = QtWidgets.QHBoxLayout()
        self.switch_container.setObjectName("switch_container")
        self.stay_on_top = QtWidgets.QCheckBox(self.app_group)
        self.stay_on_top.setObjectName("stay_on_top")
        self.switch_container.addWidget(self.stay_on_top)
        self.delete_extra_key = QtWidgets.QCheckBox(self.app_group)
        self.delete_extra_key.setObjectName("delete_extra_key")
        self.switch_container.addWidget(self.delete_extra_key)
        self.verticalLayout_3.addLayout(self.switch_container)
        self.verticalLayout.addWidget(self.app_group)
        self.button_box = QtWidgets.QDialogButtonBox(settings)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(settings)
        self.button_box.accepted.connect(settings.accept) # type: ignore
        self.button_box.rejected.connect(settings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Settings"))
        self.hotkey_group.setTitle(_translate("settings", "Keys Settings"))
        self.key_title_text.setText(_translate("settings", "Quick Paste Shortcut"))
        self.key_reset_button.setText(_translate("settings", "Reset"))
        self.hotkey_text_1.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_1.setText(_translate("settings", "PushButton"))
        self.hotkey_text_2.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_2.setText(_translate("settings", "PushButton"))
        self.hotkey_text_3.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_3.setText(_translate("settings", "PushButton"))
        self.hotkey_text_4.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_4.setText(_translate("settings", "PushButton"))
        self.hotkey_text_5.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_5.setText(_translate("settings", "PushButton"))
        self.hotkey_text_6.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_6.setText(_translate("settings", "PushButton"))
        self.hotkey_text_7.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_7.setText(_translate("settings", "PushButton"))
        self.hotkey_text_8.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_8.setText(_translate("settings", "PushButton"))
        self.hotkey_text_9.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_9.setText(_translate("settings", "PushButton"))
        self.hotkey_text_0.setText(_translate("settings", "TextLabel"))
        self.hotkey_button_0.setText(_translate("settings", "PushButton"))
        self.app_group.setTitle(_translate("settings", "Apperance Settings"))
        self.opacity_text.setText(_translate("settings", "Opacity"))
        self.opacity_value.setText(_translate("settings", "95"))
        self.stay_on_top.setText(_translate("settings", "Always stay on top"))
        self.delete_extra_key.setText(_translate("settings", "Delete extra key when paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = QtWidgets.QDialog()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())
