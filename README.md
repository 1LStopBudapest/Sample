All the samples and their location information are here.
UL2016 samples information are in FileList_UL2016PreVFP.py and FileList_UL2016PostVFP.py
FileList_UL2018.py for UL2018 samples.

UL 2017 will be added soon

Now the year option in SampleChain.py is a string variable

legacy 2016 Samples information are in FileList_2016.py.

These samples are in naoAOD format and stored in Higgs machine. Not all samples are listed, most are there and rest will be added.

sample location path:

2018 sample example:
The path to the 2018 samples in higgs machine is /big_data/LepStop/PostProcessedNtuple/2018/UL/. This path of the samples are divided in two section, userpath as /big_data/LepStop/ provided in Dir.py and PostProcessedNtuple/2018/UL/ inside FileList_UL2018.py. This givies the flexibility to change the userpath according to where you are running your code.

Dir.py contains the name of samples path and the directory where user wants to store the plots and root files etc. Add your username and preffered paths if you are using it for the first time. 

Data luminosity (in SampleChain.py) and sample cross section (FileList_2016.py) are provided so that MC can be scaled to data luminosity by applying the lumi-weigt, Data lumi/(MC no of events/MC cross section).
The no of events for any sample can be obtained by running
```
python Nevents.py --sample TTSingleLep_pow

```
For postprocessed nanoAOD samples, no of events calculated by above script are the events after the selection applied during post processing. But the lumi weight should be calculted using the total no of events produced. Fortunately, that is done during post processing considering Data lumi as 1000 fb-1 and lumi weight is stored as a branch namely 'weight'.

So for actual lumiscaling, we need to multiply weight by Data luminosoty/1000 which is done while filling histograms. For example one can check NanoTuplePlot/FillHistos.py script.

