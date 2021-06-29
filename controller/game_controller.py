#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from view.constants import COLORS
from model.game_model import check_valid_attempt, game_attempt, game_create
from view.game_view import game_view
from view.constants import input_color, COLORS
import tkinter as tk
import tkinter.filedialog
from model.game_model import game_save


def game_controller(navigate, root, canvas, level=None, game=None, initial_time=0):
    
    secrets_by_level = [[]]
    if game is None:
        game = game_create(level=level)
        map_widget_color = {}
        current_round = 0
    else:
        level = game[0]
        current_round = len(game[-1])

    map_widget_color = {}
    _, _, max_attempts, _ = game
    
    map_secret_color = {}
    selected_color = None
    selected_index = None
    indicator_current_level_indexes = None

    gameover = lambda iswinner: navigate(root, canvas, to='gameover', iswinner=iswinner)

    def on_click_save(_):
        file = tkinter.filedialog.asksaveasfile(title='Salvar o jogo', defaultextension='mastermind')
        game_save(game, file)
        file.close()

    def on_attempt_click(_):
        attempt = []
        for secret_index in secrets_by_level[current_round]:
            if not secret_index in map_secret_color:
                return
            else:
                attempt.append(COLORS.index(map_secret_color[secret_index][1]))
        if check_valid_attempt(game, attempt):
            feedback = game_attempt(game, attempt)
            return feedback

    def back(_):
        navigate(root, canvas, to='home')

    def get_current_round():
        return current_round
    
    def set_current_round(another):
        nonlocal current_round
        current_round = another

    def on_color_click(event):                  
        nonlocal selected_color
        nonlocal selected_index
        if selected_index is not None and selected_color is not None:
            canvas.itemconfig(selected_index, outline=selected_color)
        selected_index = event.widget.find_closest(event.x, event.y)[0]
        selected_color = map_widget_color[selected_index]
        canvas.itemconfig(selected_index, outline='white')

    def on_secret_click(event):
        nonlocal selected_color
        nonlocal selected_index
        nonlocal secrets_by_level
        current_secret_id = event.widget.find_closest(event.x, event.y)[0]
        if current_secret_id in secrets_by_level[current_round]:
            if current_secret_id in map_secret_color:
                canvas.itemconfig(current_secret_id, fill=input_color)
                canvas.itemconfig(map_secret_color[current_secret_id][0], fill=map_secret_color[current_secret_id][1], state=tk.NORMAL)
                del map_secret_color[current_secret_id]
                if selected_color is not None:
                    map_secret_color[current_secret_id] = selected_index, selected_color
                    canvas.itemconfig(current_secret_id, fill=selected_color)
                    canvas.itemconfig(selected_index, fill='', outline=selected_color, state=tk.DISABLED)
                    selected_color = selected_index = None
            else:
                map_secret_color[current_secret_id] = selected_index, selected_color
                canvas.itemconfig(current_secret_id, fill=selected_color)
                canvas.itemconfig(selected_index, fill='', outline=selected_color, state=tk.DISABLED)
                selected_color = selected_index = None

    def on_secret_enter(event):
        widget_id = event.widget.find_closest(event.x, event.y)[0]
        if widget_id in secrets_by_level[current_round]:
            canvas.itemconfig(widget_id, width=1, outline='grey')

    def on_secret_leave(event):
        widget_id = event.widget.find_closest(event.x, event.y)[0]
        if widget_id in secrets_by_level[current_round]:
            canvas.itemconfig(widget_id, width=0)

    def cancel_selection(_):
        if selected_index is not None:
            canvas.itemconfig(selected_index, outline=selected_color)
    
    def set_secrets_by_level(another):
        nonlocal secrets_by_level
        secrets_by_level = another

    def get_indicator_current_level_indexes():
        return indicator_current_level_indexes

    
    def set_indicator_current_level_indexes(another):
        nonlocal indicator_current_level_indexes
        indicator_current_level_indexes = another

    def get_map_widget_color():
        return map_widget_color

    
    def set_map_widget_color(another):
        nonlocal map_widget_color
        map_widget_color = another

    

    game_view(
        root, 
        canvas, 
        game, 
        initial_time, 
        gameover, 
        on_attempt_click, 
        back, 
        get_current_round, 
        set_current_round,
        on_color_click,
        level, on_secret_click,
        on_secret_enter,
        on_secret_leave,
        set_secrets_by_level,
        max_attempts,
        get_indicator_current_level_indexes,
        set_indicator_current_level_indexes,
        get_map_widget_color,
        set_map_widget_color,
        cancel_selection,
        on_click_save
    )
