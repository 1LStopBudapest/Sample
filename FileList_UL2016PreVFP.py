import os, sys

from Dir import userpath


MC_dir = "PostProcessedNtuple/2016/UL/PreVFP/MetSingleLep"
Data_dir = MC_dir
Signal_dir = MC_dir

FullSimSignal_dir = "PostProcessedNtuple/2016/UL/PreVFP/FullsimSig/"


samples = {}

#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/

#Fullsim Signals

#samples['Sig_Displaced_300_290'] = [os.path.join(userpath, FullSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_300_mLSP_290/"), ]
#samples['Sig_Displaced_350_335'] = [os.path.join(userpath, FullSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_350_mLSP_335/"), ]
#samples['Sig_Displaced_400_380'] = [os.path.join(userpath, FullSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_400_mLSP_380/"), ]

samples['Sig_Prompt_500_420'] = [os.path.join(userpath, FullSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_420/"), ]
samples['Sig_Prompt_500_450'] = [os.path.join(userpath, FullSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_450/"), ]
samples['Sig_Prompt_500_470'] = [os.path.join(userpath, FullSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_470/"), ]


# T2tt sample fastsim
samples['T2tt'] = [os.path.join(userpath, Signal_dir, "T2tt/"), ]


#BK MC

samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow_CP5/"), 831.762*(3*0.108)*(1-3*0.108)*2, 26772952]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow_CP5/"), 831.762*((3*0.108)**2), 10529728]
samples['TTbar'] = [samples['TTSingleLep_pow'], samples['TTLep_pow']]

samples['T_tch_pow'] = [os.path.join(userpath, MC_dir, "T_tch_pow/"), 136.02, 2243837]
samples['TBar_tch_pow'] = [os.path.join(userpath, MC_dir, "TBar_tch_pow/"), 80.95, 1143532]
samples['T_tWch_ext'] = [os.path.join(userpath, MC_dir, "T_tWch_ext/"), 35.85, 610364]
samples['TBar_tWch_ext'] = [os.path.join(userpath, MC_dir, "TBar_tWch_ext/"), 35.85, 587471]
samples['ST'] = [samples['T_tch_pow'], samples['TBar_tch_pow'], samples['T_tWch_ext'], samples['TBar_tWch_ext']]

#!samples['WJetsToLNu_HT70to100'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT70to100/"), 1637.13, ]
samples['WJetsToLNu_HT100to200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT100to200/"), 1627.45, 2152537]
samples['WJetsToLNu_HT200to400'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT200to400/"), 435.237, 3529015]
samples['WJetsToLNu_HT400to600'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT400to600/"), 59.1811, 712802]
samples['WJetsToLNu_HT600to800'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT600to800/"), 14.5805, 805595]
samples['WJetsToLNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT800to1200/"), 6.65621, 991882]
samples['WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT1200to2500/"), 1.60809, 1006833]
samples['WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT2500toInf/"), 0.0389136, 494854]
samples['WJetsToLNu'] = [samples['WJetsToLNu_HT100to200'], samples['WJetsToLNu_HT200to400'], samples['WJetsToLNu_HT400to600'], samples['WJetsToLNu_HT600to800'], samples['WJetsToLNu_HT800to1200'], samples['WJetsToLNu_HT1200to2500'], samples['WJetsToLNu_HT2500toInf']]

#!samples['QCD_HT50to100'] = [os.path.join(userpath, MC_dir, "QCD_HT50to100/"), 246400000.0, ]
samples['QCD_HT100to200'] = [os.path.join(userpath, MC_dir, "QCD_HT100to200/"), 27850000.0, 14097]
#!samples['QCD_HT200to300'] = [os.path.join(userpath, MC_dir, "QCD_HT200to300/"), 1717000, ]
#!samples['QCD_HT300to500'] = [os.path.join(userpath, MC_dir, "QCD_HT300to500/"), 351300, ]
samples['QCD_HT500to700'] = [os.path.join(userpath, MC_dir, "QCD_HT500to700/"), 31630, 526996]
samples['QCD_HT700to1000_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT700to1000_madgraph/"), 6802, 365394]
samples['QCD_HT1000to1500'] = [os.path.join(userpath, MC_dir, "QCD_HT1000to1500/"), 1206, 774320]
samples['QCD_HT1000to1500_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT1000to1500_madgraph/"), 1206, 267826]
samples['QCD_HT1500to2000'] = [os.path.join(userpath, MC_dir, "QCD_HT1500to2000/"), 20.4, 1224292]
samples['QCD_HT1500to2000_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT1500to2000_madgraph/"), 20.4, 428412]
samples['QCD_HT2000toInf'] = [os.path.join(userpath, MC_dir, "QCD_HT2000toInf/"), 25.25, 1069727]
samples['QCD'] = [samples['QCD_HT100to200'], samples['QCD_HT500to700'], samples['QCD_HT700to1000_madgraph'], samples['QCD_HT1000to1500'], samples['QCD_HT1000to1500_madgraph'], samples['QCD_HT1500to2000'], samples['QCD_HT1500to2000_madgraph'], samples['QCD_HT2000toInf']]

#samples['ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT100to200_comb/"), 344.9781, ]
#samples['ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT200to400_comb/"), 96.3828, ]
#samples['ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT400to600_comb/"), 13.4562, ]
#samples['ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT600to800/"), 3.96183, ]
#samples['ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT800to1200/"), 1.81302, ]
#samples['ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT1200to2500_comb/"), 0.441078, ]
#samples['ZJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "ZJetsToNuNu_HT2500toInf/"), 0.01008969, ]
#samples['ZJetsToNuNu'] = [samples['ZJetsToNuNu_HT100to200'], samples['ZJetsToNuNu_HT200to400'], samples['ZJetsToNuNu_HT400to600'], samples['ZJetsToNuNu_HT600to800'], samples['ZJetsToNuNu_HT800to1200'], samples['ZJetsToNuNu_HT1200to2500'], samples['ZJetsToNuNu_HT2500toInf']]

samples['DYJetsToLL_M50_HT70to100'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT70to100/"), 147.4*1.23, 56857]
samples['DYJetsToLL_M50_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT100to200/"), 147.4*1.23, 243237]
samples['DYJetsToLL_M50_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT200to400/"), 40.99*1.23, 352789]
#!samples['DYJetsToLL_M50_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT400to600/"), 5.678*1.23, ]
samples['DYJetsToLL_M50_HT600to800'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT600to800/"), 1.367*1.23, 332074]
samples['DYJetsToLL_M50_HT800to1200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT800to1200/"), 0.6304*1.23, 381845]
#!samples['DYJetsToLL_M50_HT1200to2500'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT1200to2500/"), 0.1514*1.23, ]
samples['DYJetsToLL_M50_HT2500toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT2500toInf/"), 0.003565*1.23, 300630]
samples['DYJetsToLL'] = [samples['DYJetsToLL_M50_HT70to100'], samples['DYJetsToLL_M50_HT100to200'], samples['DYJetsToLL_M50_HT200to400'],  samples['DYJetsToLL_M50_HT600to800'], samples['DYJetsToLL_M50_HT800to1200'], samples['DYJetsToLL_M50_HT2500toInf']]


samples['DYJetsToNuNu_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT100to200/"), 147.4*1.23, 859401]
samples['DYJetsToNuNu_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT200to400/"), 40.99*1.23, 1694312]
samples['DYJetsToNuNu_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT400to600/"), 5.678*1.23, 2258288]
samples['DYJetsToNuNu_HT600to800'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT600to800/"), 1.367*1.23, 828557]
samples['DYJetsToNuNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT800to1200/"), 0.6304*1.23, 328287]
samples['DYJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT1200to2500/"), 0.1514*1.23, 75722]
samples['DYJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT2500toInf/"), 0.003565*1.23, 78302]
samples['DYJetsToLL'] = [samples['DYJetsToNuNu_HT100to200'], samples['DYJetsToNuNu_HT200to400'],   samples['DYJetsToNuNu_HT400to600'], samples['DYJetsToNuNu_HT600to800'], samples['DYJetsToNuNu_HT800to1200'], samples['DYJetsToNuNu_HT1200to2500'], samples['DYJetsToNuNu_HT2500toInf']]

samples['TTWToLNu'] = [os.path.join(userpath, MC_dir, "TTWToLNu_CP5/"), 0.2043, 1057139]
#samples['TTWToQQ'] = [os.path.join(userpath, MC_dir, "TTWToQQ/"), 0.40620, ]
#samples['TTZ_LO'] = [os.path.join(userpath, MC_dir, "TTZ_LO/"), 0.5297/0.692, ]
#samples['TTZToLLNuNu_m1to10'] = [os.path.join(userpath, MC_dir, "TTZToLLNuNu_m1to10/"), 0.0493, ]
#samples['TTZToQQ'] = [os.path.join(userpath, MC_dir, "TTZToQQ/"), 0.5297, ]
#samples['TTV'] = [ samples['TTWToLNu'], samples['TTWToQQ'], samples['TTZ_LO'], samples['TTZToLLNuNu_m1to10'], samples['TTZToQQ']]
samples['TTV'] = [ samples['TTWToLNu']]


samples['WWTo2L2Nu'] = [os.path.join(userpath, MC_dir, "WWTo2L2Nu/"), 12.178, 266582]
#samples['WWToLNuQQ'] = [os.path.join(userpath, MC_dir, "WWToLNuQQ/"), 49.997, ]
#samples['WZTo1L1Nu2Q'] = [os.path.join(userpath, MC_dir, "WZTo1L1Nu2Q/"), 10.71, ]
#samples['WZTo1L3Nu'] = [os.path.join(userpath, MC_dir, "WZTo1L3Nu/"), (47.13)*(3*0.108)*(0.2), ]
#samples['WZTo2L2Q'] = [os.path.join(userpath, MC_dir, "WZTo2L2Q/"), 5.60, ]
#samples['WZTo3LNu'] = [os.path.join(userpath, MC_dir, "WZTo3LNu_comb/"), 4.42965, ]
samples['ZZTo2L2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Nu/"), 0.564, 1666768]
#samples['ZZTo2L2Q'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Q/"), 3.28, ]
#samples['ZZTo2Q2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2Q2Nu/"), 4.04, ]
#samples['ZZTo4L'] = [os.path.join(userpath, MC_dir, "ZZTo4L/"), 1.256*1.1, ]
samples['VV'] = [samples['WWTo2L2Nu'], samples['ZZTo2L2Nu']]


#Data
#MET
samples['MET_Run2016B'] = [os.path.join(userpath, Data_dir, "MET_Run2016B_ver2_HIPM_UL/"), 1.00, 3687431]
samples['MET_Run2016C'] = [os.path.join(userpath, Data_dir, "MET_Run2016C_HIPM_UL/"), 1.00, 168445]
samples['MET_Run2016D'] = [os.path.join(userpath, Data_dir, "MET_Run2016D_HIPM_UL/"), 1.00, 2599522]
samples['MET_Run2016E'] = [os.path.join(userpath, Data_dir, "MET_Run2016E_HIPM_UL/"), 1.00, 2365296]
samples['MET_Run2016F'] = [os.path.join(userpath, Data_dir, "MET_Run2016F_HIPM_UL/"), 1.00, 1255892]
samples['MET_Data'] = [samples['MET_Run2016B'], samples['MET_Run2016C'], samples['MET_Run2016D'], samples['MET_Run2016E'], samples['MET_Run2016F']]



