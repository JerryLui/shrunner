import os

## Config
script_path = '/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data'
slurm_script_path = '/mnt/plkra/users/mjbf5f/Projects/shrunner/Scripts/slurm_runner.sh'

## PRIVATE FUNCTIONS
def ifiles(path):
	""" Returns an iterator with absolute path to files in path. """
	path = os.path.expanduser(path)
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			yield os.path.join(path, file)


def get_files(lst, ext='.dvl'):
	""" Returns a list of files in lst of directories with file extension ext. """
	file_list = []
	for arg in lst:
		if os.path.isdir(arg):
			file_list.extend([file for file in ifiles(arg) if file.endswith(ext)])

		elif os.path.isfile(arg):
			if arg.endswith(('.txt')):
				with open(arg, 'r') as f:
					file_list.extend([line.rstrip() for line in f.readlines()])
			elif arg.endswith(ext):
				file_list.append(arg)

		else:
			raise FileNotFoundError()
	return file_list


def slurm_check(path='.'):
	""" Quick check for slurm outputs if any issues are found """
	for file in ifiles(path):
		if file.endswith('.out'):
			with open(file, 'r') as f:
				for line in f.read().splitlines():
					if 'issue' in line.lower():
						print(file)
						print(line)
						print('-'*40)

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		if sys.argv[1] == "check":
			slurm_check(sys.argv[2])
		else:
			ext_files = get_files(sys.argv[1:])
			os.putenv('FILES', ' '.join(ext_files))
			exc_str = ['sbatch', '--array=1-' + str(len(ext_files)), slurm_script_path, script_path, '$FILES']
			os.system(' '.join(exc_str))
	else:
		print('Not enough inputs.')

