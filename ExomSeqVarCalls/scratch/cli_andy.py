import click

@click.group()
def main(args=None):
    pass




@main.command()
@click.argument('repeat_file', type=click.Path(exists=True))
@click.argument('sample_size', type=int)
def extract_repeat_file_sample(repeat_file, sample_size):
    '''
    Extract a random sample of repeats.
    '''
    sample_file = repeat_file + '.sample'



@main.command()
@click.argument('bam_file', type=click.Path(exists=True))
@click.argument('reference_assembly', type=click.Path(exists=True))
@click.argument('output_bias_distribution', type=str)
def calculate_bias_distribution(bam_file, reference_assembly,
                                output_bias_distribution):
    '''
    Calculate distribution of strand biases.
    '''
    print "in calculate_bias_distribution"


@main.command()
@click.option('--output_filtered_regions', type=str, default=None,
              help='If OUTPUT_FILTERED_REGIONS is specified, regions to be '
              'filtered based on abnormal depth will be written to this file.')
@click.option('--ploidy', type=int, default=2, help='Global ploidy')
@click.option('--cnv_bedgraph_file', type=str, default=None,
              help='bedGraph file describing CNV regions')
@click.option('--p_threshold', type=float, default=0.0001,
              help='p-value threshold for abnormal depth')
@click.option('--merge_window', type=int, default=1000,
              help='maximum distance of adjacent abnormal sites \
              for creation of filtered regions')
@click.argument('bedgraph_file', type=click.Path(exists=True))
@click.argument('reference_assembly', type=click.Path(exists=True))
@click.argument('output_depth_distribution', type=str)
def calculate_depth_distribution(bedgraph_file, reference_assembly,
                                 output_depth_distribution,
                                 output_filtered_regions, ploidy,
                                 cnv_bedgraph_file, p_threshold,
                                 merge_window):
    '''
    Calculate distribution of depths in a bedGraph file.
    '''
    print "in calculate_depth_distribution"

@main.command()
@click.option('--output_plot_header', type=str, default=None,
              help='If OUTPUT_PLOT_HEADER is specified, PNGs are written '
              'that show the fit relative to the observed repeat indel rates.')
@click.argument('bam_file', type=click.Path(exists=True))
@click.argument('repeats_file', type=click.Path(exists=True))
@click.argument('output_fits_file', type=str)
def fit_repeat_indel_rates(bam_file, repeats_file, output_fits_file,
                           output_plot_header):
    print "in  fit_repeat_indel_rates"

    '''
    Fit a logistic function to log-transformed repeat indel rates.

    The OUTPUT_FITS_FILE gives the parameters for the derived fits.
    '''
		

if __name__ == "__main__":
    main()
