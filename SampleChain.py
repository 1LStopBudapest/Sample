import os, sys
import ROOT
import subprocess
import types
import FileList_2016
import FileList_Fake_2016_janik

class SampleChain():
    luminosity_2016_HLT_Mu3_PFJet40                            = 0.007492230 # all values /fb
    luminosity_2016_HLT_Mu8                                    = 0.003978578
    luminosity_2016_HLT_Mu17                                   = 0.285902233
    luminosity_2016_HLT_Mu27                                   = 0.253220763
    luminosity_2016_HLT_PFJet40                                = 0.000267102
    luminosity_2016_HLT_Ele8_CaloIdM_TrackIdM_PFJet30          = 0.007065194
    luminosity_2016_HLT_Ele17_CaloIdM_TrackIdM_PFJet30         = 0.063442490
    luminosity_2016_HLT_Ele23_CaloIdM_TrackIdM_PFJet30         = 0.063442490
    luminosity_2016_preVFP                                     = 19.52  # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVRun2LegacyAnalysis
    luminosity_2016_postVFP                                    = 16.81  # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVRun2LegacyAnalysis
    luminosity_2016                                            = 36.333380074 
    luminosity_2017                                            = 41.479680529
    luminosity_2018                                            = 59.832475339
    
    def __init__(self, sample, startfile, filestorun, year=2016, proc = "other", treename = "Events"):
        self.sample = sample
        self.startfile = startfile
        self.filestorun = filestorun
        self.treename = treename
        if year==2016:
            self.samplelist = FileList_Fake_2016_janik.samples if 'fake' in proc else FileList_2016.samples
        elif year==2017:
            self.samplelist = FileList_Fake_2017.samples if 'fake' in proc else FileList_2017.samples
        else:
            self.samplelist = FileList_Fake_2018.samples if 'fake' in proc else FileList_2018.samples
            
    def getchain(self):
        ch = ROOT.TChain(self.treename)
        filelist = []
        if 'T2tt' in self.sample:
            filelist.append(self.samplelist['T2tt'][0] + self.sample + '.root')
            self.addtochain(ch, filelist, 0, 1)
        else:
            if isinstance(self.samplelist[self.sample][0], types.ListType):
                for s in self.samplelist[self.sample]:
                    filelist.extend(self.getfilelist(s[0]))
            else:
                filelist = self.getfilelist(self.samplelist[self.sample][0])
            self.addtochain(ch, filelist, self.startfile, self.filestorun)
        return ch

    @staticmethod
    def getfilelist(filedir):
        files = []
        ls = subprocess.Popen(["find", filedir, "-type", "f"], stdout=subprocess.PIPE)
        fs = ls.stdout
        for f in fs:
            files.append(f.strip("\n"))

        return files

    def addtochain(self, ch, filelist, startfile, filestorun):
        files = len(filelist)-startfile if filestorun == -1 else filestorun 
        for i in range(len(filelist)):

            if i < startfile or i > (startfile+files)-1: continue
            ch.Add(filelist[i])

    def getEntries(self, ch):
        return ch.GetEntries()

    def getSampleList(self):
        return self.samplelist
