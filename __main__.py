import argparse
import shrunner

parser = argparse.ArgumentParser(
        description='Simple script to run .mat generation on folders (non recursive) on HPC',
        prog='shrunner',
        usage='python %(prog)s [-h] full_dvl_folder_path [--script] [-e, --extension] [-d, --directory] [-r, --recursive]'
)

parser.add_argument(
        'folder_path',
        help='Full folder path to folder to run .mat generation on. Works with file lists ending with .list as well.'
)

parser.add_argument(
         '--script',
         help='Path to script to run on folder/file. (default: %(default)s)',
         metavar='',
         default='/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data'
)

parser.add_argument(
         '-e', '--extension',
         help='File type to run script on. (default: %(default)s)',
         metavar='',
         default='.dvl'
)

parser.add_argument(
        '-d', '--directory',
        help='Run script on directories instead of individual files. (default: %(default)s)',
        action='store_true'
)

parser.add_argument(
        '-r', '--recursive',
        help='Search recursivley for files. (default: %(default)s)',
        action='store_true'
)

args = parser.parse_args()
shrunner.main(args.folder_path, args.script, args.extension, args.directory, args.recursive)
