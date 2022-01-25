import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'schnapsen')))
from api import State, engine, util
from bots.ml import ml

startphase = 1
verbose=True
max_time=10000

ml_model_name="bully_model.pkl"
player_1_ml=ml.Bot(model_file='./bots/ml/models/'+ml_model_name)
player_2_other_bot="rand"


def play_a_game(player1,player2):
    engine.play(player1,util.load_player(player2),state=State.generate(phase=startphase), max_time=max_time, verbose=verbose)




if __name__ == "__main__":
    play_a_game(player_1_ml,player_2_other_bot)