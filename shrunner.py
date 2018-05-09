import os
from subprocess import call


def get_files(path, ext):
    """ Returns a list of files in lst of directories with file extension %(ext). """
    path = os.path.expanduser(path)

    if os.path.isdir(path):
        return [os.path.join(path, file) for file in os.listdir(path) if file.endswith(ext)]
    elif os.path.isfile(path):
        if path.endswith('.list'):
            with open(path, 'r') as f:
                return [line.rstrip() for line in f.readlines() if line.endswith(ext)]
        elif path.endswith(ext):
            return path
    else:
        # If no files found
        raise FileNotFoundError()
    return file_list


def main(folder_path, mat_script_path='/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data', ext='.dvl'):
    slurm_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Scripts/slurm_runner.sh')
    files = get_files(folder_path, ext)
    folder_path = os.path.split(files[0])[0]
    files = [os.path.split(file)[1] for file in files]
    os.putenv('LISTOFLOGS', ' '.join(files))
    exc = ['sbatch', '-a', '0-' + str(len(files)-1), slurm_script_path, mat_script_path, folder_path]
    print('executing:', ' '.join(exc))
    call(exc)


if __name__ == '__main__':
    """ Compability mode """
    import sys
    main(sys.argv[1])
