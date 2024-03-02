# -*- coding: utf-8 -*-

from Indicator import *
from os import listdir

from PySide6.QtCore import QMetaObject, QSize, Qt, QTimer, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSlider,
    QFormLayout,
    QCheckBox,
    QMessageBox,
    QFrame,
    QProgressBar,
    QLineEdit,
    QSpinBox,
    QSizePolicy,
)

"""
Comments/memo

- This code is not a good example of OOP and PySide6.
- Methods ordering:
  1. __init__
  2. setupUi
  3. setTexts
  4. setShortcuts
  5. @Slot annotated methods (in lexicographic order)
  6. events (in lexicographic order)
  7. others (in lexicographic order)
"""


class Home(QWidget):
    def __init__(self, answer_sheet):
        super().__init__()
        self.config_window = Config(self)
        self.quiz_window = Quiz(answer_sheet)
        self.time_limit = 20
        self.ignore_case = True
        self.problem_num = 5
        self.setupUi()

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

        self.verticalLayout.addWidget(self.startBtn)

        self.setTexts()
        self.setShortcuts()

        QMetaObject.connectSlotsByName(self)

    def setTexts(self):
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

        self.setConfigBtnText()
        self.startBtn.setText("시작(Enter)")

    def setShortcuts(self):
        self.startBtn.setShortcut("Return")

    @Slot()
    def on_configBtn_clicked(self):
        self.config_window.show()
        self.config_window.activateWindow()

    @Slot()
    def on_startBtn_clicked(self):
        if self.comboBox.currentIndex() == 0:
            self.comboBox.setFocus()
            return

        if self.quiz_window.isHidden():
            self.quiz_window.show()
            self.quiz_window.prepare(
                self.comboBox.currentText(),
                self.time_limit,
                self.ignore_case,
                self.problem_num,
            )
        self.config_window.activateWindow()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Quit",
            "정말 종료하시겠습니까?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.config_window.close()
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def setConfigBtnText(self):
        self.configBtn.setText(
            "환경설정(제한시간 %d초, 대소문자 무시%s, %d문제)"
            % (
                self.time_limit,
                "" if self.ignore_case else "하지 않음",
                self.problem_num,
            )
        )
        self.repaint()


class Config(QWidget):
    def __init__(self, main_widget):
        super().__init__()
        self.main_widget = main_widget
        self.setupUi()

    def setupUi(self):
        self.resize(256, 90)
        self.setMinimumSize(QSize(256, 0))
        self.formLayout = QFormLayout(self)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(15)
        self.horizontalSlider.setMaximum(25)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(20)
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

        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.spinBox = QSpinBox(self)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(30)
        self.spinBox.setValue(5)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox)

        self.setTexts()

        QMetaObject.connectSlotsByName(self)

    def setTexts(self):
        self.setWindowTitle("Config")
        self.label.setText("제한시간 (기본 20초)")
        self.label_2.setText("영문명 대소문자 무시")
        self.label_3.setText("문제 수")

    def closeEvent(self, event):
        self.main_widget.time_limit = self.horizontalSlider.value()
        self.main_widget.ignore_case = self.checkBox.isChecked()
        self.main_widget.problem_num = self.spinBox.value()
        self.main_widget.setConfigBtnText()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()


class Quiz(QWidget):
    def __init__(self, answer_sheet):
        super().__init__()
        self.answer_sheet = answer_sheet
        self.setupUi()
        self.timer = QTimer()

        # set timer
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateTimer)

    def setupUi(self):
        self.resize(960, 720)
        self.setMinimumSize(QSize(960, 720))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QLabel(self)
        self.label_image.setObjectName("label_image")
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        self.label_quiz = QLabel(self)
        self.label_quiz.setObjectName("label_quiz")
        self.label_quiz.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_quiz)

        # set size policies for two labels
        size_policy_image = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        size_policy_image.setHorizontalStretch(0)
        size_policy_image.setVerticalStretch(0)
        size_policy_image.setHeightForWidth(
            self.label_image.sizePolicy().hasHeightForWidth()
        )
        self.label_image.setSizePolicy(size_policy_image)

        size_policy_quiz = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        size_policy_quiz.setHorizontalStretch(0)
        size_policy_quiz.setVerticalStretch(0)
        size_policy_quiz.setHeightForWidth(
            self.label_quiz.sizePolicy().hasHeightForWidth()
        )
        self.label_quiz.setSizePolicy(size_policy_quiz)

        self.line = QFrame(self)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setTextVisible(False)
        self.progressBar.setMinimum(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.lineEdit_kor = QLineEdit(self)
        self.lineEdit_kor.setObjectName("lineEdit_kor")

        self.verticalLayout.addWidget(self.lineEdit_kor)

        self.lineEdit_eng = QLineEdit(self)
        self.lineEdit_eng.setObjectName("lineEdit_eng")

        self.verticalLayout.addWidget(self.lineEdit_eng)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.setTexts()
        self.setShortcuts()

        QMetaObject.connectSlotsByName(self)

    def setTexts(self):
        self.setWindowTitle("Quiz")
        self.label_image.setText("사진")
        self.label_quiz.setText("문제")
        self.lineEdit_kor.setPlaceholderText("국문명")
        self.lineEdit_eng.setPlaceholderText("영문명")
        self.pushButton.setText("확인(Enter)")

    def setShortcuts(self):
        self.pushButton.setShortcut("Return")

    @Slot()
    def on_pushButton_clicked(self):
        if self.lineEdit_kor.text() == "":
            self.lineEdit_kor.setFocus()
        elif self.lineEdit_eng.text() == "":
            self.lineEdit_eng.setFocus()
        else:
            self.completeResponse()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

    def clear(self):
        self.lineEdit_kor.setText("")
        self.lineEdit_eng.setText("")
        self.progressBar.setValue(0)
        self.timer.start()

    def completeResponse(self):
        self.submit()
        self.clear()
        self.lineEdit_kor.setFocus()

    def submit(self):
        current_answer = self.problem_list[self.problem_idx][1]
        response_kor = self.lineEdit_kor.text()
        response_eng = self.lineEdit_eng.text()

        if not (
            current_answer.cmpKor(response_kor)
            and current_answer.cmpEng(response_eng, self.ignore_case)
        ):
            self.wrong_responses.append((current_answer, response_kor, response_eng))

        self.problem_idx += 1
        if self.problem_idx == len(self.problem_list):
            # TODO
            pass

    def prepare(self, image_name, time_limit, ignore_case, problem_num):
        self.problem_list = pickProblems(self.answer_sheet, image_name, problem_num)
        self.wrong_responses = []
        self.ignore_case = ignore_case
        self.problem_idx = 0

        # set problem image (pixmap)
        pixmap = QPixmap()
        pixmap.load("resources/images/" + image_name)
        pixmap = pixmap.scaled(self.label_image.size(), aspectMode=Qt.KeepAspectRatio)
        self.label_image.setPixmap(pixmap)

        # set other UI components
        self.progressBar.setMaximum(time_limit - 1)
        self.label_quiz.setText("asdf")
        self.clear()

        self.timer.start()

    def updateTimer(self):
        curr_value = self.progressBar.value()
        if curr_value == self.progressBar.maximum():
            # timeout
            self.completeResponse()
        else:
            self.progressBar.setValue(curr_value + 1)


def warning(msg):
    QMessageBox.warning(None, "Warning", msg)


def critical(msg):
    QMessageBox.critical(None, "Error", msg)
    exit()


# THIS MUST BE HERE
app = QApplication([])

# basic variables
image_names = listdir("resources/images/")
answer_sheet = None
try:
    answer_sheet = getAnswerSheet()
except ValueError:
    critical("정답지(answer.csv)의 형식이 잘못되었습니다.\n")


# prepare chapter names
chapters, invalid_chapters = cutChapters(image_names)
if len(invalid_chapters) > 0:
    warning(
        "다음은 유효하지 않은 사진 이름 형식입니다.\n- "
        + ("\n- ".join(invalid_chapters))
    )

# check whether chapters and images are matched
foo = set(map(lambda x: x[0], chapters))
bar = set(answer_sheet.keys())
if foo != bar:
    warning(
        "사진과 정답지(answer.csv)에 나열된 챕터의 구성이 다릅니다.\
        \n다음을 확인해주세요.\n사진: %s\n정답지: %s"
        % (", ".join(sorted(foo)), ", ".join(sorted(bar)))
    )

# leave matched chapters only
chapters = list(filter(lambda ch: ch[0] in bar, chapters))

# basic UI components
ui_main = Home(answer_sheet)

# register chapter names
for chapter_num, chapter_name in chapters:
    # re-build image names from chapter names
    ui_main.comboBox.addItem("%s.%s" % (chapter_num, chapter_name))

# start application
ui_main.show()
app.exec()
