import os, sys

from Dir import userpath

MC_dir = "PostProcessedNtuple/2016/MetSingleLep/"
Data_dir = MC_dir
Signal_dir = "StopSignal/"

samples = {}
#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py

samples['Stop_500_480_prompt_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/prompt/FastSim/"), 0.609, 333881]
samples['Stop_500_480_prompt_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/prompt/FullSim/"), 0.609, 364869]
samples['Stop_500_480_tau10mm_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau10mm/FastSim/"), 0.609, 339618]
samples['Stop_500_480_tau10mm_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau10mm/FullSim/"), 0.609, 377544]
samples['Stop_500_480_tau100mm_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau100mm/FastSim/"), 0.609, 219739]
samples['Stop_500_480_tau100mm_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau100mm/FullSim/"), 0.609, 398443] 

#PostProcessed Samples
#BK MC
samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow/"), 831.762*(3*0.108)*(1-3*0.108)*2, 2678436]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow/"), 831.762*((3*0.108)**2), 23248235]
samples['WJetsToLNu_HT70to100'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT70to100/"), 1637.13, 429894]
samples['WJetsToLNu_HT100to200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT100to200/"), 1627.45, 887522]
samples['WJetsToLNu_HT200to400'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT200to400/"), 435.237, 954588]
samples['WJetsToLNu_HT400to600'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT400to600/"), 59.1811, 544406]
samples['WJetsToLNu_HT600to800'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT600to800/"), 14.5805, 534803]
samples['WJetsToLNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT800to1200/"), 6.65621, 569975]
samples['WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT1200to2500/"), 1.60809, 105922]
samples['WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT2500toInf/"), 0.0389136, 135533]
samples['WJetsToLNu'] = [samples['WJetsToLNu_HT70to100'], samples['WJetsToLNu_HT100to200'], samples['WJetsToLNu_HT200to400'], samples['WJetsToLNu_HT400to600'], samples['WJetsToLNu_HT600to800'], samples['WJetsToLNu_HT800to1200'], samples['WJetsToLNu_HT1200to2500'], samples['WJetsToLNu_HT2500toInf']]


#Data
#MET
samples['MET_Run2016B'] = [os.path.join(userpath, Data_dir, "MET_Run2016B_17Jul2018_ver2/"), 1.00, 5023831]
samples['MET_Run2016C'] = [os.path.join(userpath, Data_dir, "MET_Run2016C_17Jul2018/"), 1.00, 2389671]
samples['MET_Run2016D'] = [os.path.join(userpath, Data_dir, "MET_Run2016D_17Jul2018/"), 1.00, 3633132]
samples['MET_Run2016E'] = [os.path.join(userpath, Data_dir, "MET_Run2016E_17Jul2018/"), 1.00, 3631331]
samples['MET_Run2016F'] = [os.path.join(userpath, Data_dir, "MET_Run2016F_17Jul2018/"), 1.00, 2335934]
samples['MET_Run2016G'] = [os.path.join(userpath, Data_dir, "MET_Run2016G_17Jul2018/"), 1.00, 5150593]
samples['MET_Run2016H'] = [os.path.join(userpath, Data_dir, "MET_Run2016H_17Jul2018/"), 1.00, 6358426]
samples['MET_Data'] = [samples['MET_Run2016B'], samples['MET_Run2016C'], samples['MET_Run2016D'], samples['MET_Run2016E'], samples['MET_Run2016F'], samples['MET_Run2016G'], samples['MET_Run2016H']]

