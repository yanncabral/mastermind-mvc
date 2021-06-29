#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from tkinter.font import Font
from view.constants import input_color, background_color

def gameover_view(_, canvas, on_click, text):
    canvas.delete('all')

    background = canvas.create_rectangle(50, 582-25, 400, 582+25, fill=background_color, outline='', tags='back')

    canvas.create_text(225, 233, text="⭐️", font=Font(size=64), fill='yellow')
    canvas.create_text(225, 466, text=text, justify='center', fill='white', font='Helvetica 32')
    canvas.create_text(225, 582, text="Voltar", justify='center', fill='white', font='Helvetica 24', tags='back')
    
    canvas.tag_bind('back', '<Button-1>', lambda *_: on_click())
    canvas.tag_bind('back', '<Enter>', lambda _: canvas.itemconfig(background, fill=input_color))
    canvas.tag_bind('back', '<Leave>', lambda _: canvas.itemconfig(background, fill=background_color))
