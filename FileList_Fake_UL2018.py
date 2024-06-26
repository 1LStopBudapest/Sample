import os, sys

from Dir import userpath

MC_dir = "PostProcessedNtuple/2018/UL/Fakerate/"
Data_dir = MC_dir
#Signal_dir = "PostProcessedNtuple/2018/UL/SignalGrid/"

samples = {}

#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/


#PostProcessed Samples:

#samples['T2tt'] = [os.path.join(userpath, Signal_dir, "T2tt/"), ]

#MC

samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow_CP5/")]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow_CP5/")]
samples['TTbar'] = [os.path.join(userpath, MC_dir, "TTbar/")]

samples['WJetsToLNu_comb'] = [os.path.join(userpath, MC_dir, "WJetsToLNu/")]

samples['DYJetsToLL_M10to50'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M10to50_LO/")]
samples['DYJetsToLL_M50'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_LO/")]
samples['DYJetsToLL_M50_ext'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_LO_ext/")]
samples['DYJetsToLL'] = [samples['DYJetsToLL_M10to50'], samples['DYJetsToLL_M50'], samples['DYJetsToLL_M50_ext']]


samples['T_tch_pow'] = [os.path.join(userpath, MC_dir, "T_tch_pow/"),]
samples['TBar_tch_pow'] = [os.path.join(userpath, MC_dir, "TBar_tch_pow/"),]
samples['T_tWch'] = [os.path.join(userpath, MC_dir, "T_tWch/"),]
samples['TBar_tWch'] = [os.path.join(userpath, MC_dir, "TBar_tWch/"),]
samples['ST'] = [samples['T_tch_pow'], samples['TBar_tch_pow'], samples['T_tWch'], samples['TBar_tWch']]

samples['QCD_HT50to100'] = [os.path.join(userpath, MC_dir, "QCD_HT50to100/"), 246400000.0, 993]
samples['QCD_HT100to200'] = [os.path.join(userpath, MC_dir, "QCD_HT100to200/"), 27850000.0, 11382]
samples['QCD_HT200to300'] = [os.path.join(userpath, MC_dir, "QCD_HT200to300/"), 1717000, 21280]
samples['QCD_HT300to500'] = [os.path.join(userpath, MC_dir, "QCD_HT300to500/"), 351300, 34553]
samples['QCD_HT500to700'] = [os.path.join(userpath, MC_dir, "QCD_HT500to700/"), 31630, 129486]
samples['QCD_HT700to1000'] = [os.path.join(userpath, MC_dir, "QCD_HT700to1000/"), 6802, ]
samples['QCD_HT1000to1500'] = [os.path.join(userpath, MC_dir, "QCD_HT1000to1500/"), 1206, 679035]
samples['QCD_HT1500to2000'] = [os.path.join(userpath, MC_dir, "QCD_HT1500to2000/"), 20.4, 1114059]
samples['QCD_HT2000toInf'] = [os.path.join(userpath, MC_dir, "QCD_HT2000toInf/"), 25.25, 1034862]
samples['QCD_All'] = [samples['QCD_HT50to100'],samples['QCD_HT100to200'],samples['QCD_HT200to300'],samples['QCD_HT300to500'],samples['QCD_HT500to700'],samples['QCD_HT700to1000'], samples['QCD_HT1000to1500'],samples['QCD_HT1500to2000'],samples['QCD_HT2000toInf']]
samples['QCD'] = [samples['QCD_HT300to500'],samples['QCD_HT500to700'],samples['QCD_HT700to1000'], samples['QCD_HT1000to1500'],samples['QCD_HT1500to2000'],samples['QCD_HT2000toInf']]

samples['ZJetsToNuNu_HT100to200'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT100to200/"), 344.9781, ]
samples['ZJetsToNuNu_HT200to400'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT200to400/"), 96.3828, ]
samples['ZJetsToNuNu_HT400to600'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT400to600/"), 13.4562, ]
samples['ZJetsToNuNu_HT600to800'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT600to800/"), 3.96183, ]
samples['ZJetsToNuNu_HT800to1200'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT800to1200/"), 1.81302, ]
samples['ZJetsToNuNu_HT1200to2500'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT1200to2500/"), 0.441078, ]
samples['ZJetsToNuNu_HT2500toInf'] = [os.path.join(userpath, MC_dir, "DYJetsToNuNu_HT2500toInf/"), 0.01008969, ]
samples['ZJetsToNuNu'] = [samples['ZJetsToNuNu_HT100to200'], samples['ZJetsToNuNu_HT200to400'], samples['ZJetsToNuNu_HT400to600'], samples['ZJetsToNuNu_HT600to800'], samples['ZJetsToNuNu_HT800to1200'], samples['ZJetsToNuNu_HT1200to2500'], samples['ZJetsToNuNu_HT2500toInf']]


#Data

#DoubleMuon
samples['DoubleMuon_Run2018A'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2018A_UL/"),]
samples['DoubleMuon_Run2018B'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2018B_UL/"),]
samples['DoubleMuon_Run2018C'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2018C_UL/"),]
samples['DoubleMuon_Run2018D'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2018D_UL/"),]
samples['DoubleMuon_Data'] = [samples['DoubleMuon_Run2018A'], samples['DoubleMuon_Run2018B'], samples['DoubleMuon_Run2018C'], samples['DoubleMuon_Run2018D']]

#SingleMuon
samples['SingleMuon_Run2018A'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2018A_UL/"),]
samples['SingleMuon_Run2018B'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2018B_UL/"),]
samples['SingleMuon_Run2018C'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2018C_UL/"),]
samples['SingleMuon_Run2018D'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2018D_UL/"),]
samples['SingleMuon_Data'] = [samples['SingleMuon_Run2018A'], samples['SingleMuon_Run2018B'], samples['SingleMuon_Run2018C'], samples['SingleMuon_Run2018D']]

#JetHT
samples['JetHT_Run2018A'] = [os.path.join(userpath, Data_dir, "JetHT_Run2018A_UL/"),]
samples['JetHT_Run2018B'] = [os.path.join(userpath, Data_dir, "JetHT_Run2018B_UL/"),]
samples['JetHT_Run2018C'] = [os.path.join(userpath, Data_dir, "JetHT_Run2018C_UL/"),]
samples['JetHT_Run2018D'] = [os.path.join(userpath, Data_dir, "JetHT_Run2018D_UL/"),]
samples['JetHT_Data'] = [samples['JetHT_Run2018A'], samples['JetHT_Run2018B'], samples['JetHT_Run2018C'], samples['JetHT_Run2018D']]

#EG
samples['EGamma_Run2018A'] = [os.path.join(userpath, Data_dir, "EGamma_Run2018A_UL/"),]
samples['EGamma_Run2018B'] = [os.path.join(userpath, Data_dir, "EGamma_Run2018B_UL/"),]
samples['EGamma_Run2018C'] = [os.path.join(userpath, Data_dir, "EGamma_Run2018C_UL/"),]
samples['EGamma_Run2018D'] = [os.path.join(userpath, Data_dir, "EGamma_Run2018D_UL/"),]
samples['EGamma_Data'] = [samples['EGamma_Run2018A'], samples['EGamma_Run2018B'], samples['EGamma_Run2018C'], samples['EGamma_Run2018D']]
