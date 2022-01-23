import os

if os.environ['USER'] in ['geant']:
    userpath = "/home/kash/Work/RootFile/"
    plotDir = "/home/kash/Work/TestPlots/"
    
if os.environ['USER'] in ['mahmoud']:
    userpath = "/home/mahmoud/PhDwork/susy/"
    plotDir = "/home/mahmoud/PhDwork/susy/fake_rate/fake_rate_results/Plots/"

if os.environ['USER'] in ['mmoussa']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/mmoussa/susy/fake_rate_results/Plots/"
    #Xfiles = "/home/kmandal/1LStopBudapest/AuxFiles/"    
