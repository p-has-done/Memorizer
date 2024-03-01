# -*- coding: utf-8 -*-

from Indicator import *
from os import listdir

from PySide6.QtCore import QMetaObject, QSize, Qt, QTimer, Slot
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
)


class Ui_Main(QWidget):
    def __init__(self, answer_sheet):
        super().__init__()
        self.config_window = Ui_Config(self)
        self.quiz_window = Ui_Quiz(answer_sheet)
        self.time_limit = 10
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

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


class Ui_Config(QWidget):
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
        self.label.setText("제한시간 (기본 10초)")
        self.label_2.setText("영문명 대소문자 무시")
        self.label_3.setText("문제 수")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.main_widget.time_limit = self.horizontalSlider.value()
        self.main_widget.ignore_case = self.checkBox.isChecked()
        self.main_widget.problem_num = self.spinBox.value()
        self.main_widget.setConfigBtnText()


class Ui_Quiz(QWidget):
    def __init__(self, answer_sheet):
        super().__init__()
        self.answer_sheet = answer_sheet
        self.setupUi()
        self.timer = QTimer()

        # set timer
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start()

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
        self.label_quiz.setText("사진")
        self.label_image.setText("문제")
        self.lineEdit_kor.setPlaceholderText("국문명")
        self.lineEdit_eng.setPlaceholderText("영문명")
        self.pushButton.setText("확인(Enter)")

    def setShortcuts(self):
        self.pushButton.setShortcut("Return")

    def submit(self):
        current_answer = self.problem_list[self.problem_idx][1]
        response_kor = self.lineEdit_kor.text()
        response_eng = self.lineEdit_eng.text()
        self.problem_idx += 1
        if not (
            current_answer.cmpKor(response_kor)
            and current_answer.cmpEng(response_eng, self.ignore_case)
        ):
            self.incorrect_responses.append(
                (current_answer, response_kor, response_eng)
            )

    def clear(self):
        self.lineEdit_kor.setText("")
        self.lineEdit_eng.setText("")
        self.progressBar.setValue(0)
        self.timer.start()

    def prepare(self, chapter_name, time_limit, ignore_case, problem_num):
        self.problem_list = pickProblems(self.answer_sheet, chapter_name, problem_num)
        self.wrong_responses = []
        self.ignore_case = ignore_case
        self.problem_idx = 0
        self.progressBar.setMaximum(time_limit - 1)
        self.clear()

    def completeResponse(self):
        self.submit()
        self.clear()
        self.lineEdit_kor.setFocus()

    @Slot()
    def on_pushButton_clicked(self):
        if self.lineEdit_kor.text() == "":
            self.lineEdit_kor.setFocus()
        elif self.lineEdit_eng.text() == "":
            self.lineEdit_eng.setFocus()
        else:
            self.completeResponse()

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

# basic UI components
ui_main = Ui_Main(answer_sheet)

# register chapter names
for chapter_num, chapter_name in chapters:
    ui_main.comboBox.addItem("%s. %s" % (chapter_num, chapter_name))

# start application
ui_main.show()
app.exec()
