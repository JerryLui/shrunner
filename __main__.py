import argparse
import shrunner

parser = argparse.ArgumentParser(
        description='Simple script to run .mat generation on folders (non recursive) on HPC',
        prog='shrunner',
        usage='python %(prog)s [-h] full_dvl_folder_path [--script script_path] [-e, --extension file_type] [-d, --directory] [-r, --recursive] [-v, --version]'
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
        help='Search recursivley for files/folders. (default: %(default)s)',
        action='store_true'
)

parser.add_argument(
        '-v', '--version',
        help='Set module version, default is latest. (Python: [27, 35, 37 (Default)], MCR: [93, 92, 81 (Default)])',
        metavar='',
        default=''
)

args = parser.parse_args()
shrunner.main(args.folder_path, args.script, args.extension, args.directory, args.recursive, args.version)
