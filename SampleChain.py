import os, sys
import ROOT
import subprocess
import types
import FileList_2016
import FileList_Fake_2016_janik
import FileList_UL2016PreVFP
import FileList_UL2016PostVFP

class SampleChain():
    luminosity_2016_forTL     = 0.007492230
    luminosity_2016PreVFP     = 19520.0
    luminosity_2016PostVFP     = 16810.0
    luminosity_2016           = 35922.0
    luminosity_2017           = 41856.0
    luminosity_2018           = 58905.0
    
    def __init__(self, sample, startfile, filestorun, year='2017', proc = "other", treename = "Events"):
        self.sample = sample
        self.startfile = startfile
        self.filestorun = filestorun
        self.treename = treename
        if year=='2016PreVFP':
            self.samplelist = FileList_Fake_2016_janik.samples if 'fake' in proc else FileList_UL2016PreVFP.samples
        elif year=='2016PostVFP':
            self.samplelist = FileList_Fake_2016_janik.samples if 'fake' in proc else FileList_UL2016PostVFP.samples
        elif year=='2016':
            self.samplelist = FileList_Fake_2016_janik.samples if 'fake' in proc else FileList_2016.samples
        elif year=='2017':
            self.samplelist = FileList_Fake_2017.samples if 'fake' in proc else FileList_UL2017.samples
        else:
            self.samplelist = FileList_Fake_2018.samples if 'fake' in proc else FileList_UL2018.samples
            
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
