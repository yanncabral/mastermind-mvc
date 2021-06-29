#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from view.gameover_view import gameover_view


def gameover_controller(navigate, root, canvas, iswinner):
    on_click_back = lambda: navigate(root, canvas, to='home')
    gameover_view(root, canvas, on_click_back, 'Parabéns' if iswinner else 'Tente novamente')
