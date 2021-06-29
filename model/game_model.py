#Rodrigo Biscaia Fernandes
#Yann Cabral Dias
#Kaio Abreu de Freitas
from random import shuffle
import hmac
import hashlib
import base64

def _hash_game(game):
    digest = hmac.new(b"yann", msg=str(game).encode(), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature

def _create_random_code(level = 1):
    answer = list(range(level+5))
    shuffle(answer)
    
    answer = answer[:level + 3]
    return answer
 
def _generate_attempt_tip(game, attempt):
    answer = game[1]
    is_black = [x == y for x, y in zip(answer, attempt)]
    rest_answer = [x for i, x in enumerate(answer) if not is_black[i]]
    rest_attempt = [x for i, x in enumerate(attempt) if not is_black[i]]
    whites = sum(x in rest_answer for x in rest_attempt)
    blacks = sum(is_black)
    return blacks, whites

def check_valid_attempt(game, attempt):
    level = game[0]
    code_lenght_condition = level + 3 == len(attempt)
    code_interval_condition = all(n in range(5 + level) for n in attempt)
    return code_lenght_condition and code_interval_condition

def game_save(game, file):
    game_hash = _hash_game(game)
    game_info = (game, game_hash)
    file.write(str(game_info))

def game_load(file):
    try:
        game, game_hash_saved = eval(file.read().strip())
        game_hash = _hash_game(game)
        if game_hash_saved == game_hash:
            return game
        else:
            return None
    except:
        return None    


def game_attempt(game, attempt):
    level, _, max_attempts, attempts = game
    black_tip, white_tip = _generate_attempt_tip(game, attempt)
    attempts.append(attempt)
    remaining_attempts = max_attempts - len(attempts)
    is_gameover = not remaining_attempts
    is_winner = black_tip == level + 3
    return is_gameover, is_winner, black_tip, white_tip, remaining_attempts
    
def game_create(level=1):
    if not (isinstance(level, int) and level in range(1, 4)):
        return -1
    answer = _create_random_code(level)
    max_attempts = 8 + (level-1) * 2
    return [level, answer, max_attempts, []]
