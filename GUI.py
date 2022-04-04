import dearpygui.dearpygui as dpg
from logic import *

question, answer, wanswer = RandomQuest().getquest()

dpg.create_context()


def button_callback(sender, user_data, app_data):
    if user_data:
        print("WORKS?")
    else:
        print("WORKS!")


with dpg.window(label="ICD-10"):
    dpg.add_text(question)
    dpg.add_button(label=answer, callback=button_callback, user_data=True, tag="antwort")
    dpg.set_item_callback("antwort", button_callback)
    dpg.set_item_user_data("antwort", True)
    dpg.add_button(label=wanswer, callback=button_callback, user_data=False, tag="antwort2")
    dpg.set_item_callback("antwort2", button_callback)
    dpg.set_item_user_data("antwort2", False)
    dpg.add_button(label="NEXT", callback=button_callback, tag="SKIPPED")



with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=button_callback)


dpg.bind_item_handler_registry("antwort", "widget handler")
dpg.bind_item_handler_registry("antwort2", "widget handler")

dpg.create_viewport(title='ICD-10 Lernhelfer', width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
