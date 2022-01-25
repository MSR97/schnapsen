import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'schnapsen')))

from bots.ml import train_ml_bot as t
from bots.rand import rand
from bots.rdeep import rdeep
from bots.kbbot import kbbot
from bots.bully import bully

number_of_games=1000

###############################################################################
# rand_ml=t.TrainingModel(rand.Bot(),"rand",number_of_games)
# rand_ml.create_dataset()
# rand_ml.train_model()
###############################################################################
bully_ml=t.TrainingModel(bully.Bot(),"bully",number_of_games)
bully_ml.create_dataset()
bully_ml.train_model()
###############################################################################
# kb_ml=t.TrainingModel(kbbot.Bot(),"kb",number_of_games)
# kb_ml.create_dataset()
# kb_ml.train_model()
###############################################################################
# rdeep_ml=t.TrainingModel(rdeep.Bot(),"rdeep",number_of_games)
# rdeep_ml.create_dataset()
# rdeep_ml.train_model()
###############################################################################

