import numpy as np
from statsmodels.stats.proportion import binom_test
# k is number of scores A
# N is total of games

# binom_test(k,N,prop=0.5,alternative='smaller')

#compare_all_bots
def compare_all_bots(ks,Ns,games):
    hypo_num=len(ks)
    pvals=np.zeros(hypo_num)

    print("for number of {}".format(games)+"\n")
    
    for i in range(len(ks)):
        pvals[i]=binom_test(ks[i],Ns[i],prop=0.5,alternative='two-sided')
        
        print(pvals)
        print(pvals<0.5)
        print("\n")


#comparing 5 bots all together

# Playing 10 games:
# Results Of 10.0 TotalGames
# Neural_Network/rdeep_model.pkl: 4 points
# MultinomialNB/rdeep_model.pkl: 2 points
# Logistic_Regression/rdeep_model.pkl: 3 points
# GradientBoosting/rdeep_model.pkl: 1 points
# AdaBoost/rdeep_model.pkl: 2 points
ks_10_games=[4,2,3,1,2]
Ns_10_games=[10,10,10,10,10]
compare_all_bots(ks_10_games,Ns_10_games,10)

# Playing 100 games:
# Results Of 100.0 TotalGames
# Neural_Network/rdeep_model.pkl: 37 points
# MultinomialNB/rdeep_model.pkl: 39 points
# Logistic_Regression/rdeep_model.pkl: 38 points
# GradientBoosting/rdeep_model.pkl: 28 points
# AdaBoost/rdeep_model.pkl: 24 points 
ks_100_games=[37,39,38,28,24]
Ns_100_games=[50,50,50,50,50]
compare_all_bots(ks_100_games,Ns_100_games,100)


# Playing 500 games:
# Results Of 500.0 TotalGames
# Neural_Network/rdeep_model.pkl: 182 points
# MultinomialNB/rdeep_model.pkl: 164 points
# Logistic_Regression/rdeep_model.pkl: 137 points
# GradientBoosting/rdeep_model.pkl: 134 points
# AdaBoost/rdeep_model.pkl: 148 points 
ks_500_games=[182,164,137,134,148]
Ns_500_games=[500,500,500,500,500]
compare_all_bots(ks_500_games,Ns_500_games,500)


# Neural_Network/rdeep_model.pkl: 330 points
# MultinomialNB/rdeep_model.pkl: 351 points
# Logistic_Regression/rdeep_model.pkl: 296 points
# GradientBoosting/rdeep_model.pkl: 263 points
# AdaBoost/rdeep_model.pkl: 305 points
ks_1000_games=[330,351,296,263,305]
Ns_1000_games=[1000,1000,1000,1000,1000]
compare_all_bots(ks_1000_games,Ns_1000_games,1000)

# Playing 5000 games:
# Results Of 5000.0 TotalGames
# Neural_Network/rdeep_model.pkl: 1735 points
# MultinomialNB/rdeep_model.pkl: 1563 points
# Logistic_Regression/rdeep_model.pkl: 1531 points
# GradientBoosting/rdeep_model.pkl: 1237 points
# AdaBoost/rdeep_model.pkl: 1436 points
ks_5000_games=[1735,1563,1531,1237,1436]
Ns_5000_games=[5000,5000,5000,5000,5000]
compare_all_bots(ks_1000_games,Ns_5000_games,5000)

# Playing 10000 games:
# Results Of 10000.0 TotalGames
# Neural_Network/rdeep_model.pkl: 3593 points
# MultinomialNB/rdeep_model.pkl: 3188 points
# Logistic_Regression/rdeep_model.pkl: 2985 points
# GradientBoosting/rdeep_model.pkl: 2480 points
# AdaBoost/rdeep_model.pkl: 2976 points
ks_10000_games=[3593,3188,2985,2480,2976]
Ns_10000_games=[10000,10000,10000,10000,10000]
compare_all_bots(ks_1000_games,Ns_5000_games,10000)




