import gui
import time
import functions
import structures

TICK = 0.05

window = gui.Window()
screen = window.screen

white_cells = structures.glider_gun(25, 25) + structures.glider_gun(8, 8)

running = False

while True:
    if running:
        white_cells = functions.update_new(white_cells)
    else:
        for element in window.get_clicks():
            if element in white_cells:
                white_cells.remove(element)
            else:
                white_cells.append(element)

    running = window.change_game_mode(running, white_cells)
    window.update_display(white_cells, running)
    time.sleep(TICK)
