from guizero import Picture


def experimental_image(main_container):

    path_full = r"C:\Users\kojia\PycharmProjects\PreserveTheNerveNCS\Images"

    pictues = ["startTest.PNG", "snapSetup.png", "snapSetup_WristStrap.png",
               "snapSetup_writStrap_3.png", "shockPrompt.png"]

    intro = path_full  + "\luffy_gif_test.png"

    Picture(main_container, image=intro)
