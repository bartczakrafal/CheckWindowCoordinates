import pyautogui
import re
import win32gui


class ActiveWindow:

    def __init__(self, window_name):
        self.window_name = window_name
        self.__mouse_x = None
        self.__mouse_y = None
        self.padding_top = None
        self.padding_bottom = None
        self.padding_left = None
        self.padding_right = None

    @staticmethod
    def get_mouse_position():
        return pyautogui.position()

    def set_mouse_coordinates(self):
        mouse_coordinates = str(self.get_mouse_position())
        coordinates_x_y = re.findall(r'\d+', mouse_coordinates)
        self.__mouse_x = coordinates_x_y[0]
        self.__mouse_y = coordinates_x_y[1]

    def set_padding(self):
        active_window = win32gui.FindWindow(None, self.window_name)
        left, top, right, bottom = win32gui.GetWindowRect(active_window)
        active_window_height = bottom - top
        active_window_width = right - left

        self.padding_right = right - int(self.__mouse_x)
        self.padding_left = active_window_width - self.padding_right

        self.padding_bottom = bottom - int(self.__mouse_y)
        self.padding_top = active_window_height - self.padding_bottom
