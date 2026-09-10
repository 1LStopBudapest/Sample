import os
    
if os.environ['USER'] in ['mahmoud']:
    userpath = "/home/mahmoud/PhDwork/susy/"
    plotDir = "/home/mahmoud/PhDwork/susy/fake_rate/fake_rate_results/Plots/"

if os.environ['USER'] in ['mmoussa']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/mmoussa/susy/fake_rate_results/Plots/"

if os.environ['USER'] in ['rabnora']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/rabnora/sandbox/Plots/"
    Xfiles = "/home/kmandal/1LStopBudapest/AuxFiles/"

if os.environ['USER'] in ['kmandal']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/kmandal/1LStopAN/Plots/"
    Xfiles = "/home/kmandal/1LStopBudapest/AuxFiles/"    

if os.environ['USER'] in ['mleoncoe']:
    userpath = "/big_data/LepStop/"
    plotDir = "/home/mleoncoe/stopAnalysis/test/Plots/"
    Xfiles = "/home/mleoncoe/stopAnalysis/test/AuxFiles/"   

# --- lxplus -----------------------------------------------------------------
_host = os.uname()[1]
if _host.startswith('lxplus') or 'cern.ch' in _host:
    basedir  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    userpath = "unused"
    plotDir  = os.path.join(basedir, "Plots") + "/"
    Xfiles   = os.path.join(basedir, "AuxFiles") + "/"
