import os, sys
import ROOT

from SampleChain import SampleChain

def get_parser():
    ''' Argument parser.                                                                                                                                                
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--sample',           action='store',                     type=str,            default='TTLep_pow',                                help="Which sample?" )
    argParser.add_argument('--year',             action='store',                     type=str,            default='2016PostVFP',                                             help="Which year?" )
    argParser.add_argument('--proc',             action='store',                     type=str,            default='other',                                             help="Which year?" )    
    return argParser

options = get_parser().parse_args()

sample  = options.sample
year = options.year
proc = options.proc

ch = SampleChain(sample, 0, -1, year, proc).getchain()
print 'Total Events for ', sample, ': ', ch.GetEntries()
