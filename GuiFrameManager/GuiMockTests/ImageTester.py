from guizero import Picture


def experimental_image(main_container):
    file_url = "/home/pi/Documents/Python Modules/images/NerveTest/"
    file_name = "Nerve test-page-0"
    full_name = ""

    for i in range(1, 13):
        if (1 <= i <= 9):
            full_name = file_url + file_name + "0" + str(i) + ".jpg"
        else:
            full_name = file_url + file_name + str(i) + ".jpg"

        print(full_name)
        Picture(main_container, image=full_name)
