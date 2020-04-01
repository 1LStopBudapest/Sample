import os, sys
import ROOT

from SampleChain import SampleChain

def get_parser():
    ''' Argument parser.                                                                                                                                                
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--sample',           action='store',                     type=str,            default='TTSingleLep_pow',                                help="Which sample?" )
    
    return argParser

options = get_parser().parse_args()

sample  = options.sample

ch = SampleChain(sample, 0, -1).getchain()
print 'Total Events for ', sample, ': ', ch.GetEntries()
