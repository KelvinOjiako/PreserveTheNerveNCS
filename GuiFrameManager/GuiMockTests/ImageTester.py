from guizero import Picture
import os


def experimental_image(main_container):

    path_full = r"C:\Users\kojia\PycharmProjects\PreserveTheNerveNCS\Images"

    pictues = ["startTest.PNG", "snapSetup.png", "snapSetup_WristStrap.png",
               "snapSetup_writStrap_3.png", "shockPrompt.png"]

    intro = os.path.join(path_full, pictues[0])

    Picture(main_container, image=intro)
