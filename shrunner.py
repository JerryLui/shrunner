import os
from subprocess import call


def get_files(path, ext):
    """
        Returns a list of files in lst of directories with file extension %(ext).
    """
    path = os.path.expanduser(path)
    ans_dict = dict()

    if os.path.isdir(path):
        return {path:[file for file in os.listdir(path) if file.endswith(ext)]}
    elif os.path.isfile(path):
        if path.endswith(('.list', '.txt')):    # If it is an list file
            with open(path, 'r') as f:
                for line in f.readlines():
                    line = line.rstrip()
                    if line.endswith(ext):
                        folder, file = os.path.split(line)
                        ans_dict[folder] = ans_dict.get(folder, list()) + [file]
                return ans_dict
        elif path.endswith(ext):
            folder, file = os.path.split(path)
            return {folder:file}
    else:
        # If no files found
        raise FileNotFoundError('2', 'File/Folder not found!', path)
    return file_list


def main(folder_path, mat_script_path='/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data', ext='.dvl'):
    slurm_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Scripts/slurm_runner.sh')
    for folder, files in get_files(folder_path, ext).items():
        dirname = os.path.split(folder)[-1]
        os.putenv('LISTOFLOGS', ' '.join(files))
        exc = ['sbatch', '-a', '0-' + str(len(files)-1), '--job-name', dirname, slurm_script_path,
                mat_script_path, folder]
        print('\nexecuting:', ' '.join(exc))
        call(exc)


if __name__ == '__main__':
    """ Compability mode """
    import sys
    main(sys.argv[1])
