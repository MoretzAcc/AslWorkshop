"""
Author: Moritz van Eimern
Date: 7/31/25
"""
import time

from PythonCourse.gui_tasks.traffic_light.traffic_light_gui import TrafficLightGUI

# Init
gui = TrafficLightGUI()

ui.onstartup(main)


async def main():
    # Setup
    gui.set_light(1, "light gray")
    gui.set_light(2, "light gray")
    gui.set_light(3, "light gray")

    # Loop
    while True:
        time.sleep(1)
        print("red")
        gui.set_light(1, "red")
        time.sleep(1)
        print("light gray")
        gui.set_light(1, "light gray")
