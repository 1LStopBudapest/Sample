import os, sys

from Dir import userpath

Signal_dir = "PostProcessedNtuple/2016/UL/SignalGrid"

samples = {}

#samples[samplename] = [path, Xsec, Nevents].
#Xec twiki
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom#NNLOapprox_NNLL
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
#From Vienna AN framework
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_nanoAODv6.py
#https://github.com/HephyAnalysisSW/Samples/blob/master/nanoAOD/python/Summer16_14Dec2018.py
#postprocessed ntuples are stored at /eos/cms/store/group/phys_susy/hephy/StopsCompressed/nanoTuples/




# T2tt sample fastsim grid:
samples['T2tt_prompt'] = [os.path.join(userpath, Signal_dir, "Prompt/T2tt/"), ]
#samples['T2tt_displaced'] = [os.path.join(userpath, Signal_dir, "Displaced/T2tt_LL/"), ]



