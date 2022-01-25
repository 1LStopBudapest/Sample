import os, sys

from Dir import userpath

MC_dir = "PostProcessedNtuple/2016/fakerate_janik_1j1mu_Mu3_PFJet40/"
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

# we need for fake rate only MC and data
#PostProcessed Samples
#samples['T2tt'] = [os.path.join(userpath, Signal_dir, "T2tt/"), ]

#MC
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


samples['TTSingleLep_pow'] = [os.path.join(userpath, MC_dir, "TTSingleLep_pow/")]
samples['TTLep_pow'] = [os.path.join(userpath, MC_dir, "TTLep_pow/")]
samples['TTbar'] = [os.path.join(userpath, MC_dir, "TTbar/")]

samples['WJetsToLNu_comb'] = [os.path.join(userpath, MC_dir, "WJetsToLNu_comb/")]

samples['DYJetsToLL_M10to50_LO'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M10to50_LO/")]
samples['DYJetsToLL_M50_LO_ext1_comb'] = [os.path.join(userpath, MC_dir, "DYJetsToLL_M50_LO_ext1_comb/")]
samples['DYJetsToLL'] = [samples['DYJetsToLL_M10to50_LO'], samples['DYJetsToLL_M50_LO_ext1_comb']]

#Data

#DoubleMuon
samples['DoubleMuon_Run2016B'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016B_25Oct2019_ver2/")]
samples['DoubleMuon_Run2016C'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016C_25Oct2019/")]
samples['DoubleMuon_Run2016D'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016D_25Oct2019/")]
samples['DoubleMuon_Run2016E'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016E_25Oct2019/")]
samples['DoubleMuon_Run2016F'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016F_25Oct2019/")]
samples['DoubleMuon_Run2016G'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016G_25Oct2019/")]
samples['DoubleMuon_Run2016H'] = [os.path.join(userpath, Data_dir, "DoubleMuon_Run2016H_25Oct2019/")]
samples['DoubleMuon_Data'] = [samples['DoubleMuon_Run2016B'], samples['DoubleMuon_Run2016C'], samples['DoubleMuon_Run2016D'], samples['DoubleMuon_Run2016E'], samples['DoubleMuon_Run2016F'], samples['DoubleMuon_Run2016G'], samples['DoubleMuon_Run2016H']]


'''
#SingleMuon
samples['SingleMuon_Run2016B'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016B_17Jul2018_ver2/"), 1.00, 865966]
samples['SingleMuon_Run2016C'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016C_17Jul2018/"), 1.00, 463161]
samples['SingleMuon_Run2016D'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016D_17Jul2018/"), 1.00, 700244]
samples['SingleMuon_Run2016E'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016E_17Jul2018/"), 1.00, 836822]
samples['SingleMuon_Run2016F'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016F_17Jul2018/"), 1.00, 556410]
samples['SingleMuon_Run2016G'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016G_17Jul2018/"), 1.00, 1224131]
samples['SingleMuon_Run2016H'] = [os.path.join(userpath, Data_dir, "SingleMuon_Run2016H_17Jul2018/"), 1.00, 1287221]
samples['SingleMuon_Data'] = [samples['SingleMuon_Run2016B'], samples['SingleMuon_Run2016C'], samples['SingleMuon_Run2016D'], samples['SingleMuon_Run2016E'], samples['SingleMuon_Run2016F'], samples['SingleMuon_Run2016G'], samples['SingleMuon_Run2016H']] 
'''

