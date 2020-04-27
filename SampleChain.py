import os, sys
import ROOT
import subprocess
import types
import FileList_2016

class SampleChain():
    luminosity_2016           = 35922.0
    luminosity_2017           = 41856.0
    luminosity_2018           = 58905.0
    samplelist = FileList_2016.samples
    
    def __init__(self, sample, startfile, filestorun, treename = "Events"):
        self.sample = sample
        self.startfile = startfile
        self.filestorun = filestorun
        self.treename = treename
        
    def getchain(self):
        ch = ROOT.TChain(self.treename)
        filelist = []
        if isinstance(self.samplelist[self.sample][0], types.ListType):
            for s in self.samplelist[self.sample]:
                filelist.extend(getfilelist(s[0]))
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
