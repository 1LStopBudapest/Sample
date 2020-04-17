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

samples['Stop_500_480_prompt_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/prompt/FastSim/"), 0.609, ]
samples['Stop_500_480_prompt_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/prompt/FullSim/"), 0.609, ]
samples['Stop_500_480_tau10mm_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau10mm/FastSim/"), 0.609, 339618]
samples['Stop_500_480_tau10mm_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau10mm/FullSim/"), 0.609, 377544]
samples['Stop_500_480_tau100mm_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau100mm/FastSim/"), 0.609, 219739]
samples['Stop_500_480_tau100mm_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau100mm/FullSim/"), 0.609, 398443] 



samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow/"), 831.762*(3*0.108)*(1-3*0.108)*2, 2678436]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow/"), 831.762*((3*0.108)**2), 1.00]
samples['WJetsToLNu_HT70to100'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT70to100/"), 1.00]
samples['WJetsToLNu_HT100to200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT100to200/"), 1.00]
samples['WJetsToLNu_HT200to400'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT200to400/"), 1.00]
samples['WJetsToLNu_HT400to600'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT400to600/"), 1.00]
samples['WJetsToLNu_HT600to800'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT600to800/"), 1.00]
samples['WJetsToLNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT800to1200/"), 1.00]
samples['WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT1200to2500/"), 1.00]
samples['WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT2500toInf/"), 1.00]

