import os

if os.environ['USER'] in ['kash']:
    userpath = "/home/kash/Work/RootFile/"
    plotDir = "/home/kash/Work/TestPlots/"
    
if os.environ['USER'] in ['mahmoud']:
    userpath = "/home/mahmoud/PhDwork/susy/"
    plotDir = "/home/mahmoud/PhDwork/susy/fake_rate/fake_rate_results/Plots/"

if os.environ['USER'] in ['mmoussa']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/mmoussa/susy/fake_rate_results/Plots/"

if os.environ['USER'] in ['kmandal']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/kmandal/1LStopAN/Plots/"
    Xfiles = "/home/kmandal/1LStopBudapest/AuxFiles/"    
