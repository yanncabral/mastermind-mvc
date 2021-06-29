#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from model.game_model import game_load
from view.shared import container_view
from view.shared.container_view import container_view
from view.shared.play_button_view import play_button_view
from view.constants import input_color
import tkinter.filedialog
import tkinter.messagebox

def home_screen_view(canvas, select_level1, select_level2, select_level3, load):
    canvas.delete('all')
    
    def get_file(_):
        f = tkinter.filedialog.askopenfile(title='Carregar jogo', filetypes=[("Mastermind files", ".mastermind")])
        if not load(f):
            tkinter.messagebox.showerror(title="Erro", message="Arquivo inválido")

    for i in range(9):
        for j in range(2, 6):
            container_view(canvas, column=i, row=j, color=input_color, padding_x=0, padding_y=8, tags=f'l{j-1}')
        
    for i in range(2, 5):
        play_button_view(canvas, column=0, row=i, color='white', tags=f'l{i-1}')


    canvas.create_text(8, 5*50 + 24, text="☁️", justify='left', anchor='w', fill='white', font='Helvetica 28', tags='l4')
    canvas.create_text(58, 2*50 + 18, text="Nível 1", justify='left', anchor='w', fill='white', font='Helvetica 14', tags='l1')
    canvas.create_text(58, 2*50 + 32, text="8 tentativas p/ acertar uma combinação de 4 em 6 cores", justify='left', anchor='w', fill='grey', font='Helvetica 9', tags='l1')
    canvas.create_text(58, 3*50 + 18, text="Nível 2", justify='left', anchor='w', fill='white', font='Helvetica 14', tags='l2')
    canvas.create_text(58, 3*50 + 32, text="10 tentativas p/ acertar uma combinação de 5 em 7 cores", justify='left', anchor='w', fill='grey', font='Helvetica 9', tags='l2')
    canvas.create_text(58, 4*50 + 18, text="Nível 3", justify='left', anchor='w', fill='white', font='Helvetica 14', tags='l3')
    canvas.create_text(58, 4*50 + 32, text="12 tentativas p/ acertar uma combinação de 6 em 8 cores", justify='left', anchor='w', fill='grey', font='Helvetica 9', tags='l3')
    canvas.create_text(58, 5*50 + 18, text="Continuar jogo", justify='left', anchor='w', fill='white', font='Helvetica 14', tags='l4')
    canvas.create_text(58, 5*50 + 32, text="Carregue um jogo previamente salvo.", justify='left', anchor='w', fill='grey', font='Helvetica 9', tags='l4')

    canvas.tag_bind("l1","<Button-1>", select_level1)
    canvas.tag_bind("l2","<Button-1>", select_level2)
    canvas.tag_bind("l3","<Button-1>", select_level3)
    canvas.tag_bind("l4","<Button-1>", get_file)
