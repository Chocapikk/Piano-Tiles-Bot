import threading
import time
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import keyboard
import pyautogui
import win32api
import win32con

is_started = False
stop_threads = True
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


# touche 1 600 600
# touche 2 720 600
# touche 3 845 600
# touche 4 970 600
# touche 1 secours 600 300
# touche 2 secours 720 300
# touche 3 secours 845 300
# touche 4 secours 970 300

def click(x, y, timer=0):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # pyautogui.mouseDown(x=x, y=y)
    if timer != 0:
        # win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE, x, y - 10)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # time.sleep(timer)
        pass


def debug():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    R_lst = []
    G_lst = []
    B_lst = []

    while True:

        a = win32api.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            if a < 0:
                print('Left Button Pressed')
                position = pyautogui.position()
                print(position)
                color = pyautogui.pixel(position[0], position[1] - 10)
                rouge_jaune = color[0] in range(230, 256) and color[1] in range(60, 255) and color[2] in range(0, 220)
                try:
                    R_min, R_max = min(R_lst), max(R_lst)
                    G_min, G_max = min(G_lst), max(G_lst)
                    B_min, B_max = min(B_lst), max(B_lst)
                except:
                    pass

                if rouge_jaune:
                    print(f"Couleur dans l'intervalle : {color[0], color[1], color[2]}")
                    R_lst.append(color[0])
                    G_lst.append(color[1])
                    B_lst.append(color[2])
                    try:
                        print(
                            f"Moyenne intervalle cliquée : R - [{R_min, R_max}], G - [{G_min, G_max}], B - [{B_min, B_max}]")
                    except:
                        pass

                else:
                    print(f'Non bouffon : {color[0], color[1], color[2]}')
                    R_lst.append(color[0])
                    G_lst.append(color[1])
                    B_lst.append(color[2])
                    try:
                        print(f"Moyenne intervalle cliquée : R - [{R_min, R_max}], G - [{G_min, G_max}], B - [{B_min, B_max}]")
                    except:
                        pass

        time.sleep(0.001)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def changebot_state(bot_state, canvas):
    global is_started
    while True:
        print(f'Bot {["On" if is_started else "Off"]}')
        touche1, touche2, touche3, touche4 = (615, 600), (735, 600), (850, 600), (985, 600)
        # touche1_s, touche2_s, touche3_s, touche4_s = (600, 520), (720, 520), (845, 520), (970, 520)
        listeTouche = [touche1, touche2, touche3, touche4]
        # touche1_se,touche2_se,touche3_se,touche4_se = (600,450),(720,450),(845,450),(970,450)

        # touche2_se,touche3_se,touche4_se,touche1_s,touche2_s,touche3_s,touche4_s,touche1,touche2,touche3,touche4]
        for touche in listeTouche:
            color = pyautogui.pixel(touche[0], touche[1] - 10)
            rouge_jaune = color[0] in range(230, 256) and color[1] in range(60, 255) and color[2] in range(0, 150)
            noir = color[0] in range(30) or color[1] in range(30) or color[2] in range(30)
            if noir:
                # print(f"Touche {(listeTouche.index(touche) + 1) % 4 + 1}")
                print(color)
                click(touche[0], touche[1] - 20)
            elif rouge_jaune:
                print(f"Touche {(listeTouche.index(touche) + 1) % 4 + 1} mais rouge ou jaune")
                print(f"R : {color[0]}, G : {color[1]}, B {color[2]}")
                click(touche[0], touche[1] + 15, timer=10 ^ -6)
        if keyboard.is_pressed('a'):
            is_started =  not is_started
            time.sleep(0.5)
            canvas.itemconfig(bot_state, text=f"Bot state : {'Yes' if is_started else 'No'}")
            break

            # print(pyautogui.position())


def main():
    window = Tk()
    window.attributes("-topmost", True)
    window.title('Piano Tiles Bot by Chocapikk')
    window.geometry("564x263")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=263,
        width=564,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png")
    )
    image_1 = canvas.create_image(
        282.0,
        131.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        449.0,
        82.0,
        image=image_image_2
    )

    title = canvas.create_text(
        22.0,
        32.0,
        anchor="nw",
        text="Piano Tiles 2 Bot by Chocapikk",
        fill="#000000",
        font=("AdventPro Bold", 24 * -1)
    )

    bot_state = canvas.create_text(
        17.0,
        146.0,
        anchor="nw",
        text=f"Bot State : {'Yes' if is_started else 'No'}",
        fill="#000000",
        font=("AkayaTelivigala Regular", 20 * -1)
    )

    calibration = canvas.create_text(
        240.0,
        146.0,
        anchor="nw",
        text="Calibrated screen : No",
        fill="#000000",
        font=("AkayaKanadaka Regular", 20 * -1)
    )

    instructions = canvas.create_text(
        101.0,
        193.0,
        anchor="nw",
        text="Please Click Top Left Corner",
        fill="#000000",
        font=("AdventPro Bold", 20 * -1)
    )

    version = canvas.create_text(
        407.0,
        212.0,
        anchor="nw",
        text="Version : 1.0",
        fill="#000000",
        font=("AdventPro Bold", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changebot_state(bot_state, canvas),
        relief="flat"
    )
    button_1.place(
        x=22.0,
        y=97.0,
        width=104.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=162.0,
        y=97.0,
        width=200.0,
        height=35.0
    )

    window.resizable(False, False)
    window.bind("<a>", lambda x: changebot_state(bot_state, canvas))
    window.mainloop()


if __name__ == '__main__':
    main()
    # debug()
