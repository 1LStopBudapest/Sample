import os, sys

from Dir import userpath

MC_dir = "PostProcessedNtuple/2016/UL/PostVFP/Met"
Data_dir = MC_dir
Signal_dir = "PostProcessedNtuple/2016/UL/SignalGrid/"

FullSimSignal_dir = "PostProcessedNtuple/2016/UL/PostVFP/FullsimSig/"
FastSimSignal_dir = "PostProcessedNtuple/2016/UL/FastsimSig/"

samples = {}

#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/


#Fullsim Signals points

samples['Sig_Displaced_300_290_full'] = [os.path.join(userpath, FullSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_300_mLSP_290/"), ]
samples['Sig_Displaced_350_335_full'] = [os.path.join(userpath, FullSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_350_mLSP_335/"), ]
samples['Sig_Displaced_400_380_full'] = [os.path.join(userpath, FullSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_400_mLSP_380/"), ]

samples['Sig_Prompt_500_420_full'] = [os.path.join(userpath, FullSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_420/"), ]
samples['Sig_Prompt_500_450_full'] = [os.path.join(userpath, FullSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_450/"), ]
samples['Sig_Prompt_500_470_full'] = [os.path.join(userpath, FullSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_470/"), ]

#Fastsim Signals points

samples['Sig_Displaced_300_290_fast'] = [os.path.join(userpath, FastSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_300_mLSP_290_FS/"), ]
samples['Sig_Displaced_350_335_fast'] = [os.path.join(userpath, FastSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_350_mLSP_335_FS/"), ]
samples['Sig_Displaced_400_380_fast'] = [os.path.join(userpath, FastSimSignal_dir, "Displaced/SMS_T2tt_LL_mStop_400_mLSP_380_FS/"), ]

samples['Sig_Prompt_500_420_fast'] = [os.path.join(userpath, FastSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_420_FS/"), ]
samples['Sig_Prompt_500_450_fast'] = [os.path.join(userpath, FastSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_450_FS/"), ]
samples['Sig_Prompt_500_470_fast'] = [os.path.join(userpath, FastSimSignal_dir, "Prompt/SMS_T2tt_mStop_500_mLSP_470_FS/"), ]


# T2tt sample fastsim: prompt
samples['T2tt'] = [os.path.join(userpath, Signal_dir, "Prompt/T2tt/"), ]

# BK MC

samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow_CP5/"), 831.762*(3*0.108)*(1-3*0.108)*2, 26049063]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow_CP5/"), 831.762*((3*0.108)**2), 10873735]
samples['TTbar'] = [samples['TTSingleLep_pow'], samples['TTLep_pow']]

samples['T_tch_pow'] = [os.path.join(userpath, MC_dir, "T_tch_pow/"), 136.02, 2497436]
samples['TBar_tch_pow'] = [os.path.join(userpath, MC_dir, "TBar_tch_pow/"), 80.95, 1122945]
samples['T_tWch_ext'] = [os.path.join(userpath, MC_dir, "T_tWch_ext/"), 35.85, 627086]
samples['TBar_tWch_ext'] = [os.path.join(userpath, MC_dir, "TBar_tWch_ext/"), 35.85, 679038]
samples['ST'] = [samples['T_tch_pow'], samples['TBar_tch_pow'], samples['T_tWch_ext'], samples['TBar_tWch_ext']]

samples['WJetsToLNu_HT70to100'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT70to100/"), 1637.13, 734363]
samples['WJetsToLNu_HT100to200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT100to200/"), 1627.45, 1970177]
samples['WJetsToLNu_HT200to400'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT200to400/"), 435.237, 2980106]
samples['WJetsToLNu_HT400to600'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT400to600/"), 59.1811, 610024]
samples['WJetsToLNu_HT600to800'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT600to800/"), 14.5805, 774011]
samples['WJetsToLNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT800to1200/"), 6.65621, 840640]
samples['WJetsToLNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT1200to2500/"), 1.60809, 988860]
samples['WJetsToLNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_HT2500toInf/"), 0.0389136, 435178]
samples['WJetsToLNu'] = [samples['WJetsToLNu_HT70to100'], samples['WJetsToLNu_HT100to200'], samples['WJetsToLNu_HT200to400'], samples['WJetsToLNu_HT400to600'], samples['WJetsToLNu_HT600to800'], samples['WJetsToLNu_HT800to1200'], samples['WJetsToLNu_HT1200to2500'], samples['WJetsToLNu_HT2500toInf']]

samples['QCD_HT50to100'] = [os.path.join(userpath, MC_dir, "QCD_HT50to100/"), 246400000.0, 993]
samples['QCD_HT100to200'] = [os.path.join(userpath, MC_dir, "QCD_HT100to200/"), 27850000.0, 11382]
samples['QCD_HT200to300'] = [os.path.join(userpath, MC_dir, "QCD_HT200to300/"), 1717000, 21280]
samples['QCD_HT200to300_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT200to300_madgraph/"), 1717000, 8769]
samples['QCD_HT300to500_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT300to500_madgraph/"), 351300, 34553]
samples['QCD_HT500to700_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT500to700_madgraph/"), 31630, 129486]
samples['QCD_HT700to1000_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT700to1000_madgraph/"), 6802, ]
samples['QCD_HT1000to1500'] = [os.path.join(userpath, MC_dir, "QCD_HT1000to1500/"), 1206, 679035]
samples['QCD_HT1500to2000'] = [os.path.join(userpath, MC_dir, "QCD_HT1500to2000/"), 20.4, 1114059]
samples['QCD_HT2000toInf'] = [os.path.join(userpath, MC_dir, "QCD_HT2000toInf/"), 25.25, 1034862]
samples['QCD_HT2000toInf_madgraph'] = [os.path.join(userpath, MC_dir, "QCD_HT2000toInf_madgraph/"), 25.25, 392968]
samples['QCD_All'] = [samples['QCD_HT50to100'],samples['QCD_HT100to200'],samples['QCD_HT200to300'],samples['QCD_HT200to300_madgraph'],samples['QCD_HT300to500_madgraph'],samples['QCD_HT500to700_madgraph'],samples['QCD_HT700to1000_madgraph'], samples['QCD_HT1000to1500'],samples['QCD_HT1500to2000'],samples['QCD_HT2000toInf'],samples['QCD_HT2000toInf_madgraph'] ]
samples['QCD'] = [samples['QCD_HT300to500_madgraph'],samples['QCD_HT500to700_madgraph'],samples['QCD_HT700to1000_madgraph'], samples['QCD_HT1000to1500'],samples['QCD_HT1500to2000'],samples['QCD_HT2000toInf'],samples['QCD_HT2000toInf_madgraph'] ]

samples['ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT100to200/"), 344.9781, ]
samples['ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT200to400/"), 96.3828, ]
samples['ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT400to600/"), 13.4562, ]
samples['ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT600to800/"), 3.96183, ]
samples['ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT800to1200/"), 1.81302, ]
samples['ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT1200to2500/"), 0.441078, ]
samples['ZJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT2500toInf/"), 0.01008969, ]
samples['ZJetsToNuNu'] = [samples['ZJetsToNuNu_HT100to200'], samples['ZJetsToNuNu_HT200to400'], samples['ZJetsToNuNu_HT400to600'], samples['ZJetsToNuNu_HT600to800'], samples['ZJetsToNuNu_HT800to1200'], samples['ZJetsToNuNu_HT1200to2500'], samples['ZJetsToNuNu_HT2500toInf']]

samples['DYJetsToLL_M50_HT70to100'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT70to100/"), 147.4*1.23, 48305]
samples['DYJetsToLL_M50_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT100to200/"), 147.4*1.23, 207937]
samples['DYJetsToLL_M50_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT200to400/"), 40.99*1.23, 336126]
samples['DYJetsToLL_M50_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT400to600/"), 5.678*1.23, 236959]
samples['DYJetsToLL_M50_HT600to800'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT600to800/"), 1.367*1.23, 279151]
samples['DYJetsToLL_M50_HT800to1200'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT800to1200/"), 0.6304*1.23, 370262]
samples['DYJetsToLL_M50_HT1200to2500'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT1200to2500/"), 0.1514*1.23, 455446]
samples['DYJetsToLL_M50_HT2500toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_HT2500toInf/"), 0.003565*1.23, 290243]
samples['DYJetsToLL'] = [samples['DYJetsToLL_M50_HT70to100'], samples['DYJetsToLL_M50_HT100to200'], samples['DYJetsToLL_M50_HT200to400'], samples['DYJetsToLL_M50_HT400to600'], samples['DYJetsToLL_M50_HT600to800'], samples['DYJetsToLL_M50_HT800to1200'], samples['DYJetsToLL_M50_HT1200to2500'], samples['DYJetsToLL_M50_HT2500toInf']]#we only have M>50 samples now



samples['TTWToLNu'] = [os.path.join(userpath, MC_dir, "TTWToLNu_CP5/"), 0.2043, 1230591]
samples['TTWToQQ'] = [os.path.join(userpath, MC_dir, "TTWToQQ/"), 0.40620, 61593]
#samples['TTZ_LO'] = [os.path.join(userpath, MC_dir, "TTZ_LO/"), 0.5297/0.692, ]
#samples['TTZToLLNuNu_m1to10'] = [os.path.join(userpath, MC_dir, "TTZToLLNuNu_m1to10/"), 0.0493, ]
#samples['TTZToQQ'] = [os.path.join(userpath, MC_dir, "TTZToQQ/"), 0.5297, ]
samples['TTG'] = [os.path.join(userpath, MC_dir, "TTGJets/"), 3.697, ]
#samples['TTV'] = [ samples['TTWToLNu'], samples['TTWToQQ'], samples['TTZ_LO'], samples['TTZToLLNuNu_m1to10'], samples['TTZToQQ']]
samples['TTV'] = [ samples['TTWToLNu'], samples['TTWToQQ'], samples['TTG']]

samples['WWTo2L2Nu'] = [os.path.join(userpath, MC_dir, "WWTo2L2Nu/"), 12.178, 255545]
#samples['WWToLNuQQ'] = [os.path.join(userpath, MC_dir, "WWToLNuQQ/"), 49.997, ]
#samples['WZTo1L1Nu2Q'] = [os.path.join(userpath, MC_dir, "WZTo1L1Nu2Q/"), 10.71, ]
#samples['WZTo1L3Nu'] = [os.path.join(userpath, MC_dir, "WZTo1L3Nu/"), (47.13)*(3*0.108)*(0.2), ]
#samples['WZTo2L2Q'] = [os.path.join(userpath, MC_dir, "WZTo2L2Q/"), 5.60, ]
samples['WZTo3LNu'] = [os.path.join(userpath, MC_dir, "WZTo3LNu_amcatnlo/"), 4.42965, 703430]
samples['ZZTo2L2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Nu/"), 0.564, 1578296]
#samples['ZZTo2L2Q'] = [os.path.join(userpath, MC_dir, "ZZTo2L2Q/"), 3.28, ]
#samples['ZZTo2Q2Nu'] = [os.path.join(userpath, MC_dir, "ZZTo2Q2Nu/"), 4.04, ]
#samples['ZZTo4L'] = [os.path.join(userpath, MC_dir, "ZZTo4L/"), 1.256*1.1, ]
samples['WW'] = [os.path.join(userpath, MC_dir, "WW/"), 62.175, 255545]
samples['VV'] = [samples['WW'], samples['WZTo3LNu'], samples['ZZTo2L2Nu']]


#Data
#MET
samples['MET_Run2016F'] = [os.path.join(userpath, Data_dir, "MET_Run2016F_UL/"), 1.00, 152867]
samples['MET_Run2016G'] = [os.path.join(userpath, Data_dir, "MET_Run2016G_UL/"), 1.00, 2801321]
samples['MET_Run2016H'] = [os.path.join(userpath, Data_dir, "MET_Run2016H_UL/"), 1.00, 5337885]
samples['MET_Data'] = [samples['MET_Run2016F'], samples['MET_Run2016G'], samples['MET_Run2016H']]

