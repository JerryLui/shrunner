import os


def ifiles(path):
    """ Returns an iterator with absolute path to files in path. """
    path = os.path.expanduser(path)
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield os.path.join(path, file)


def get_files(path, ext):
    """ Returns a list of files in lst of directories with file extension %(ext). """
    file_list = []
    if os.path.isdir(path):
        # Append directory to file_list
        file_list.extend([file for file in ifiles(path) if file.endswith(ext)])

    elif os.path.isfile(path):
        if path.endswith('.list'):
            # Read and extract file paths ending with %(ext) from .list file
            with open(path, 'r') as f:
                file_list.extend([line.rstrip() for line in f.readlines() if line.endswith(ext)])
        elif path.endswith(ext):
            # Add file to file_list if it ends with %(ext)
            file_list.append(path)
    else:
        # If no files found
        raise FileNotFoundError()
    return file_list


def _get_slurm_script_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Scripts/slurm_runner.sh')


def main(folder_path, mat_script_path='/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data', ext='.dvl'):
    slurm_script_path = _get_slurm_script_path()
    for file in get_files(folder_path, ext):
        exc_str = ['sbatch', slurm_script_path, mat_script_path, file]
        os.system(' '.join(exc_str))


if __name__ == '__main__':
    """ Compability mode """
    import sys
    print('Warning: this mode is getting deleted next version.',
            '\nPlease call shrunner folder instead of shrunner/shrunner.py')
    main(sys.argv[1])
