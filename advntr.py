import argparse

from src.advntr_commands import genotype, view_model, not_implemented_command
from src import settings


def run_advntr():
    description = '=======================================================\n' \
                  'adVNTR 1.0.0: Genopyting tool for VNTRs\n' \
                  '=======================================================\n' \
                  'Source code: https://github.com/mehrdadbakhtiari/adVNTR\n' \
                  'Instructions: http://advntr.readthedocs.io\n' \
                  '-------------------------------------------------------\n'
    help = 'Command: genotype\tfind RU counts and mutations in VNTRs\n' \
           '         viewmodel\tview existing models in database\n' \
           '         addmodel\tadd custom VNTR to the database\n' \
           '         delmodel\tremove a model from database\n'

    usage = '\r{}\nusage: %(prog)s <command> [options]\n\n\r{}\r{}'.format(description.ljust(len('usage:')), help, '\n')
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, usage=usage, add_help=False)
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    genotype_parser = subparsers.add_parser('genotype', usage='python advntr.py genotype [options]')
    genotype_parser.add_argument('-a', '--alignment_file', type=str, help='Alignment file in BAM format or SAM format',
                                 metavar='FILE')
    genotype_parser.add_argument('-f', '--fasta', type=str, help='Fasta file containing raw reads', metavar='FILE')
    genotype_parser.add_argument('-fs', '--frameshift', action='store_true',
                                 help='Set this flag to search for frameshifts in VNTR instead of copy number.'
                                 '\n    * Supported VNTR IDs: %s' % settings.FRAMESHIFT_VNTRS)
    genotype_parser.add_argument('-e', '--expansion', action='store_true',
                                 help='Set this flag to determine long expansion from PCR-free data')
    genotype_parser.add_argument('-c', '--coverage', type=float, metavar='<COVERAGE>',
                                 help='Average sequencing coverage in PCR-free sequencing')
    genotype_parser.add_argument('-p', '--pacbio', action='store_true',
                                 help='Set this flag if input file contains PacBio reads instead of Illumina reads')
    genotype_parser.add_argument('-n', '--nanopore', action='store_true',
                                 help='Set this flag if input file contains Nanopore MinION reads instead of Illumina')
    genotype_parser.add_argument('-wd', '--working_directory', type=str, metavar='<DIRECTORY>',
                                 help='Working directory for creating temporary files needed for computation')
    genotype_parser.add_argument('-m', '--models', type=str, metavar='<FILE>', default='vntr_data/hg19_VNTRs.db',
                                 help='File containing VNTRs information [%(default)s]')
    genotype_parser.add_argument('-t', '--threads', type=int, metavar='<nthreads>', default=4,
                                 help='Run the tool on <nthreads> parallel threads which will run on separate processors/cores [%(default)s]')
    genotype_parser.add_argument('-vid', '--vntr_id', type=str, metavar='<VNTR ID>', default=None,
                                 help='Comma-separated list of VNTR IDs')
    genotype_parser.add_argument('-naive', '--naive', action='store_true', default=False,
                                 help='Use naive approach for PacBio reads')

    viewmodel_parser = subparsers.add_parser('viewmodel', usage='python advntr.py viewmodel [options]')
    viewmodel_parser.add_argument('-g', '--gene', type=str, default='', help='Comma-separated list of Gene Names')
    viewmodel_parser.add_argument('-p', '--pattern', type=str, default=None,
                                  help='Repeating pattern of VNTR in forward (5\' to 3\') direction')

    addmodel_parser = subparsers.add_parser('addmodel', usage='python advntr.py addmodel [options]')
    delmodel_parser = subparsers.add_parser('delmodel', usage='python advntr.py delmodel [options]')

    args = parser.parse_args()
    if args.command == 'genotype':
        genotype(args, genotype_parser)
    elif args.command == 'viewmodel':
        view_model(args, viewmodel_parser)
    elif args.command == 'addmodel':
        not_implemented_command(parser, args.command)
    elif args.command == 'delmodel':
        not_implemented_command(parser, args.command)
    else:
        parser.error('Please specify a valid command')

if __name__ == '__main__':
    run_advntr()
