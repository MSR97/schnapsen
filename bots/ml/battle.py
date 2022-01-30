import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'schnapsen')))
from api import State, engine, util
from bots.ml import ml
import random
import csv

startphase = 1
verbose=True
max_time=10000

number_of_games_sets_to_play=[1,2,3]


#For changing Model Please change the name of models directory
trained_directory='Neural_Network'

#Please Dont change the below codes
#####################################################################################
ml_model_name="rdeep_model.pkl"
player_ML=ml.Bot(model_file='./bots/ml/models/'+trained_directory+'/'+ml_model_name)
player_2_other_bot="rdeep"
csv_filename = "./bots/ml/reports/"+trained_directory+"_games.csv"
writer=open(csv_filename, 'a+', newline='')
#####################################################################################

def play_a_game(player1,player2):
    engine.play(player1,util.load_player(player2),state=State.generate(phase=startphase), max_time=max_time, verbose=verbose)

def run_tournament(players,mlbot):

    for game in number_of_games_sets_to_play:
        writer.write("|||||||||||||||||||||||||||||||||||||||||||||"+"\n")

        writer.write('Number of set of games {} :'.format(int(game))+"\n")
        
        players= players
        repeats=game
        phase=1
        max_time=5
        botnames = players.split(",")

        bots = []
        for botname in botnames:
            bots.append(util.load_player(botname))
            bots.append(mlbot)

        n = len(bots)
        wins = [0] * len(bots)
        matches = [(p1, p2) for p1 in range(n) for p2 in range(n) if p1 < p2]

        totalgames = (n*n - n)/2 * repeats
        playedgames = 0

        print('Playing {} games:'.format(int(totalgames)))
        writer.write('Playing {} games:'.format(int(totalgames))+"\n")

        for a, b in matches:
            for r in range(repeats):

                if random.choice([True, False]):
                    p = [a, b]
                else:
                    p = [b, a]

                state = State.generate(phase=int(phase))

                winner, score = engine.play(bots[p[0]], bots[p[1]], state, max_time*1000, verbose=verbose, fast=False)

                if winner is not None:
                    winner = p[winner - 1]
                    wins[winner] += score

                playedgames += 1
                print('Played {} out of {:.0f} games ({:.0f}%): {} \r'.format(playedgames, totalgames, playedgames/float(totalgames) * 100, wins))

        print('Results:')
        writer.write("Results Of {} TotalGames".format(totalgames)+"\n")
        for i in range(len(bots)):
            print('    bot {}: {} points'.format(bots[i], wins[i]))
            writer.write('    bot {}: {} points'.format(bots[i], wins[i])+"\n")

    writer.write('////////////////////////////////////////////////////////////')

            




if __name__ == "__main__":
    # play_a_game(player_1_ml,player_2_other_bot)
    run_tournament("rdeep",player_ML)
    writer.close()
