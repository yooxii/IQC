import catuo
from catuo import *
from PIL import Image

__all__ = ["catuo"]


class AutoEnterData:
    def __init__(self):
        self.initPic()

    def initPic(self):
        self.pic_value = "pics/001.png"
        self.pic_enter = "pics/002.png"

    def initVar(self):
        pass

    def single_component(self, data: list):
        click_image(self.pic_value, ["left", (50, 20)], confidence=0.7)
        pg.typewrite(f"{data[0]}")
        pg.press("tab")
        pg.typewrite(f"{data[1]}")
        pg.press("tab")
        pg.typewrite(f"{data[2]}")
        pg.press("tab")
        pg.typewrite(f"{data[3]}")
        pg.press("tab")
        pg.typewrite(f"{data[4]}")
        click_image(self.pic_enter, confidence=0.7)


def main():
    ato = AutoEnterData()
    ato.single_component([1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    main()
