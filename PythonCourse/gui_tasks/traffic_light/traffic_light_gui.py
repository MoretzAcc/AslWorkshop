"""
Author: Moritz van Eimern
Date: 7/31/25
"""

from nicegui import ui
from typing import Dict


class TrafficLightGUI:

    def __init__(self):
        print("Init GUI")

        self.circles: Dict[int, ui.element] = {}

        with ui.row().classes('justify-center'):
            with ui.column().classes('items-center').style('background-color: black; padding: 20px; border-radius: 10px'):
                self.circles[1] = ui.html('<div style="width:60px;height:60px;border-radius:50%;background:red;margin:10px;"></div>')
                self.circles[2] = ui.html('<div style="width:60px;height:60px;border-radius:50%;background:yellow;margin:10px;"></div>')
                self.circles[3] = ui.html('<div style="width:60px;height:60px;border-radius:50%;background:green;margin:10px;"></div>')

        print("Starting NiceGUI server")
        ui.run(title='Traffic Light', reload=False)

    def set_light(self, number: int, color: str):
        if number not in self.circles:
            raise ValueError("number must be 1, 2, or 3")
        # Update the circle color via JavaScript (modify the element’s style)
        self.circles[number].run_javascript(f"element.style.background = '{color}'")


if __name__ == "__main__":
    gui = TrafficLightGUI()
