from guizero import App, Text, PushButton, Box

from GuiFrameManager.GuiFrameManager import GuiFrameManager


def experimental_main(main_app):
    # Creates 4 Box container UI Elements that will be rendered on the main_app
    welcome_container = Box(main_app, width=200, height=350, border=3)
    testing_container = Box(main_app,  width=200, height=350, border=10)
    results_container = Box(main_app,  width=200, height=350, border=15)
    export_container = Box(main_app,  width=300, height=350, border=3)

    # A text box is then added to all the various Box Containers
    box1text = Text(welcome_container, text="Welcome to the HomePage")
    box2text = Text(testing_container, text="Testing will begin")
    box3text = Text(results_container, text="Results are Ready")
    box4text = Text(export_container, text="Where do you wanna export data to")

    # The box containers are then compiled together into a list
    widget_stack = [welcome_container, testing_container, results_container, export_container]
    # GuiFrame Object is created from list of Box containers
    manager_object = GuiFrameManager(widget_stack)
    manager_object.deactivate_all_elements()
    print(manager_object.size)
    return manager_object


# Triggers the GuiFrame to activate the next element and disable all other elements
def move_to_previous_widget(test_manager):
    test_manager.activate_previous_element()


# Triggers the previous element to be activated while disabling all else
def move_to_next_widget(test_manager):
    test_manager.activate_next_element()
