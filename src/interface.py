# -*- coding: utf-8 -*-

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QSlider,
    QFormLayout,
    QCheckBox,
    QMessageBox,
)


class Ui_Main(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(368, 201)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setStyleSheet('font: 10pt "Consolas";')
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.configBtn = QPushButton(Form)
        self.configBtn.setObjectName("configBtn")

        self.verticalLayout.addWidget(self.configBtn)

        self.startBtn = QPushButton(Form)
        self.startBtn.setObjectName("startBtn")
        self.startBtn.setShortcut("Return")

        self.verticalLayout.addWidget(self.startBtn)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("Memorizer")
        self.label.setText(
            "___  ___                          _              \n"
            "|  \\/  |                         (_)             \n"
            "| .  . | ___ _ __ ___   ___  _ __ _ _______ _ __ \n"
            "| |\\/| |/ _ \\ '_ ` _ \\ / _ \\| '__| |_  / _ \\ '__|\n"
            "| |  | |  __/ | | | | | (_) | |  | |/ /  __/ |   \n"
            "\\_|  |_/\\___|_| |_| |_|\\___/|_|  |_/___\\___|_|",
        )
        self.comboBox.setItemText(0, "--- 선택 ---")

        self.configBtn.setText(
            "환경설정 (제한시간 10초, 대소문자 무시)",
        )
        self.startBtn.setText("시작 (Enter)")

    # retranslateUi


class Ui_Config(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(257, 58)
        Form.setMinimumSize(QSize(257, 0))
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(15)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.horizontalSlider)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("Config")
        self.label.setText("제한시간 (기본 10초)")
        self.label_2.setText("영문명 대소문자 무시")

    # retranslateUi
