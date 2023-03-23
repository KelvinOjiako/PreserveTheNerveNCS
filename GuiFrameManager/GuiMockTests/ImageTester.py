from guizero import Picture
import os


def experimental_image(main_container):

    path_full = r"C:\Users\kojia\PycharmProjects\PreserveTheNerveNCS\Images"

    pictues = ["startTest.png", "snapSetup.png", "snapSetup_WristStrap.png",
               "snapSetup_writStrap_3.png", "shockPrompt.png"]

    mugi = ""
    i1 = "1.GIF"
    i2 = "2.GIF"

    image_list = [mugi, "1.GIF", "2.GIF", "1_1.GIF", "3.GIF", "3_1.GIF"]

    intro = os.path.join(path_full, i1)

    Picture(main_container, image=intro)
