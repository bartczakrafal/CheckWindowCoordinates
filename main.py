import os
import pyperclip
import sys
import time
from ActiveWindow import ActiveWindow
from win32gui import GetWindowText, GetForegroundWindow


def run():
    print('Tool will start within 5 secs.\n\tPlease move your mouse to proper place ...\n\n')
    time.sleep(5)

    while True:
        window = GetWindowText(GetForegroundWindow())
        print('\tWindow Name:\t' + str(window))

        selected_window = ActiveWindow(window)
        selected_window.set_mouse_coordinates()
        selected_window.set_padding()

        print(f'\tMouse position:'
              f'\n\t\tLeft: {selected_window.padding_left}'
              f'\n\t\tRight: {selected_window.padding_right}\n\t\t'
              f'Top: {selected_window.padding_top}\n\t\t'
              f'Bottom: {selected_window.padding_bottom}\n')

        pyperclip.copy(f'{window},{selected_window.padding_left},'
                       f'{selected_window.padding_right},'
                       f'{selected_window.padding_top},'
                       f'{selected_window.padding_bottom}')

        my_input = input('\tData copied to your clipboard. Would you like to try again(y/n)')

        if my_input.lower() == 'n':
            sys.exit()
        else:
            os.system('cls')
            print('Tool will start within 5 secs.\nPlease move your mouse to proper place.\n\n')
            time.sleep(5)


if __name__ == '__main__':

    run()
