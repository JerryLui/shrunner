import shrunner


def slurm_check(path='.'):
    """ Quick check for slurm outputs if any issues are found """
    for file in shrunner.get_files(path, '.out'):
        with open(file, 'r') as f:
            for line in f.read().splitlines():
                if 'issue' in line.lower():
                    print(file)
                    print(line)
                    print('-' * 40)


if __name__ == '__main__':
    import sys
    for folder in sys.argv[1:]:
        slurm_check(folder)
