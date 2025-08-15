from . import catuo
from .catuo import *

__all__ = ["catuo"]


class AutoEnterData:
    def __init__(self):
        self.initPic()

    def initPic(self):
        self.pic_value = "pics/001.png"
        self.pic_enter = "pics/002.png"

    def initVar(self):
        pass

    def singleComponent(self, data: list):
        click_image(self.pic_value, ["left", (50, 20)], confidence=0.7)
        for i in range(len(data)):
            pg.typewrite(f"{data[i]}")
            pg.press("tab")
        click_image(self.pic_enter, confidence=0.7)


def main():
    ato = AutoEnterData()
    ato.singleComponent([1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    main()
