## shrunner
The best job scheduler for matlab scripting on HPCC.
To compile MATLAB scripts use [Grand Compile Auto](http://10.239.124.134:5000/).

### Beginner guide:
To run mat generation on your HPCC folder, do the following (replace path/to/dvl/folder)
    
    $: echo module load python >> ~/.bashrc
    $: source ~/.bashrc
    $: python /mnt/plkra/users/mjbf5f/Projects/shrunner /path/to/dvl/folder
    

### More explanatory guide:
Step 1. Ensure that python module is loaded by checking .bashrc using `cat ~/.bashrc`,
the output should include the following:
    
    ...
    module load python
    ...
    
If not, add it with the following command `echo module load python >> ~/.bashrc` and reload your
.bashrc either by reconnecting or `source ~/.bashrc`

Step 2. Run the script on your log folder to generate .mat files by navigating to the folder containing
the shrunner folder and executing:

    $: python shrunner /absolute/folder/path/to/your/log/files/with/dvl
    
P.S. this works with file lists ending with .list

### Pro guide:
For usage help try
    
    $: python shrunner -h
    
Shrunner can read file/folder lists and run recursivley.
