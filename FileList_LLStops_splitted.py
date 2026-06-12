import os, sys

from Dir import userpath

NoSplittedSignal_dir = "PostProcessedNtuple/displacedProcessedSamples/"

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

samples['Sig_Splitted_250_240_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '250_240_files/BR_1.000/'), ]
samples['Sig_Splitted_250_240_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '250_240_files/BR_0.300/'), ]
samples['Sig_Splitted_300_280_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '300_280_files/BR_1.000/'), ]
samples['Sig_Splitted_300_280_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '300_280_files/BR_0.300/'), ]
samples['Sig_Splitted_325_315_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '325_315_files/BR_1.000/'), ]
samples['Sig_Splitted_325_315_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '325_315_files/BR_0.300/'), ]
samples['Sig_Splitted_350_340_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '350_340_files/BR_1.000/'), ]
samples['Sig_Splitted_350_340_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '350_340_files/BR_0.300/'), ]
samples['Sig_Splitted_350_320_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '350_320_files/BR_1.000/'), ]
samples['Sig_Splitted_350_320_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '350_320_files/BR_0.300/'), ]
samples['Sig_Splitted_375_365_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '375_365_files/BR_1.000/'), ]
samples['Sig_Splitted_375_365_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '375_365_files/BR_0.300/'), ]
samples['Sig_Splitted_375_355_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '375_355_files/BR_1.000/'), ]
samples['Sig_Splitted_375_355_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '375_355_files/BR_0.300/'), ]
samples['Sig_Splitted_400_390_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '400_390_files/BR_1.000/'), ]
samples['Sig_Splitted_400_390_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '400_390_files/BR_0.300/'), ]
samples['Sig_Splitted_425_400_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '425_400_files/BR_1.000/'), ]
samples['Sig_Splitted_425_400_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '425_400_files/BR_0.300/'), ]
samples['Sig_Splitted_500_490_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '500_490_files/BR_1.000/'), ]
samples['Sig_Splitted_500_490_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '500_490_files/BR_0.300/'), ]
samples['Sig_Splitted_525_515_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '525_515_files/BR_1.000/'), ]
samples['Sig_Splitted_525_515_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '525_515_files/BR_0.300/'), ]
samples['Sig_Splitted_550_535_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '550_535_files/BR_1.000/'), ]
samples['Sig_Splitted_550_535_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '550_535_files/BR_0.300/'), ]
samples['Sig_Splitted_600_590_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '600_590_files/BR_1.000/'), ]
samples['Sig_Splitted_600_590_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '600_590_files/BR_0.300/'), ]
samples['Sig_Splitted_600_575_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '600_575_files/BR_1.000/'), ]
samples['Sig_Splitted_600_575_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '600_575_files/BR_0.300/'), ]
samples['Sig_Splitted_650_635_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '650_635_files/BR_1.000/'), ]
samples['Sig_Splitted_650_635_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '650_635_files/BR_0.300/'), ]
samples['Sig_Splitted_675_665_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '675_665_files/BR_1.000/'), ]
samples['Sig_Splitted_675_665_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '675_665_files/BR_0.300/'), ]
samples['Sig_Splitted_725_715_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '725_715_files/BR_1.000/'), ]
samples['Sig_Splitted_725_715_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '725_715_files/BR_0.300/'), ]
samples['Sig_Splitted_725_705_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '725_705_files/BR_1.000/'), ]
samples['Sig_Splitted_725_705_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '725_705_files/BR_0.300/'), ]
samples['Sig_Splitted_800_790_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '800_790_files/BR_1.000/'), ]
samples['Sig_Splitted_800_790_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '800_790_files/BR_0.300/'), ]
samples['Sig_Splitted_850_840_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '850_840_files/BR_1.000/'), ]
samples['Sig_Splitted_850_840_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '850_840_files/BR_0.300/'), ]
samples['Sig_Splitted_900_875_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '900_875_files/BR_1.000/'), ]
samples['Sig_Splitted_900_875_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '900_875_files/BR_0.300/'), ]
samples['Sig_Splitted_925_900_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '925_900_files/BR_1.000/'), ]
samples['Sig_Splitted_925_900_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '925_900_files/BR_0.300/'), ]
samples['Sig_Splitted_975_965_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '975_965_files/BR_1.000/'), ]
samples['Sig_Splitted_975_965_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '975_965_files/BR_0.300/'), ]
samples['Sig_Splitted_1000_990_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '1000_990_files/BR_1.000/'), ]
samples['Sig_Splitted_1000_990_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '1000_990_files/BR_0.300/'), ]
samples['Sig_Splitted_1075_1065_BR_1p000'] = [os.path.join(userpath, NoSplittedSignal_dir, '1075_1065_files/BR_1.000/'), ]
samples['Sig_Splitted_1075_1065_BR_0p300'] = [os.path.join(userpath, NoSplittedSignal_dir, '1075_1065_files/BR_0.300/'), ]