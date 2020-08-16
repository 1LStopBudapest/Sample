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
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/

samples['Stop_500_480_prompt_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/prompt/FastSim/"), 0.609, 333881]
samples['Stop_500_480_prompt_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/prompt/FullSim/"), 0.609, 364869]
samples['Stop_500_480_tau10mm_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau10mm/localMini/FastSim/"), 0.609, 339618]
samples['Stop_500_480_tau10mm_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau10mm/localMini/FullSim/"), 0.609, 377544]
samples['Stop_500_480_tau100mm_fast'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau100mm/localMini/FastSim/"), 0.609, 232463]
samples['Stop_500_480_tau100mm_full'] = [os.path.join(userpath, Signal_dir, "Stop_500_480/tau100mm/localMini/FullSim/"), 0.609, 279466] 

#PostProcessed Samples
#BK MC
samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow/"), 831.762*(3*0.108)*(1-3*0.108)*2, 2678436]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow/"), 831.762*((3*0.108)**2), 23248235]

samples['T_tch_pow'] = [os.path.join(userpath, MC_dir, "T_tch_pow/"), 136.02, ]
samples['TBar_tch_pow'] = [os.path.join(userpath, MC_dir, "TBar_tch_pow/"), 80.95, ]
samples['T_tWch_ext'] = [os.path.join(userpath, MC_dir, "T_tWch_ext/"), 35.85, ]
samples['TBar_tWch_ext'] = [os.path.join(userpath, MC_dir, "TBar_tWch_ext/"), 35.85, ]
samples['ST'] = [samples['T_tch_pow'], samples['TBar_tch_pow'], samples['T_tWch_ext'], samples['TBar_tWch_ext']]

samples['WJetsToLNu_HT70to100'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT70to100/"), 1637.13, 429894]
samples['WJetsToLNu_HT100to200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT100to200/"), 1627.45, 887522]
samples['WJetsToLNu_HT200to400'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT200to400/"), 435.237, 954588]
samples['WJetsToLNu_HT400to600'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT400to600/"), 59.1811, 544406]
samples['WJetsToLNu_HT600to800'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT600to800/"), 14.5805, 534803]
samples['WJetsToLNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT800to1200/"), 6.65621, 569975]
samples['WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT1200to2500/"), 1.60809, 105922]
samples['WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT2500toInf/"), 0.0389136, 135533]
samples['WJetsToLNu'] = [samples['WJetsToLNu_HT70to100'], samples['WJetsToLNu_HT100to200'], samples['WJetsToLNu_HT200to400'], samples['WJetsToLNu_HT400to600'], samples['WJetsToLNu_HT600to800'], samples['WJetsToLNu_HT800to1200'], samples['WJetsToLNu_HT1200to2500'], samples['WJetsToLNu_HT2500toInf']]

samples['QCD_HT50to100'] = [os.path.join(userpath, MC_dir, "QCD_HT50to100/"), 246400000.0, ]
samples['QCD_HT100to200'] = [os.path.join(userpath, MC_dir, "QCD_HT100to200/"), 27850000.0, ]
samples['QCD_HT200to300'] = [os.path.join(userpath, MC_dir, "QCD_HT200to300/"), 1717000, ]
samples['QCD_HT300to500'] = [os.path.join(userpath, MC_dir, "QCD_HT300to500/"), 351300, ]
samples['QCD_HT500to700'] = [os.path.join(userpath, MC_dir, "QCD_HT500to700/"), 31630, ]
samples['QCD_HT700to1000'] = [os.path.join(userpath, MC_dir, "QCD_HT700to1000/"), 6802, ]
samples['QCD_HT1000to1500'] = [os.path.join(userpath, MC_dir, "QCD_HT1000to1500/"), 1206, ]
samples['QCD_HT1500to2000'] = [os.path.join(userpath, MC_dir, "QCD_HT1500to2000/"), 20.4, ]
samples['QCD_HT2000toInf'] = [os.path.join(userpath, MC_dir, "QCD_HT2000toInf/"), 25.25]
samples['QCD'] = [samples['QCD_HT50to100'], samples['QCD_HT100to200'], samples['QCD_HT200to300'], samples['QCD_HT300to500'], samples['QCD_HT500to700'], samples['QCD_HT700to1000'], samples['QCD_HT1000to1500'], samples['QCD_HT1500to2000'], samples['QCD_HT2000toInf']]

samples['ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT100to200/"), 344.9781, ]
samples['ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT200to400/"), 96.3828, ]
samples['ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT400to600/"), 13.4562, ]
samples['ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT600to800/"), 3.96183, ]
samples['ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT800to1200/"), 1.81302, ]
samples['ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT1200to2500/"), 0.441078, ]
samples['ZJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT2500toInf/"), 0.01008969, ]
samples['ZJetsToNuNu'] = [samples['ZJetsToNuNu_HT100to200'], samples['ZJetsToNuNu_HT200to400'], samples['ZJetsToNuNu_HT400to600'], samples['ZJetsToNuNu_HT600to800'], samples['ZJetsToNuNu_HT800to1200'], samples['ZJetsToNuNu_HT1200to2500'], samples['ZJetsToNuNu_HT2500toInf']]

samples['DYJetsToLL_M50_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT100to200_ext/"), 147.4*1.23, ]
samples['DYJetsToLL_M50_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT200to400_comb/"), 40.99*1.23, ]
samples['DYJetsToLL_M50_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT400to600_comb/"), 5.678*1.23, ]
samples['DYJetsToLL_M50_HT600to800'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT600to800/"), 1.367*1.23, ]
samples['DYJetsToLL_M50_HT800to1200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT800to1200/"), 0.6304*1.23, ]
samples['DYJetsToLL_M50_HT1200to2500'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT1200to2500/"), 0.1514*1.23, ]
samples['DYJetsToLL_M50_HT2500toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT2500toInf/"), 0.003565*1.23, ]
#samples['DYJetsToLL_M50'] = [samples['DYJetsToLL_M50_HT100to200'], samples['DYJetsToLL_M50_HT200to400'], samples['DYJetsToLL_M50_HT400to600'], samples['DYJetsToLL_M50_HT600to800'], samples['DYJetsToLL_M50_HT800to1200'], samples['DYJetsToLL_M50_HT1200to2500'], samples['DYJetsToLL_M50_HT2500toInf']]
samples['DYJetsToLL_M5to50_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M5to50_HT100to200_comb/"), 224.2, ]
samples['DYJetsToLL_M5to50_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M5to50_HT200to400_comb/"), 37.2, ]
samples['DYJetsToLL_M5to50_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M5to50_HT400to600_comb/"), 3.581, ]
samples['DYJetsToLL_M5to50_HT600toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M5to50_HT600toInf/"), 1.124, ]
#samples['DYJetsToLL_M5to50'] = [samples['DYJetsToLL_M5to50_HT100to200'], samples['DYJetsToLL_M5to50_HT200to400'], samples['DYJetsToLL_M5to50_HT400to600'], samples['DYJetsToLL_M5to50_HT600toInf']]
samples['DYJetsToLL'] = [samples['DYJetsToLL_M50_HT100to200'], samples['DYJetsToLL_M50_HT200to400'], samples['DYJetsToLL_M50_HT400to600'], samples['DYJetsToLL_M50_HT600to800'], samples['DYJetsToLL_M50_HT800to1200'], samples['DYJetsToLL_M50_HT1200to2500'], samples['DYJetsToLL_M50_HT2500toInf'], samples['DYJetsToLL_M5to50_HT100to200'], samples['DYJetsToLL_M5to50_HT200to400'], samples['DYJetsToLL_M5to50_HT400to600'], samples['DYJetsToLL_M5to50_HT600toInf']]

samples['TTWToLNu'] = [os.path.join(userpath, MC_dir, "TTWToLNu_ext2/"), 0.2043, ]
samples['TTWToQQ'] = [os.path.join(userpath, MC_dir, "TTWToQQ/"), 0.40620, ]
samples['TTZ_LO'] = [os.path.join(userpath, MC_dir, "TTZ_LO/"), 0.5297/0.692, ]
#samples['TTZToLLNuNu_m1to10'] = [os.path.join(userpath, MC_dir, "TTZToLLNuNu_m1to10/"), 0.0493, ]
#samples['TTZToQQ'] = [os.path.join(userpath, MC_dir, "TTZToQQ/"), 0.5297, ]
#samples['TTV'] = [ samples['TTWToLNu'], samples['TTWToQQ'], samples['TTZ_LO'], samples['TTZToLLNuNu_m1to10'], samples['TTZToQQ']]
samples['TTV'] = [ samples['TTWToLNu'], samples['TTWToQQ'], samples['TTZ_LO']]

samples['WWTo2L2Nu'] = [os.path.join(userpath, MC_dir, "WWTo2L2Nu/"), 12.178, ]
samples['WWToLNuQQ'] = [os.path.join(userpath, MC_dir, "WWToLNuQQ/"), 49.997, ]
samples['WZTo1L1Nu2Q'] = [os.path.join(userpath, MC_dir, "WZTo1L1Nu2Q/"), 10.71, ]
samples['WZTo1L3Nu'] = [os.path.join(userpath, MC_dir, "WZTo1L3Nu/"), (47.13)*(3*0.108)*(0.2), ]
samples['WZTo2L2Q'] = [os.path.join(userpath, MC_dir, "WZTo2L2Q/"), 5.60, ]
samples['WZTo3LNu'] = [os.path.join(userpath, MC_dir, "WZTo3LNu/"), 4.42965, ]
samples['ZZTo2L2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Nu/"), 0.564, ]
samples['ZZTo2L2Q'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Q/"), 3.28, ]
samples['ZZTo2Q2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2Q2Nu/"), 4.04, ]
samples['ZZTo4L'] = [os.path.join(userpath, MC_dir, "ZZTo4L/"), 1.256*1.1, ]
samples['VV'] = [samples['WWTo2L2Nu'], samples['WWToLNuQQ'], samples['WZTo1L1Nu2Q'], samples['WZTo1L3Nu'], samples['WZTo2L2Q'], samples['WZTo3LNu'], samples['ZZTo2L2Nu'], samples['ZZTo2L2Q'], samples['ZZTo2Q2Nu'], samples['ZZTo4L']]

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

#SingleElectron
samples['SingleElectron_Run2016B'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016B_17Jul2018_ver2/"), 1.00, 865966]
samples['SingleElectron_Run2016C'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016C_17Jul2018/"), 1.00, 463161]
samples['SingleElectron_Run2016D'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016D_17Jul2018/"), 1.00, 700244]
samples['SingleElectron_Run2016E'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016E_17Jul2018/"), 1.00, 836822]
samples['SingleElectron_Run2016F'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016F_17Jul2018/"), 1.00, 556410]
samples['SingleElectron_Run2016G'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016G_17Jul2018/"), 1.00, 1224131]
samples['SingleElectron_Run2016H'] = [os.path.join(userpath, Data_dir, "SingleElectron_Run2016H_17Jul2018/"), 1.00, 1287221]
samples['SingleElectron_Data'] = [samples['SingleElectron_Run2016B'], samples['SingleElectron_Run2016C'], samples['SingleElectron_Run2016D'], samples['SingleElectron_Run2016E'], samples['SingleElectron_Run2016F'], samples['SingleElectron_Run2016G'], samples['SingleElectron_Run2016H']] 

#SingleMuon
samples['SingleMuon_Run2016B'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016B_17Jul2018_ver2/"), 1.00, 865966]
samples['SingleMuon_Run2016C'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016C_17Jul2018/"), 1.00, 463161]
samples['SingleMuon_Run2016D'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016D_17Jul2018/"), 1.00, 700244]
samples['SingleMuon_Run2016E'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016E_17Jul2018/"), 1.00, 836822]
samples['SingleMuon_Run2016F'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016F_17Jul2018/"), 1.00, 556410]
samples['SingleMuon_Run2016G'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016G_17Jul2018/"), 1.00, 1224131]
samples['SingleMuon_Run2016H'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016H_17Jul2018/"), 1.00, 1287221]
samples['SingleMuon_Data'] = [samples['SingleMuon_Run2016B'], samples['SingleMuon_Run2016C'], samples['SingleMuon_Run2016D'], samples['SingleMuon_Run2016E'], samples['SingleMuon_Run2016F'], samples['SingleMuon_Run2016G'], samples['SingleMuon_Run2016H']] 

#JetHT
samples['JetHT_Run2016B'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016B_17Jul2018_ver2/"), 1.00, 5023831]
samples['JetHT_Run2016C'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016C_17Jul2018/"), 1.00, 2389671]
samples['JetHT_Run2016D'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016D_17Jul2018/"), 1.00, 3633132]
samples['JetHT_Run2016E'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016E_17Jul2018/"), 1.00, 3631331]
samples['JetHT_Run2016F'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016F_17Jul2018/"), 1.00, 2335934]
samples['JetHT_Run2016G'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016G_17Jul2018/"), 1.00, 5150593]
samples['JetHT_Run2016H'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016H_17Jul2018/"), 1.00, 6358426]
samples['JetHT_Data'] = [samples['JetHT_Run2016B'], samples['JetHT_Run2016C'], samples['JetHT_Run2016D'], samples['JetHT_Run2016E'], samples['JetHT_Run2016F'], samples['JetHT_Run2016G'], samples['JetHT_Run2016H']]
