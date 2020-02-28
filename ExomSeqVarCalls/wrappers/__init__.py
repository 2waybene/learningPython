import os

#this is python 2.xx
#import ConfigParser

import configparser
import subprocess


PATHS = dict()

config = configparser.ConfigParser()

#this is python 2.xx
#import ConfigParser
#config = ConfigParser.ConfigParser()

config.read(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../..', 'config/paths.cfg'))


##FIXME for future building, now I use manual way
PATHS ={"bowtie2":" bowtie2","bowtie2_build":"bowtie2-build", "gatk":"/ddn/gs1/home/li11/NGS_projects/tools/GATK/GATK3.8/GenomeAnalysisTK.jar","java":"java","picard":"/ddn/gs1/home/li11/NGS_projects/tools/picard/picardCurrent/picard.jar","samtools":"samtools"}


##FIXME for future building, now I use manual way
#for key, value in config.items('paths'):
#    PATHS[key] = value


def quiet_call(call_list, stdout=os.devnull):
    '''
    Call outside program while suppressing messages to stdout and stderr.

    stdout_file -- captures stdout (default os.devnull)
    '''
    with open(stdout, 'w') as OUT:
        return subprocess.call(
            call_list, stdout=OUT, stderr=open(os.devnull, 'w'))
