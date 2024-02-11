def readAnswerFile():
    with open("resources/answer.csv", "r", encoding="UTF-8") as file:
        return file.readlines()


class Answer:
    def __init__(self, kor, eng):
        self.kor = kor
        self.eng = eng

    def cmpKor(self, other):
        return self.kor.strip() == other.strip()

    def cmpEng(self, other):
        return self.eng.strip().lower() == other.strip().lower()

    def __repr__(self):
        return "[정답: 국문명 %s, 영문명 %s]" % (self.kor, self.eng)

    def __str__(self):
        return self.__repr__()


def parse(lines):
    lines = lines[1:]  # erase header of the csv file
    ret = dict()

    for line in lines:
        imageID, indiID, kor, eng = line.strip().split(",")
        if imageID not in ret:
            ret[imageID] = dict()
        ret[imageID][indiID] = Answer(kor, eng)

    return ret


def getAnswerSheet():
    return parse(readAnswerFile())
