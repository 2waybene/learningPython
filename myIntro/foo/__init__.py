#!/ddn/gs1/biotools/python3/bin/python3
class hg19Ref ():

    BWAIndex = "/ddn/gs1/home/li11/project2017/SEQC2_TGSWG2/refDB/indexBWA_hg19nohaplo/hg19"
    Bowtie2Index = "/ddn/gs1/home/li11/project2017/SEQC2_TGSWG2/refDB/indexBowtie2_hg19nohaplo/hg19"

    def HelloWorld(self):
        print ("helloworld\n")

def main():
    genome = hg19Ref
    print (genome.BWAIndex)
    print (genome.Bowtie2Index)
    genome.HelloWorld(genome)

if __name__ == '__main__':
    main()

