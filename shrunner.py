import os
from subprocess import call


def get_files(path, extension='.dvl', recursive=False):
    """ Returns list of tuples (file directory, file name) """
    # If path is a list or text file
    if os.path.isfile(path) and path.endswith(('.list', '.txt')):
        ans = []

        # Open text file and go through each line
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.rstrip()

                # If line is a directory
                if os.path.isdir(line):
                    ans += [(os.path.dirname(entry.path), entry.name) for entry in _recursive_file_scan(line, extension, recursive)]
                # If line ends with file
                elif os.path.splitext(line) == extension:
                    ans.append(line)
                else:
                    print('WARNING: Unmatched file extension ', os.path.splitext(line))
            return ans
    else:
        return [(os.path.dirname(entry.path), entry.name) for entry in _recursive_file_scan(path, extension, recursive)]


def get_folders(path):
    """ Returns folder or list of folders if path is a file. """
    if os.path.isdir(path):
        return [path]
    elif os.path.isfile(path):
        with open(path, 'r') as f:
            return [line.rstrip() for line in f.readlines()]
    else:
        raise FileNotFoundError(2, 'File/Folder not found!', path)


def _recursive_file_scan(path, extension='.dvl', recursive=False):
    """ Recursive iterator for files in path with extension. """
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False) and recursive:
            yield from _recursive_file_scan(entry, extension, recursive)
        elif os.path.splitext(entry.name)[1] == extension:
            yield entry


def _sort_by_folders(tuple_list):
    """
        Sorts entries with a dict by the first entry
        :return dict
            With each key as a directory and a list of files as it's value.
    """
    ans = dict()

    for folder, file in tuple_list:
        if ans.get(folder):
            ans.get(folder).append(file)
        else:
            ans[folder] = [file]
    return ans


def main(folder_path,
         script_path='/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data',
         extension='.dvl',
         directory=False,
         recursive=False):
    """
    :param folder_path:     Full path to folder/file list (.list, .txt) to run script on.
    :param script_path: Full path to script to run on folder/file.
    :param extension:       File type to run script on.
    :param directory:       Wether or not to run only run on folders.
    :param recursive:       Wether or not to include files in subdirectories.
    """
    # Input checks
    if directory and recursive:
        print('WARNING: Cannot search recursively in folders!')

    if not extension.startswith('.'):
        print("WARNING: File extensions needs to start with '.'")

    if os.path.splitext(script_path)[1] == '.py':
        run_python = True
        print('INFO: Running Python script.')
    else:
        run_python = False

    slurm_folders_script = 'Script/slurm_python_folder.sh' if run_python else 'Script/slurm_folder.sh'
    slurm_files_script = 'Script/slurm_python_runner.sh' if run_python else 'Script/slurm_runner.sh'

    folder_path = os.path.expanduser(folder_path)

    # Run script on directories
    if directory:
        print("INFO: Running on directories, file extension and recursive options ignored.")
        # Get path to slurm script runner
        slurm_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), slurm_folders_script)

        folders = get_folders(folder_path)
        os.putenv('LISTOFFOLDERS', ' '.join(folders))
        exc = ['sbatch', '-a', '0-' + str(len(folders) - 1), '--job-name', 'DIRCHECK', slurm_script_path,
               script_path]

        print('\nExecuting:', ' '.join(exc))
        print('\nSubmitting', len(folders), 'job(s).')
        call(exc)
    # Run script on files
    else:
        # Get path to slurm script runner
        slurm_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), slurm_files_script)

        for folder, files in _sort_by_folders(get_files(folder_path, extension, recursive)).items():
            directory_name = os.path.split(folder)[-1]

            os.putenv('LISTOFLOGS', ' '.join(files))
            exc = ['sbatch', '-a', '0-' + str(len(files) - 1), '--job-name', directory_name, slurm_script_path,
                   script_path, folder]

            print('\nExecuting:', ' '.join(exc))
            print('\nSubmitting', len(files), 'job(s).')
            call(exc)


if __name__ == '__main__':
    import sys

    print('INFO: Deprecated, please call the whole module instead of this file!')
    main(sys.argv[1])
