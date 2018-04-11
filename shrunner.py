import os

## Config
script_path = '/mnt/plkra/projects/VGTT/users/Script_Checkout/read_vasp_data'
slurm_script_path = '/mnt/plkra/users/mjbf5f/Projects/shrunner/Scripts/slurm_runner.sh'

## Code
def ifiles(path):
	""" Returns an iterator with absolute path to files in path. """
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			yield os.path.join(path, file)

def get_files(lst, ext='.dvl'):
	""" Returns a list of files from args. """
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

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		os.system('module load mcr/8.1')
		for index, file in enumerate(get_files(sys.argv[1:])):
			exc_str = ['sbatch', slurm_script_path, script_path, file, str(index)]
			os.system(' '.join(exc_str))

