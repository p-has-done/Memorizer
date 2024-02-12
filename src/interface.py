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
    QFrame,
    QProgressBar,
    QLineEdit,
)


class Ui_Main(QWidget):
    def setupUi(self):
        self.resize(368, 201)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self)
        self.label.setObjectName("label")
        self.label.setStyleSheet('font: 10pt "Consolas";')
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.configBtn = QPushButton(self)
        self.configBtn.setObjectName("configBtn")

        self.verticalLayout.addWidget(self.configBtn)

        self.startBtn = QPushButton(self)
        self.startBtn.setObjectName("startBtn")
        self.startBtn.setShortcut("Return")

        self.verticalLayout.addWidget(self.startBtn)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle("Memorizer")
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
            "환경설정(제한시간 10초, 대소문자 무시)",
        )
        self.startBtn.setText("시작(Enter)")

    # retranslateUi


class Ui_Config(QWidget):
    def setupUi(self):
        self.resize(256, 58)
        self.setMinimumSize(QSize(256, 0))
        self.formLayout = QFormLayout(self)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(15)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.horizontalSlider)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.checkBox = QCheckBox(self)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle("Config")
        self.label.setText("제한시간 (기본 10초)")
        self.label_2.setText("영문명 대소문자 무시")

    # retranslateUi


class Ui_Quiz(QWidget):
    def setupUi(self):
        self.resize(640, 480)
        self.setMinimumSize(QSize(640, 480))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_quiz = QLabel(self)
        self.label_quiz.setObjectName("label_quiz")

        self.verticalLayout.addWidget(self.label_quiz)

        self.label_image = QLabel(self)
        self.label_image.setObjectName("label_image")

        self.verticalLayout.addWidget(self.label_image)

        self.line = QFrame(self)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.lineEdit_kor = QLineEdit(self)
        self.lineEdit_kor.setObjectName("lineEdit_kor")

        self.verticalLayout.addWidget(self.lineEdit_kor)

        self.lineEdit_eng = QLineEdit(self)
        self.lineEdit_eng.setObjectName("lineEdit_eng")

        self.verticalLayout.addWidget(self.lineEdit_eng)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setShortcut("Return")

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, Form):
        self.setWindowTitle("Quiz")
        self.label_quiz.setText("사진")
        self.label_image.setText("문제")
        self.lineEdit_kor.setPlaceholderText("국문명")
        self.lineEdit_eng.setPlaceholderText("영문명")
        self.pushButton.setText("확인(Enter)")

    # retranslateUi


def warning(msg):
    QMessageBox.warning(None, "Warning", msg)


def critical(msg):
    QMessageBox.critical(None, "Error", msg)
    exit()
