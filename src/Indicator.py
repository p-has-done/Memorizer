from random import sample
from typing import Tuple, List, Dict


class Answer:
    def __init__(self, kor: str, eng: str):
        self.kor = kor
        self.eng = eng

    def cmpKor(self, other: str):
        return self.kor.strip() == other.strip()

    def cmpEng(self, other: str, ignore_case: bool):
        if ignore_case:
            return self.eng.strip().lower() == other.strip().lower()
        else:
            return self.eng.strip() == other.strip()

    def __repr__(self):
        return "[정답: 국문명 %s, 영문명 %s]" % (self.kor, self.eng)

    def __str__(self):
        return self.__repr__()


class Chapter:
    def __init__(self, image_name: str):
        self.image_name = image_name

        # .index and int() both raise ValueError
        idx = image_name.index(".")
        self.chapter_id = int(image_name[:idx])
        self.chapter_name = image_name[idx + 1 :]

        # remove extensions
        self.chapter_name = self.chapter_name.strip()
        if self.chapter_name.endswith(".jpg"):
            self.chapter_name = self.chapter_name[:-4]
        elif self.chapter_name.endswith(".jpeg"):
            self.chapter_name = self.chapter_name[:-5]
        elif self.chapter_name.endswith(".png"):
            self.chapter_name = self.chapter_name[:-4]

    def __repr__(self):
        return "[ID: %d; NAME: %s]" % (self.chapter_id, self.chapter_name)

    def __str__(self):
        return self.__repr__()


def getAnswerSheet() -> Dict[str, Dict[str, Answer]]:
    file = open("resources/answer.csv", "r", encoding="UTF-8")
    ret = dict()

    file.readline()  # erase header of the csv file
    for line in file:
        chID, indiID, kor, eng = map(str.strip, line.split(","))
        chID = int(chID)
        indiID = int(indiID)
        if chID not in ret:
            ret[chID] = dict()
        ret[chID][indiID] = Answer(kor, eng)

    file.close()
    return ret


def imageName2chapter(image_name: str) -> Chapter:
    return Chapter(image_name)


def pickProblems(
    answer_sheet: Dict[str, Dict[str, Answer]], chapter_id: int, problem_num: int
) -> List[Tuple[int, Answer]]:
    all_problems = answer_sheet[chapter_id]
    if len(all_problems) < problem_num:
        problem_num = len(all_problems)
    return sample(list(all_problems.items()), problem_num)
