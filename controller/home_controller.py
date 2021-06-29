#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from view.home_view import home_screen_view
from model.game_model import game_load


def home_controller(navigate, root, canvas, *args, **kwargs):
    
    def load(file):
        game = game_load(file)
        file.close()
        if game:
            navigate(root, canvas, to='game', game=game)
            return True
        else:
            return False

    select_level1 = lambda *_: navigate(root, canvas, to='game', level=1)
    select_level2 = lambda *_: navigate(root, canvas, to='game', level=2)
    select_level3 = lambda *_: navigate(root, canvas, to='game', level=3)

    home_screen_view(canvas, select_level1, select_level2, select_level3, load)

    
