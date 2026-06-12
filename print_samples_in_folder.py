import os

directory = "/mnt/newDisk/stop_samples_long_lived/2018/reweighted"  # Current directory, or specify your path like "/path/to/directory"
n_samples = 0
for filename in os.listdir(directory):
    if filename.endswith(".root"):
        stop_mass = filename.split("_")[2]
        x0_mass = filename.split("_")[3]
        br = filename.split("_")[5]

        key = 'Sig_Splitted_'+stop_mass+'_'+x0_mass+'_'+br
        print( "samples['"+key+"']= ['"+directory+"/"+filename+"', ] ")
        n_samples +=1

print(n_samples)