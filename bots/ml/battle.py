import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'schnapsen')))
from api import State, engine, util
from bots.ml import ml

startphase = 1
verbose=True
max_time=10000


def play_a_game(player1,player2):
    engine.play(player1,util.load_player(player2),state=State.generate(phase=startphase), max_time=max_time, verbose=verbose)


ml_model_name="kb_model.pkl"
ml_player=ml.Bot(model_file='./bots/ml/models/'+ml_model_name)
other_player="rand"


play_a_game(ml_player,other_player)