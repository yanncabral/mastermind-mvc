#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from controller.game_controller import game_controller
from controller.gameover_controller import gameover_controller
from controller.home_controller import home_controller

def navigate(root, canvas, to, *args, **kwargs):
    if to == 'home':
        home_controller(navigate, root, canvas, *args, **kwargs)
    elif to == 'game':
        game_controller(navigate, root, canvas, *args, **kwargs)
    elif to == 'gameover':
        gameover_controller(navigate, root, canvas, *args, **kwargs)
