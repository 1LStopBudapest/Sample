import os, sys

from Dir import userpath

MC_dir = "PostProcessedNtuple/2016/MetSingleLep/"
MCV9_dir = "PostProcessedNtuple/2016/MetSingleLep/"
Data_dir = MC_dir
Signal_dir = MC_dir
UL16PreVFP_dir = "PostProcessedNtuple/2016/UL/PreVFP/MetSingleLep"
UL16PostVFP_dir = "PostProcessedNtuple/2016/UL/PostVFP/MetSingleLep"
StopSignal_500_480_dir = "StopSignal/Stop_500_480/"
StopSignal_500_485_dir = "StopSignal/Stop_500_485/"
StopSignal_500_490_dir = "StopSignal/Stop_500_490/"
V9_nanoAOD_500_485_dir = "StopSignal/V9/Stop_500_485/"
BKdir = "TestFile/"

samples = {}
#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/


# Full Sim samples for EleRecoStudy
samples['FullSim0'] = [os.path.join(userpath, StopSignal_500_480_dir, "prompt/FullSim/"), ]
samples['FullSim5'] = [os.path.join(userpath, StopSignal_500_480_dir, "tau5mm/FullSim/"), ]
samples['FullSim10'] = [os.path.join(userpath, StopSignal_500_480_dir, "tau10mm/FullSim/"), ]
samples['FullSim100'] = [os.path.join(userpath, StopSignal_500_480_dir, "tau100mm/FullSim/"), ]
samples['FullSim100m'] = [os.path.join(userpath, StopSignal_500_480_dir, "tau100mm/FullSim_Mod1/"), ]
samples['FullSim100m2'] = [os.path.join(userpath, StopSignal_500_480_dir, "tau100mm/FullSim_Mod2/File/"), ]

samples['UL17_Full99mm'] = [os.path.join(userpath, StopSignal_500_485_dir, "Full/"), ]
samples['UL17_Fast99mm'] = [os.path.join(userpath, StopSignal_500_485_dir, "Fast/"), ]
samples['UL17_Full59mm'] = [os.path.join(userpath, StopSignal_500_485_dir, "59mm/Full/"), ]
samples['UL17_Fast59mm'] = [os.path.join(userpath, StopSignal_500_485_dir, "59mm/Fast/"), ]
samples['UL17_Full966mm'] = [os.path.join(userpath, StopSignal_500_490_dir, "UL17_966mm/Full/"), ]
samples['UL17_Fast966mm'] = [os.path.join(userpath, StopSignal_500_490_dir, "UL17_966mm/Fast/"), ]

samples['UL17V9_Full99mm'] = [os.path.join(userpath, V9_nanoAOD_500_485_dir, "99mm/FullSim/"), ]
 

samples['UL17V9_Full99mm'] = [os.path.join(userpath, V9_nanoAOD_500_485_dir, "99mm/FullSim/"), ]

# temporary: BK files:
samples['UL17V9_TTTo2L2Nu'] = [os.path.join(userpath, BKdir, "TTTo2L2Nu/"), ]
samples['UL17V9_TTToSemiLeptonic'] = [os.path.join(userpath, BKdir, "TTToSemiLeptonic/"), ]



# T2tt sample
samples['T2tt'] = [os.path.join(userpath, Signal_dir, "T2tt/"), ]

#PostProcessed Samples
#BK MC
samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow/"), 831.762*(3*0.108)*(1-3*0.108)*2, 2678436]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow/"), 831.762*((3*0.108)**2), 23248235]
samples['TTbar'] = [samples['TTSingleLep_pow'], samples['TTLep_pow']]

samples['T_tch_pow'] = [os.path.join(userpath, MC_dir, "T_tch_pow/"), 136.02, ]
samples['TBar_tch_pow'] = [os.path.join(userpath, MC_dir, "TBar_tch_pow/"), 80.95, ]
samples['T_tWch_ext'] = [os.path.join(userpath, MC_dir, "T_tWch_ext/"), 35.85, ]
samples['TBar_tWch_ext'] = [os.path.join(userpath, MC_dir, "TBar_tWch_ext/"), 35.85, ]
samples['ST'] = [samples['T_tch_pow'], samples['TBar_tch_pow'], samples['T_tWch_ext'], samples['TBar_tWch_ext']]

samples['WJetsToLNu_HT70to100'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT70to100/"), 1637.13, 429894]
samples['WJetsToLNu_HT100to200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT100to200_comb/"), 1627.45, 887522]
samples['WJetsToLNu_HT200to400'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT200to400_comb/"), 435.237, 954588]
samples['WJetsToLNu_HT400to600'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT400to600_comb/"), 59.1811, 544406]
samples['WJetsToLNu_HT600to800'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT600to800_comb/"), 14.5805, 534803]
samples['WJetsToLNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT800to1200_comb/"), 6.65621, 569975]
samples['WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT1200to2500_comb/"), 1.60809, 105922]
samples['WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT2500toInf_comb/"), 0.0389136, 135533]
samples['WJetsToLNu'] = [samples['WJetsToLNu_HT70to100'], samples['WJetsToLNu_HT100to200'], samples['WJetsToLNu_HT200to400'], samples['WJetsToLNu_HT400to600'], samples['WJetsToLNu_HT600to800'], samples['WJetsToLNu_HT800to1200'], samples['WJetsToLNu_HT1200to2500'], samples['WJetsToLNu_HT2500toInf']]

samples['QCD_HT50to100'] = [os.path.join(userpath, MC_dir, "QCD_HT50to100/"), 246400000.0, ]
samples['QCD_HT100to200'] = [os.path.join(userpath, MC_dir, "QCD_HT100to200/"), 27850000.0, ]
samples['QCD_HT200to300'] = [os.path.join(userpath, MC_dir, "QCD_HT200to300_comb/"), 1717000, ]
samples['QCD_HT300to500'] = [os.path.join(userpath, MC_dir, "QCD_HT300to500_comb/"), 351300, ]
samples['QCD_HT500to700'] = [os.path.join(userpath, MC_dir, "QCD_HT500to700_comb/"), 31630, ]
samples['QCD_HT700to1000'] = [os.path.join(userpath, MC_dir, "QCD_HT700to1000_comb/"), 6802, ]
samples['QCD_HT1000to1500'] = [os.path.join(userpath, MC_dir, "QCD_HT1000to1500_comb/"), 1206, ]
samples['QCD_HT1500to2000'] = [os.path.join(userpath, MC_dir, "QCD_HT1500to2000_comb/"), 20.4, ]
samples['QCD_HT2000toInf'] = [os.path.join(userpath, MC_dir, "QCD_HT2000toInf_comb/"), 25.25]
samples['QCD'] = [samples['QCD_HT50to100'], samples['QCD_HT100to200'], samples['QCD_HT200to300'], samples['QCD_HT300to500'], samples['QCD_HT500to700'], samples['QCD_HT700to1000'], samples['QCD_HT1000to1500'], samples['QCD_HT1500to2000'], samples['QCD_HT2000toInf']]

samples['ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT100to200_comb/"), 344.9781, ]
samples['ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT200to400_comb/"), 96.3828, ]
samples['ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT400to600_comb/"), 13.4562, ]
samples['ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT600to800/"), 3.96183, ]
samples['ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT800to1200/"), 1.81302, ]
samples['ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT1200to2500_comb/"), 0.441078, ]
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
samples['WZTo3LNu'] = [os.path.join(userpath, MC_dir, "WZTo3LNu_comb/"), 4.42965, ]
samples['ZZTo2L2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Nu_comb/"), 0.564, ]
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

#Following data are currently unavailable!!
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





# UL16 samples
# PreVFP era
samples['UL16PreVFP_TTSingleLep_pow'] = [os.path.join(userpath, UL16PreVFP_dir, "TTSingleLep_pow_CP5/"), 831.762*(3*0.108)*(1-3*0.108)*2, 26772952]
samples['UL16PreVFP_TTLep_pow'] = [os.path.join(userpath, UL16PreVFP_dir, "TTLep_pow_CP5/"), 831.762*((3*0.108)**2), 10529728]

samples['UL16PreVFP_T_tch_pow'] = [os.path.join(userpath, UL16PreVFP_dir, "T_tch_pow/"), 136.02, 2243837]
samples['UL16PreVFP_TBar_tch_pow'] = [os.path.join(userpath, UL16PreVFP_dir, "TBar_tch_pow/"), 80.95, 1143532]
samples['UL16PreVFP_T_tWch_ext'] = [os.path.join(userpath, UL16PreVFP_dir, "T_tWch_ext/"), 35.85, 610364]
samples['UL16PreVFP_TBar_tWch_ext'] = [os.path.join(userpath, UL16PreVFP_dir, "TBar_tWch_ext/"), 35.85, 587471]
samples['UL16PreVFP_ST'] = [samples['UL16PreVFP_T_tch_pow'], samples['UL16PreVFP_TBar_tch_pow'], samples['UL16PreVFP_T_tWch_ext'], samples['UL16PreVFP_TBar_tWch_ext']]

#!samples['UL16PreVFP_WJetsToLNu_HT70to100'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT70to100/"), 1637.13, ]
samples['UL16PreVFP_WJetsToLNu_HT100to200'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT100to200/"), 1627.45, 2152537]
samples['UL16PreVFP_WJetsToLNu_HT200to400'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT200to400/"), 435.237, 3529015]
samples['UL16PreVFP_WJetsToLNu_HT400to600'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT400to600/"), 59.1811, 712802]
samples['UL16PreVFP_WJetsToLNu_HT600to800'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT600to800/"), 14.5805, 805595]
samples['UL16PreVFP_WJetsToLNu_HT800to1200'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT800to1200/"), 6.65621, 991882]
samples['UL16PreVFP_WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT1200to2500/"), 1.60809, 1006833]
samples['UL16PreVFP_WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, UL16PreVFP_dir, "WJetsToLNu_HT2500toInf/"), 0.0389136, 494854]
samples['UL16PreVFP_WJetsToLNu'] = [samples['UL16PreVFP_WJetsToLNu_HT100to200'], samples['UL16PreVFP_WJetsToLNu_HT200to400'], samples['UL16PreVFP_WJetsToLNu_HT400to600'], samples['UL16PreVFP_WJetsToLNu_HT600to800'], samples['UL16PreVFP_WJetsToLNu_HT800to1200'], samples['UL16PreVFP_WJetsToLNu_HT1200to2500'], samples['UL16PreVFP_WJetsToLNu_HT2500toInf']]

#!samples['UL16PreVFP_QCD_HT50to100'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT50to100/"), 246400000.0, ]
samples['UL16PreVFP_QCD_HT100to200'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT100to200/"), 27850000.0, 14097]
#!samples['UL16PreVFP_QCD_HT200to300'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT200to300/"), 1717000, ]
#!samples['UL16PreVFP_QCD_HT300to500'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT300to500/"), 351300, ]
samples['UL16PreVFP_QCD_HT500to700'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT500to700/"), 31630, 526996]
samples['UL16PreVFP_QCD_HT700to1000_madgraph'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT700to1000_madgraph/"), 6802, 365394]
samples['UL16PreVFP_QCD_HT1000to1500'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT1000to1500/"), 1206, 774320]
samples['UL16PreVFP_QCD_HT1000to1500_madgraph'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT1000to1500_madgraph/"), 1206, 267826]
samples['UL16PreVFP_QCD_HT1500to2000'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT1500to2000/"), 20.4, 1224292]
samples['UL16PreVFP_QCD_HT1500to2000_madgraph'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT1500to2000_madgraph/"), 20.4, 428412]
samples['UL16PreVFP_QCD_HT2000toInf'] = [os.path.join(userpath, UL16PreVFP_dir, "QCD_HT2000toInf/"), 25.25, 1069727]
samples['UL16PreVFP_QCD'] = [samples['UL16PreVFP_QCD_HT100to200'], samples['UL16PreVFP_QCD_HT500to700'], samples['UL16PreVFP_QCD_HT700to1000_madgraph'], samples['UL16PreVFP_QCD_HT1000to1500'], samples['UL16PreVFP_QCD_HT1000to1500_madgraph'], samples['UL16PreVFP_QCD_HT1500to2000'], samples['UL16PreVFP_QCD_HT1500to2000_madgraph'], samples['UL16PreVFP_QCD_HT2000toInf']]

#samples['UL16PreVFP_ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT100to200_comb/"), 344.9781, ]
#samples['UL16PreVFP_ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT200to400_comb/"), 96.3828, ]
#samples['UL16PreVFP_ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT400to600_comb/"), 13.4562, ]
#samples['UL16PreVFP_ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT600to800/"), 3.96183, ]
#samples['UL16PreVFP_ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT800to1200/"), 1.81302, ]
#samples['UL16PreVFP_ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT1200to2500_comb/"), 0.441078, ]
#samples['UL16PreVFP_ZJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, UL16PreVFP_dir, "ZJetsToNuNu_HT2500toInf/"), 0.01008969, ]
#samples['UL16PreVFP_ZJetsToNuNu'] = [samples['UL16PreVFP_ZJetsToNuNu_HT100to200'], samples['UL16PreVFP_ZJetsToNuNu_HT200to400'], samples['UL16PreVFP_ZJetsToNuNu_HT400to600'], samples['UL16PreVFP_ZJetsToNuNu_HT600to800'], samples['UL16PreVFP_ZJetsToNuNu_HT800to1200'], samples['UL16PreVFP_ZJetsToNuNu_HT1200to2500'], samples['UL16PreVFP_ZJetsToNuNu_HT2500toInf']]

samples['UL16PreVFP_DYJetsToLL_M50_HT70to100'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT70to100/"), 147.4*1.23, 56857]
samples['UL16PreVFP_DYJetsToLL_M50_HT100to200'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT100to200/"), 147.4*1.23, 243237]
samples['UL16PreVFP_DYJetsToLL_M50_HT200to400'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT200to400/"), 40.99*1.23, 352789]
#!samples['UL16PreVFP_DYJetsToLL_M50_HT400to600'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT400to600/"), 5.678*1.23, ]
samples['UL16PreVFP_DYJetsToLL_M50_HT600to800'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT600to800/"), 1.367*1.23, 332074]
samples['UL16PreVFP_DYJetsToLL_M50_HT800to1200'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT800to1200/"), 0.6304*1.23, 381845]
#!samples['UL16PreVFP_DYJetsToLL_M50_HT1200to2500'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT1200to2500/"), 0.1514*1.23, ]
samples['UL16PreVFP_DYJetsToLL_M50_HT2500toInf'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToLL_M50_HT2500toInf/"), 0.003565*1.23, 300630]
samples['UL16PreVFP_DYJetsToLL'] = [samples['UL16PreVFP_DYJetsToLL_M50_HT70to100'], samples['UL16PreVFP_DYJetsToLL_M50_HT100to200'], samples['UL16PreVFP_DYJetsToLL_M50_HT200to400'],  samples['UL16PreVFP_DYJetsToLL_M50_HT600to800'], samples['UL16PreVFP_DYJetsToLL_M50_HT800to1200'], samples['UL16PreVFP_DYJetsToLL_M50_HT2500toInf']]


samples['UL16PreVFP_DYJetsToNuNu_HT100to200'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT100to200/"), 147.4*1.23, 859401]
samples['UL16PreVFP_DYJetsToNuNu_HT200to400'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT200to400/"), 40.99*1.23, 1694312]
samples['UL16PreVFP_DYJetsToNuNu_HT400to600'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT400to600/"), 5.678*1.23, 2258288]
samples['UL16PreVFP_DYJetsToNuNu_HT600to800'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT600to800/"), 1.367*1.23, 828557]
samples['UL16PreVFP_DYJetsToNuNu_HT800to1200'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT800to1200/"), 0.6304*1.23, 328287]
samples['UL16PreVFP_DYJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT1200to2500/"), 0.1514*1.23, 75722]
samples['UL16PreVFP_DYJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, UL16PreVFP_dir, "DYJetsToNuNu_HT2500toInf/"), 0.003565*1.23, 78302]
samples['UL16PreVFP_DYJetsToLL'] = [samples['UL16PreVFP_DYJetsToNuNu_HT100to200'], samples['UL16PreVFP_DYJetsToNuNu_HT200to400'],   samples['UL16PreVFP_DYJetsToNuNu_HT400to600'], samples['UL16PreVFP_DYJetsToNuNu_HT600to800'], samples['UL16PreVFP_DYJetsToNuNu_HT800to1200'], samples['UL16PreVFP_DYJetsToNuNu_HT1200to2500'], samples['UL16PreVFP_DYJetsToNuNu_HT2500toInf']]

samples['UL16PreVFP_TTWToLNu'] = [os.path.join(userpath, UL16PreVFP_dir, "TTWToLNu_CP5/"), 0.2043, 1057139]
#samples['UL16PreVFP_TTWToQQ'] = [os.path.join(userpath, UL16PreVFP_dir, "TTWToQQ/"), 0.40620, ]
#samples['UL16PreVFP_TTZ_LO'] = [os.path.join(userpath, UL16PreVFP_dir, "TTZ_LO/"), 0.5297/0.692, ]
#samples['UL16PreVFP_TTZToLLNuNu_m1to10'] = [os.path.join(userpath, UL16PreVFP_dir, "TTZToLLNuNu_m1to10/"), 0.0493, ]
#samples['UL16PreVFP_TTZToQQ'] = [os.path.join(userpath, UL16PreVFP_dir, "TTZToQQ/"), 0.5297, ]
#samples['UL16PreVFP_TTV'] = [ samples['UL16PreVFP_TTWToLNu'], samples['UL16PreVFP_TTWToQQ'], samples['UL16PreVFP_TTZ_LO'], samples['UL16PreVFP_TTZToLLNuNu_m1to10'], samples['UL16PreVFP_TTZToQQ']]
samples['UL16PreVFP_TTV'] = [ samples['UL16PreVFP_TTWToLNu']]


samples['UL16PreVFP_WWTo2L2Nu'] = [os.path.join(userpath, UL16PreVFP_dir, "WWTo2L2Nu/"), 12.178, 266582]
#samples['UL16PreVFP_WWToLNuQQ'] = [os.path.join(userpath, UL16PreVFP_dir, "WWToLNuQQ/"), 49.997, ]
#samples['UL16PreVFP_WZTo1L1Nu2Q'] = [os.path.join(userpath, UL16PreVFP_dir, "WZTo1L1Nu2Q/"), 10.71, ]
#samples['UL16PreVFP_WZTo1L3Nu'] = [os.path.join(userpath, UL16PreVFP_dir, "WZTo1L3Nu/"), (47.13)*(3*0.108)*(0.2), ]
#samples['UL16PreVFP_WZTo2L2Q'] = [os.path.join(userpath, UL16PreVFP_dir, "WZTo2L2Q/"), 5.60, ]
#samples['UL16PreVFP_WZTo3LNu'] = [os.path.join(userpath, UL16PreVFP_dir, "WZTo3LNu_comb/"), 4.42965, ]
samples['UL16PreVFP_ZZTo2L2Nu'] = [os.path.join(userpath, UL16PreVFP_dir, "ZZTo2L2Nu/"), 0.564, 1666768]
#samples['UL16PreVFP_ZZTo2L2Q'] = [os.path.join(userpath, UL16PreVFP_dir, "ZZTo2L2Q/"), 3.28, ]
#samples['UL16PreVFP_ZZTo2Q2Nu'] = [os.path.join(userpath, UL16PreVFP_dir, "ZZTo2Q2Nu/"), 4.04, ]
#samples['UL16PreVFP_ZZTo4L'] = [os.path.join(userpath, UL16PreVFP_dir, "ZZTo4L/"), 1.256*1.1, ]
samples['UL16PreVFP_VV'] = [samples['UL16PreVFP_WWTo2L2Nu'], samples['UL16PreVFP_ZZTo2L2Nu']]


#Data
#MET
samples['UL16PreVFP_MET_Run2016B'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016B_ver2_HIPM_UL/"), 1.00, 3687431]
samples['UL16PreVFP_MET_Run2016C'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016C_HIPM_UL/"), 1.00, 168445]
samples['UL16PreVFP_MET_Run2016D'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016D_HIPM_UL/"), 1.00, 2599522]
samples['UL16PreVFP_MET_Run2016E'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016E_HIPM_UL/"), 1.00, 2365296]
samples['UL16PreVFP_MET_Run2016F'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016F_HIPM_UL/"), 1.00, 1255892]
#samples['UL16PreVFP_MET_Run2016G'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016G_HIPM_UL/"), 1.00, ]
#samples['UL16PreVFP_MET_Run2016H'] = [os.path.join(userpath, UL16PreVFP_dir, "MET_Run2016H_HIPM_UL/"), 1.00, ]
samples['UL16PreVFP_MET_Data'] = [samples['UL16PreVFP_MET_Run2016B'], samples['UL16PreVFP_MET_Run2016C'], samples['UL16PreVFP_MET_Run2016D'], samples['UL16PreVFP_MET_Run2016E'], samples['UL16PreVFP_MET_Run2016F']]



# PostVFP era
samples['UL16PostVFP_TTSingleLep_pow'] = [os.path.join(userpath, UL16PostVFP_dir, "TTSingleLep_pow_CP5/"), 831.762*(3*0.108)*(1-3*0.108)*2, 26049063]
samples['UL16PostVFP_TTLep_pow'] = [os.path.join(userpath, UL16PostVFP_dir, "TTLep_pow_CP5/"), 831.762*((3*0.108)**2), 10873735]

samples['UL16PostVFP_T_tch_pow'] = [os.path.join(userpath, UL16PostVFP_dir, "T_tch_pow/"), 136.02, 2497436]
samples['UL16PostVFP_TBar_tch_pow'] = [os.path.join(userpath, UL16PostVFP_dir, "TBar_tch_pow/"), 80.95, 1122945]
samples['UL16PostVFP_T_tWch_ext'] = [os.path.join(userpath, UL16PostVFP_dir, "T_tWch_ext/"), 35.85, 627086]
samples['UL16PostVFP_TBar_tWch_ext'] = [os.path.join(userpath, UL16PostVFP_dir, "TBar_tWch_ext/"), 35.85, 679038]
samples['UL16PostVFP_ST'] = [samples['UL16PostVFP_T_tch_pow'], samples['UL16PostVFP_TBar_tch_pow'], samples['UL16PostVFP_T_tWch_ext'], samples['UL16PostVFP_TBar_tWch_ext']]

samples['UL16PostVFP_WJetsToLNu_HT70to100'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT70to100/"), 1637.13, 734363]
samples['UL16PostVFP_WJetsToLNu_HT100to200'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT100to200/"), 1627.45, 1970177]
samples['UL16PostVFP_WJetsToLNu_HT200to400'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT200to400/"), 435.237, 2980106]
samples['UL16PostVFP_WJetsToLNu_HT400to600'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT400to600/"), 59.1811, 610024]
samples['UL16PostVFP_WJetsToLNu_HT600to800'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT600to800/"), 14.5805, 774011]
samples['UL16PostVFP_WJetsToLNu_HT800to1200'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT800to1200/"), 6.65621, 840640]
samples['UL16PostVFP_WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT1200to2500/"), 1.60809, 988860]
samples['UL16PostVFP_WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, UL16PostVFP_dir, "WJetsToLNu_HT2500toInf/"), 0.0389136, 435178]
samples['UL16PostVFP_WJetsToLNu'] = [samples['UL16PostVFP_WJetsToLNu_HT70to100'], samples['UL16PostVFP_WJetsToLNu_HT100to200'], samples['UL16PostVFP_WJetsToLNu_HT200to400'], samples['UL16PostVFP_WJetsToLNu_HT400to600'], samples['UL16PostVFP_WJetsToLNu_HT600to800'], samples['UL16PostVFP_WJetsToLNu_HT800to1200'], samples['UL16PostVFP_WJetsToLNu_HT1200to2500'], samples['UL16PostVFP_WJetsToLNu_HT2500toInf']]

samples['UL16PostVFP_QCD_HT50to100'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT50to100/"), 246400000.0, 993]
samples['UL16PostVFP_QCD_HT100to200'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT100to200/"), 27850000.0, 11382]
samples['UL16PostVFP_QCD_HT200to300'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT200to300/"), 1717000, 21280]
samples['UL16PostVFP_QCD_HT200to300_madgraph'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT200to300_madgraph/"), 1717000, 8769]
samples['UL16PostVFP_QCD_HT300to500_madgraph'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT300to500_madgraph/"), 351300, 34553]
samples['UL16PostVFP_QCD_HT500to700_madgraph'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT500to700_madgraph/"), 31630, 129486]
#!samples['UL16PostVFP_QCD_HT700to1000_madgraph'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT700to1000_madgraph/"), 6802, ]
samples['UL16PostVFP_QCD_HT1000to1500'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT1000to1500/"), 1206, 679035]
samples['UL16PostVFP_QCD_HT1500to2000'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT1500to2000/"), 20.4, 1114059]
samples['UL16PostVFP_QCD_HT2000toInf'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT2000toInf/"), 25.25, 1034862]
samples['UL16PostVFP_QCD_HT2000toInf_madgraph'] = [os.path.join(userpath, UL16PostVFP_dir, "QCD_HT2000toInf_madgraph/"), 25.25, 392968]
samples['UL16PostVFP_QCD'] = [samples['UL16PostVFP_QCD_HT50to100'],samples['UL16PostVFP_QCD_HT100to200'],samples['UL16PostVFP_QCD_HT200to300'],samples['UL16PostVFP_QCD_HT200to300_madgraph'],samples['UL16PostVFP_QCD_HT300to500_madgraph'],samples['UL16PostVFP_QCD_HT500to700_madgraph'],samples['UL16PostVFP_QCD_HT1000to1500'],samples['UL16PostVFP_QCD_HT1500to2000'],samples['UL16PostVFP_QCD_HT2000toInf'],samples['UL16PostVFP_QCD_HT2000toInf_madgraph'] ]

#samples['UL16PostVFP_ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT100to200_comb/"), 344.9781, ]
#samples['UL16PostVFP_ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT200to400_comb/"), 96.3828, ]
#samples['UL16PostVFP_ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT400to600_comb/"), 13.4562, ]
#samples['UL16PostVFP_ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT600to800/"), 3.96183, ]
#samples['UL16PostVFP_ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT800to1200/"), 1.81302, ]
#samples['UL16PostVFP_ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT1200to2500_comb/"), 0.441078, ]
#samples['UL16PostVFP_ZJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, UL16PostVFP_dir, "ZJetsToNuNu_HT2500toInf/"), 0.01008969, ]
#samples['UL16PostVFP_ZJetsToNuNu'] = [samples['UL16PostVFP_ZJetsToNuNu_HT100to200'], samples['UL16PostVFP_ZJetsToNuNu_HT200to400'], samples['UL16PostVFP_ZJetsToNuNu_HT400to600'], samples['UL16PostVFP_ZJetsToNuNu_HT600to800'], samples['UL16PostVFP_ZJetsToNuNu_HT800to1200'], samples['UL16PostVFP_ZJetsToNuNu_HT1200to2500'], samples['UL16PostVFP_ZJetsToNuNu_HT2500toInf']]

samples['UL16PostVFP_DYJetsToLL_M50_HT70to100'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT70to100/"), 147.4*1.23, 48305]
samples['UL16PostVFP_DYJetsToLL_M50_HT100to200'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT100to200/"), 147.4*1.23, 207937]
samples['UL16PostVFP_DYJetsToLL_M50_HT200to400'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT200to400/"), 40.99*1.23, 336126]
samples['UL16PostVFP_DYJetsToLL_M50_HT400to600'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT400to600/"), 5.678*1.23, 236959]
samples['UL16PostVFP_DYJetsToLL_M50_HT600to800'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT600to800/"), 1.367*1.23, 279151]
samples['UL16PostVFP_DYJetsToLL_M50_HT800to1200'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT800to1200/"), 0.6304*1.23, 370262]
samples['UL16PostVFP_DYJetsToLL_M50_HT1200to2500'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT1200to2500/"), 0.1514*1.23, 455446]
samples['UL16PostVFP_DYJetsToLL_M50_HT2500toInf'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToLL_M50_HT2500toInf/"), 0.003565*1.23, 290243]
samples['UL16PostVFP_DYJetsToLL'] = [samples['UL16PostVFP_DYJetsToLL_M50_HT70to100'], samples['UL16PostVFP_DYJetsToLL_M50_HT100to200'], samples['UL16PostVFP_DYJetsToLL_M50_HT200to400'], samples['UL16PostVFP_DYJetsToLL_M50_HT400to600'], samples['UL16PostVFP_DYJetsToLL_M50_HT600to800'], samples['UL16PostVFP_DYJetsToLL_M50_HT800to1200'], samples['UL16PostVFP_DYJetsToLL_M50_HT1200to2500'], samples['UL16PostVFP_DYJetsToLL_M50_HT2500toInf']]


samples['UL16PostVFP_DYJetsToNuNu_HT100to200'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT100to200/"), 147.4*1.23, 799712]
samples['UL16PostVFP_DYJetsToNuNu_HT200to400'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT200to400/"), 40.99*1.23, 1553972]
#samples['UL16PostVFP_DYJetsToNuNu_HT400to600'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT400to600/"), 5.678*1.23, ]
samples['UL16PostVFP_DYJetsToNuNu_HT600to800'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT600to800/"), 1.367*1.23, 773894]
#samples['UL16PostVFP_DYJetsToNuNu_HT800to1200'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT800to1200/"), 0.6304*1.23, ]
samples['UL16PostVFP_DYJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT1200to2500/"), 0.1514*1.23, 64322]
samples['UL16PostVFP_DYJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, UL16PostVFP_dir, "DYJetsToNuNu_HT2500toInf/"), 0.003565*1.23, 78157]
samples['UL16PostVFP_DYJetsToLL'] = [samples['UL16PostVFP_DYJetsToNuNu_HT100to200'], samples['UL16PostVFP_DYJetsToNuNu_HT200to400'],  samples['UL16PostVFP_DYJetsToNuNu_HT600to800'], samples['UL16PostVFP_DYJetsToNuNu_HT1200to2500'], samples['UL16PostVFP_DYJetsToNuNu_HT2500toInf']]

samples['UL16PostVFP_TTWToLNu'] = [os.path.join(userpath, UL16PostVFP_dir, "TTWToLNu_CP5/"), 0.2043, 1230591]
samples['UL16PostVFP_TTWToQQ'] = [os.path.join(userpath, UL16PostVFP_dir, "TTWToQQ/"), 0.40620, 61593]
#samples['UL16PostVFP_TTZ_LO'] = [os.path.join(userpath, UL16PostVFP_dir, "TTZ_LO/"), 0.5297/0.692, ]
#samples['UL16PostVFP_TTZToLLNuNu_m1to10'] = [os.path.join(userpath, UL16PostVFP_dir, "TTZToLLNuNu_m1to10/"), 0.0493, ]
#samples['UL16PostVFP_TTZToQQ'] = [os.path.join(userpath, UL16PostVFP_dir, "TTZToQQ/"), 0.5297, ]
#samples['UL16PostVFP_TTV'] = [ samples['UL16PostVFP_TTWToLNu'], samples['UL16PostVFP_TTWToQQ'], samples['UL16PostVFP_TTZ_LO'], samples['UL16PostVFP_TTZToLLNuNu_m1to10'], samples['UL16PostVFP_TTZToQQ']]
samples['UL16PostVFP_TTV'] = [ samples['UL16PostVFP_TTWToLNu'], samples['UL16PostVFP_TTWToQQ']]

samples['UL16PostVFP_WWTo2L2Nu'] = [os.path.join(userpath, UL16PostVFP_dir, "WWTo2L2Nu/"), 12.178, 255545]
#samples['UL16PostVFP_WWToLNuQQ'] = [os.path.join(userpath, UL16PostVFP_dir, "WWToLNuQQ/"), 49.997, ]
#samples['UL16PostVFP_WZTo1L1Nu2Q'] = [os.path.join(userpath, UL16PostVFP_dir, "WZTo1L1Nu2Q/"), 10.71, ]
#samples['UL16PostVFP_WZTo1L3Nu'] = [os.path.join(userpath, UL16PostVFP_dir, "WZTo1L3Nu/"), (47.13)*(3*0.108)*(0.2), ]
#samples['UL16PostVFP_WZTo2L2Q'] = [os.path.join(userpath, UL16PostVFP_dir, "WZTo2L2Q/"), 5.60, ]
samples['UL16PostVFP_WZTo3LNu'] = [os.path.join(userpath, UL16PostVFP_dir, "WZTo3LNu_amcatnlo/"), 4.42965, 703430]
samples['UL16PostVFP_ZZTo2L2Nu'] = [os.path.join(userpath, UL16PostVFP_dir, "ZZTo2L2Nu/"), 0.564, 1578296]
#samples['UL16PostVFP_ZZTo2L2Q'] = [os.path.join(userpath, UL16PostVFP_dir, "ZZTo2L2Q/"), 3.28, ]
#samples['UL16PostVFP_ZZTo2Q2Nu'] = [os.path.join(userpath, UL16PostVFP_dir, "ZZTo2Q2Nu/"), 4.04, ]
#samples['UL16PostVFP_ZZTo4L'] = [os.path.join(userpath, UL16PostVFP_dir, "ZZTo4L/"), 1.256*1.1, ]
samples['UL16PostVFP_VV'] = [samples['UL16PostVFP_WWTo2L2Nu'], samples['UL16PostVFP_WZTo3LNu'], samples['UL16PostVFP_ZZTo2L2Nu']]


#Data
#MET
#samples['UL16PostVFP_MET_Run2016B'] = [os.path.join(userpath, UL16PostVFP_dir, "MET_Run2016B_ver2_HIPM_UL/"), 1.00, ]
#samples['UL16PostVFP_MET_Run2016C'] = [os.path.join(userpath, UL16PostVFP_dir, "MET_Run2016C_HIPM_UL/"), 1.00, ]
#samples['UL16PostVFP_MET_Run2016D'] = [os.path.join(userpath, UL16PostVFP_dirr, "MET_Run2016D_HIPM_UL/"), 1.00,]
#samples['UL16PostVFP_MET_Run2016E'] = [os.path.join(userpath, UL16PostVFP_dir, "MET_Run2016E_HIPM_UL/"), 1.00, ]
samples['UL16PostVFP_MET_Run2016F'] = [os.path.join(userpath, UL16PostVFP_dir, "MET_Run2016F_UL/"), 1.00, 152867]
samples['UL16PostVFP_MET_Run2016G'] = [os.path.join(userpath, UL16PostVFP_dir, "MET_Run2016G_UL/"), 1.00, 2801321]
samples['UL16PostVFP_MET_Run2016H'] = [os.path.join(userpath, UL16PostVFP_dir, "MET_Run2016H_UL/"), 1.00, 5337885]
samples['UL16PostVFP_MET_Data'] = [samples['UL16PostVFP_MET_Run2016F'], samples['UL16PostVFP_MET_Run2016G'], samples['UL16PostVFP_MET_Run2016H']]


# TTGJets?

