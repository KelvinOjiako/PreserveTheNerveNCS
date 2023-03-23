from guizero import App

from GuiFrameManager.GuiMockTests.ImageTester import experimental_image


def imageExperiments():
    app = App()
    experimental_image(app)
    app.display()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageExperiments()
