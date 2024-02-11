from indicator import *
from interface import *
from os import listdir

image_names = listdir("resources/images/")
answer_sheet = getAnswerSheet()

app = QApplication([])

foo = set(map(lambda name: name.split(".")[0], image_names))
bar = set(answer_sheet.keys())
if foo != bar:
    msg = QMessageBox.critical(
        None,
        "Error",
        "사진과 정답지(answer.csv)에 나열된 챕터의 구성이 다릅니다.\
        \n다음을 확인해주세요.\n사진: %s\n정답지: %s"
        % (", ".join(sorted(foo)), ", ".join(sorted(bar))),
    )
    exit()


ui_main = Ui_Main()
ui_config = Ui_Config()

main_window = QWidget()
ui_main.setupUi(main_window)

main_window.show()

app.exec()
