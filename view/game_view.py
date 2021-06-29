#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from random import shuffle
from tkinter.font import Font
from view.constants import input_color, COLORS, background_color
from view.shared.container_view import container_view
from view.shared.play_button_view import play_button_view
from datetime import timedelta

def game_view(
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
    ):
    canvas.delete('all')

    def render_feedback(feedback):
        if not feedback:
            return
        is_gameover, is_winner, black_tip, white_tip, _ = feedback
        current_round=get_current_round()
        padding = 8
        column = 7
        row = current_round + 2
        top_left = padding + 50 * column, padding + 50 * row
        top_right = 50 * (column+1) - padding, padding + 50 * row
        bottom_left = padding + 50 * column, 50 * (row+1) - padding
        # bottom_right = 50 * (column+1) - padding, 50 * (row+1) - padding
        total_width = top_right[0] - top_left[0]
        total_height = bottom_left[1] - top_left[1]
        block_width = total_width / 3
        block_height = total_height / 2
        entries = ['black'] * black_tip + ['white'] * white_tip
        shuffle(entries)
        for i, color in enumerate(entries):
            x = i % 3
            y = i // 3
            canvas.create_rectangle(
                top_left[0] + x * block_width, 
                top_left[1] + y * block_height, 
                top_left[0] + (x+1) * block_width, 
                top_left[1] + (y+1) * block_height, 
                fill=color,
                outline='white' if color == 'black' else 'black'
            )

        if is_winner or is_gameover:
            gameover(is_winner)
        else:
            set_current_round(current_round+1)
            render_current_round(current_round+1)
            render_colors()

    def render_colors():
        map_widget_color = get_map_widget_color()
        for button_id in map_widget_color.keys():
            canvas.delete(button_id)
            
        map_widget_color = {}
        for index, color in enumerate(COLORS[:level + 5]):
            button_id = container_view(canvas, column=8, row=index+2, color=color, tags="color")
            map_widget_color[button_id] = color
        canvas.tag_bind("color","<Button-1>", on_color_click)
        set_map_widget_color(map_widget_color)

    def render_secret():
        for column in range(1, 4 + level):
            container_view(canvas, column=column, row=1, color=input_color, tags='secret')
            canvas.create_text(column * 50 + 25, 50 + 25, text="?", font=Font(size=22), fill='white')

    def render_secret_inputs():
        secrets = []
        for row in range(2, max_attempts + 2):
            current_round = []
            for column in range(1, 4 + level):
                current_round.append(container_view(canvas, column=column, row=row, color=input_color, tags='secret'))
            secrets.append(current_round)
        canvas.tag_bind('secret', "<Button-1>", on_secret_click)
        canvas.tag_bind('secret', '<Enter>', on_secret_enter)
        canvas.tag_bind('secret', '<Leave>', on_secret_leave)
        set_secrets_by_level(secrets)
        for history, secrets in zip(game[-1], secrets):
            for color, widget in zip(history, secrets):
                canvas.itemconfig(widget, fill=COLORS[color])

    def render_tick():
        nonlocal initial_time
        time = initial_time
        clock = canvas.create_text(50 * 9 - 4, 21, fill='grey', justify='right', anchor='e', text=str(timedelta(seconds=time)) + " ⌚︎")
        
        def change_clock():
            nonlocal time
            time += 1
            canvas.itemconfig(clock, text=str(timedelta(seconds=time)) + " ⌚︎")
            canvas.after(1000, change_clock)
        canvas.after(1000, change_clock)
        
    def render_levels_text():
        for row in range(1, max_attempts + 1):
            current_round = row
            container_view(canvas, column=0, row=(1+row), color=input_color)
            canvas.create_text(25, 50 * (1+row) + 25, text=current_round, fill='grey')

    def render_save():
        column = 8
        row = 12
        container_view(canvas, column=column, row=(1+row), color=input_color, tags='save')
        canvas.create_text(50 * column + 25, 50 * (1+row) + 25, text="☁", fill='grey', font=Font(size=22), tags='save')
        canvas.tag_bind('save', '<Button-1>', on_click_save)

    def render_current_round(round):
        round += 1
        indicator_current_level_indexes = get_indicator_current_level_indexes()
        if indicator_current_level_indexes is not None:
            play_button, rectangle = indicator_current_level_indexes
            canvas.delete(play_button)
            canvas.delete(rectangle)
        widgets = [
        play_button_view(canvas, column=4+level, row=round+1, color='white', tags='attempt'),
        canvas.create_rectangle(
                0, 
                50 * (round+1), 
                50 * (5 + level), 
                50 * (round+2), 
                fill='',
                width=1,
                outline='white'
            )
        ]
        canvas.tag_bind('attempt', '<Button-1>', lambda *_:  render_feedback(on_attempt_click(*_)))
        set_indicator_current_level_indexes(widgets)

    def render_back_button():
        background = container_view(canvas, column=0, row=0, color=background_color, tags='back')
        canvas.create_text(25, 25, text="←", fill='grey', font='Helvetica 28', tags='back')
        canvas.tag_bind('back', '<Button-1>', back)
        canvas.tag_bind('back', '<Enter>', lambda _: canvas.itemconfig(background, fill=input_color))
        canvas.tag_bind('back', '<Leave>', lambda _: canvas.itemconfig(background, fill=background_color))


    canvas.after(1, render_tick)
    render_back_button()
    root.bind("<Escape>", lambda event: cancel_selection(event))
    render_secret()
    render_levels_text()
    render_colors()
    render_secret_inputs()
    render_save()
    render_current_round(get_current_round())
