import pyautogui
import win32api, win32con


# touche 1 600 600
# touche 2 720 600
# touche 3 845 600
# touche 4 970 600
# touche 1 secours 600 300
# touche 2 secours 720 300
# touche 3 secours 845 300
# touche 4 secours 970 300


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # pyautogui.mouseDown(x=x, y=y)

    """while True:
        color = pyautogui.pixel(x, y - 3)
        noir_gris = color[0] in range(60) and color[1] in range(60) and color[2] in range(60)
        bleu = color[0] in range(5, 44) or color[1] in range(27, 154) or color[2] in range(46, 234)
        blanc = color[0] in range(245, 255) or color[1] in range(245, 255) or color[2] in range(245, 255)
        if bleu or blanc or noir_gris:
            time.sleep(0.01)

        else:
            print(f"Couleur : {color}")
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            pyautogui.mouseUp(x=x, y=y)
            break"""


def main():
    touche1, touche2, touche3, touche4 = (615, 550), (735, 550), (850, 550), (985, 550)
    listeTouche = [touche1, touche2, touche3, touche4]
    while True:
        # touche1_se,touche2_se,touche3_se,touche4_se = (600,450),(720,450),(845,450),(970,450)
        # touche1_s,touche2_s,touche3_s,touche4_s = (600,300),(720,300),(845,300),(970,300)
        # listeTouche = [touche1_se,touche2_se,touche3_se,touche4_se,touche1_s,touche2_s,touche3_s,touche4_s,touche1,touche2,touche3,touche4]
        for touche in listeTouche:
            color = pyautogui.pixel(touche[0], touche[1] + 3)
            rouge_jaune = (
                color[0] in range(237, 255)
                and color[1] in range(79, 171)
                and color[2] in range(57, 127)
            )
            noir = (
                color[0] in range(40) or color[1] in range(40) or color[2] in range(40)
            )

            if noir:
                print(f"Touche {(listeTouche.index(touche) + 1) % 4 + 1}")
                click(touche[0], touche[1] - 20)
            elif rouge_jaune:
                print(
                    f"Touche {(listeTouche.index(touche) + 1) % 4 + 1} mais rouge ou jaune"
                )
                click(touche[0], touche[1] - 20)

        # print(pyautogui.position())


if __name__ == "__main__":
    main()
