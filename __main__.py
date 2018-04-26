import argparse
import shrunner
import slurmchecker

parser = argparse.ArgumentParser(
        description='Simple script to run .mat generation on folders (non recursive) on HPC',
        prog='shrunner',
        usage='python %(prog)s [-h] full_dvl_folder_path'
)

parser.add_argument(
        'folder_path',
        help='Full folder path to folder to run .mat generation on. Works with file lists ending with .list as well.'
)


# parser.add_argument(
#         '--script',
#         help='The script to run on files. (default: %(default)s',
#         metavar='',
#         default=''
# )
#
# parser.add_argument(
#         '-e', '--extension',
#         help='Log file type. (default: %(default)s)',
#         metavar='',
#         default='.dvl'
# )
#
# parser.add_argument(
#         '-c', '--check',
#         help="Search for the word 'issue' in mat files in folder given folder.",
#         metavar='',
#         dest='check'
# )

args = parser.parse_args()
shrunner.main(args.folder_path)
