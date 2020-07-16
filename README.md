All the samples and user information are here.
2016 Samples information are in FileList_2016.py. These samples are in naoAOD format and stored in Higgs machine. Not all samples are listed, some are there and rest will be added.

The path to the 2016 samples in higgs machine is /big_data/LepStop/PostProcessedNtuple/2016/MetSingleLep/. This path of the samples are divided in two section, userpath as /big_data/LepStop/ provided in Dir.py and PostProcessedNtuple/2016/MetSingleLep/ as MC_dir inside FileList_2016.py. This givies the flexibility to change the userpath according to where you are running your code.

Data luminosity (in SampleChain.py) and sample cross section (FileList_2016.py) are provided so that MC can be scaled to data luminosity by applying the lumi-weigt, Data lumi/(MC no of events/MC cross section).
The no of events for any sample can be obtained by running
```
python Nevents.py --sample TTSingleLep_pow

```
For postprocessed nanoAOD samples, no of events calculated by above script are the events after the selection applied during post processing. But the lumi weight should be calculted using the total no of events produced. Fortunately, that is done during post processing considering Data lumi as 1000 fb-1 and lumi weight is stored as a branch namely 'weight'.

So for actual lumiscaling, we need to multiply weight by Data luminosoty/1000 which is done while filling histograms in FillHistos.py script.

