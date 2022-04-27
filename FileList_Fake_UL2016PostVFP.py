import os, sys

from Dir import userpath

MC_dir = "PostProcessedNtuple/2016/UL/Fakerate/PostVFP/"
Data_dir = MC_dir
#Signal_dir = "PostProcessedNtuple/2016/MetSingleLep/"

samples = {}

#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/


#PostProcessed Samples: no need
#samples['T2tt'] = [os.path.join(userpath, Signal_dir, "T2tt/"), ]

#MC
"""
samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow/")]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow/")]
samples['TTbar'] = [os.path.join(userpath, MC_dir, "TTbar/")]

samples['WJetsToLNu_comb'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_comb/")]

samples['DYJetsToLL_M10to50_LO'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M10to50_LO/")]
samples['DYJetsToLL_M50_LO_ext1_comb'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_LO_ext1_comb/")]
samples['DYJetsToLL'] = [samples['DYJetsToLL_M10to50_LO'], samples['DYJetsToLL_M50_LO_ext1_comb']]


samples['QCD_pt15to30'] = [os.path.join(userpath, MC_dir, "QCD_pt15to30/")]
samples['QCD_pt30to50'] = [os.path.join(userpath, MC_dir, "QCD_pt30to50/")]
samples['QCD_pt50to80'] = [os.path.join(userpath, MC_dir, "QCD_pt50to80/")]
samples['QCD_pt80to120'] = [os.path.join(userpath, MC_dir, "QCD_pt80to120/")]
samples['QCD_pt120to170'] = [os.path.join(userpath, MC_dir, "QCD_pt120to170_comb/")]
samples['QCD_pt170to300'] = [os.path.join(userpath, MC_dir, "QCD_pt170to300_comb/")]
samples['QCD_pt300to470'] = [os.path.join(userpath, MC_dir, "QCD_pt300to470_comb/")]
samples['QCD_pt470to600'] = [os.path.join(userpath, MC_dir, "QCD_pt470to600/")]
samples['QCD_pt600to800'] = [os.path.join(userpath, MC_dir, "QCD_pt600to800_comb/")]
samples['QCD_pt800to1000'] = [os.path.join(userpath, MC_dir, "QCD_pt800to1000/")]
samples['QCD_pt1000to1400'] = [os.path.join(userpath, MC_dir, "QCD_pt1000to1400/")]
samples['QCD_pt1400to1800'] = [os.path.join(userpath, MC_dir, "QCD_pt1400to1800_comb/")]
samples['QCD_pt1800to2400'] = [os.path.join(userpath, MC_dir, "QCD_pt1800to2400_comb/")]
samples['QCD_pt2400to3200'] = [os.path.join(userpath, MC_dir, "QCD_pt2400to3200_comb/")]
samples['QCD_pt3200toInf'] = [os.path.join(userpath, MC_dir, "QCD_pt3200toInf/")]
samples['QCD'] = [samples['QCD_pt15to30'], samples['QCD_pt30to50'], samples['QCD_pt50to80'], samples['QCD_pt80to120'], samples['QCD_pt120to170'], samples['QCD_pt170to300'], samples['QCD_pt300to470'], samples['QCD_pt470to600'], samples['QCD_pt600to800'], samples['QCD_pt800to1000'], samples['QCD_pt1000to1400'], samples['QCD_pt1400to1800'], samples['QCD_pt1800to2400'], samples['QCD_pt2400to3200'], samples['QCD_pt3200toInf']]
"""

#Data

#DoubleMuon
samples['DoubleMuon_Run2016F'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016F_UL/"),]
samples['DoubleMuon_Run2016G'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016G_UL/"),]
samples['DoubleMuon_Run2016H'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016H_UL/"),]
samples['DoubleMuon_Data'] = [samples['DoubleMuon_Run2016F'], samples['DoubleMuon_Run2016G'], samples['DoubleMuon_Run2016H']]

#SingleMuon
samples['SingleMuon_Run2016F'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016F_UL/"), 1.00,]
samples['SingleMuon_Run2016G'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016G_UL/"), 1.00,]
samples['SingleMuon_Run2016H'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016H_UL/"), 1.00,]
samples['SingleMuon_Data'] = [samples['SingleMuon_Run2016F'], samples['SingleMuon_Run2016G'], samples['SingleMuon_Run2016H']] 

#JetHT
samples['JetHT_Run2016F'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016F_UL/"), 1.00,]
samples['JetHT_Run2016G'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016G_UL/"), 1.00,]
samples['JetHT_Run2016H'] = [os.path.join(userpath, Data_dir, "JetHT_Run2016H_UL/"), 1.00,]
samples['JetHT_Data'] = [samples['JetHT_Run2016F'], samples['JetHT_Run2016G'], samples['JetHT_Run2016H']]

#DoubleEG
samples['DoubleEG_Run2016F'] = [os.path.join(userpath, Data_dir, "DoubleEG_Run2016F_UL/"),]
samples['DoubleEG_Run2016G'] = [os.path.join(userpath, Data_dir, "DoubleEG_Run2016G_UL/"),]
samples['DoubleEG_Run2016H'] = [os.path.join(userpath, Data_dir, "DoubleEG_Run2016H_UL/"),]
samples['DoubleEG_Data'] = [samples['DoubleEG_Run2016F'], samples['DoubleEG_Run2016G'], samples['DoubleEG_Run2016H']]
