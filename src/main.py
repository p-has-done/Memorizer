from indicator import *
from interface import *
from os import listdir

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
chapters, invalid_chapters = cut_chapters(image_names)
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
