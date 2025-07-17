import os, sys

from Dir import userpath

NoSplittedSignal_dir = "PostProcessedNtuple/displacedNonProcessedSamples/"

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

samples['Sig_NoSplitted_mStop_250to1100_full'] = [os.path.join(userpath, NoSplittedSignal_dir), ]